"""Consulta la base de odorantes.
  python3 scripts/consulta.py A B          → odorantes clave compartidos por A y B, con confianza y fuentes
  python3 scripts/consulta.py A            → perfil de A y alimentos con más odorantes clave en común
Confianza (regla de la skill odorantes-clave): alta = nivel A–C en ambos; media = A–C en uno y D en el otro; baja = D en ambos."""
import sqlite3, sys, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
db = sqlite3.connect("datos/odorantes.sqlite")
fuerte = lambda n: n in ("A", "B", "C")
def conf(a, b): return "alta" if fuerte(a) and fuerte(b) else ("media" if fuerte(a) or fuerte(b) else "baja")
def perfil(x): return {r[0]: r[1:] for r in db.execute("SELECT compuesto, nivel, dois, descriptor, tipo FROM mejor WHERE alimento=?", (x,))}
def doi_links(s): return "; ".join(f"[{d}](https://doi.org/{d})" for d in s.split(","))
ids = [r[0] for r in db.execute("SELECT id FROM alimentos")]
args = sys.argv[1:]
for a in args:
    if a not in ids: sys.exit(f"Alimento desconocido: {a}. Opciones: {', '.join(ids)}")
if len(args) == 2:
    A, B = args; pa, pb = perfil(A), perfil(B)
    comunes = sorted(set(pa) & set(pb), key=lambda c: ("alta media baja".split().index(conf(pa[c][0], pb[c][0])), pa[c][0] + pb[c][0]))
    print(f"## Odorantes compartidos: {A} + {B} ({len(comunes)})\n")
    print("| Compuesto | Olor | Tipo | Nivel en A | Nivel en B | Confianza | Fuentes A | Fuentes B |\n|---|---|---|---|---|---|---|---|")
    for c in comunes:
        print(f"| {c} | {pa[c][2] or pb[c][2] or ''} | {pa[c][3] or pb[c][3] or ''} | {pa[c][0]} | {pb[c][0]} | {conf(pa[c][0], pb[c][0])} | {doi_links(pa[c][1])} | {doi_links(pb[c][1])} |")
    for X, P, Q in ((A, pa, pb), (B, pb, pa)):
        propios = sorted([c for c in P if c not in Q and fuerte(P[c][0])], key=lambda c: P[c][0])[:10]
        print(f"\n**Propios de {X} (nivel A–C):** " + ", ".join(f"{c} ({P[c][2] or '—'})" for c in propios))
elif len(args) == 1:
    A = args[0]; pa = perfil(A)
    print(f"## Perfil de {A}: {len(pa)} odorantes\n")
    for c, (n, d, desc, t) in sorted(pa.items(), key=lambda x: x[1][0]): print(f"- {n} · {c} · {desc or ''} · {t}")
    print(f"\n## Alimentos con más odorantes clave compartidos (confianza alta)")
    rank = []
    for B in ids:
        if B == A: continue
        pb = perfil(B); n = [c for c in set(pa) & set(pb) if conf(pa[c][0], pb[c][0]) == "alta"]
        if n: rank.append((len(n), B, n))
    for k, B, n in sorted(rank, reverse=True): print(f"- {B}: {k} ({', '.join(sorted(n))})")
else:
    print(__doc__)
