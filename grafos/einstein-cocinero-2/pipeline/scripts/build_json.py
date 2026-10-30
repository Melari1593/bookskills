"""Construye grafo.json de Lo que Einstein le contó a su cocinero 2 (Robert L. Wolke).
Entradas: trabajo/toc.json, trabajo/conceptos.md, trabajo/resumenes_*.json. Uso: python3 scripts/build_json.py salida/grafo.json"""
import json, re, glob, sys
from collections import Counter
TOC = json.load(open('trabajo/toc.json', encoding='utf-8'))
TIT = {m.group(1): m.group(2).strip() for m in re.finditer(r'^\| (c_\w+) \| (.+?) \|$', open('trabajo/conceptos.md', encoding='utf-8').read(), re.M)}
R = {"chapters": {}, "sections": {}, "conceptos": {}, "conceptos_nuevos": {}}
for f in sorted(glob.glob('trabajo/resumenes_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    R["chapters"].update(d.get("chapters", {})); R["sections"].update(d.get("sections", {}))
    for k in ("conceptos", "conceptos_nuevos"):
        for c, v in d.get(k, {}).items(): R[k].setdefault(c, v)
for c, v in R["conceptos_nuevos"].items():
    TIT.setdefault(c, v["title"]); R["conceptos"].setdefault(c, v)
order = {s["id"]: i for i, s in enumerate(TOC["sections"])}
present = {}
for s in TOC["sections"]:
    for c in R["sections"].get(s["id"], {}).get("presenta", []): present.setdefault(c, []).append(s["id"])
canon = {}
for c in TIT:
    sec = R["conceptos"].get(c, {}).get("section")
    if sec not in order: sec = (present.get(c) or [None])[0]
    if sec: canon[c] = sec
items = {c: {"title": TIT[c], "summary": R["conceptos"].get(c, {}).get("summary", "")} for c in canon}
BLOCK = {1: "bebidas", 2: "granja", 3: "huerto", 4: "huerto", 5: "cereales", 6: "mar_carne", 7: "mar_carne", 8: "especias", 9: "cocina", 10: "cereales"}
chapters = []
for c in TOC["chapters"]:
    secs = []
    for s in TOC["sections"]:
        if s["ch"] != c["num"]: continue
        r = R["sections"].get(s["id"], {})
        its = [x for x in r.get("presenta", []) if x in items]
        its += [x for x, v in canon.items() if v == s["id"] and x not in its]
        sec = {"num": s["id"], "title": s["title"], "summary": r.get("summary", ""), "page": s["page"]}
        if its: sec["items"] = its
        secs.append(sec)
    chapters.append({"num": c["num"], "title": c["title"], "block": BLOCK[c["num"]], "page": c["page"],
                     "summary": R["chapters"].get(str(c["num"]), {}).get("summary", ""), "sections": secs})
req_sec = {}
for s in TOC["sections"]:
    deps = []
    for c in R["sections"].get(s["id"], {}).get("requiere", []):
        t = canon.get(c)
        if t and t != s["id"] and order[t] < order[s["id"]] and t not in deps: deps.append(t)
    if deps: req_sec[s["id"]] = deps[:4]
cnt = {}
for a, deps in req_sec.items():
    ca = int(a.split(".")[0])
    for b in deps:
        cb = int(b.split(".")[0])
        if cb < ca: cnt.setdefault(ca, Counter())[cb] += 1
req_ch = {str(a): [b for b, n in c.most_common(3) if n >= 2] for a, c in cnt.items()}
req_ch = {k: v for k, v in req_ch.items() if v}
DEP = {"c_indicadores": ["c_ph"], "c_clorofila": ["c_ph"], "c_maillard": ["c_proteinas", "c_azucares"], "c_caramelizacion": ["c_azucares"],
       "c_grasas_trans": ["c_grasas"], "c_oxidacion": ["c_grasas"], "c_punto_humo": ["c_grasas"], "c_emulsion": ["c_grasas", "c_solubilidad"],
       "c_espuma": ["c_proteinas"], "c_osmosis": ["c_solubilidad"], "c_curado": ["c_mioglobina", "c_osmosis"], "c_colageno": ["c_proteinas"],
       "c_pardeamiento_enzimatico": ["c_enzimas"], "c_gluten": ["c_proteinas"], "c_fermentacion": ["c_microbios", "c_azucares"],
       "c_alcohol": ["c_fermentacion"], "c_ebullicion": ["c_evaporacion"], "c_capacidad_calorifica": ["c_transferencia_calor"],
       "c_microondas": ["c_transferencia_calor"], "c_lacteos": ["c_proteinas", "c_grasas"], "c_huevo": ["c_proteinas"],
       "c_cristalizacion": ["c_solubilidad"], "c_conservacion": ["c_microbios"], "c_pungencia": ["c_gusto"], "c_polifenoles": ["c_gusto"],
       "c_cafeina": ["c_gusto"], "c_etileno": ["c_enzimas"], "c_azufrados": ["c_aroma"], "c_gases_disueltos": ["c_solubilidad"]}
req_it = {}
for a, bs in DEP.items():
    if a in items:
        v = [b for b in bs if b in items and order[canon[b]] < order[canon[a]]]
        if v: req_it[a] = v
n_sec = len(TOC["sections"])
g = {"meta": {"title": "Lo que Einstein le contó a su cocinero 2 como grafo",
  "subtitle": f"Robert L. Wolke · química y física de la cocina: 10 capítulos, {n_sec} preguntas y {len(items)} conceptos científicos",
  "language": "es", "itemLabel": "Concepto científico", "itemLabelPlural": "Conceptos científicos",
  "resourceLabel": "Recurso", "resourceLabelPlural": "Recursos", "searchHint": "Buscar: Maillard, emulsión, hielo, aguacate…"},
 "blocks": {"bebidas": {"name": "Bebidas", "color": "#3F6FA0"}, "granja": {"name": "Lácteos y huevos", "color": "#B08A2E"},
            "huerto": {"name": "Verduras, legumbres, frutas y aceites", "color": "#4E8A5B"},
            "cereales": {"name": "Cereales, azúcares y dulces", "color": "#A05A3C"},
            "mar_carne": {"name": "Pescados, mariscos y carnes", "color": "#B5465A"},
            "especias": {"name": "Especias y sabores", "color": "#C07A1E"}, "cocina": {"name": "La cocina y sus utensilios", "color": "#6B5B95"}},
 "chapters": chapters, "items": items, "resources": [],
 "requires": {"chapters": req_ch, "sections": req_sec, "items": req_it}}
json.dump(g, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("secciones", n_sec, "conceptos", len(items), "prerreq. secciones", len(req_sec), "capítulos", req_ch,
      "faltan resúmenes", [s["id"] for s in TOC["sections"] if s["id"] not in R["sections"]])
