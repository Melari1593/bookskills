#!/usr/bin/env python3
"""Busca un tema del grafo de The Five Elements Cookbook (Zoey Xinyi Gong) y enumera sus secciones previas,
las tablas que se consultan y las alertas de evidencia de las hierbas y recetas implicadas."""
import json
import sys
import unicodedata
from pathlib import Path


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(s).lower())
                   if not unicodedata.combining(c))


def key(num):
    return tuple(map(int, str(num).split('.')))


def main(query):
    data = json.loads((Path(__file__).resolve().parents[1] / 'references/grafo.json').read_text())
    secs = {s['num']: (c, s) for c in data['chapters'] for s in c['sections']}
    items = data['items']
    item_sec = {iid: s['num'] for c in data['chapters'] for s in c['sections']
                for iid in s.get('items', [])}
    q = norm(query)
    matches = [('chapter', str(c['num']), c['title']) for c in data['chapters'] if q == str(c['num'])]
    matches += [('section', k, s['title']) for k, (_, s) in secs.items()
                if q == norm(k) or q in norm(s['title'])]
    matches += [('item', k, v['title']) for k, v in items.items()
                if q == norm(k) or q in norm(v['title'])]
    matches += [('chapter', str(c['num']), c['title']) for c in data['chapters']
                if q in norm(c['title']) and q != str(c['num'])]
    if not matches:
        print(f'Sin coincidencias: {query}')
        return 1
    kind, k, title = next((m for m in matches if norm(m[1]) == q), matches[0])
    print(f'{kind}: {k} — {title}')
    if kind == 'chapter':
        chapter = next(c for c in data['chapters'] if str(c['num']) == k)
        targets = [s['num'] for s in chapter['sections']]
    elif kind == 'section':
        targets = [k]
    else:
        targets = [item_sec[k]]

    found = set(targets)
    stack = list(targets)
    req = data['requires']['sections']
    while stack:
        for dep in req.get(stack.pop(), []):
            if dep not in found:
                found.add(dep)
                stack.append(dep)
    if kind == 'item':
        seen = {k}
        stack = [k]
        while stack:
            for dep in data['requires']['items'].get(stack.pop(), []):
                if dep not in seen and dep in item_sec:
                    seen.add(dep)
                    stack.append(dep)
                    found.add(item_sec[dep])
    ordered = sorted(found, key=key)
    print('Ruta de lectura (el grafo no trae páginas impresas):')
    for number in ordered:
        chapter, section = secs[number]
        print(f"  {number} {section['title']} ({chapter['num']}. {chapter['title']})")

    used = []
    for res in data.get('resources', []):
        hits = [n for n in ordered if n in res.get('usedBy', [])]
        if hits:
            used.append(f"  Tabla {res['id']}: {res['title']} (para {', '.join(hits[:8])}{'…' if len(hits) > 8 else ''})")
    if used:
        print('Tablas que se consultan:')
        print('\n'.join(used))

    alerts = [(n, secs[n][1]) for n in ordered if secs[n][1].get('caution')]
    if alerts:
        print('Atención (alertas de evidencia, verificadas el 2026-11-21):')
        for n, s in alerts:
            print(f"  {n} {s['title'].split(' · ')[0]}: {s['caution']}")

    if len(matches) > 1:
        print('Otras coincidencias:', '; '.join(f'{a} {b} {c}' for a, b, c in matches[1:6]))
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python scripts/ruta.py "término o número"', file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
