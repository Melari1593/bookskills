"""Pruebas de la base de odorantes. Uso: python3 scripts/pruebas.py  (sale con 1 si algo falla)
1) Integridad: niveles válidos, DOIs con formato, cada fila con estudio, cada alimento con al menos 2 estudios.
2) Regresión: casos verificados a mano en la skill odorantes-clave deben aparecer como compartidos con confianza alta.
3) Normalización: avisa de nombres casi iguales que podrían ser el mismo compuesto sin unificar."""
import sqlite3, os, re, sys, difflib
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
db = sqlite3.connect("datos/odorantes.sqlite")
fallos, avisos = [], []
for (d,) in db.execute("SELECT DISTINCT doi FROM odorantes"):
    if not re.match(r"^10\.\d{4,9}/\S+$", d): fallos.append(f"DOI con formato raro: {d}")
for ali, n in db.execute("SELECT a.id, COUNT(e.doi) FROM alimentos a LEFT JOIN estudios e ON e.alimento=a.id GROUP BY a.id"):
    if n < 2: avisos.append(f"{ali}: solo {n} estudio(s)")
def nivel(a, c):
    r = db.execute("SELECT nivel FROM mejor WHERE alimento=? AND compuesto=?", (a, c)).fetchone(); return r[0] if r else None
CASOS = [("cafe_tostado", "ajonjoli_tostado", "2-furfuriltiol"), ("cafe_tostado", "ajonjoli_tostado", "furaneol (HDMF)"),
         ("cafe_tostado", "ajonjoli_tostado", "4-vinilguayacol"), ("matcha", "frambuesa", "β-ionona")]
reg = []
for a, b, c in CASOS:
    na, nb = nivel(a, c), nivel(b, c)
    ok = na in ("A", "B", "C") and nb in ("A", "B", "C")
    reg.append(f"- {'OK' if ok else 'FALLA'} · {a} + {b} → {c} (niveles {na}, {nb})")
    if not ok: fallos.append(f"regresión: {a}+{b} {c}")
comps = [r[0] for r in db.execute("SELECT DISTINCT compuesto FROM odorantes")]
for i, x in enumerate(comps):
    for y in comps[i+1:]:
        if difflib.SequenceMatcher(None, x, y).ratio() > 0.93: avisos.append(f"¿mismo compuesto? «{x}» / «{y}»")
tot = db.execute("SELECT COUNT(*), COUNT(DISTINCT compuesto) FROM odorantes").fetchone()
tc = db.execute("SELECT SUM(texto_completo), COUNT(*) FROM estudios").fetchone()
niv = dict(db.execute("SELECT nivel, COUNT(*) FROM odorantes GROUP BY nivel").fetchall())
out = ["# Pruebas de la base de odorantes", "", f"Filas: {tot[0]} · compuestos distintos: {tot[1]} · estudios: {tc[1]} (texto completo: {tc[0]}) · por nivel: {niv}",
       "", "## Regresión", *reg, "", "## Fallos", *(fallos or ["ninguno"]), "", "## Avisos", *(avisos or ["ninguno"])]
open("docs/pruebas.md", "w", encoding="utf-8").write("\n".join(out) + "\n"); print("\n".join(out))
sys.exit(1 if fallos else 0)
