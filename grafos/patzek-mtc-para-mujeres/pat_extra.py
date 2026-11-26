"""Añade al grafo de Patzek las fórmulas de hierbas, las recetas de cocina y los puntos de la oreja.
Uso: python3 -I pat_extra.py <pat/grafo.json>   (modifica el archivo; se ejecuta después de pat_build.py)
"""
import json, sys

gp = sys.argv[1]
g = json.load(open(gp, encoding="utf-8"))
A = "⚠ "
SEC = {s["num"]: s for c in g["chapters"] for s in c["sections"]}
items, req = g["items"], g["requires"]["items"]

def add(sec, iid, title, summ, needs=()):
    items[iid] = {"title": title, "summary": summ}
    SEC[sec].setdefault("items", []).append(iid)
    if needs: req[iid] = list(needs)

# ---------- puntos de la oreja (presentados en 2.14) ----------
NOTE = " Nomenclatura de la escuela alemana de auriculoterapia (Nogier, Bahr); la ubicación exacta se confirma en un atlas auricular."
O = {
 "o_55": ("Oreja: 55 (Shenmen)", "Punto calmante y analgésico general en la fosa triangular; el libro lo usa en casi todos los cuadros."),
 "o_vg": ("Oreja: Vg I y Vg II (puntos vegetativos)", "Regulan el sistema nervioso autónomo; Vg I aparece en casi todos los cuadros y Vg II en la depresión posparto."),
 "o_psiq": ("Oreja: puntos psíquicos", "Frustración, antiagresión y antidepresión (llamado también punto tranquilizador); se eligen según el estado de ánimo."),
 "o_jerome": ("Oreja: Jerome", "Punto de relajación y sueño; en la cefalea y la migraña."),
 "o_cojin": ("Oreja: cojín (occipucio)", "Punto de cabeza y dolor; en migraña, climaterio y lactancia."),
 "o_sol": ("Oreja: sol", "Punto de la sien; en la migraña."),
 "o_omega": ("Oreja: Omega principal", "Punto de regulación general; en migraña, climaterio y depresión posparto."),
 "o_cero": ("Oreja: punto cero", "Punto de equilibrio general; en la retención de orina posparto."),
 "o_endocrino": ("Oreja: endocrino", "Regulación hormonal; el punto auricular más usado en los cuadros ginecológicos del libro."),
 "o_suprarrenal": ("Oreja: suprarrenales", "En cuadros de Yang de riñón, edema, climaterio e hipertensión."),
 "o_genital": ("Oreja: útero o matriz, ovarios, vagina y pecho", "Puntos del aparato reproductor y la mama. En las náuseas del embarazo el libro no los usa."),
 "o_organos": ("Oreja: puntos de órganos", "Riñón, hígado, bazo, estómago, corazón, vejiga, intestinos y triple calentador, elegidos según el síndrome chino."),
 "o_digest": ("Oreja: diafragma y náusea", "Puntos para las náuseas y los vómitos del embarazo."),
 "o_acth": ("Oreja: ACTH", "Punto hormonal; en el dolor menstrual por carencia de Qi y sangre."),
 "o_hta": ("Oreja: puntos de hipertensión", "Punto de hipertensión 19 y punto que baja la tensión, en la parte superior de la oreja. " + A + "No sustituyen el tratamiento de la preeclampsia."),
 "o_local": ("Oreja: zonas de la columna y puntos de dolor", "Columna lumbar, vértebras y puntos sensibles según la zona del dolor; regla sí-no del libro."),
}
for k, (t, s) in O.items():
    add("2.14", k, t, s + NOTE, ["auricular"])
items["ev_auricular"] = {"title": "Evidencia: auriculoterapia", "summary": "Resumen de revisiones sistemáticas 2018: efecto positivo como complemento en insomnio y dolor; faltan estudios en otras indicaciones, incluidas las ginecológicas (PMID 30396628, doi:10.1016/j.ctcp.2018.08.005). Consultado en PubMed el 2026-11-26."}
SEC["2.14"]["items"].append("ev_auricular"); req["ev_auricular"] = ["auricular"]

OREJA = {
 "3.2": "vagina, endocrino, bazo, estómago, 55, Vg I y psíquicos; en el Yang de riñón: riñón, columna lumbar, suprarrenales, útero y vagina",
 "3.3": "riñón, matriz, hígado, suprarrenales, endocrino, Vg I y vejiga",
 "3.4": "hígado, matriz y pecho; con cefalea, Jerome, cojín y Omega; además riñón, bazo, ovarios, endocrino, suprarrenales, 55, Vg I y psíquicos",
 "3.5": "hígado, matriz, ovarios, endocrino, suprarrenales, riñón, estómago, bazo, ACTH, 55, Vg I y psíquicos",
 "3.6": "55, Vg I, Jerome, sol, cojín, Omega, ojo, estómago, hígado, riñón, endocrino, matriz, suprarrenales, columna y puntos de dolor",
 "3.7": "estómago, bazo, útero, ovarios, endocrino y psíquicos",
 "3.8": "hígado, matriz, útero, ovarios, endocrino, suprarrenales, riñón, bazo, 55 y Vg I",
 "3.9": "matriz, ovarios, hígado, riñón, corazón, bazo, triple calentador, estómago, endocrino, suprarrenales, cojín, Vg I y psíquicos",
 "3.10": "riñón, hígado, matriz, ovarios, endocrino, suprarrenales, 55, Vg I y psíquicos",
 "3.11": "endocrino, corazón, riñón, suprarrenales, hígado, ovarios, matriz, bazo, vértebras lumbares, 55, Vg I, cojín, Omega, frustración y antidepresión",
 "3.12": "bazo, estómago, riñón, vejiga, matriz, 55 y Vg I",
 "4.2": "diafragma, náusea, estómago, bazo, hígado, riñón, 55, Vg I y psíquicos (sin puntos genitales)",
 "4.3": "riñón, bazo, estómago, vejiga, suprarrenales, 55 y Vg I",
 "4.4": "riñón, estómago, bazo, corazón, hígado, suprarrenales, 55, Vg I, punto de hipertensión 19 y punto que baja la tensión",
 "4.6": "55, útero, endocrino, Vg I y puntos de dolor de la columna",
 "4.8": "hígado, útero y puntos relajantes",
 "4.9": "intestino grueso, intestino delgado, vejiga, riñón, Vg I, punto cero y psíquicos",
 "4.10": "55, Vg I, pecho, matriz, riñón, bazo, hígado, endocrino, suprarrenales, cojín y conductos vegetativos",
 "4.11": "psíquicos (sobre todo antidepresión), bazo, riñón, hígado, estómago, matriz, Vg I, Vg II y Omega",
}
for s, txt in OREJA.items():
    SEC[s]["summary"] += " Oreja: " + txt + "."
    g["requires"]["sections"].setdefault(s, [])
    if "2.14" not in g["requires"]["sections"][s]: g["requires"]["sections"][s].append("2.14")

# ---------- fórmulas de hierbas ----------
F = "Fórmula del libro (sin cantidades). Correspondencia con la fórmula clásica: interpretación de Claude. "
FORM = [
 ("3.2", "f_wandai", "Fórmula: Yang de bazo y flujo (≈ Wan Dai Tang)", "Atractylodes blanco, ñame chino, ginseng, cáscara de mandarina, semilla de llantén, peonía blanca, bupleurum, schizonepeta carbonizada y regaliz.", ["shanyao", "baishao"]),
 ("3.2", "f_shenqi", "Fórmula: Yang de riñón y flujo (≈ Jin Gui Shen Qi Wan)", "Rehmannia, cornejo, ñame chino, acónito preparado, ramita de canela, alisma, poria y moutan. " + A + "Contiene acónito.", ["rehmannia", "shanyao"]),
 ("3.3", "f_ermiao", "Fórmula: calor húmedo (≈ Er Miao San)", "Corteza de felodendro y atractylodes.", ["p_humcal"]),
 ("3.4", "f_chaihu", "Fórmula: estancamiento de Qi de hígado (≈ Chai Hu Shu Gan San)", "Mandarina, bupleurum, ligusticum, naranja amarga, peonía blanca, regaliz y ciperus. Se repite en el ciclo irregular.", ["p_qi_hig", "baishao"]),
 ("3.4", "f_yougui", "Fórmula: Yang de bazo y riñón (≈ You Gui Wan modificada)", "Rehmannia preparada, ñame chino, cornejo, goji, gelatina de cuerno de ciervo, cuscuta, eucomia, acónito, astrágalo, haloisita roja, psoralea y frambuesa china. Se repite en el climaterio. " + A + "Contiene acónito; la psoralea es fotosensibilizante y se ha asociado a daño hepático.", ["p_yang_br", "goji"]),
 ("3.4", "f_yiguan", "Fórmula: Yin de hígado y riñón (≈ Yi Guan Jian)", "Rehmannia, goji, adenophora o glehnia, ophiopogon, danggui, fruto de toosendan y cidra mano de Buda. Se repite en la esterilidad por Yin. " + A + "Toosendan es hepatotóxico.", ["p_yin_hr", "danggui"]),
 ("3.4", "f_xiaoyao", "Fórmula: sangre de hígado (≈ Xiao Yao San)", "Bupleurum, danggui, peonía blanca, atractylodes, poria, regaliz, jengibre fresco y menta. Se repite en el ciclo prolongado.", ["p_sangre_hig", "danggui"]),
 ("3.5", "f_shaofu", "Fórmula: frío en la matriz (≈ Shao Fu Zhu Yu Tang)", "Hinojo, jengibre seco, corydalis, danggui, ligusticum, mirra, canela, peonía roja y polen de typha.", ["p_frio_matriz", "danggui"]),
 ("3.5", "f_bazhen_ym", "Fórmula: carencia de Qi y sangre (≈ Ba Zhen Tang con agripalma)", "Ginseng, atractylodes, poria, regaliz, rehmannia, peonía blanca, danggui, ligusticum, jengibre, azufaifo y agripalma.", ["danggui", "rehmannia"]),
 ("3.6", "f_tianma", "Fórmula: ascenso de Yang de hígado (≈ Tian Ma Gou Teng Yin modificada)", "Concha de ostra y de oreja de mar, peonía blanca, rehmannia, gardenia, uncaria, gastrodia, tribulus, agripalma y escutelaria.", ["p_yang_hig"]),
 ("3.6", "f_bazhen", "Fórmula: Qi de bazo y anemia (≈ Ba Zhen Tang)", "Danggui, ginseng, atractylodes, regaliz, rehmannia, peonía blanca, ligusticum, jengibre y azufaifo. Se repite en el estreñimiento posparto.", ["p_qi_bazo", "danggui"]),
 ("3.6", "f_humedad", "Fórmula: humedad con bazo débil", "Agastache, eupatorium, atractylodes, magnolia, poria y semilla de dolichos.", ["p_humedad"]),
 ("3.8", "f_siwu", "Fórmula: anemia y frío en la sangre (≈ Si Wu Tang)", "Rehmannia preparada, peonía blanca, danggui y ligusticum.", ["danggui", "rehmannia"]),
 ("3.9", "f_zuogui", "Fórmula: carencia de jing de riñón (≈ Zuo Gui Wan)", "Rehmannia, ñame chino, goji, cyathula, cornejo, cuscuta, gelatina de cuerno de ciervo y de caparazón de tortuga. " + A + "Productos animales de especies protegidas.", ["p_jing", "goji"]),
 ("3.10", "f_aifu", "Fórmula: Yang de riñón y esterilidad (≈ Ai Fu Nuan Gong Wan)", "Ciperus, hoja de artemisa, danggui, astrágalo, evodia, ligusticum, peonía blanca, rehmannia preparada, canela y dipsacus.", ["danggui"]),
 ("3.10", "f_libido", "Fórmula: afrodisíacos chinos", "Gelatina de cuerno de ciervo, epimedio o cynomorium y danggui. El libro añade zinc. " + A + "Epimedio: interacciones y efectos hormonales poco estudiados.", ["danggui"]),
 ("3.11", "f_zhibai", "Fórmula: Yin de riñón con Yang de hígado (≈ Zhi Bai Di Huang Wan con hueso de dragón y concha de ostra)", "Rehmannia, cornejo, ñame chino, poria, moutan, alisma, anemarrhena, felodendro, hueso fósil y concha de ostra.", ["rehmannia"]),
 ("3.11", "f_erxian", "Fórmula: jing de riñón en el climaterio (≈ Er Xian Tang)", "Curculigo, epimedio, morinda, felodendro, anemarrhena y danggui. " + A + "Curculigo se ha asociado a toxicidad hepática y renal en modelos animales.", ["danggui"]),
 ("3.12", "f_buzhong", "Fórmula: descenso de Qi de bazo (≈ Bu Zhong Yi Qi Tang)", "Astrágalo, ginseng, atractylodes, regaliz, danggui, mandarina, cimicifuga y bupleurum.", ["p_desc_qi", "danggui"]),
 ("4.2", "f_liujunzi", "Fórmula: Qi de bazo y estómago en el embarazo (≈ Liu Jun Zi Tang)", "Ginseng, atractylodes, poria, mandarina, pinellia y regaliz. " + A + "Pinellia: prudencia clásica en el embarazo; solo procesada y bajo prescripción.", ["qi_rebelde"]),
 ("4.2", "f_guipi", "Fórmula: bazo y corazón (≈ Gui Pi Tang modificada)", "Jengibre carbonizado, hueso de sepia, artemisa carbonizada, atractylodes, poria, astrágalo, longan, semilla de azufaifo, ginseng, danggui, polygala, regaliz, aucklandia, azufaifo y jengibre.", ["danggui"]),
 ("4.2", "f_suye", "Fórmula: el hígado ataca al estómago (≈ Su Ye Huang Lian Tang modificada)", "Concha de oreja de mar y de ostra, perilla, coptis, pinellia, bambú, rizoma de carrizo y mandarina. " + A + "Coptis (berberina) se evita en el embarazo por riesgo de ictericia neonatal.", ["p_hig_est"]),
 ("4.2", "f_mucosidad", "Fórmula: mucosidad por Qi de bazo débil", "Pinellia preparada, poria, jengibre fresco, atractylodes, mandarina y amomum.", ["qi_rebelde"]),
 ("4.3", "f_edema_bazo", "Fórmula: edema por Yang de bazo", "Atractylodes, cáscara de areca, poria, jengibre fresco, mandarina y amomum. La cáscara de areca es clásica en el edema gestacional; la nuez de areca no.", ["sp9"]),
 ("4.3", "f_zhenwu", "Fórmula: edema por Yang de riñón (≈ Zhen Wu Tang)", "Atractylodes, acónito preparado, poria, jengibre fresco y peonía blanca. " + A + "Acónito en una embarazada: contraindicado.", ["baishao"]),
 ("4.4", "f_liuwei", "Fórmula: Yin de riñón e hipertensión (≈ Liu Wei Di Huang Wan)", "Rehmannia, cornejo, ñame chino, poria, moutan y alisma. No reemplaza el antihipertensivo.", ["rehmannia"]),
 ("4.9", "f_bazheng", "Fórmula: retención de orina por humedad-calor (≈ Ba Zheng San modificada)", "Polygonum aviculare, dianthus, talco, atractylodes, felodendro, gardenia, akebia, llantén y cáscara de areca; luego ruibarbo. " + A + "Akebia (mu tong) puede venir sustituida por Aristolochia; el ruibarbo pasa a la leche.", ["kd3"]),
 ("4.10", "f_gualou", "Fórmula: mastitis (≈ Gua Lou Niu Bang Zi Tang)", "Madreselva, forsythia, bardana, trichosanthes (fruto y raíz), escrofularia, mandarina madura y verde, gardenia, espina de gleditsia, bupleurum y regaliz. Si hay fiebre o absceso, valorar antibiótico y drenaje.", []),
]
for sec, iid, t, s, needs in FORM:
    add(sec, iid, t, F + s, list(needs) + ["receta"])

# ---------- recetas de cocina ----------
R = "Receta de cocina del libro (resumen de ingredientes, sin cantidades). "
REC = [
 ("3.2", "r_pimiento", "Receta: pimiento con carne", "Carne picada con cebolla, ajo, pimienta, cayena, pimiento, tomate, vino tinto, tomillo, pimentón y alubias rojas, con arroz. Para calentar el Yang del bazo.", ["p_yang_br"]),
 ("3.4", "r_coco", "Receta: sopa de leche de coco y gambas", "Champiñones y gambas salteados con limón, pimentón, caldo de verdura y leche de coco. Para nutrir el Yin de hígado y riñón.", ["p_yin_hr"]),
 ("3.4", "r_pollo", "Receta: caldo de pollo para generar sangre", "Pollo con zanahoria, patata, perejil y su raíz y cebolla, hervido dos horas; se cambia la verdura al final. Se repite en la migraña por anemia y en la depresión posparto.", ["p_sangre_hig"]),
 ("3.6", "r_cerdo", "Receta: verduras con carne de cerdo", "Cerdo salteado con puerro, jengibre, ajo, soja, limón, pimiento rojo, judías verdes y brócoli. Para el ascenso del Yang de hígado.", ["p_yang_hig"]),
 ("3.6", "r_vaca", "Receta: sopa de carne de vaca", "Ternera y huesos con zanahoria, apio, patata, raíz de perejil y puerro, jengibre y ajo, hervida 2–3 horas. Para la carencia de Qi de bazo.", ["p_qi_bazo"]),
 ("3.11", "r_pescado", "Receta: sopa de pescado", "Cabezas de salmón, bacalao o atún con verduras, jengibre y pimienta, hervidas 2–3 horas; luego pescado y gambas. Para la carencia de jing de riñón.", ["p_jing"]),
 ("3.10", "r_libido", "Menú afrodisíaco", "Cordero en vino tinto con patata, calabaza y zanahoria; pescado a la parrilla con puerro; peras al vino con canela y jengibre. Para el Yang de riñón y el Qi de bazo.", ["f_libido"]),
 ("4.2", "r_pie", "Receta: pastel de carne (shepherd's pie)", "Ternera con zanahoria, patata, col china, pimiento, cebolla, ajo, hierbas y jerez, cubierta con masa de yogur. Para la carencia de Qi de bazo en el embarazo. " + A + "Lleva jerez: en el embarazo se omite el alcohol.", ["qi_rebelde"]),
 ("4.2", "r_espinacas", "Receta: espinacas con salsa de gambas", "Espinacas con mantequilla y nuez moscada; gambas con limón, pimienta rosa y nata. Para el hígado que ataca al estómago.", ["p_hig_est"]),
 ("4.2", "r_hinojo", "Receta: gratinado de hinojo, zanahoria y patata", "Verduras con pimienta, cayena, nuez moscada y pimienta rosa, gratinadas con queso y nata. Para la mucosidad por bazo débil.", ["qi_rebelde"]),
 ("4.3", "r_risotto", "Receta: risotto con verduras", "Arroz con hinojo, calabacín, pimiento rojo, zanahoria, jengibre, cardamomo y pavo o ternera, con poca sal. Para el edema por Yang de bazo.", ["sp9"]),
 ("4.8", "r_mijo", "Receta: mijo asado", "Albóndigas de mijo cocido con huevo, cebolla, cebollino, perejil y pan rallado, fritas. Para la carencia de Qi tras el parto.", ["lr3"]),
 ("4.11", "r_nacimiento", "Receta: sopa china del nacimiento", "Caldo de pollo y verdura que se recalienta durante semanas antes y después del parto. " + A + "Un caldo mantenido varias semanas tiene riesgo microbiológico: mejor prepararlo fresco y refrigerarlo.", []),
]
for sec, iid, t, s, needs in REC:
    add(sec, iid, t, R + s, list(needs) + ["termica"])

g["meta"]["subtitle"] = "Sabine Patzek y Karin Hertzer, Arkano Books 2003: fundamentos, práctica, ginecología y embarazo; fórmulas, recetas, puntos corporales y de la oreja, cruce con acupuntura-puntos y alertas de PubMed"
pm = [r for r in g["resources"] if r["id"] == "PM"][0]
pm["summary"] = pm["summary"].rstrip(".") + "; auricular acupuncture systematic review overview (desde 2018)."
if "2.14" not in pm["usedBy"]: pm["usedBy"].append("2.14")
json.dump(g, open(gp, "w"), ensure_ascii=False, indent=1)
print(len(items), "ítems")
