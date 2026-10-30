"""Construye salida/grafo.json (versión profunda) de Lo que Einstein le contó a su cocinero 2 (Robert L. Wolke).
Entradas: trabajo/toc.json (estructura y páginas), trabajo/resumenes_*.json (resúmenes parafraseados de capítulos y secciones),
trabajo/sintesis.json (conceptos con tres capas, enlaces con tipo y motivo, requisitos entre secciones),
trabajo/correcciones.json (opcional: revisión independiente), trabajo/alertas_*.json (opcional: {id_sección: alerta de vigencia científica}).
Uso: python3 scripts/build_json.py salida/grafo.json"""
import json, glob, os, sys
TOC = json.load(open('trabajo/toc.json', encoding='utf-8'))
S = json.load(open('trabajo/sintesis.json', encoding='utf-8'))
AL = {}   # alertas de vigencia por sección (verificación frente a la ciencia actual)
for f in sorted(glob.glob('trabajo/alertas_*.json')): AL.update(json.load(open(f, encoding='utf-8')))
RS = {"chapters": {}, "sections": {}}
for f in sorted(glob.glob('trabajo/resumenes_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for k in RS: RS[k].update(d.get(k, {}))
order = {s["id"]: i for i, s in enumerate(TOC["sections"])}
# correcciones de la revisión independiente (trabajo/correcciones.json), si existen
CO = json.load(open('trabajo/correcciones.json', encoding='utf-8')) if os.path.exists('trabajo/correcciones.json') else {}
FIELD = {"summary": "mecanismo", "misconception": "error_comun", "formula": "en_cocina"}
for cid, ch in CO.get("items", {}).items():
    for f, v in ch.items():
        if cid in S["conceptos"]: S["conceptos"][cid][FIELD.get(f, f)] = v.removeprefix("En la cocina: ")
for sid, ch in CO.get("sections", {}).items():
    RS["sections"].setdefault(sid, {}).update(ch)
quitar = {tuple(x) for x in CO.get("quitar_enlaces", [])}
S["enlaces_conceptos"] = [e for e in S["enlaces_conceptos"] if (e["de"], e["a"]) not in quitar] + CO.get("anadir_enlaces", [])
C = S["conceptos"]

items = {}
for cid, c in C.items():
    it = {"title": c["title"], "summary": c["mecanismo"], "misconception": c.get("error_comun", ""),
          "formula": "En la cocina: " + c["en_cocina"] if c.get("en_cocina") else ""}
    items[cid] = {k: v for k, v in it.items() if v}

# sección → conceptos; la sección de origen va primero para que la plantilla la tome como "dónde se presenta"
sec_items = {sid: list(v.get("conceptos", [])) for sid, v in S["secciones"].items()}
for cid, c in C.items():
    for sid in c.get("secciones", []):
        sec_items.setdefault(sid, [])
        if cid not in sec_items[sid]: sec_items[sid].append(cid)
first = {}
for s in TOC["sections"]:
    for cid in sec_items.get(s["id"], []): first.setdefault(cid, s["id"])
for cid, c in C.items():   # el origen declarado debe ser la primera aparición; si no, se usa la primera
    if c.get("origen") in order and order[c["origen"]] <= order[first.get(cid, c["origen"])]: first[cid] = c["origen"]
for sid in sec_items:
    sec_items[sid] = [x for x in sec_items[sid] if x in items]
for cid, sid in first.items():   # quita el concepto de secciones anteriores a su origen
    for s in TOC["sections"]:
        if order[s["id"]] < order[sid] and cid in sec_items.get(s["id"], []): sec_items[s["id"]].remove(cid)

BLOCK = {1: "bebidas", 2: "granja", 3: "huerto", 4: "huerto", 5: "cereales", 6: "mar_carne", 7: "mar_carne", 8: "especias", 9: "cocina", 10: "cereales"}
chapters = []
for c in TOC["chapters"]:
    secs = []
    for s in TOC["sections"]:
        if s["ch"] != c["num"]: continue
        sec = {"num": s["id"], "title": s["title"], "summary": RS["sections"].get(s["id"], {}).get("summary", ""), "page": s["page"]}
        if sec_items.get(s["id"]): sec["items"] = sec_items[s["id"]]
        if AL.get(s["id"]): sec["caution"] = AL[s["id"]]
        secs.append(sec)
    chapters.append({"num": c["num"], "title": c["title"], "block": BLOCK[c["num"]], "page": c["page"],
                     "summary": RS["chapters"].get(str(c["num"]), {}).get("summary", ""), "sections": secs})

why = {}
req_sec = {}
for sid, v in S["secciones"].items():
    for r in v.get("requiere", []):
        if r["sec"] in order and order[r["sec"]] < order[sid]:
            req_sec.setdefault(sid, []).append(r["sec"]); why[f"s{sid}>s{r['sec']}"] = r["porque"]
req_it = {}
contr = {}
for e in S["enlaces_conceptos"]:   # "contrasta con" no es dependencia: se muestra como texto en ambos conceptos
    if e["tipo"].startswith("contrasta") and e["de"] in items and e["a"] in items:
        contr.setdefault(e["de"], []).append(f'{items[e["a"]]["title"]} ({e["porque"]})')
        contr.setdefault(e["a"], []).append(f'{items[e["de"]]["title"]} ({e["porque"]})')
for k, v in contr.items(): items[k]["contrasts"] = "; ".join(v)
for e in S["enlaces_conceptos"]:
    if e["tipo"].startswith("contrasta"): continue
    a, b = e["de"], e["a"]
    if a in items and b in items and a != b:
        req_it.setdefault(a, [])
        if b not in req_it[a]: req_it[a].append(b)
        why[f"i:{a}>i:{b}"] = f"{e['tipo'].capitalize()}: {e['porque']}"
req_ch = {k: v["requiere"] for k, v in S.get("capitulos", {}).items() if v.get("requiere")}

g = {"meta": {"title": "Lo que Einstein le contó a su cocinero 2 como grafo",
  "subtitle": f"Robert L. Wolke · química y física de la cocina: {len(TOC['sections'])} preguntas y {len(items)} conceptos con su mecanismo, el error que corrigen y su uso en la cocina",
  "language": "es", "itemLabel": "Concepto científico", "itemLabelPlural": "Conceptos científicos",
  "resourceLabel": "Recurso", "resourceLabelPlural": "Recursos", "searchHint": "Buscar: Maillard, emulsión, yema verde, aguacate…"},
 "blocks": {"bebidas": {"name": "Bebidas", "color": "#3F6FA0"}, "granja": {"name": "Lácteos y huevos", "color": "#B08A2E"},
            "huerto": {"name": "Verduras, legumbres, frutas y aceites", "color": "#4E8A5B"},
            "cereales": {"name": "Cereales, azúcares y dulces", "color": "#A05A3C"},
            "mar_carne": {"name": "Pescados, mariscos y carnes", "color": "#B5465A"},
            "especias": {"name": "Especias y sabores", "color": "#C07A1E"}, "cocina": {"name": "La cocina y sus utensilios", "color": "#6B5B95"}},
 "chapters": chapters, "items": items, "resources": [],
 "requires": {"chapters": req_ch, "sections": req_sec, "items": req_it}, "why": why}
json.dump(g, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("secciones", len(TOC["sections"]), "conceptos", len(items), "alertas", sum(1 for c in chapters for x in c["sections"] if "caution" in x), "alertas sin sección", [k for k in AL if k not in order],
      "requisitos sección", sum(map(len, req_sec.values())), "enlaces concepto", sum(map(len, req_it.values())), "motivos", len(why))
