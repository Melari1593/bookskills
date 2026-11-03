"""Construye grafo.json de un capítulo a partir de un archivo de definición (capitulo.py) y trabajo/alertas.json.
Uso (desde la carpeta del capítulo): python3 ../grafos-nuts-comun/construir.py salida/grafo.json"""
import json, os, sys, importlib.util
spec = importlib.util.spec_from_file_location("cap", "scripts/capitulo.py"); cap = importlib.util.module_from_spec(spec); spec.loader.exec_module(cap)
AL = json.load(open('trabajo/alertas.json', encoding='utf-8')) if os.path.exists('trabajo/alertas.json') else {}
items = {}
for k, v in cap.ITEMS.items():
    t, s = v[0], v[1]; f = v[2] if len(v) > 2 else ""
    it = {"title": t, "summary": s}
    if f: it["formula"] = f
    if AL.get(k): it["caution"] = AL[k]
    items[k] = it
g = {"meta": cap.META, "blocks": cap.BLOCKS, "chapters": cap.CHAPTERS, "items": items, "resources": getattr(cap, "RESOURCES", []),
     "requires": {"chapters": cap.REQ_CH, "sections": cap.REQ_SEC, "items": cap.REQ_IT}}
json.dump(g, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("partes", len(cap.CHAPTERS), "secciones", sum(len(c["sections"]) for c in cap.CHAPTERS), "ítems", len(items),
      "alertas", sum('caution' in v for v in items.values()), "alertas sin ítem", [k for k in AL if k not in items])
