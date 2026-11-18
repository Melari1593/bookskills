#!/usr/bin/env python3
"""Busca un tema del grafo de Origami Design Secrets (Lang) y lista su ruta de lectura."""
import json
import sys
import unicodedata
from pathlib import Path


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(s).lower())
                   if not unicodedata.combining(c))


def sec_key(x):
    return tuple(int(p) for p in x.split('.'))


def closure(start, deps):
    """Devuelve start más todo lo que alcanza siguiendo deps (dict nodo -> lista)."""
    found = set(start)
    stack = list(start)
    while stack:
        for dep in deps.get(stack.pop(), []):
            if dep not in found:
                found.add(dep)
                stack.append(dep)
    return found


def main(query):
    data = json.loads((Path(__file__).resolve().parents[1] / 'references/grafo-lang.json')
                      .read_text(encoding='utf-8'))
    chapters = data['chapters']
    secs = {s['num']: (c, s) for c in chapters for s in c.get('sections', [])}
    items = data['items']
    item_sec = {iid: s['num'] for c in chapters for s in c.get('sections', [])
                for iid in s.get('items', [])}
    q = norm(query)

    matches = [('section', key, s['title']) for key, (_, s) in secs.items()
               if q in norm(key) or q in norm(s['title'])]
    matches += [('item', key, v['title']) for key, v in items.items()
                if q in norm(key) or q in norm(v['title'])]
    matches += [('chapter', str(c['num']), c['title']) for c in chapters
                if q == norm(c['num']) or q in norm(c['title'])]
    if not matches:
        print(f'Sin coincidencias: {query}')
        return 1
    kind, key, title = next((m for m in matches if norm(m[1]) == q), matches[0])
    print(f'{kind}: {key} — {title}')

    if kind == 'item':
        v = items[key]
        print(f"  Qué es: {v['summary']}")
        if v.get('formula'):
            ref = f" (Ec. {v['ref']})" if v.get('ref') else ''
            print(f"  Fórmula: {v['formula']}{ref}")
        print(f"  Se presenta en la sección {item_sec[key]}")
        needed_items = closure([key], data['requires']['items'])
        targets = {item_sec[i] for i in needed_items}
    elif kind == 'chapter':
        chapter = next(c for c in chapters if str(c['num']) == key)
        targets = {s['num'] for s in chapter.get('sections', [])}
        if not targets:
            print(f"Capítulo sin secciones numeradas — p. {chapter['page']}")
            return 0
    else:
        targets = {key}

    found = closure(targets, data['requires']['sections'])
    print('Ruta de lectura (páginas impresas):')
    for number in sorted(found, key=sec_key):
        chapter, section = secs[number]
        print(f"  {number} {section['title']} — p. {section['page']} "
              f"(cap. {chapter['num']}: {chapter['title']})")
    for r in data.get('resources', []):
        if set(r.get('usedBy', [])) & found:
            print(f"  Anexo: {r['title']} — p. {r['page']}")
    if len(matches) > 1:
        print('Otras coincidencias:', '; '.join(f'{k} {n} {t}' for k, n, t in matches[1:6]))
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python scripts/ruta.py "término o número"', file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
