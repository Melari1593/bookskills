"""Combina los grafos de Dalet, Rosenfarb y Patzek en un solo grafo.json con puentes de puntos y evidencia de PubMed.
Uso: python3 -I combinar.py <bookskills_dir> <salida.json>
"""
import json, re, sys, glob, collections

B, OUT = sys.argv[1], sys.argv[2]
G = B + "/grafos/"
BOOKS = [
    ("D", "dal", "Dalet · Autoacupresión", G + "dalet-acupressure-self-care/grafo_dalet_acupressure.json", "Dalet"),
    ("R", "ros", "Rosenfarb · Ojos", G + "rosenfarb-healing-your-eyes/grafo_rosenfarb_healing_eyes.json", "Rosenfarb"),
    ("P", "pat", "Patzek · Mujeres", G + "patzek-mtc-para-mujeres/grafo_patzek_mtc_mujeres.json", "Patzek"),
]
CODE = re.compile(r"\b(LU|LI|ST|SP|HT|SI|BL|KI|PC|TE|GB|LR|CV|GV)(\d{1,2})\b")

# fichas de la skill acupuntura-puntos: código -> pinyin
PIN = {}
for f in glob.glob(B + "/.claude/skills/acupuntura-puntos/references/*.md"):
    for m in re.finditer(r"^### ([A-Z]{2}\d{1,2}) · (.+)$", open(f, encoding="utf-8").read(), re.M):
        PIN.setdefault(m.group(1), m.group(2).strip())
EMB = {"LI4", "SP6", "BL60", "BL67", "GB21", "BL31", "BL32", "BL33", "BL34"}

out = {"meta": {"title": "Acupresión en tres libros: Dalet, Rosenfarb y Patzek",
                "subtitle": "Grafo combinado con puntos compartidos, evidencia de PubMed y alertas de seguridad (consulta 2026-11-26)",
                "itemLabel": "Punto o concepto", "itemLabelPlural": "Puntos y conceptos",
                "chapterLabel": "Capítulo", "searchHint": "SP6, náuseas, migraña…"},
       "blocks": {}, "chapters": [], "items": {}, "resources": [],
       "requires": {"chapters": {}, "sections": {}, "items": {}}}
use = collections.defaultdict(lambda: collections.defaultdict(list))  # code -> libro -> [secciones]
sectitle, itemmap = {}, {}

for P, bid, bname, path, short in BOOKS:
    g = json.load(open(path, encoding="utf-8"))
    out["blocks"][bid] = {"name": bname}
    pre = P.lower() + "_"
    for c in g["chapters"]:
        cc = {"num": P + str(c["num"]), "title": c["title"], "block": bid, "summary": c.get("summary", ""), "sections": []}
        for s in c["sections"]:
            ns = P + s["num"]
            ss = {"num": ns, "title": s["title"], "summary": s.get("summary", ""), "items": [pre + i for i in s.get("items", [])]}
            if s.get("page"): ss["page"] = s["page"]
            cc["sections"].append(ss); sectitle[ns] = f"{short} {s['num']} {s['title']}"
        out["chapters"].append(cc)
    for k, v in g["items"].items():
        out["items"][pre + k] = v; itemmap[pre + k] = v["title"]
    for r in g.get("resources", []):
        r2 = dict(r); r2["id"] = P + "-" + r["id"]; r2["title"] = short + ": " + r["title"]
        r2["usedBy"] = [P + u for u in r.get("usedBy", [])]; out["resources"].append(r2)
    rq = g.get("requires", {})
    for k, v in rq.get("chapters", {}).items(): out["requires"]["chapters"][P + str(k)] = [P + str(x) for x in v]
    for k, v in rq.get("sections", {}).items(): out["requires"]["sections"][P + k] = [P + x for x in v]
    for k, v in rq.get("items", {}).items(): out["requires"]["items"][pre + k] = [pre + x for x in v]

# uso de puntos por sección
dal = json.load(open(G + "dalet-acupressure-self-care/cruce_acupuntura_puntos.json", encoding="utf-8"))
for s, d in dal["sections"].items():
    for c in d["book"]:
        if not c.startswith("x:"): use[c]["Dalet"].append("D" + s)
pat = json.load(open(G + "patzek-mtc-para-mujeres/cruce_acupuntura_puntos.json", encoding="utf-8"))
for s, cs in pat["puntos"].items():
    for c in cs:
        c = "BL40" if c == "BL54" else c  # numeración antigua del libro: V 54 = BL40
        use[c]["Patzek"].append("P" + s)
ros = json.load(open(BOOKS[1][3], encoding="utf-8"))
for c in ros["chapters"]:
    for s in c["sections"]:
        txt = s.get("summary", "") + " " + " ".join(ros["items"][i]["title"] + " " + ros["items"][i].get("summary", "") for i in s.get("items", []))
        for m in set(a + b for a, b in CODE.findall(txt)):
            use[m]["Rosenfarb"].append("R" + s["num"])

# ---------- capítulo X1: puntos compartidos ----------
shared = sorted([c for c in use if len(use[c]) >= 2], key=lambda c: (-len(use[c]), -sum(map(len, use[c].values())), c))
x1 = {"num": "X1", "title": "Puntos compartidos entre libros", "block": "x",
      "summary": f"{len(shared)} puntos aparecen en al menos dos libros. Cada sección traza las secciones de cada libro que usan el punto.", "sections": []}
for c in shared:
    iid = "x_" + c.lower()
    libros = "; ".join(f"{b}: " + ", ".join(sectitle[s].split(' ', 1)[1] for s in v) for b, v in use[c].items())
    warn = " ⚠ Prohibido o con precaución en el embarazo (skill acupuntura-puntos)." if c in EMB else ""
    out["items"][iid] = {"title": f"{c} · {PIN.get(c, '')}".strip(" ·"), "summary": f"En {len(use[c])} libros. {libros}.{warn}"}
    x1["sections"].append({"num": "X1." + c, "title": f"{c} {PIN.get(c, '')}".strip(), "items": [iid],
                           "summary": f"Usado en {', '.join(use[c])}."})
    out["requires"]["sections"]["X1." + c] = sorted({s for v in use[c].values() for s in v})
    rel = [k for k, t in itemmap.items() if re.search(rf"\b{c}\b", t)]
    if rel: out["requires"]["items"][iid] = rel

# ---------- capítulo X2: evidencia PubMed ----------
F = " Consultado en PubMed el 2026-11-26."
EV = [
 ("X2.1", "Dolor y aparato locomotor", ["D3.7", "D3.8", "D3.9", "D7.1", "P3.6"], [
  ("ev_lumbar", "Evidencia: acupresión en lumbalgia crónica", "Revisión sistemática 2020 de 6 ECA (468 adultos): todos encontraron menos dolor y discapacidad y mejor sueño, sin efectos adversos graves. Son pocos estudios y pequeños (PMID 32379678, doi:10.1016/j.ctcp.2020.101146).", []),
  ("ev_migr", "Evidencia: acupuntura en la prevención de la migraña", "Cochrane 2016, 22 ECA (4985 personas): reduce la frecuencia de crisis frente a no tratar; frente a la acupuntura simulada el efecto es pequeño; es al menos similar a los fármacos preventivos, con menos efectos adversos. Certeza moderada. Se refiere a agujas, no a acupresión (PMID 27351677, doi:10.1002/14651858.CD001218.pub3).", ["x_li4", "x_gb20"])]),
 ("X2.2", "Sueño, ánimo y digestión", ["D12.2", "D12.3", "D10.6", "D4.5", "P3.4", "P4.9", "P4.11"], [
  ("ev_insomnio", "Evidencia: acupresión en insomnio", "Metanálisis 2025 (42 ECA de higiene del sueño): la acupresión fue superior a la sola educación en higiene del sueño (ISI, 1,9 puntos), con 86 % de ensayos de alto riesgo de sesgo (PMID 40449065, doi:10.1016/j.smrv.2025.102109). En el insomnio por quimioterapia, la acupresión auricular mejoró el sueño en 14 ECA de baja calidad (PMID 40472678, doi:10.1016/j.explore.2025.103188). La terapia cognitivo-conductual sigue siendo el primer tratamiento.", []),
  ("ev_ansiedad", "Evidencia: acupresión en ansiedad", "Metanálisis 2022 de 27 ECA: reduce la ansiedad, sobre todo antes de una cirugía, con heterogeneidad muy alta (PMID 35085025, doi:10.1089/jicm.2020.0256). La acupresión auricular también la reduce (25 ECA, sesgo en 23) (PMID 38417402, doi:10.1159/000537734).", ["x_pc6"]),
  ("ev_estren", "Evidencia: acupresión en estreñimiento", "Acupresión auricular, 34 ECA (2023): más deposiciones espontáneas, certeza baja a muy baja (PMID 37908337, doi:10.3389/fphys.2023.1257660). Masaje abdominal, 23 estudios (2024): más deposiciones y menos síntomas; la variante con acupresión tuvo el mayor efecto, con pocos estudios (PMID 39531948, doi:10.1016/j.ijnurstu.2024.104936).", ["x_st36"])]),
 ("X2.3", "Ojos", ["R4.3", "R7.6", "R7.10", "R7.12", "R5.1", "D1.2", "D1.3", "D1.4"], [
  ("ev_ojo_seco", "Evidencia: acupuntura en ojo seco", "Metanálisis 2024 de 16 ensayos: junto con lágrimas artificiales mejora la ruptura lagrimal y el test de Schirmer, sin cambio en los síntomas (OSDI) (PMID 38181299, doi:10.1097/MD.0000000000036374). Otro análisis 2023 propone combinaciones como KI3-LI4-SP6 o KI3-BL1-EX-HN7-SP6 (PMID 37539212, doi:10.1016/j.heliyon.2023.e18226).", ["x_bl1", "x_li4"]),
  ("ev_miopia", "Evidencia: acupresión auricular en miopía infantil", "Revisión 2020 de 10 ECA: podría frenar la progresión, con baja calidad y poco seguimiento (PMID 31672461, doi:10.1016/j.ctcp.2019.101067). No sustituye la corrección óptica ni los tratamientos indicados por oftalmología.", []),
  ("ev_ojos_sintesis", "Síntesis: degeneraciones de la retina y glaucoma", "La acupuntura en DMAE, retinosis pigmentaria y glaucoma tiene certeza baja o muy baja (ver evidencia de Rosenfarb). ⚠ No retrasar anti-VEGF, hipotensores oculares ni controles.", ["r_ev_dmae", "r_ev_degen", "r_ultimo_recurso"])]),
 ("X2.4", "Ginecología", ["P3.4", "P3.5", "P3.11", "D11.5", "D11.6"], [
  ("ev_gin_sintesis", "Síntesis: dismenorrea, SPM y climaterio", "Dismenorrea: Cochrane 2016 insuficiente; SPM: resultados prometedores con fallos metodológicos; sofocos: sin reducción clara (ver evidencia de Patzek).", ["p_ev_dism", "p_ev_spm", "p_ev_meno", "x_sp6"])]),
 ("X2.5", "Embarazo, parto y fertilidad", ["D11.4", "P4.2", "P4.5", "P4.6", "P4.7", "P3.10"], [
  ("ev_parto", "Evidencia: acupuntura y acupresión en el dolor del parto", "Cochrane 2020, 28 ECA (3960 mujeres): la acupuntura frente a simulada puede aumentar la satisfacción y reducir la analgesia farmacológica; la acupresión puede reducir un poco el dolor; ningún estudio tuvo bajo riesgo de sesgo en todos los dominios (PMID 32032444, doi:10.1002/14651858.CD009232.pub2).", ["x_sp6", "x_li4"]),
  ("ev_lumbopelvico", "Evidencia: dolor lumbopélvico del embarazo", "Revisión sistemática 2015: evidencia fuerte a favor de la acupuntura y del cinturón pélvico durante el embarazo (PMID 26018758, doi:10.1111/aogs.12681).", []),
  ("ev_fiv", "Evidencia: acupuntura en FIV", "Metanálisis 2021 de 8 ECA (3607 mujeres): la acupuntura en la transferencia embrionaria no mejoró el embarazo clínico ni los nacidos vivos frente a la simulada; certeza moderada a alta (PMID 33040570, doi:10.1177/0964528420958711).", []),
  ("ev_emb_sintesis", "Síntesis: náuseas, nalgas y placenta", "PC6 en náuseas: certeza baja a moderada. BL67 con moxa: menos presentaciones de nalgas (Cochrane 2023). Placenta retenida: solo series de casos.", ["d_ev_pc6_nvp", "p_bl67", "p_ev_placenta", "x_pc6"])]),
 ("X2.6", "Auriculoterapia", ["P2.14", "D0.3"], [
  ("ev_aur_sintesis", "Síntesis: auriculoterapia", "Resumen de revisiones 2018: complemento útil en insomnio y dolor. Revisiones 2023–2025 con efecto en ansiedad, estreñimiento e insomnio por quimioterapia, siempre con calidad baja.", ["p_ev_auricular", "ev_ansiedad", "ev_estren", "ev_insomnio"])]),
]
x2 = {"num": "X2", "title": "Evidencia de PubMed por tema", "block": "x",
      "summary": "Revisiones sistemáticas que cruzan los tres libros. Cada sección traza las secciones de los libros que tratan el tema.", "sections": []}
for sn, st, secs, its in EV:
    sec = {"num": sn, "title": st, "items": []}
    for iid, t, s, req in its:
        out["items"][iid] = {"title": t, "summary": s + F}; sec["items"].append(iid)
        req = [r for r in req if r in out["items"] or r.startswith("ev_")]
        if req: out["requires"]["items"][iid] = req
    x2["sections"].append(sec); out["requires"]["sections"][sn] = secs

# ---------- capítulo X3: seguridad ----------
emb_use = "; ".join(f"{c}: " + ", ".join(sorted({s for v in use[c].values() for s in v})) for c in sorted(EMB) if c in use)
x3 = {"num": "X3", "title": "Seguridad común", "block": "x", "summary": "Alertas que valen para los tres libros.", "sections": [
  {"num": "X3.1", "title": "Puntos prohibidos en el embarazo", "items": ["x_prohibidos"]},
  {"num": "X3.2", "title": "Hierbas y fórmulas con riesgo", "items": ["x_hierbas"]},
  {"num": "X3.3", "title": "Cuándo no sustituir el tratamiento", "items": ["x_derivar"]}]}
out["items"]["x_prohibidos"] = {"title": "Puntos prohibidos en el embarazo", "summary": "LI4, SP6, BL60, BL67, GB21, BL31–BL34, Zigong, Duyin y el abdomen bajo no se estimulan en el embarazo, salvo indicación profesional (BL67 con moxa para la presentación de nalgas). Uso en los libros: " + emb_use + "."}
out["items"]["x_hierbas"] = {"title": "Hierbas y fórmulas con riesgo", "summary": "Acónito (fu zi) en You Gui Wan de Rosenfarb y en 4 fórmulas de Patzek: cardiotóxico. Toosendan: hepatotóxico. Mu tong: riesgo de sustitución por Aristolochia. Danggui: potencia la warfarina. Pinellia y coptis: prudencia en el embarazo."}
out["items"]["x_derivar"] = {"title": "Cuándo derivar", "summary": "Pérdida de visión, dolor ocular, glaucoma o DMAE húmeda; hipertensión o edema en el embarazo (preeclampsia); fiebre con mastitis; sangrado uterino anormal; dolor torácico. La acupresión es complemento, no sustituto."}
out["requires"]["items"]["x_prohibidos"] = [k for k in ["p_prohibidos", "p_evitar_emb", "p_bl67"] if k in out["items"]]
out["requires"]["items"]["x_hierbas"] = [k for k in ["r_you_gui", "p_ev_toxicas", "p_danggui", "p_f_zhenwu"] if k in out["items"]]
out["requires"]["items"]["x_derivar"] = [k for k in ["r_ultimo_recurso", "p_o_hta"] if k in out["items"]]
out["requires"]["sections"]["X3.1"] = [s for s in ["D11.4", "P4.1", "P2.15"] if s in sectitle]

out["blocks"]["x"] = {"name": "Puentes: puntos, evidencia y seguridad"}
out["chapters"] += [x1, x2, x3]
out["requires"]["chapters"].update({"X1": ["D0", "P2"], "X2": ["X1"], "X3": ["X1"]})
out["resources"].append({"id": "PM", "title": "PubMed: revisiones sistemáticas (2026-11-26)", "usedBy": [s["num"] for s in x2["sections"]],
                         "summary": "acupressure insomnia / low back pain / anxiety / constipation; acupuncture migraine Cochrane; dry eye; myopia; labour pain; IVF; pregnancy lumbopelvic."})
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(shared), "puntos compartidos;", len(out["items"]), "ítems;", sum(len(c["sections"]) for c in out["chapters"]), "secciones")
print(" ".join(f"{c}:{''.join(b[0] for b in use[c])}" for c in shared))
