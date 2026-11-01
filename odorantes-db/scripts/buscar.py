"""Búsqueda de texto (la capa RAG) sobre las notas propias de cada estudio, con fuente.
Uso: python3 scripts/buscar.py "nota de alga matcha"   (operadores FTS5: AND, OR, NOT, "frase", prefijo*)"""
import sqlite3, sys, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
db = sqlite3.connect("datos/odorantes.sqlite")
q = " ".join(sys.argv[1:]) or sys.exit(__doc__)
terms = q if any(op in q for op in ('"', " AND ", " OR ", " NOT ", "*")) else " OR ".join(q.split())
for doi, ali, snip, rank in db.execute("SELECT doi, alimento, snippet(notas, 2, '«', '»', '…', 24), bm25(notas) FROM notas WHERE notas MATCH ? ORDER BY bm25(notas) LIMIT 8", (terms,)):
    e = db.execute("SELECT autor, anio, metodos FROM estudios WHERE doi=?", (doi,)).fetchone()
    print(f"- **{e[0]} {e[1]}** · {ali} · {e[2]}\n  {snip}\n  https://doi.org/{doi}")
