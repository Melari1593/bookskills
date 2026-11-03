"""Definición del grafo del capítulo 7 (2.ª ed., 2020): compuestos bioactivos de la semilla de orégano (Atar y Çölgeçen). Resúmenes propios."""
def s(num, title, summary, items=None, page=None):
    d = {"num": num, "title": title, "summary": summary}
    if items: d["items"] = items
    if page: d["page"] = page
    return d
META = {"title": "Semilla de orégano como grafo", "subtitle": "Atar y Çölgeçen, capítulo 7 de Nuts and Seeds in Health and Disease Prevention, 2.ª ed. (Elsevier, 2020) · con alertas de evidencia actual",
        "itemLabel": "Concepto o afirmación", "itemLabelPlural": "Conceptos y afirmaciones", "resourceLabel": "Recurso", "resourceLabelPlural": "Recursos", "searchHint": "Buscar: carvacrol, colesterol, aceite esencial…"}
BLOCKS = {"planta": {"name": "La planta y su uso", "color": "#6B8E4E"}, "salud": {"name": "Salud y composición", "color": "#3F6FA0"}, "riesgo": {"name": "Seguridad", "color": "#B5465A"}}
CHAPTERS = [
 {"num": 1, "title": "El orégano y su cultivo", "block": "planta", "page": 73, "summary": "Qué es el género Origanum, por qué Turquía lo cultiva cada vez más y cómo se ha usado desde la Antigüedad.",
  "sections": [s("1.1", "Introducción", "El orégano es la planta medicinal más extendida de Turquía; su producción crece por sus compuestos bioactivos: aceite esencial, fenoles, flavonoides y ácido rosmarínico.", ["i_compuestos"], 73),
               s("1.2", "Descripción botánica", "Género de la familia Lamiaceae con 41 especies; en Turquía se cultivan con fines medicinales O. onites, O. vulgare, O. majorana, O. minutiflorum y O. syriacum.", ["i_especies"], 74),
               s("1.3", "Usos históricos", "Planta ligada a ritos y mitos antiguos; los autores afirman que la investigación ya demostró que las plantas tratan enfermedades graves.", ["i_plantas_curan"], 74),
               s("1.4", "Cultivo y usos actuales", "Se usa como especia, en infusiones y cosméticos; su aceite esencial alarga la vida útil de carnes, pescados y frutas en recubrimientos comestibles.", ["i_conservacion_alimentos"], 74)]},
 {"num": 2, "title": "Salud y composición de la semilla", "block": "salud", "page": 75, "summary": "Usos tradicionales y supuestos beneficios del orégano, y lo poco que se sabe de la composición de su semilla.",
  "sections": [s("2.1", "Usos tradicionales", "Medicina tradicional iraní y turca: diurético, expectorante y remedio para afecciones respiratorias, menstruales, renales y metabólicas; el agua de orégano bajaría colesterol y glucosa.", ["i_usos_tradicionales"], 75),
               s("2.2", "Composición de la semilla", "Las semillas tienen catequina, ácidos fenólicos y un aceite muy rico en ácido linolénico; también triacilgliceroles y planteosa.", ["i_semilla_acidos"], 75),
               s("2.3", "Aceite esencial y sus actividades", "El aceite (carvacrol, timol, p-cimeno, γ-terpineno) se vende como antioxidante y antimicrobiano y se le atribuyen efectos hipolipemiantes, analgésicos, antivirales y anticancerosos.", ["i_aceite_esencial", "i_compuestos"], 75),
               s("2.4", "Efecto protector del ADN", "Un extracto redujo micronúcleos en linfocitos humanos y médula de ratón y se describe como radioprotector.", ["i_radioproteccion"], 75)]},
 {"num": 3, "title": "Efectos adversos y resumen", "block": "riesgo", "page": 75, "summary": "Dosis altas del aceite pueden causar síntomas digestivos y nerviosos; los autores piden prudencia en niños, embarazo, lactancia y diabetes.",
  "sections": [s("3.1", "Efectos adversos, alergias y toxicidad", "En dosis altas el aceite causa náuseas, vómitos y molestias gástricas; los fitoquímicos en exceso pueden ser tóxicos para varios órganos.", ["i_seguridad"], 75),
               s("3.2", "Puntos de resumen", "Planta de cultivo antiguo con semillas ricas en aceite esencial y ácidos grasos, útil para la industria y para alimentos funcionales según los autores.", None, 76)]}]
ITEMS = {
 "i_especies": ("Especies de Origanum", "Las especies medicinales cultivadas en Turquía; O. onites y O. vulgare son las comerciales más importantes.", "41 especies en el mundo · 23 en Turquía"),
 "i_compuestos": ("Compuestos bioactivos", "Aceite esencial con carvacrol y timol, fenoles, flavonoides, tocoferoles y ácidos rosmarínico y cinámico.", "Carvacrol · timol · p-cimeno · γ-terpineno"),
 "i_plantas_curan": ("Afirmación: las plantas tratan enfermedades graves", "El capítulo afirma que la investigación demostró la eficacia de las plantas contra cáncer, sida, Alzheimer, alcoholismo e infecciones."),
 "i_usos_tradicionales": ("Usos tradicionales del orégano", "Expectorante, diurético, digestivo y para trastornos menstruales, renales, hepáticos y metabólicos, según la medicina tradicional citada."),
 "i_semilla_acidos": ("Ácidos grasos del aceite de semilla", "Un estudio citado halla un aceite de semilla de O. vulgare dominado por ácido linolénico.", "Linolénico 64,6 % · linoleico 23,8 %"),
 "i_aceite_esencial": ("Aceite esencial de orégano", "Concentrado de terpenos y fenoles al que el capítulo atribuye efectos hipolipemiantes, analgésicos, antimicrobianos, antivirales y anticancerosos."),
 "i_radioproteccion": ("Afirmación: protege el ADN y la radiación", "Reducción de micronúcleos y efecto radioprotector de un extracto en células humanas y en ratones."),
 "i_seguridad": ("Seguridad del aceite de orégano", "Riesgo de síntomas digestivos e hiperactividad con dosis altas; prudencia en niños, embarazo, lactancia y diabetes."),
 "i_conservacion_alimentos": ("Conservación de alimentos", "Películas y recubrimientos comestibles con aceite de orégano que reducen el crecimiento microbiano y la oxidación.")}
REQ_IT = {"i_aceite_esencial": ["i_compuestos"], "i_seguridad": ["i_aceite_esencial"], "i_conservacion_alimentos": ["i_aceite_esencial"], "i_radioproteccion": ["i_compuestos"], "i_semilla_acidos": ["i_especies"], "i_usos_tradicionales": ["i_especies"]}
REQ_SEC = {"1.2": ["1.1"], "1.3": ["1.1"], "1.4": ["1.1"], "2.1": ["1.3"], "2.2": ["1.2"], "2.3": ["1.1"], "2.4": ["2.3"], "3.1": ["2.3"], "3.2": ["3.1"]}
REQ_CH = {"2": [1], "3": [2]}
