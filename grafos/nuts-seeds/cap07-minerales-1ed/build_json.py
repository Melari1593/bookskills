"""Construye salida/grafo.json del capítulo 7 de Nuts and Seeds in Health and Disease Prevention
(Rodushkin, Baxter y Engström, 2011): elementos inorgánicos de frutos secos y semillas.
Resúmenes escritos a mano (paráfrasis propia); alertas desde trabajo/alertas.json si existe.
Uso: python3 scripts/build_json.py salida/grafo.json"""
import json, os, sys
AL = json.load(open('trabajo/alertas.json', encoding='utf-8')) if os.path.exists('trabajo/alertas.json') else {}
def sec(num, title, summary, items=None, page=None):
    s = {"num": num, "title": title, "summary": summary}
    if items: s["items"] = items
    if page: s["page"] = page
    return s
chapters = [
 {"num": 1, "title": "Minerales esenciales y elementos tóxicos", "block": "base", "page": 65,
  "summary": "Planteamiento: los frutos secos y las semillas aportan minerales esenciales, pero también pueden contener elementos tóxicos; para valorarlos hace falta saber cuánto se consume y en qué concentración.",
  "sections": [sec("1.1", "Riqueza mineral y salud", "Los autores atribuyen parte de los beneficios de los frutos secos (hueso, presión arterial, insulina, corazón) a su calcio, magnesio y potasio y a su bajo sodio.", ["i_minerales_salud", "i_selenio"], 65),
               sec("1.2", "Qué datos hacen falta para evaluar el riesgo", "Para estimar beneficio o daño se necesitan tres datos: consumo diario, concentración típica y valores de referencia (ingesta recomendada, máxima tolerable o tolerable semanal).", ["i_valores_referencia"], 66)]},
 {"num": 2, "title": "Cuántos frutos secos se consumen", "block": "consumo", "page": 66,
  "summary": "El consumo medio en Europa y EE. UU. es de pocos gramos al día, lejos de los 30–40 g que proponen las guías.",
  "sections": [sec("2.1", "Consumo medio en Europa y EE. UU.", "En el estudio europeo EPIC el promedio fue de unos 4–5 g/día; en EE. UU., 3–7 g/día, sobre todo maní, almendra y nuez. Las encuestas probablemente lo subestiman.", ["i_consumo"], 66),
               sec("2.2", "Porciones y recomendación", "Las porciones de los envases van de 10 a 100 g; las guías suelen recomendar unos 30 g/día y algunos estudios, 40 g o más.", ["i_consumo"], 67)]},
 {"num": 3, "title": "Composición inorgánica", "block": "composicion", "page": 67,
  "summary": "Concentraciones de 27 elementos en 12 frutos secos y semillas crudos, compiladas de más de 60 fuentes, y por qué varían tanto los oligoelementos.",
  "sections": [sec("3.1", "Cómo se compilaron los datos", "Tablas nacionales para los macroelementos y publicaciones científicas para el resto; se dan medianas con su variabilidad, o rangos cuando los valores difieren más de diez veces.", ["i_variabilidad"], 67),
               sec("3.2", "Por qué varían los oligoelementos", "Los macroelementos varían poco; los oligoelementos varían hasta varios órdenes de magnitud por suelo y clima, contaminación al pelar y envasar, y errores analíticos.", ["i_variabilidad", "f_nuez_brasil"], 68)]},
 {"num": 4, "title": "Importancia nutricional", "block": "nutricion", "page": 69,
  "summary": "Cuántos gramos de cada fruto seco cubren el 10 % de la necesidad diaria de cada elemento (tabla 7.2).",
  "sections": [sec("4.1", "Fuentes ricas: magnesio, cobre, manganeso, hierro, zinc, potasio", "Los frutos secos y semillas son fuentes muy ricas de magnesio, cobre y manganeso, e importantes de hierro, zinc y potasio; la semilla de calabaza encabeza la lista y el coco la cierra.", ["i_mg_cu_mn", "f_calabaza", "f_coco", "i_niquel"], 69),
               sec("4.2", "Selenio de la nuez de Brasil", "Incluso una nuez de Brasil con poco selenio aporta una parte importante del día; girasol, cashew y nuez también son fuentes relevantes.", ["f_nuez_brasil", "i_selenio"], 69),
               sec("4.3", "Calcio y elementos escasos", "Salvo la almendra, no son una fuente importante de calcio; el aporte de sodio, cloro, yodo y vanadio es despreciable.", ["i_calcio", "f_almendra"], 69),
               sec("4.4", "Cromo, molibdeno y boro", "El valor del cromo es incierto porque los datos varían casi cien veces; maní y semillas aportan molibdeno; nuez de Brasil, avellana, almendra y cashew aportan boro.", ["i_cromo", "i_boro"], 69)]},
 {"num": 5, "title": "Efectos adversos", "block": "toxicos", "page": 70,
  "summary": "Cuándo el consumo de frutos secos acerca a los límites de seguridad: selenio, cadmio, bario y, con dudas analíticas, arsénico, plomo y mercurio.",
  "sections": [sec("5.1", "Exceso de elementos esenciales", "Para fósforo, manganeso, cobre, níquel, zinc y hierro harían falta más de 300 g/día para llegar al máximo tolerable; con el selenio de la nuez de Brasil bastan pocas unidades.", ["f_nuez_brasil", "i_niquel"], 70),
               sec("5.2", "Elementos tóxicos en concentraciones bajas", "La mayoría de los tóxicos (aluminio, antimonio, estaño, talio, uranio y otros) aparece en cantidades muy pequeñas en frutos secos crudos.", ["i_aluminio"], 70),
               sec("5.3", "Cadmio", "El cadmio es tóxico para el riñón y el hueso y cancerígeno; la semilla de girasol, la almendra, el piñón y el maní pesan en la exposición, sobre todo con el límite más estricto de la EFSA.", ["i_cadmio", "f_girasol", "f_pinon"], 71),
               sec("5.4", "Arsénico, plomo y mercurio", "Con los valores bajos publicados el riesgo es mínimo; los valores altos de nuez, pistacho, piñón y nuez de Brasil podrían deberse a errores analíticos.", ["i_as_pb_hg"], 71),
               sec("5.5", "Bario de la nuez de Brasil", "La nuez de Brasil tiene mucho bario; según el capítulo, más de 50 g/día superarían el nivel considerado seguro.", ["i_bario", "f_nuez_brasil"], 71)]},
 {"num": 6, "title": "Puntos de resumen", "block": "base", "page": 71,
  "summary": "Fuentes importantes de varios minerales, escasas de calcio y sodio, con riesgo a vigilar por selenio y bario de la nuez de Brasil y por cadmio de ciertas semillas.",
  "sections": [sec("6.1", "Balance de beneficios y riesgos", "Aportan muchos minerales esenciales con poco consumo; el selenio y el bario de la nuez de Brasil y el cadmio de girasol, almendra, piñón y maní merecen atención.", None, 71)]}]
I = {
 "i_minerales_salud": ("Minerales y beneficios de los frutos secos", "El capítulo atribuye a la riqueza en calcio, magnesio y potasio y al bajo sodio parte de la protección asociada a los frutos secos.", ""),
 "i_valores_referencia": ("Valores de referencia", "Ingesta recomendada (RDA/RDI) y máxima tolerable (UL) para elementos esenciales; ingesta tolerable semanal o diaria (PTWI, TWI, TDI) para tóxicos.", ""),
 "i_consumo": ("Consumo de frutos secos", "Consumo real bajo en la población frente a la recomendación de las guías.", "Europa 4–5 g/día · EE. UU. 3–7 g/día · guías ≈ 30 g/día"),
 "i_variabilidad": ("Variabilidad y errores analíticos", "Los oligoelementos varían mucho entre muestras por suelo, contaminación y errores de laboratorio; los autores desconfían de los valores extremos.", "Macroelementos: RSD < 30 %"),
 "i_mg_cu_mn": ("Magnesio, cobre y manganeso", "Los tres elementos para los que los frutos secos y semillas son fuentes más ricas; los frutos secos se consideran la mejor fuente dietética de manganeso.", "10–30 g cubren el 10 % del magnesio diario"),
 "i_selenio": ("Selenio", "Oligoelemento esencial; la nuez de Brasil es probablemente el alimento más rico. El capítulo menciona un efecto antitumoral en animales.", ""),
 "i_calcio": ("Calcio", "Los frutos secos son una fuente moderada a pobre de calcio, salvo la almendra.", "Almendra: 2500 mg/kg"),
 "i_cromo": ("Cromo", "El capítulo lo trata como esencial; sus datos en frutos secos varían casi cien veces, así que su aporte es incierto.", ""),
 "i_boro": ("Boro", "Elemento potencialmente esencial; los frutos secos son una buena fuente, sobre todo para vegetarianos.", "Nuez de Brasil 40 mg/kg"),
 "i_niquel": ("Níquel", "El capítulo lo cuenta entre los elementos de los que los frutos secos son fuente muy rica, con cashew y semilla de calabaza a la cabeza.", "Nuez de Brasil 7 mg/kg · cashew, calabaza y girasol 3 mg/kg"),
 "i_cadmio": ("Cadmio", "Metal tóxico para riñón y hueso y cancerígeno; los alimentos son la principal fuente en no fumadores y algunas semillas aportan una parte relevante.", "Girasol: hasta 1 mg/kg"),
 "i_as_pb_hg": ("Arsénico, plomo y mercurio", "Concentraciones muy bajas en la mayoría de los estudios; los valores altos aislados podrían ser artefactos analíticos.", ""),
 "i_bario": ("Bario", "Elemento no esencial; la nuez de Brasil lo acumula en concentraciones muy altas y variables.", "Nuez de Brasil: 70–2000 mg/kg"),
 "i_aluminio": ("Aluminio", "Presente en concentraciones bajas; el piñón tiene los valores más altos del grupo.", "Piñón: 4–40 mg/kg"),
 "f_nuez_brasil": ("Nuez de Brasil", "El fruto seco más extremo del capítulo: muy rica en selenio y bario, con concentraciones que dependen del suelo de origen.", "Selenio 1–50 mg/kg · bario 70–2000 mg/kg"),
 "f_calabaza": ("Semilla de calabaza", "La de mayor potencial nutricional mineral: fósforo, magnesio, hierro, zinc y manganeso.", "Fósforo 11 000 mg/kg · magnesio 5300 mg/kg"),
 "f_girasol": ("Semilla de girasol", "Buena fuente de selenio, cobre y níquel; también la que más cadmio puede aportar.", "Selenio 0,6 mg/kg · cadmio 0,01–1 mg/kg"),
 "f_pinon": ("Piñón", "Rico en manganeso; con cadmio y aluminio relativamente altos en algunos estudios.", "Manganeso 91 mg/kg"),
 "f_almendra": ("Almendra", "El único fruto seco del grupo que es fuente relevante de calcio.", "Calcio 2500 mg/kg"),
 "f_coco": ("Coco", "El de menor aporte mineral del grupo, salvo sodio.", "Sodio 370 mg/kg")}
items = {}
for k, (t, s, f) in I.items():
    it = {"title": t, "summary": s}
    if f: it["formula"] = f
    if AL.get(k): it["caution"] = AL[k]
    items[k] = it
req_it = {"i_selenio": ["i_valores_referencia"], "i_cadmio": ["i_valores_referencia"], "i_bario": ["i_valores_referencia"], "i_as_pb_hg": ["i_variabilidad", "i_valores_referencia"],
          "i_aluminio": ["i_valores_referencia"], "i_niquel": ["i_valores_referencia"], "i_cromo": ["i_variabilidad"], "f_nuez_brasil": ["i_selenio", "i_bario"],
          "f_girasol": ["i_cadmio"], "f_pinon": ["i_cadmio"], "f_calabaza": ["i_mg_cu_mn"], "f_almendra": ["i_calcio"], "i_mg_cu_mn": ["i_consumo"], "i_minerales_salud": ["i_mg_cu_mn", "i_calcio"]}
req_sec = {"1.2": ["1.1"], "2.2": ["2.1"], "3.1": ["1.2"], "3.2": ["3.1"], "4.1": ["2.2", "3.1"], "4.2": ["4.1"], "4.3": ["4.1"], "4.4": ["3.2"],
           "5.1": ["4.1", "4.2"], "5.2": ["3.2"], "5.3": ["5.2"], "5.4": ["3.2"], "5.5": ["5.2"], "6.1": ["5.1", "5.3", "5.5"]}
req_ch = {"2": [1], "3": [1], "4": [2, 3], "5": [4], "6": [5]}
g = {"meta": {"title": "Minerales y tóxicos en frutos secos y semillas como grafo",
  "subtitle": "Rodushkin, Baxter y Engström, capítulo 7 de Nuts and Seeds in Health and Disease Prevention (Elsevier, 2011) · con alertas de evidencia actual",
  "itemLabel": "Elemento o alimento", "itemLabelPlural": "Elementos y alimentos", "resourceLabel": "Tabla", "resourceLabelPlural": "Tablas",
  "searchHint": "Buscar: selenio, cadmio, nuez de Brasil…"},
 "blocks": {"base": {"name": "Planteamiento y resumen", "color": "#6B8E4E"}, "consumo": {"name": "Consumo", "color": "#B08A2E"},
            "composicion": {"name": "Composición", "color": "#6B5B95"}, "nutricion": {"name": "Importancia nutricional", "color": "#3F6FA0"},
            "toxicos": {"name": "Efectos adversos", "color": "#B5465A"}},
 "chapters": chapters, "items": items,
 "resources": [{"id": "7.1", "title": "Concentración de 27 elementos en 12 frutos secos y semillas", "page": 68, "usedBy": ["3.1", "3.2", "4.2", "5.3", "5.5"]},
               {"id": "7.2", "title": "Gramos diarios que cubren el 10 % de la ingesta recomendada o tolerable", "page": 70, "usedBy": ["4.1", "4.3", "4.4", "5.1", "5.4"]}],
 "requires": {"chapters": req_ch, "sections": req_sec, "items": req_it}}
json.dump(g, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("partes", len(chapters), "secciones", sum(len(c["sections"]) for c in chapters), "ítems", len(items), "alertas", sum('caution' in v for v in items.values()),
      "alertas sin ítem", [k for k in AL if k not in items])
