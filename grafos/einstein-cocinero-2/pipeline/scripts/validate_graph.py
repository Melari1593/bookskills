#!/usr/bin/env python3
"""Valida un grafo de libro (JSON) antes de construir el HTML.

Uso:  python validate_graph.py grafo.json

Errores (bloquean la construcción):
  - referencias a capítulos, secciones, ítems o recursos que no existen
  - números de sección o ids repetidos
  - ítems definidos en `items` pero que ninguna sección presenta, o al revés
Advertencias (revisar, no bloquean):
  - ciclos en los prerrequisitos (A requiere B y B requiere A)
  - capítulos sin secciones, ítems sin resumen, secciones sin página
  - prerrequisitos que apuntan "hacia adelante" en el libro (puede ser correcto, pero es raro)
"""
import json, sys
from collections import defaultdict


def validate(g):
    """Devuelve (errores, advertencias, estadísticas)."""
    errors, warns = [], []

    for key in ("meta", "chapters", "items"):
        if key not in g:
            errors.append(f"Falta la clave de primer nivel '{key}'.")
    if errors:
        return errors, warns, {}

    blocks = set((g.get("blocks") or {}).keys())
    ch_ids, sec_ids, sec_order, defined = set(), set(), {}, defaultdict(list)
    order = 0
    for c in g["chapters"]:
        cid = str(c.get("num"))
        if cid in ch_ids:
            errors.append(f"Capítulo repetido: {cid}")
        ch_ids.add(cid)
        if blocks and c.get("block") not in blocks:
            errors.append(f"Capítulo {cid}: bloque '{c.get('block')}' no está en 'blocks'.")
        if not c.get("title"):
            errors.append(f"Capítulo {cid} sin título.")
        if not c.get("sections"):
            warns.append(f"Capítulo {cid} no tiene secciones.")
        for s in c.get("sections", []):
            sid = str(s.get("num"))
            if sid in sec_ids:
                errors.append(f"Sección repetida: {sid}")
            sec_ids.add(sid)
            order += 1
            sec_order[sid] = order
            if s.get("page") is None:
                warns.append(f"Sección {sid} sin página.")
            for it in s.get("items", []):
                defined[it].append(sid)

    items = g["items"]
    for it, secs in defined.items():
        if it not in items:
            errors.append(f"La sección {secs[0]} presenta el ítem '{it}', que no existe en 'items'.")
        if len(secs) > 1:
            warns.append(f"El ítem '{it}' aparece en varias secciones {secs}; se tomará {secs[0]} como origen.")
    for it, v in items.items():
        if it not in defined:
            errors.append(f"El ítem '{it}' no lo presenta ninguna sección (agrégalo a 'items' de una sección).")
        if not v.get("title"):
            errors.append(f"Ítem '{it}' sin título.")
        if not v.get("summary"):
            warns.append(f"Ítem '{it}' sin resumen.")

    res_ids = set()
    for r in g.get("resources") or []:
        if r.get("id") in res_ids:
            errors.append(f"Recurso repetido: {r.get('id')}")
        res_ids.add(r.get("id"))
        for s in r.get("usedBy", []):
            if str(s) not in sec_ids:
                errors.append(f"Recurso {r.get('id')}: la sección '{s}' no existe.")

    req = g.get("requires") or {}
    universes = {"chapters": ch_ids, "sections": sec_ids, "items": {str(x) for x in items}}
    for level, universe in universes.items():
        graph = defaultdict(list)
        for a, bs in (req.get(level) or {}).items():
            a = str(a)
            if a not in universe:
                errors.append(f"requires.{level}: '{a}' no existe.")
            for b in bs:
                b = str(b)
                if b not in universe:
                    errors.append(f"requires.{level}: '{a}' requiere '{b}', que no existe.")
                elif a == b:
                    errors.append(f"requires.{level}: '{a}' se requiere a sí mismo.")
                graph[a].append(b)
                if level == "sections" and a in sec_order and b in sec_order and sec_order[b] > sec_order[a]:
                    warns.append(f"La sección {a} requiere {b}, que aparece después en el libro.")
        cyc = find_cycle(graph)
        if cyc:
            warns.append(f"Ciclo en requires.{level}: {' → '.join(cyc)}. Rompe el enlace menos importante.")

    stats = {
        "capítulos": len(ch_ids), "secciones": len(sec_ids), "ítems": len(items),
        "recursos": len(res_ids),
        "prerrequisitos": sum(len(v) for m in req.values() for v in (m or {}).values()),
    }
    return errors, warns, stats


def find_cycle(graph):
    color, stack = {}, []

    def dfs(u):
        color[u] = 1
        stack.append(u)
        for v in graph.get(u, []):
            if color.get(v) == 1:
                return stack[stack.index(v):] + [v]
            if color.get(v) is None:
                r = dfs(v)
                if r:
                    return r
        stack.pop()
        color[u] = 2
        return None

    for n in list(graph):
        if color.get(n) is None:
            r = dfs(n)
            if r:
                return r
    return None


def report(errors, warns, stats):
    if stats:
        print("Resumen: " + ", ".join(f"{v} {k}" for k, v in stats.items()))
    for w in warns:
        print("ADVERTENCIA:", w)
    for e in errors:
        print("ERROR:", e)
    print("OK" if not errors else f"{len(errors)} error(es): corrige antes de construir.")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        sys.exit(report(*validate(json.load(f))))
