"""Pruebas de contenido del grafo (no de renderizado). Uso: python3 scripts/pruebas.py salida/grafo.json
1) Control de copia: ningún texto del grafo comparte 8 palabras seguidas con el libro (trabajo/texto.txt).
2) Preguntas de control: la traza de cada pregunta pasa por los conceptos esperados (trabajo/sintesis.json).
3) Métricas: conceptos en menos de 2 secciones, conceptos sin enlaces, secciones sin conceptos.
Escribe trabajo/pruebas.md y sale con código 1 si falla 1) o 2)."""
import json, re, sys, unicodedata
g = json.load(open(sys.argv[1], encoding='utf-8'))
S = json.load(open('trabajo/sintesis.json', encoding='utf-8'))
def toks(t):
    t = unicodedata.normalize('NFKD', t.lower()).encode('ascii', 'ignore').decode()
    return re.findall(r'[a-z0-9]+', t)
book = toks(open('trabajo/texto.txt', encoding='utf-8').read())
N = 8
grams = {tuple(book[i:i+N]) for i in range(len(book) - N + 1)}
texts = []
for c in g["chapters"]:
    texts.append((f"cap {c['num']}", c.get("summary", "")))
    for s in c["sections"]: texts += [(f"sec {s['num']}", s.get("summary", "")), (f"sec {s['num']}.caution", s.get("caution", ""))]
for k, it in g["items"].items():
    for f in ("summary", "misconception", "formula", "caution"): texts.append((f"{k}.{f}", it.get(f, "") or ""))
for k, v in g.get("why", {}).items(): texts.append((f"why {k}", v))
copias = []
for where, t in texts:
    w = toks(t)
    hits = [" ".join(w[i:i+N]) for i in range(len(w) - N + 1) if tuple(w[i:i+N]) in grams]
    if hits: copias.append((where, hits[0]))
# trazas (misma lógica que la plantilla)
R = g["requires"]; sec_items = {s["num"]: s.get("items", []) for c in g["chapters"] for s in c["sections"]}
def trace_sec(sid):
    seen_s, seen_i = set(), set()
    qs, qi = [sid], list(sec_items.get(sid, []))
    while qs or qi:
        if qs:
            x = qs.pop()
            for y in R["sections"].get(x, []):
                if y not in seen_s: seen_s.add(y); qs.append(y)
        if qi:
            x = qi.pop()
            if x in seen_i: continue
            seen_i.add(x); qi += R["items"].get(x, [])
    return seen_s, seen_i
fallos = []
for p in S.get("preguntas_control", []):
    _, its = trace_sec(p["seccion"])
    falta = [c for c in p["debe_pasar_por"] if c not in its]
    fallos.append((p["pregunta"], p["seccion"], falta))
uso = {k: sum(1 for v in sec_items.values() if k in v) for k in g["items"]}
enl = {k: 0 for k in g["items"]}
for a, bs in R["items"].items():
    enl[a] = enl.get(a, 0) + len(bs)
    for b in bs: enl[b] = enl.get(b, 0) + 1
out = ["# Pruebas de contenido", "", f"## 1. Control de copia (8-gramas frente al libro)", f"Textos revisados: {len(texts)}. Coincidencias: {len(copias)}."]
out += [f"- {w}: «{h}»" for w, h in copias]
ok_q = sum(1 for *_, f in fallos if not f)
out += ["", f"## 2. Preguntas de control: {ok_q}/{len(fallos)} superadas"]
out += [f"- {'OK' if not f else 'FALLA'} · {q} ({s})" + (f" — falta: {', '.join(f)}" if f else "") for q, s, f in fallos]
out += ["", "## 3. Métricas",
        f"- Conceptos: {len(g['items'])}; en menos de 2 secciones: {[k for k, n in uso.items() if n < 2]}",
        f"- Conceptos sin enlaces conceptuales: {[k for k, n in enl.items() if n == 0]}",
        f"- Secciones sin conceptos: {sum(1 for v in sec_items.values() if not v)} de {len(sec_items)}",
        f"- Enlaces entre secciones con motivo: {sum(len(v) for v in R['sections'].values())}; entre conceptos: {sum(len(v) for v in R['items'].values())}"]
open('trabajo/pruebas.md', 'w', encoding='utf-8').write("\n".join(out) + "\n")
print("\n".join(out))
sys.exit(1 if copias or ok_q < len(fallos) else 0)
