"""Busca un punto, síntoma o concepto en el grafo combinado de Dalet, Rosenfarb y Patzek.

Uso:
  python scripts/buscar.py "SP6"            # código OMS de un punto
  python scripts/buscar.py "náuseas"        # síntoma o concepto (sin acentos también vale)
  python scripts/buscar.py "P3.5"           # número de sección (D=Dalet, R=Rosenfarb, P=Patzek, X=puentes)
  python scripts/buscar.py "migraña" --max 5

Imprime las secciones y los ítems encontrados, su libro, los prerrequisitos directos,
la evidencia de PubMed relacionada y las alertas ⚠.
"""
import json, re, sys, unicodedata, pathlib, argparse

ap = argparse.ArgumentParser()
ap.add_argument("termino")
ap.add_argument("--max", type=int, default=8)
ap.add_argument("--grafo", default=str(pathlib.Path(__file__).resolve().parent.parent / "references" / "grafo.json"))
a = ap.parse_args()
g = json.load(open(a.grafo, encoding="utf-8"))
LIB = {"D": "Dalet", "R": "Rosenfarb", "P": "Patzek", "X": "Puentes"}

def norm(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()

secs, owner = {}, {}
for c in g["chapters"]:
    for s in c["sections"]:
        secs[s["num"]] = s
        for i in s.get("items", []): owner[i] = s["num"]
items, rq = g["items"], g["requires"]
q = a.termino.strip()
code = re.fullmatch(r"[A-Za-z]{2}\d{1,2}", q)
pat = re.compile(rf"\b{re.escape(q.upper())}\b") if code else None
nq = norm(q)

def hit(text):
    return bool(pat.search(text)) if code else nq in norm(text)

hs = [n for n, s in secs.items() if n.upper() == q.upper() or hit(s["title"] + " " + s.get("summary", ""))]
hi = [k for k, v in items.items() if hit(v["title"] + " " + v.get("summary", ""))]
# ordena: puentes primero, luego por libro
key = lambda n: ("XDRP".index(n[0]) if n[0] in "XDRP" else 9, n)
hs.sort(key=key)
# ítems con el término en el título primero; luego evidencia; luego el resto
hi.sort(key=lambda k: (not hit(items[k]["title"]), "PMID" not in items[k].get("summary", ""), key(owner.get(k, "Z"))))

def libro(n): return LIB.get(n[0], "?")

print(f"# «{q}»: {len(hs)} secciones, {len(hi)} ítems\n")
if hs:
    print("## Secciones")
    for n in hs[: a.max]:
        s = secs[n]
        print(f"- {n} [{libro(n)}] {s['title']}: {s.get('summary', '')[:400]}")
        if rq["sections"].get(n): print(f"  antes leer: {', '.join(rq['sections'][n][:12])}")
    if len(hs) > a.max: print(f"  … {len(hs) - a.max} más (usa --max)")
if hi:
    print("\n## Ítems")
    for k in hi[: a.max]:
        v, n = items[k], owner.get(k, "?")
        print(f"- {k} [{libro(n)} {n}] {v['title']}: {v.get('summary', '')[:500]}")
        if rq["items"].get(k): print(f"  depende de: {', '.join(rq['items'][k][:10])}")
    if len(hi) > a.max: print(f"  … {len(hi) - a.max} más (usa --max)")

# evidencia y alertas relacionadas
found = set(hi) | {i for n in hs for i in secs[n].get("items", [])}
ev = [k for k, v in items.items() if "PMID" in v.get("summary", "") and
      (k in found or set(rq["items"].get(k, [])) & found or set(rq["sections"].get(owner.get(k, ""), [])) & set(hs))]
if ev:
    print("\n## Evidencia de PubMed relacionada")
    for k in ev:
        print(f"- {items[k]['title']} ({libro(owner.get(k, 'X'))}): {items[k]['summary']}")
al = [k for k in found if "⚠" in items[k].get("summary", "")]
if al:
    print("\n## Alertas ⚠")
    for k in al:
        s = items[k]["summary"]; print(f"- {items[k]['title']}: {s[s.index('⚠'):][:300]}")
if not hs and not hi:
    print("Sin resultados. Prueba el código OMS (SP6), otra palabra o el nombre en pinyin.")
