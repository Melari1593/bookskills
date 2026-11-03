"""Construye salida/grafo.json del capítulo 4 de Nuts and Seeds in Health and Disease Prevention (Li y Hu, 2011).
Estructura y resúmenes escritos a mano (paráfrasis propia); alertas desde trabajo/alertas.json si existe.
Uso: python3 scripts/build_json.py salida/grafo.json"""
import json, os, sys
AL = json.load(open('trabajo/alertas.json', encoding='utf-8')) if os.path.exists('trabajo/alertas.json') else {}
def sec(num, title, summary, items=None, page=None):
    s = {"num": num, "title": title, "summary": summary}
    if items: s["items"] = items
    if page: s["page"] = page
    return s
chapters = [
 {"num": 1, "title": "Por qué importan las grasas de frutos secos y semillas", "block": "base", "page": 35,
  "summary": "Planteamiento del capítulo: los frutos secos y las semillas aportan sobre todo grasas insaturadas, incluidos los dos ácidos grasos esenciales y otros poco comunes.",
  "sections": [sec("1.1", "Fuentes de grasas insaturadas", "Los frutos secos y las semillas destacan por su grasa insaturada; los autores citan evidencia epidemiológica que la asocia con efectos en la salud.", ["i_salud"], 35),
               sec("1.2", "Ácidos grasos esenciales y raros", "El linoleico y el α-linolénico son esenciales y precursores de los PUFA de 20 y 22 carbonos; algunas semillas añaden estearidónico, CLNA y ximenínico.", ["i_linoleico", "i_ala"], 35)]},
 {"num": 2, "title": "Clases de lípidos", "block": "lipidos", "page": 36,
  "summary": "Cuánta grasa tienen 12 frutos secos y semillas y en qué forma: casi toda como triacilgliceroles, con fitosteroles en la mayoría.",
  "sections": [sec("2.1", "Contenido total de lípidos", "La grasa total va de unos 2 g/100 g en la semilla de ginkgo a unos 75 g/100 g en la nuez; los datos vienen de muestras pequeñas (n = 3).", ["i_composicion", "f_ginkgo", "f_nuez"], 36),
               sec("2.2", "Triacilgliceroles, diacilgliceroles y ácidos grasos libres", "Los triacilgliceroles superan el 90 % de los lípidos (98 % en macadamia); el cáñamo tiene algo de diacilglicerol y el ginkgo algo de ácidos grasos libres.", ["i_tag", "f_canamo"], 36),
               sec("2.3", "Fitosteroles y sus ésteres", "Casi todas las muestras tienen fitosteroles, con el máximo en el pistacho; los ésteres de esterol varían de trazas a cerca del 7 %.", ["i_fitoesteroles"], 36)]},
 {"num": 3, "title": "Perfil de ácidos grasos de 20 frutos secos y semillas", "block": "perfil", "page": 36,
  "summary": "Comparación de saturados, monoinsaturados y poliinsaturados en 20 frutos secos y semillas (tablas 4.2 a 4.4 y figura 4.1).",
  "sections": [sec("3.1", "Ácidos grasos saturados", "Palmítico y esteárico son los saturados principales; el total va de unos 6 % en la pecana a unos 26 % en la nuez de Brasil.", ["i_saturados", "f_nuez_brasil"], 36),
               sec("3.2", "Monoinsaturados", "El oleico domina en avellana, macadamia, almendra, pistacho, cashew y calabaza; la macadamia destaca además por su palmitoleico.", ["i_mufa", "i_palmitoleico", "f_macadamia", "f_mani"], 36),
               sec("3.3", "Poliinsaturados n-6 y n-3", "El linoleico es el PUFA más abundante (hasta unos tres cuartos en la semilla de melón negro); el α-linolénico es mucho menor, salvo en cáñamo y nuez.", ["i_linoleico", "i_ala", "f_semilla_melon_negro", "f_nuez", "f_canamo"], 37),
               sec("3.4", "Ácidos grasos poco comunes del ginkgo", "La semilla de ginkgo es la única con 20:2n-6 y 20:3n-6 y con cantidades apreciables de 18:1n-7 y 18:3n-6.", ["f_ginkgo"], 37)]},
 {"num": 4, "title": "Semillas con ácidos grasos especiales", "block": "especiales", "page": 37,
  "summary": "Semillas que aportan ácidos grasos raros: linolénicos conjugados, ximenínico, γ-linolénico y estearidónico (tablas 4.5 a 4.7).",
  "sections": [sec("4.1", "Linolénicos conjugados en granada y Trichosanthes", "La semilla de granada tiene más de 80 % de CLNA, sobre todo punícico; la de Trichosanthes kirilowii, algo más de un tercio.", ["i_clna", "f_granada", "f_trichosanthes"], 37),
               sec("4.2", "Ácido ximenínico en el sándalo", "Las almendras de varias especies de Santalum contienen ácido ximenínico, un ácido graso con triple enlace; en S. album llega a unos cuatro quintos.", ["i_ximeninico", "f_santalum"], 39),
               sec("4.3", "GLA y SDA en Ribes y cinco familias", "Las semillas de grosellas (Ribes) y de Boraginaceae aportan γ-linolénico y estearidónico; todas las familias estudiadas tienen α-linolénico.", ["i_gla", "i_sda", "f_boraginaceas"], 39)]},
 {"num": 5, "title": "Conclusiones y puntos de resumen", "block": "base", "page": 39,
  "summary": "Todos los grupos estudiados son bajos en saturados y altos en insaturados; cada grupo especial se distingue por un ácido graso característico.",
  "sections": [sec("5.1", "Qué distingue a cada grupo", "Linoleico como PUFA principal; ALA alto en cáñamo, nuez y Ribes; SDA en Ribes y Boraginaceae; CLNA en granada y Trichosanthes; ximenínico en Santalum.", None, 39)]}]

I = {
 "i_salud": ("Grasas de frutos secos y salud", "El capítulo afirma, citando una revisión previa, que hay evidencia epidemiológica amplia que asocia estas grasas con efectos en la salud; no la desarrolla.", ""),
 "i_composicion": ("Calidad de los datos de composición", "Las cifras del capítulo vienen de muestras pequeñas y de orígenes concretos (sobre todo mercados de China y estudios únicos); la composición varía con variedad, cultivo y procesado.", "n = 3 por muestra en las tablas 4.1–4.2"),
 "i_tag": ("Triacilgliceroles", "Forma principal de la grasa en todas las muestras: más del 90 % de los lípidos.", "TAG > 90 % · máximo 98,4 % en macadamia"),
 "i_fitoesteroles": ("Fitosteroles", "Esteroles vegetales presentes en la mayoría de los frutos secos y semillas analizados; el pistacho tiene la mayor proporción.", "Pistacho: 5,0 % de los lípidos totales"),
 "i_saturados": ("Ácidos grasos saturados", "Sobre todo palmítico (16:0) y esteárico (18:0); minoritarios en todos los frutos secos y semillas del capítulo.", "SFA: 6,3 % (pecana) – 26,2 % (nuez de Brasil)"),
 "i_mufa": ("Monoinsaturados (oleico)", "El oleico (18:1n-9) es el ácido graso principal de avellana, macadamia, almendra, pistacho, cashew y calabaza.", "MUFA: 42,7 % (calabaza) – 82,6 % (macadamia)"),
 "i_palmitoleico": ("Ácido palmitoleico (16:1n-7)", "Monoinsaturado de 16 carbonos casi ausente en los demás frutos secos, pero abundante en la macadamia.", "Macadamia: 25,5 % de los ácidos grasos"),
 "i_linoleico": ("Ácido linoleico (18:2n-6)", "Ácido graso esencial omega-6; es el poliinsaturado más abundante en casi todos los frutos secos y semillas del capítulo.", "2,5 % (macadamia) – 75,7 % (semilla de melón negro)"),
 "i_ala": ("Ácido α-linolénico (ALA, 18:3n-3)", "Ácido graso esencial omega-3 y precursor de EPA y DHA; es escaso en la mayoría de las muestras y abundante en cáñamo y nuez.", "Cáñamo 15,2 % · nuez 11,4 %"),
 "i_gla": ("Ácido γ-linolénico (GLA, 18:3n-6)", "Omega-6 que se forma a partir del linoleico; aparece en semillas de Ribes y de varias familias silvestres, sobre todo Boraginaceae.", ""),
 "i_sda": ("Ácido estearidónico (SDA, 18:4n-3)", "Omega-3 que sigue al ALA en la ruta de síntesis de EPA; el capítulo lo encuentra en semillas de Ribes y Boraginaceae.", ""),
 "i_clna": ("Linolénicos conjugados (CLNA) y ácido punícico", "Isómeros de 18:3 con dobles enlaces conjugados; el punícico es el principal en la semilla de granada.", "Granada: CLNA 83–88 %, punícico 73–78 %"),
 "i_ximeninico": ("Ácido ximenínico", "Ácido graso poco común con un triple enlace, característico de las almendras de sándalo (Santalum).", "S. album: 82,8 %"),
 "f_nuez": ("Nuez", "El fruto seco con más grasa del capítulo y uno de los más ricos en linoleico y en ALA.", "Lípidos 75,4 g/100 g · PUFA 71,7 %"),
 "f_macadamia": ("Macadamia", "La más monoinsaturada del grupo, con oleico y un palmitoleico inusualmente alto; casi sin poliinsaturados.", "MUFA 82,6 % · PUFA 2,8 %"),
 "f_mani": ("Maní", "Legumbre que se consume como fruto seco; su grasa es sobre todo oleico y linoleico, sin ALA detectable.", "MUFA 44,6 % · PUFA 33,3 %"),
 "f_ginkgo": ("Semilla de ginkgo", "Semilla con muy poca grasa pero con ácidos grasos poco comunes; el capítulo la incluye entre los frutos secos de consumo habitual.", "Lípidos 2,2 g/100 g"),
 "f_canamo": ("Semilla de cáñamo (Cannabis sativa)", "La semilla con más ALA de las 20 estudiadas y con un poco de diacilglicerol.", "ALA 15,2 % · PUFA 70,9 %"),
 "f_nuez_brasil": ("Nuez de Brasil", "La de mayor proporción de saturados del grupo, con un esteárico especialmente alto.", "SFA 26,2 % · esteárico 11,8 %"),
 "f_semilla_melon_negro": ("Semilla de melón negro", "Semilla con la mayor proporción de linoleico y de poliinsaturados del capítulo.", "Linoleico 75,7 % · PUFA 75,8 %"),
 "f_granada": ("Semilla de granada", "Semilla dominada por ácido punícico; los autores citan un estudio propio de su metabolismo en humanos.", ""),
 "f_trichosanthes": ("Semilla de Trichosanthes kirilowii", "Semilla de una cucurbitácea china con un tercio de punícico junto a oleico y linoleico.", "CLNA 36,9 %"),
 "f_santalum": ("Almendras de sándalo (Santalum)", "Almendras de seis especies de sándalo ricas en ximenínico; algunas se consumen en Australia y el Pacífico.", ""),
 "f_boraginaceas": ("Semillas de Boraginaceae (borraja, Echium y otras)", "Familia de plantas cuyas semillas reúnen GLA, SDA y ALA en proporciones variables.", "")}
items = {}
for k, (t, s, f) in I.items():
    it = {"title": t, "summary": s}
    if f: it["formula"] = f
    if AL.get(k): it["caution"] = AL[k]
    items[k] = it
req_it = {"i_gla": ["i_linoleico"], "i_sda": ["i_ala"], "i_clna": ["i_ala"], "i_ximeninico": ["i_mufa"], "i_palmitoleico": ["i_mufa"],
          "f_nuez": ["i_ala", "i_linoleico"], "f_canamo": ["i_ala"], "f_macadamia": ["i_palmitoleico"], "f_mani": ["i_mufa"],
          "f_ginkgo": ["i_composicion"], "f_nuez_brasil": ["i_saturados"], "f_semilla_melon_negro": ["i_linoleico"], "f_granada": ["i_clna"],
          "f_trichosanthes": ["i_clna"], "f_santalum": ["i_ximeninico"], "f_boraginaceas": ["i_gla", "i_sda"], "i_saturados": ["i_tag"], "i_mufa": ["i_tag"], "i_linoleico": ["i_tag"], "i_ala": ["i_tag"]}
req_sec = {"2.1": ["1.1"], "2.2": ["2.1"], "2.3": ["2.1"], "3.1": ["2.2"], "3.2": ["3.1"], "3.3": ["1.2"], "3.4": ["3.3"], "4.1": ["3.3"], "4.2": ["3.2"], "4.3": ["3.3"], "5.1": ["4.1", "4.2", "4.3"]}
req_ch = {"2": [1], "3": [2], "4": [3], "5": [4]}
g = {"meta": {"title": "Ácidos grasos de frutos secos y semillas como grafo",
  "subtitle": "Li y Hu, capítulo 4 de Nuts and Seeds in Health and Disease Prevention (Elsevier, 2011) · con alertas de evidencia actual",
  "itemLabel": "Ácido graso o alimento", "itemLabelPlural": "Ácidos grasos y alimentos", "resourceLabel": "Tabla", "resourceLabelPlural": "Tablas",
  "searchHint": "Buscar: nuez, ALA, ginkgo, punícico…"},
 "blocks": {"base": {"name": "Planteamiento y conclusiones", "color": "#6B8E4E"}, "lipidos": {"name": "Clases de lípidos", "color": "#B08A2E"},
            "perfil": {"name": "Perfil de ácidos grasos", "color": "#3F6FA0"}, "especiales": {"name": "Ácidos grasos especiales", "color": "#A05A3C"}},
 "chapters": chapters, "items": items,
 "resources": [{"id": "4.1", "title": "Lípidos totales y clases de lípidos de 12 frutos secos y semillas", "page": 36, "usedBy": ["2.1", "2.2", "2.3"]},
               {"id": "4.2–4.4", "title": "Ácidos grasos de 20 frutos secos y semillas (y figura 4.1)", "page": 37, "usedBy": ["3.1", "3.2", "3.3", "3.4"]},
               {"id": "4.5", "title": "Ácidos grasos de semillas de Trichosanthes y granada", "page": 39, "usedBy": ["4.1"]},
               {"id": "4.6", "title": "Ácidos grasos de almendras de seis especies de Santalum", "page": 39, "usedBy": ["4.2"]},
               {"id": "4.7", "title": "Ácidos grasos de semillas de Ribes y cuatro familias silvestres", "page": 40, "usedBy": ["4.3"]}],
 "requires": {"chapters": req_ch, "sections": req_sec, "items": req_it}}
json.dump(g, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("partes", len(chapters), "secciones", sum(len(c["sections"]) for c in chapters), "ítems", len(items), "alertas", sum('caution' in v for v in items.values()),
      "alertas sin ítem", [k for k in AL if k not in items])
