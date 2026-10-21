#!/usr/bin/env python3
"""Busca un tema del grafo del Manual of Pediatric Nutrition y enumera sus secciones previas,
los apéndices que se consultan y las alertas de guías vigentes de los conceptos implicados."""
import json
import sys
import unicodedata
from pathlib import Path


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(s).lower())
                   if not unicodedata.combining(c))


def main(query):
    data = json.loads((Path(__file__).resolve().parents[1] / 'references/grafo.json').read_text())
    secs = {s['num']: (c, s) for c in data['chapters'] for s in c['sections']}
    items = data['items']
    item_sec = {iid: s['num'] for c in data['chapters'] for s in c['sections']
                for iid in s.get('items', [])}
    q = norm(query)
    matches = [('section', key, s['title']) for key, (_, s) in secs.items()
               if q in norm(key) or q in norm(s['title'])]
    matches += [('item', key, v['title']) for key, v in items.items()
                if q in norm(key) or q in norm(v['title'])]
    matches += [('chapter', str(c['num']), c['title']) for c in data['chapters']
                if q in norm(c['title'])]
    if not matches:
        print(f'Sin coincidencias: {query}')
        return 1
    kind, key, title = next((m for m in matches if norm(m[1]) == q), matches[0])
    print(f'{kind}: {key} — {title}')
    if kind == 'chapter':
        chapter = next(c for c in data['chapters'] if str(c['num']) == key)
        targets = [s['num'] for s in chapter['sections']]
    elif kind == 'section':
        targets = [key]
    else:
        targets = [item_sec[key]]

    found = set(targets)
    stack = list(targets)
    req = data['requires']['sections']
    while stack:
        for dep in req.get(stack.pop(), []):
            if dep not in found:
                found.add(dep)
                stack.append(dep)
    if kind == 'item':
        seen = {key}
        stack = [key]
        while stack:
            for dep in data['requires']['items'].get(stack.pop(), []):
                if dep not in seen:
                    seen.add(dep)
                    stack.append(dep)
                    found.add(item_sec[dep])
    ordered = sorted(found, key=lambda x: tuple(map(int, x.split('.'))))
    print('Ruta de lectura (páginas impresas):')
    for number in ordered:
        chapter, section = secs[number]
        print(f"  {number} {section['title']} — p. {section.get('page') or '¿?'} ({chapter['title']})")

    used = []
    for res in data.get('resources', []):
        hits = [n for n in ordered if n in res.get('usedBy', [])]
        if hits:
            used.append(f"  Apéndice {res['id']} {res['title']} — p. {res['page']} (para {', '.join(hits)})")
    if used:
        print('Apéndices que se consultan:')
        print('\n'.join(used))

    alerts = [(iid, items[iid]) for n in ordered for iid in secs[n][1].get('items', [])
              if items[iid].get('caution')]
    if alerts:
        print('Atención (guías vigentes y cifras por verificar):')
        for iid, it in alerts:
            print(f"  {item_sec[iid]} {it['title']}: {it['caution']}")

    if len(matches) > 1:
        print('Otras coincidencias:', '; '.join(f'{k} {n} {t}' for k, n, t in matches[1:6]))
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python scripts/ruta.py "término o número"', file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
