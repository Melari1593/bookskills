#!/usr/bin/env python3
"""Busca un tema en los grafos de libros de agentes de IA y enumera su ruta de lectura.

Uso:
  python scripts/ruta.py "término o número"                 # busca en los 4 libros
  python scripts/ruta.py --grafo graphrag "PathRAG"         # ruta en un libro
  python scripts/ruta.py --grafo ahmad 7.4
Libros: albada, lanham, graphrag, ahmad.
"""
import json
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / 'references'
GRAFOS = {
    'albada': 'grafo_albada.json',
    'lanham': 'grafo_lanham.json',
    'graphrag': 'grafo_graphrag.json',
    'ahmad': 'grafo_ahmad.json',
}


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(s).lower())
                   if not unicodedata.combining(c))


def orden(num):
    out = []
    for part in str(num).split('.'):
        out.append((0, int(part)) if part.isdigit() else (1, part))
    return tuple(out)


def cargar(clave):
    return json.loads((BASE / GRAFOS[clave]).read_text(encoding='utf-8'))


def buscar(data, q):
    secs = {s['num']: (c, s) for c in data['chapters'] for s in c['sections']}
    m = [('sección', k, s['title']) for k, (_, s) in secs.items()
         if q == norm(k) or q in norm(s['title'])]
    m += [('ítem', k, v['title']) for k, v in data['items'].items()
          if q == norm(k) or q in norm(v['title'])]
    m += [('capítulo', str(c['num']), c['title']) for c in data['chapters']
          if q == norm(c['num']) or q in norm(c['title'])]
    return secs, m


def cierre(inicio, grafo):
    vistos, pila = set(inicio), list(inicio)
    while pila:
        for dep in grafo.get(str(pila.pop()), []):
            dep = str(dep)
            if dep not in vistos:
                vistos.add(dep)
                pila.append(dep)
    return vistos


def ruta(clave, query):
    data = cargar(clave)
    secs, matches = buscar(data, norm(query))
    if not matches:
        print(f'[{clave}] Sin coincidencias: {query}')
        return 1
    tipo, key, titulo = next((x for x in matches if norm(x[1]) == norm(query)), matches[0])
    print(f"[{clave}] {data['meta']['title']}")
    print(f'{tipo}: {key} — {titulo}')
    item_sec = {i: s['num'] for c in data['chapters'] for s in c['sections'] for i in s.get('items', [])}
    if tipo == 'capítulo':
        cap = next(c for c in data['chapters'] if str(c['num']) == key)
        objetivo = [s['num'] for s in cap['sections']]
    elif tipo == 'sección':
        objetivo = [key]
    else:
        objetivo = [item_sec[key]] if key in item_sec else []
        objetivo += [item_sec[i] for i in cierre([key], data['requires'].get('items', {})) if i in item_sec]
    encontradas = cierre(objetivo, data['requires'].get('sections', {}))
    print('Ruta de lectura (orden del libro; numeración del grafo, sin páginas):')
    for num in sorted(encontradas, key=orden):
        if num in secs:
            cap, s = secs[num]
            print(f"  {num} {s['title']} ({cap['title']})")
    if tipo == 'ítem':
        it = data['items'][key]
        print('Resumen:', it.get('summary', ''))
        if it.get('formula'):
            print('Esquema:', it['formula'])
    otras = [m for m in dict.fromkeys(matches) if m != (tipo, key, titulo)]
    if otras:
        print('Otras coincidencias:', '; '.join(f'{t} {n} {x}' for t, n, x in otras[:5]))
    return 0


def buscar_todos(query):
    q, total = norm(query), 0
    for clave in GRAFOS:
        _, m = buscar(cargar(clave), q)
        total += len(m)
        for tipo, key, titulo in m[:8]:
            print(f'[{clave}] {tipo} {key} — {titulo}')
    if not total:
        print(f'Sin coincidencias en los 4 libros: {query}')
        return 1
    print('Para la ruta: python scripts/ruta.py --grafo <libro> "<número o término>"')
    return 0


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 3 and args[0] == '--grafo' and args[1] in GRAFOS:
        sys.exit(ruta(args[1], args[2]))
    if len(args) == 1:
        sys.exit(buscar_todos(args[0]))
    print('Uso: python scripts/ruta.py [--grafo albada|lanham|graphrag|ahmad] "término o número"',
          file=sys.stderr)
    sys.exit(2)
