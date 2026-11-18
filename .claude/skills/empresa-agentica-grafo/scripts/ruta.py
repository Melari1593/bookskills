#!/usr/bin/env python3
"""Busca un tema en el grafo de La empresa agéntica y lista sus secciones previas.

Uso: python scripts/ruta.py "término, número de sección o id de concepto"
Ejemplos: "AAOSA", "7.5", "raci_segunda_capa", "capítulo 8"
"""
import json
import re
import sys
import unicodedata
from pathlib import Path


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(s).lower())
                   if not unicodedata.combining(c))


def clave(num):
    """Ordena 'I.1' (introducción) antes de '1.1' y '3.10' después de '3.9'."""
    partes = str(num).split('.')
    cab = 0 if partes[0] in ('I', 'Int') else int(partes[0])
    return (cab, *[int(p) for p in partes[1:]])


def main(query):
    base = Path(__file__).resolve().parents[1]
    data = json.loads((base / 'references/grafo.json').read_text(encoding='utf-8'))
    secs = {s['num']: (c, s) for c in data['chapters'] for s in c['sections']}
    items = data['items']
    item_sec = {i: s['num'] for c in data['chapters'] for s in c['sections'] for i in s.get('items', [])}
    q = norm(query)
    m = re.fullmatch(r'(capitulo|cap\.?)\s*(\w+)', q)
    if m:
        q = m.group(2)
        matches = [('chapter', str(c['num']), c['title']) for c in data['chapters'] if norm(c['num']) == q]
    else:
        matches = [('section', k, s['title']) for k, (_, s) in secs.items()
                   if q == norm(k) or q in norm(s['title'])]
        matches += [('item', k, v['title']) for k, v in items.items()
                    if q == norm(k) or q in norm(v['title']) or q in norm(v.get('formula', ''))]
        matches += [('chapter', str(c['num']), c['title']) for c in data['chapters'] if q in norm(c['title'])]
    if not matches:
        print(f'Sin coincidencias: {query}')
        return 1
    kind, key, title = next((x for x in matches if norm(x[1]) == q), matches[0])
    print(f'{kind}: {key} — {title}')
    if kind == 'item':
        v = items[key]
        print(f"  Esquema: {v['formula']}\n  Resumen: {v['summary']}\n  Sección: {item_sec[key]}")
    if kind == 'chapter':
        cap = next(c for c in data['chapters'] if str(c['num']) == key)
        targets = [s['num'] for s in cap['sections']]
    elif kind == 'section':
        targets = [key]
    else:
        targets = [item_sec[key]]

    found, stack = set(targets), list(targets)
    req = data['requires']['sections']
    while stack:
        for dep in req.get(stack.pop(), []):
            if dep not in found:
                found.add(dep)
                stack.append(dep)
    if kind == 'item':
        seen, stack = {key}, [key]
        while stack:
            for dep in data['requires']['items'].get(stack.pop(), []):
                if dep not in seen:
                    seen.add(dep)
                    stack.append(dep)
                    found.add(item_sec[dep])
        previos = sorted(seen - {key}, key=lambda i: clave(item_sec[i]))
        if previos:
            print('Conceptos previos:', '; '.join(items[i]['title'] for i in previos))
    print('Ruta de lectura (páginas impresas):')
    for n in sorted(found, key=clave):
        cap, s = secs[n]
        print(f"  {n} {s['title']} — p. {s['page']} (cap. {cap['num']})")
    if len(matches) > 1:
        print('Otras coincidencias:', '; '.join(f'{k} {n} {t}' for k, n, t in matches[1:6]))
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
