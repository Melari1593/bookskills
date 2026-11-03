"""Definición del grafo del capítulo 14 (2.ª ed., 2020): semilla de tamarindo en salud y nutrición (Pal y Mukherjee). Resúmenes propios."""
def s(num, title, summary, items=None, page=None):
    d = {"num": num, "title": title, "summary": summary}
    if items: d["items"] = items
    if page: d["page"] = page
    return d
META = {"title": "Semilla de tamarindo como grafo", "subtitle": "Pal y Mukherjee, capítulo 14 de Nuts and Seeds in Health and Disease Prevention, 2.ª ed. (Elsevier, 2020) · con alertas de evidencia actual",
        "itemLabel": "Componente o efecto", "itemLabelPlural": "Componentes y efectos", "resourceLabel": "Tabla", "resourceLabelPlural": "Tablas", "searchHint": "Buscar: proteína, antiveneno, TSP, ojo seco…"}
BLOCKS = {"planta": {"name": "La planta", "color": "#6B8E4E"}, "nutricion": {"name": "Composición", "color": "#B08A2E"}, "actividad": {"name": "Actividades biológicas", "color": "#3F6FA0"},
          "tsp": {"name": "Polisacárido (TSP)", "color": "#6B5B95"}, "riesgo": {"name": "Seguridad y resumen", "color": "#B5465A"}}
CHAPTERS = [
 {"num": 1, "title": "El tamarindo y su cultivo", "block": "planta", "page": 171, "summary": "Árbol tropical de la familia Fabaceae cuyas semillas son un subproducto de la industria de la pulpa.",
  "sections": [s("1.1", "Introducción", "La semilla es un tercio del fruto y un subproducto de la pulpa; se le atribuyen efectos antidiabéticos, hipolipemiantes, hepatoprotectores y antimicrobianos.", None, 171),
               s("1.2", "Descripción, nombres y taxonomía", "Árbol perenne de hasta 24 m con vainas que contienen de 3 a 10 semillas duras y brillantes; se recogen sus nombres en lenguas de la India.", None, 172),
               s("1.3", "Cultivo histórico y actual", "Probablemente originario de África tropical, cultivado desde hace milenios en la India y llevado a América en el siglo XVI; la pulpa es laxante por sus ácidos orgánicos.", None, 174)]},
 {"num": 2, "title": "Composición de la semilla", "block": "nutricion", "page": 176, "summary": "Proteína, aceite, minerales y fitoquímicos de la semilla y de su cubierta.",
  "sections": [s("2.1", "Proteína y aminoácidos", "Semilla y almendra son ricas en proteína con aminoácidos esenciales cerca del patrón de la OMS, salvo triptófano; la cubierta tiene mucha fibra y taninos.", ["i_proteina"], 176),
               s("2.2", "Aceite y ácidos grasos", "Aceite ámbar, no secante y estable; el capítulo destaca su linoleico y lo propone como aceite comestible.", ["i_aceite"], 176),
               s("2.3", "Minerales", "Calcio, fósforo, magnesio y potasio con rangos muy amplios entre estudios; el potasio es el más abundante (tabla 14.1).", ["i_minerales"], 176),
               s("2.4", "Fitoquímicos", "Fenoles, procianidinas, flavonoides (apigenina, naringenina, taxifolina), triterpenos y un polisacárido de xiloglucano.", ["i_fitoquimicos"], 177)]},
 {"num": 3, "title": "Actividades biológicas", "block": "actividad", "page": 177, "summary": "Efectos descritos sobre todo en extractos, células y animales: antioxidante, antidiabético, antiveneno, anticanceroso, antiinflamatorio, ocular y de reparación nerviosa.",
  "sections": [s("3.1", "Antioxidante", "Los extractos de la cubierta muestran actividad antioxidante en ensayos químicos; se proponen como antioxidante barato.", ["i_antioxidante"], 177),
               s("3.2", "Antidiabético", "Un extracto acuoso bajó la glucemia y los lípidos en ratas diabéticas.", ["i_antidiabetico"], 177),
               s("3.3", "Antiveneno de serpiente", "El extracto inhibió enzimas del veneno y redujo sus efectos en modelos; los autores lo plantean como alternativa a la sueroterapia.", ["i_antiveneno"], 177),
               s("3.4", "Anticanceroso", "Efecto protector en nefrotoxicidad química y carcinoma renal atribuido a sus polifenoles.", ["i_anticancer"], 178),
               s("3.5", "Antiinflamatorio y analgésico", "Efecto antiinflamatorio menor que el de la aspirina, con acción analgésica en modelos de dolor.", ["i_antiinflamatorio"], 178),
               s("3.6", "Ojo y nervio", "El polisacárido se usa en colirios para ojo seco y cicatrización corneal; también sirve de soporte para regenerar nervios.", ["i_tsp_ojo"], 178)]},
 {"num": 4, "title": "Polisacárido de semilla de tamarindo (TSP)", "block": "tsp", "page": 178, "summary": "El TSP como excipiente farmacéutico y aditivo alimentario.",
  "sections": [s("4.1", "TSP como excipiente", "Espesante, aglutinante, estabilizante y vehículo de liberación de fármacos por vía oral, bucal, colónica y ocular; también en alimentos y cosméticos.", ["i_tsp_aditivo"], 178)]},
 {"num": 5, "title": "Seguridad y resumen", "block": "riesgo", "page": 180, "summary": "Los autores consideran la semilla segura y advierten de posibles efectos sobre la glucemia y la absorción de analgésicos.",
  "sections": [s("5.1", "Posibles efectos adversos", "Sin riesgo con uso adecuado según el capítulo; advierte de hipoglucemia y de mayor absorción de aspirina e ibuprofeno.", ["i_seguridad"], 180),
               s("5.2", "Puntos clave", "Fuente de aminoácidos esenciales y fitoquímicos con usos tradicionales; los autores piden más investigación.", None, 180)]}]
ITEMS = {
 "i_proteina": ("Proteína de la semilla", "Proteína con perfil de aminoácidos esenciales cercano al patrón de referencia, salvo triptófano.", "Leucina 531 mg/g de proteína · lisina 475 mg/g"),
 "i_aceite": ("Aceite de semilla", "Aceite no secante con linoleico como ácido graso principal; el capítulo lo propone como aceite comestible.", "Linoleico 36–49 % · palmítico 14–20 %"),
 "i_minerales": ("Minerales", "Potasio como mineral más abundante; rangos muy amplios entre estudios.", "Potasio 273–610 mg/100 g · calcio 9–786 mg/100 g"),
 "i_fitoquimicos": ("Fitoquímicos", "Procianidinas, catequinas, flavonoides y triterpenos (lupeol, lupanona), sobre todo en la cubierta."),
 "i_antioxidante": ("Actividad antioxidante", "Capacidad antioxidante de extractos de la cubierta en ensayos químicos de laboratorio."),
 "i_antidiabetico": ("Efecto antidiabético", "Descenso de glucemia y lípidos con extracto acuoso en ratas diabéticas."),
 "i_antiveneno": ("Efecto antiveneno", "Inhibición de enzimas del veneno de serpiente por el extracto en modelos de laboratorio."),
 "i_anticancer": ("Efecto anticanceroso", "Protección frente a daño renal químico y carcinoma renal en modelos, atribuida a polifenoles."),
 "i_antiinflamatorio": ("Efecto antiinflamatorio y analgésico", "Efecto en modelos de inflamación y dolor, menor que el de la aspirina."),
 "i_tsp_ojo": ("TSP en el ojo", "Polisacárido mucoadhesivo usado en colirios para ojo seco y cicatrización corneal."),
 "i_tsp_aditivo": ("TSP como excipiente y aditivo", "Xiloglucano usado como espesante, aglutinante y vehículo de fármacos, y en alimentos."),
 "i_seguridad": ("Seguridad e interacciones", "Afirmación de ausencia de riesgo con uso adecuado; posibles efectos sobre glucemia y absorción de aspirina e ibuprofeno.")}
REQ_IT = {"i_antioxidante": ["i_fitoquimicos"], "i_anticancer": ["i_antioxidante"], "i_antiinflamatorio": ["i_fitoquimicos"], "i_antidiabetico": ["i_fitoquimicos"], "i_tsp_ojo": ["i_tsp_aditivo"], "i_seguridad": ["i_antidiabetico"]}
REQ_SEC = {"1.2": ["1.1"], "1.3": ["1.2"], "2.1": ["1.1"], "2.2": ["2.1"], "2.3": ["2.1"], "2.4": ["2.1"], "3.1": ["2.4"], "3.2": ["2.4"], "3.3": ["2.4"], "3.4": ["3.1"],
           "3.5": ["2.4"], "3.6": ["2.4"], "4.1": ["2.4"], "5.1": ["3.2"], "5.2": ["5.1"]}
REQ_CH = {"2": [1], "3": [2], "4": [2], "5": [3]}
RESOURCES = [{"id": "14.1", "title": "Composición mineral de la semilla de tamarindo", "page": 176, "usedBy": ["2.3"]}]
