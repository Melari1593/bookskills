"""Construye datos/odorantes.sqlite y datos/odorantes.csv a partir de datos/extracciones/*.json.
Normaliza nombres con datos/sinonimos.json y crea un índice FTS5 sobre las notas propias de cada estudio
(nunca sobre texto de los artículos). Uso: python3 scripts/build_db.py"""
import json, glob, sqlite3, csv, re, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ALI = json.load(open("datos/alimentos.json", encoding="utf-8"))
SIN = {k.lower(): v for k, v in json.load(open("datos/sinonimos.json", encoding="utf-8")).items()}

def clave(n):
    n = n.strip().lower().replace("’", "'").replace("–", "-")
    n = re.sub(r"\s+", " ", n)
    return n
def normaliza(n):
    k = clave(n)
    if k in SIN: return SIN[k]
    k2 = re.sub(r"^\((e|z|r|s)\)-", "", k)          # prueba sin estereodescriptor inicial
    if k2 in SIN: return SIN[k2]
    return k

# tipos de aroma (14 de Foodpairing) a partir del descriptor del estudio: heurística por palabras clave
TIPOS = [("tostado", ["tostad", "café", "roast", "palomita", "pan", "cereal", "malta"]), ("frutos secos", ["nuez", "frutos secos", "almendra", "avellana", "maní", "nut"]),
         ("caramelo", ["caramel", "dulce", "algodón", "miel", "azúcar"]), ("especiado", ["clavo", "especia", "canela", "pimienta", "anís", "curry"]),
         ("leñoso", ["ahumad", "humo", "madera", "leñ", "fenól"]), ("floral", ["floral", "rosa", "violeta", "flor", "jazmín", "miel"]),
         ("cítrico", ["cítric", "limón", "naranja", "pomelo", "lima"]), ("frutal", ["frutal", "fruta", "manzana", "plátano", "piña", "fresa", "melocot", "grosella", "coco", "mango"]),
         ("verde", ["verde", "hierba", "pepino", "césped", "hoja"]), ("herbal", ["herb", "menta", "eucalipto"]),
         ("vegetal", ["papa", "patata", "col", "maíz", "vegetal", "tomate", "alga", "champiñ", "seta", "terroso", "tierra"]),
         ("quesero", ["queso", "mantec", "lácte", "crem", "rancio", "sudor", "ácido"]), ("animal", ["carne", "cárnic", "animal", "pescad"]),
         ("químico", ["metálic", "químic", "azufr", "sulfur", "gas", "medicin"])]
def tipo(desc):
    d = (desc or "").lower()
    for t, ws in TIPOS:
        if any(w in d for w in ws): return t
    return ""

est, odo = [], []
for f in sorted(glob.glob("datos/extracciones/lote_*.json")):
    d = json.load(open(f, encoding="utf-8"))
    est += d.get("estudios", []); odo += d.get("odorantes", [])
errores = []
dois = {e["doi"] for e in est}
for o in odo:
    if o["doi"] not in dois: errores.append(f"odorante sin estudio: {o['doi']} {o['nombre']}")
    if o.get("nivel") not in ("A", "B", "C", "D"): errores.append(f"nivel inválido: {o}")
    if o.get("alimento") not in ALI: errores.append(f"alimento inválido: {o.get('alimento')}")

if os.path.exists("datos/odorantes.sqlite"): os.remove("datos/odorantes.sqlite")
db = sqlite3.connect("datos/odorantes.sqlite")
db.executescript("""
CREATE TABLE alimentos(id TEXT PRIMARY KEY, nombre TEXT, en TEXT);
CREATE TABLE estudios(doi TEXT, pmid TEXT, pmcid TEXT, autor TEXT, anio INT, alimento TEXT, muestra TEXT, metodos TEXT,
                      texto_completo INT, licencia TEXT, nota TEXT);
CREATE TABLE odorantes(alimento TEXT, compuesto TEXT, nombre_original TEXT, descriptor TEXT, tipo TEXT, fd REAL, oav REAL,
                       nivel TEXT, doi TEXT, ubicacion TEXT);
CREATE VIEW mejor AS SELECT alimento, compuesto, MIN(nivel) AS nivel, GROUP_CONCAT(DISTINCT doi) AS dois,
       MAX(descriptor) AS descriptor, MAX(tipo) AS tipo, COUNT(DISTINCT doi) AS n_estudios
       FROM odorantes GROUP BY alimento, compuesto;
CREATE VIRTUAL TABLE notas USING fts5(doi, alimento, texto, tokenize='unicode61 remove_diacritics 2');
""")
db.executemany("INSERT INTO alimentos VALUES (?,?,?)", [(k, v["nombre"], v["en"]) for k, v in ALI.items()])
for e in est:
    db.execute("INSERT INTO estudios VALUES (?,?,?,?,?,?,?,?,?,?,?)", (e["doi"], e.get("pmid"), e.get("pmcid"), e.get("autor"), e.get("anio"),
               e["alimento"], e.get("muestra"), ", ".join(e.get("metodos", [])), int(bool(e.get("texto_completo"))), e.get("licencia"), e.get("nota")))
for o in odo:
    db.execute("INSERT INTO odorantes VALUES (?,?,?,?,?,?,?,?,?,?)", (o["alimento"], normaliza(o["nombre"]), o["nombre"], o.get("descriptor"),
               tipo(o.get("descriptor")), o.get("fd"), o.get("oav"), o["nivel"], o["doi"], o.get("ubicacion")))
for e in est:
    comps = ", ".join(sorted({normaliza(o["nombre"]) for o in odo if o["doi"] == e["doi"]}))
    db.execute("INSERT INTO notas VALUES (?,?,?)", (e["doi"], e["alimento"], f"{ALI[e['alimento']]['nombre']}. {e.get('muestra','')}. "
               f"Métodos: {', '.join(e.get('metodos', []))}. {e.get('nota','')} Compuestos: {comps}"))
db.commit()
with open("datos/odorantes.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["alimento", "compuesto", "nombre_original", "descriptor", "tipo", "fd", "oav", "nivel", "doi", "ubicacion"])
    w.writerows(db.execute("SELECT * FROM odorantes ORDER BY alimento, nivel, compuesto"))
n = db.execute("SELECT COUNT(DISTINCT compuesto) FROM odorantes").fetchone()[0]
print(f"estudios {len(est)} · filas {len(odo)} · compuestos distintos {n} · alimentos con datos "
      f"{db.execute('SELECT COUNT(DISTINCT alimento) FROM estudios').fetchone()[0]}/{len(ALI)}")
for e in errores: print("ERROR:", e)
sys.exit(1 if errores else 0)
