"""Definición del grafo del capítulo «Apharsemon, Myrrh and Olibanum: Ancient Medical Plants» (Ben-Yehoshua y Hanuš, 2014). Resúmenes propios."""
def s(num, title, summary, items=None, page=None):
    d = {"num": num, "title": title, "summary": summary}
    if items: d["items"] = items
    if page: d["page"] = page
    return d
META = {"title": "Mirra, olíbano y apharsemon como grafo", "subtitle": "Ben-Yehoshua y Hanuš, capítulo de Medicinal and Aromatic Plants of the Middle-East (Yaniv y Dudai, eds.; Springer, 2014) · con alertas de evidencia actual",
        "itemLabel": "Planta, compuesto o uso", "itemLabelPlural": "Plantas, compuestos y usos", "resourceLabel": "Tabla", "resourceLabelPlural": "Tablas", "searchHint": "Buscar: AKBA, incensol, Forsskål, Mirazid, Punt…"}
BLOCKS = {"botanica": {"name": "Botánica", "color": "#6B8E4E"}, "historia": {"name": "Historia y usos antiguos", "color": "#B08A2E"},
          "quimica": {"name": "Química", "color": "#6B5B95"}, "produccion": {"name": "Ecología y producción", "color": "#3F8A8A"},
          "investigacion": {"name": "Investigación y futuro", "color": "#3F6FA0"}}
CHAPTERS = [
 {"num": 1, "title": "Taxonomía e identificación", "block": "botanica", "page": 68, "summary": "Cómo se identificaron el apharsemon, la mirra y el olíbano, y por qué la clasificación de las Burseráceas sigue siendo inestable.",
  "sections": [s("1.1", "El apharsemon y sus nombres", "Los autores identifican el bálsamo bíblico con Commiphora gileadensis y proponen que el cultivo en Judea mejoró la planta traída de Saba.", ["p_apharsemon"], 68),
               s("1.2", "La expedición de Forsskål", "En 1763 Forsskål halló en Yemen un árbol aromático y lo vinculó con el bálsamo; murió en el viaje y Niebuhr publicó sus notas.", ["h_forsskal"], 70),
               s("1.3", "De Amyris a Commiphora", "Durante el siglo XIX el bálsamo cambió de género varias veces; Engler adoptó Commiphora en 1883 y la familia sigue siendo difícil de clasificar.", ["p_burseraceae"], 72),
               s("1.4", "Taxonomía actual", "Hoy el nombre aceptado es Commiphora gileadensis, con C. opobalsamum como sinónimo, dentro de Burseraceae y el orden Sapindales.", None, 76),
               s("1.5", "Identificación de la mirra", "La mirra procede sobre todo de Commiphora myrrha; no hay acuerdo sobre qué especie daba la mirra bíblica.", ["p_mirra"], 77),
               s("1.6", "Identificación del olíbano", "Boswellia agrupa varias especies; B. sacra (o B. carterii) y B. frereana dan el incienso de mayor valor comercial.", ["p_olibano"], 77)]},
 {"num": 2, "title": "Usos como droga cruda", "block": "historia", "page": 79, "summary": "Qué productos se obtenían de cada resina en la Antigüedad y qué rastros se han buscado del apharsemon.",
  "sections": [s("2.1", "La resina del apharsemon", "La resina servía para incienso, perfume y medicinas; su precio superaba al de cualquier otro producto agrícola.", None, 79),
               s("2.2", "El apharsemon en Judea", "La Biblia cita el comercio del tzori, aunque los autores fechan su llegada a Judea en la época de Salomón.", None, 80),
               s("2.3", "Búsqueda actual de restos", "Ningún hallazgo arqueológico de Qumrán ni de cajas antiguas mostró marcadores químicos de Commiphora o Boswellia.", None, 80),
               s("2.4", "La mirra en ritos y embalsamamiento", "En Egipto la mirra se quemaba en ofrendas y se usaba para embalsamar; también aparece en los Evangelios.", ["h_embalsamamiento"], 82),
               s("2.5", "El nombre del olíbano", "Olíbano y levonah aluden al color blanco de las mejores gotas de resina; su uso principal es quemarlo en ceremonias.", None, 83)]},
 {"num": 3, "title": "Constituyentes químicos y compuestos bioactivos", "block": "quimica", "page": 84, "summary": "Terpenos y otros compuestos aislados de cada resina, con algunas actividades medidas en laboratorio.",
  "sections": [s("3.1", "Compuestos del apharsemon", "Monoterpenos y sesquiterpenos como linalol, germacreno D y β-cariofileno; las muestras de distintos países quizá no sean la misma planta.", ["c_terpenos_apharsemon"], 84),
               s("3.2", "Compuestos de la mirra", "Furanosesquiterpenos típicos y muchos compuestos nuevos; algunos inhiben la aromatasa o el crecimiento de células endoteliales.", ["c_sesquiterpenos_mirra"], 84),
               s("3.3", "Compuestos del olíbano", "Ácidos boswélicos, incensol y su acetato, triterpenos nuevos y un aceite esencial rico en pineno o limoneno según la especie.", ["c_acidos_boswellicos", "c_incensol", "c_aceite_olibano"], 88)]},
 {"num": 4, "title": "Descripción morfológica", "block": "botanica", "page": 93, "summary": "Rasgos de hoja, flor, corteza y porte de las tres plantas.",
  "sections": [s("4.1", "Morfología del apharsemon", "Árbol mediano de hojas trifoliadas, corteza gris lisa que suelta resina al herirse y flores de cuatro pétalos.", None, 93),
               s("4.2", "Morfología de la mirra", "Árbol bajo y espinoso de corteza que se pela, casi siempre sin hojas; nunca se ha cultivado en plantaciones.", None, 94),
               s("4.3", "Morfología del olíbano", "Arbusto o árbol pequeño; el clima de Dhofar da las resinas más finas y B. serrata tiene tronco recto y aroma distinto.", None, 95)]},
 {"num": 5, "title": "Distribución geográfica, producción y ecología", "block": "produccion", "page": 96, "summary": "Dónde crecen las tres plantas, cómo se comerciaban y por qué hoy su producción es escasa.",
  "sections": [s("5.1", "Apharsemon y rutas del incienso", "El apharsemon se cultivó solo en Jericó y Ein Gedi; mirra e incienso viajaban desde el sur de Arabia por rutas controladas por varios pueblos.", ["h_ruta_incienso"], 96),
               s("5.2", "Zonas de la mirra", "La mirra antigua venía del sur de Arabia; hoy se concentra en Somalia y también en la India.", None, 98),
               s("5.3", "Zonas del olíbano", "La lluvia y el suelo limitan la distribución de Boswellia; el tipo Hojari de Omán es el más caro.", None, 99),
               s("5.4", "Producción actual en África", "La producción y la exportación son bajas, las poblaciones de árboles disminuyen y la sangría excesiva reduce la germinación.", ["h_produccion_actual"], 99),
               s("5.5", "Requisitos ecológicos", "Mirra e incienso crecen en suelos pobres y rocosos; Boswellia prefiere caliza y clima seco.", None, 101)]},
 {"num": 6, "title": "Cosecha", "block": "produccion", "page": 101, "summary": "Técnicas de incisión para obtener cada resina y costumbres asociadas a la cosecha.",
  "sections": [s("6.1", "Cosecha del apharsemon", "Los agricultores de Judea cortaban con vidrio, piedra o hueso, porque el hierro dañaba el arbusto; hoy el hacha daña mirra e incienso.", ["h_cosecha"], 101),
               s("6.2", "Cosecha de la mirra", "Se corta la corteza y la goma amarilla fluye y se endurece en lágrimas rojizas.", None, 102),
               s("6.3", "Cosecha del olíbano y folclore de Dhofar", "Se raspa la corteza, se recoge a las dos semanas y se cosecha unas dos veces al año; en Dhofar acompaña partos, bodas y funerales.", None, 102)]},
 {"num": 7, "title": "Historia, uso tradicional, ritual y cosmético", "block": "historia", "page": 103, "summary": "Papel de las tres resinas en Egipto, Judea, Roma y las religiones, y causas del fin del apharsemon.",
  "sections": [s("7.1", "Arqueología e historia", "La alta demanda de resinas escasas impulsó rutas comerciales largas hacia los grandes imperios.", None, 103),
               s("7.2", "Especias en el antiguo Egipto", "Egipto importaba mirra de Punt; Hatshepsut envió una expedición que trajo árboles, sin pruebas de que prosperaran.", ["h_punt"], 104),
               s("7.3", "Especias en Judea", "Restos de altares, recipientes y sellos muestran comercio entre el sur de Arabia y Judea desde el siglo IX a. C.", None, 105),
               s("7.4", "Auge y caída del apharsemon", "Un gremio guardó en secreto su cultivo durante siglos; Herodes y Roma lo explotaron y desapareció tras la conquista árabe.", ["h_gremio_ein_gedi"], 106),
               s("7.5", "La mirra en ritos y bebidas", "La mirra formó parte del kyphi egipcio, de vinos romanos y de licores de hierbas modernos.", ["h_kyphi"], 111),
               s("7.6", "El olíbano en religión y folclore", "El incienso acompaña rezos judíos y cristianos; en Yemen sirve para perfumar, reparar vasijas, teñir y como remedio casero.", None, 112)]},
 {"num": 8, "title": "Investigación moderna basada en usos tradicionales, y patentes", "block": "investigacion", "page": 114, "summary": "Usos tradicionales de cada resina contrastados con estudios de laboratorio, animales, algunos ensayos clínicos y patentes.",
  "sections": [s("8.1", "Apharsemon en la medicina tradicional", "Se usó como remedio para casi todo; el capítulo también recoge avisos de alergia y confusiones con otros «bálsamos de Galaad».", ["u_seguridad"], 114),
               s("8.2", "Apharsemon: estudios farmacológicos", "Extractos con efecto antiinflamatorio, antimicrobiano y citotóxico; el β-cariofileno induciría apoptosis en células tumorales.", ["u_antimicrobiano", "c_beta_cariofileno"], 116),
               s("8.3", "Mirra: tradición, mitridato y parásitos", "La mirra entró en antídotos antiguos; un extracto de C. molmol se probó contra la esquistosomiasis con resultados opuestos.", ["h_mitridato", "u_esquistosomiasis"], 118),
               s("8.4", "Mirra y guggul: estudios y patentes", "Estudios en animales y células sobre dolor, lípidos, infección y cáncer, y patentes sobre Commiphora y gugulípido.", ["p_guggul", "u_analgesia"], 120),
               s("8.5", "Olíbano: tradición y patentes", "Textos egipcios, árabes, chinos y ayurvédicos lo recetan; hay patentes de ácidos boswélicos para inflamación, cerebro, piel y cáncer.", None, 128),
               s("8.6", "Olíbano: investigación reciente", "Ácidos boswélicos en inflamación crónica y artrosis, incensol en el ánimo, efectos antitumorales y daño del humo en ratas.", ["u_artrosis", "u_inflamacion_cronica", "u_animo", "u_cancer", "u_humo_incienso"], 131)]},
 {"num": 9, "title": "Conclusiones", "block": "investigacion", "page": 136, "summary": "Los autores ven en el potencial médico de estas resinas una vía para reactivar su producción, incluido el apharsemon en el mar Muerto.",
  "sections": [s("9.1", "Futuro de mirra e incienso", "El comercio es mínimo, pero los autores proponen buscar fármacos en textos antiguos y dar ingresos a las regiones productoras.", ["h_arqueofarmacologia"], 136),
               s("9.2", "¿Revivir el apharsemon?", "Ya crecen miles de plantas candidatas cerca del mar Muerto; su resina mostró actividad citotóxica en líneas tumorales.", None, 138)]}]
ITEMS = {
 "p_apharsemon": ("Apharsemon (bálsamo de Judea)", "Commiphora gileadensis, sinónimo C. opobalsamum. Según el capítulo, se cultivó solo junto al mar Muerto y hoy está extinguido allí.", "Precio: el doble de su peso en oro en la Edad Media"),
 "h_forsskal": ("Expedición de Forsskål", "Viaje danés a Yemen en 1763 que identificó un árbol aromático como fuente del opobálsamo; Linneo lo llamó Amyris gileadensis.", "Año 1763 · unas 2 000 notas sueltas"),
 "p_burseraceae": ("Familia Burseraceae", "Familia de árboles con resina aromática que incluye Commiphora y Boswellia; su taxonomía es inestable porque las plantas pasan casi todo el año sin hojas.", "17 géneros · unas 560 especies"),
 "p_mirra": ("Mirra (Commiphora myrrha y afines)", "Oleogomorresina amarga de Commiphora myrrha y especies cercanas, recogida de árboles silvestres de Arabia y el Cuerno de África.", "Aceite volátil 7–17 % · resina 25–40 % · goma 57–61 %"),
 "p_olibano": ("Olíbano (Boswellia spp.: incienso)", "Resina de varias especies de Boswellia; B. sacra (o B. carterii) es el incienso bíblico y B. serrata el indio.", "5 especies; 2 de valor comercial (van Beek)"),
 "h_embalsamamiento": ("Mirra en el embalsamamiento", "Según el capítulo, los egipcios usaban mucha mirra e incienso para preservar los cuerpos por su acción antibacteriana."),
 "c_terpenos_apharsemon": ("Terpenos del apharsemon", "Monoterpenos y sesquiterpenos como linalol, α-terpineol, germacreno D y β-cariofileno, más lactonas y triterpenos nuevos."),
 "c_sesquiterpenos_mirra": ("Furanosesquiterpenos de la mirra", "Compuestos típicos de la mirra, como curzereno, furanodieno y furanoeudesma-1,3-dieno; algunos inhiben la aromatasa en ensayos.", "CI50 de aromatasa 0,2–0,3 μM (dos compuestos)"),
 "c_acidos_boswellicos": ("Ácidos boswélicos (incluido AKBA)", "Triterpenos α y β del olíbano y sus acetatos; el AKBA (ácido acetil-11-ceto-β-boswélico) es el más estudiado."),
 "c_incensol": ("Incensol y acetato de incensol", "Diterpenos característicos del olíbano; el capítulo señala el acetato de incensol como uno de sus principios activos principales."),
 "c_aceite_olibano": ("Aceite esencial del olíbano", "Mezcla de monoterpenos cuya composición cambia con la especie y el origen; domina el limoneno, el ocimeno o el α-pineno.", "B. sacra: α-pineno 46,8–76,0 % en Omán (tabla 4)"),
 "h_ruta_incienso": ("Rutas del incienso", "Cadenas de pueblos árabes llevaban mirra e incienso del sur de Arabia hasta Egipto, Siria y Mesopotamia, y guardaban en secreto su origen.", "Aelana–Minea: 70 días de viaje"),
 "h_produccion_actual": ("Producción actual y declive", "Según el capítulo, el comercio es hoy mínimo, viene sobre todo de Somalia y los árboles disminuyen por sobreexplotación, pastoreo y fuego.", "Exportación 1 000–1 500 t/año · germinación 16 % frente a >80 %"),
 "h_cosecha": ("Técnica de cosecha sin hierro", "Los agricultores de Judea hacían incisiones con vidrio, piedra o hueso; el capítulo atribuye al hierro un efecto letal sobre el arbusto."),
 "h_punt": ("Expedición a Punt", "Hatshepsut envió barcos a Punt que volvieron con árboles de incienso o mirra en macetas; no consta que crecieran en Egipto.", "Hacia 1500 a. C. · 31 árboles en un barco"),
 "h_gremio_ein_gedi": ("Gremio de Ein Gedi", "Agricultores organizados que guardaron el secreto del cultivo del apharsemon; su producción decayó tras la conquista árabe del siglo VII.", "Más de 1 000 años de cultivo"),
 "h_kyphi": ("Kyphi", "Perfume sagrado egipcio con mirra e incienso, usado en ritos y como medicina.", "16 ingredientes"),
 "u_seguridad": ("Seguridad y toxicidad", "Según el capítulo, el bálsamo de La Meca causaba reacciones faciales y alergia, la mirra en exceso da náusea y vómito, y el apharsemon se usaba como abortivo; no trata interacciones."),
 "u_antimicrobiano": ("Efecto antimicrobiano", "Según el capítulo, la savia del apharsemon y los aceites de mirra e incienso inhiben bacterias y hongos en ensayos de laboratorio."),
 "c_beta_cariofileno": ("β-cariofileno del apharsemon", "Componente principal del aceite esencial del apharsemon; según los autores, induce apoptosis en células de linfoma y no en células normales.", "20,12 % del aceite esencial"),
 "h_mitridato": ("Mitridato y teriaca", "Antídoto antiguo con mirra, ampliado por Galeno como teriaca; Jerusalén fue un centro de producción.", "63 ingredientes en 1659"),
 "u_esquistosomiasis": ("Mirra contra parásitos (Mirazid)", "Según el capítulo, un extracto de C. molmol (Mirazid) curó esquistosomiasis y otras parasitosis en algunos estudios, pero otros no hallaron eficacia."),
 "p_guggul": ("Guggul (Commiphora mukul o wightii)", "Resina ayurvédica cuyo extracto, el gugulípido, se propone para bajar lípidos; según el capítulo, un ensayo aleatorizado no mejoró el colesterol."),
 "u_analgesia": ("Efecto analgésico de la mirra", "Según el capítulo, el furanoeudesma-1,3-dieno y el curzereno redujeron el dolor en ratones al actuar sobre receptores opioides."),
 "u_artrosis": ("Boswellia en artrosis", "Según el capítulo, un extracto enriquecido de B. serrata (5-Loxin) redujo el dolor de rodilla y mejoró la función frente a placebo.", "75 pacientes con artrosis de rodilla"),
 "u_inflamacion_cronica": ("Boswellia en inflamación crónica", "Según el capítulo, los ácidos boswélicos ayudan en colitis, enfermedad de Crohn, artritis reumatoide y asma, sin dañar el cartílago como los AINE."),
 "u_animo": ("Incensol y estado de ánimo", "Según el capítulo, el acetato de incensol redujo la ansiedad y produjo una conducta similar a la antidepresiva en ratones."),
 "u_cancer": ("Efectos antitumorales", "Según el capítulo, extractos y compuestos de las tres plantas frenan o matan células tumorales de próstata, mama, páncreas, vejiga y linfoma en laboratorio."),
 "u_humo_incienso": ("Exposición al humo de incienso", "Según el capítulo, el humo de B. carterii bajó el recuento de espermatozoides en ratas, y los autores advierten del riesgo en exposición continua en interiores.", "4 g/día, 30–40 min/día durante 4 meses"),
 "h_arqueofarmacologia": ("Arqueofarmacología", "Propuesta de buscar nuevos fármacos a partir de textos médicos antiguos; los autores la aplican a mirra, incienso y apharsemon.")}
REQ_IT = {"h_forsskal": ["p_apharsemon"], "p_burseraceae": ["h_forsskal"], "p_mirra": ["p_burseraceae"], "p_olibano": ["p_burseraceae"],
          "h_embalsamamiento": ["p_mirra"], "c_terpenos_apharsemon": ["p_apharsemon"], "c_sesquiterpenos_mirra": ["p_mirra"],
          "c_acidos_boswellicos": ["p_olibano"], "c_incensol": ["p_olibano"], "c_aceite_olibano": ["p_olibano"],
          "h_ruta_incienso": ["p_mirra", "p_olibano"], "h_produccion_actual": ["h_ruta_incienso"], "h_cosecha": ["p_apharsemon"],
          "h_punt": ["h_ruta_incienso"], "h_gremio_ein_gedi": ["h_cosecha"], "h_kyphi": ["p_mirra", "p_olibano"],
          "u_seguridad": ["p_apharsemon", "p_mirra"], "c_beta_cariofileno": ["c_terpenos_apharsemon"],
          "u_antimicrobiano": ["c_terpenos_apharsemon", "c_sesquiterpenos_mirra"], "h_mitridato": ["h_kyphi"],
          "u_esquistosomiasis": ["c_sesquiterpenos_mirra"], "p_guggul": ["p_mirra"], "u_analgesia": ["c_sesquiterpenos_mirra"],
          "u_artrosis": ["c_acidos_boswellicos"], "u_inflamacion_cronica": ["c_acidos_boswellicos"], "u_animo": ["c_incensol"],
          "u_cancer": ["c_beta_cariofileno", "c_acidos_boswellicos"], "u_humo_incienso": ["p_olibano"],
          "h_arqueofarmacologia": ["h_mitridato", "u_cancer"]}
REQ_SEC = {"1.2": ["1.1"], "1.3": ["1.2"], "1.4": ["1.3"], "1.5": ["1.3"], "1.6": ["1.3"],
           "2.1": ["1.1"], "2.2": ["2.1"], "2.3": ["2.2"], "2.4": ["1.5"], "2.5": ["1.6"],
           "3.1": ["1.4"], "3.2": ["1.5"], "3.3": ["1.6"], "4.1": ["1.4"], "4.2": ["1.5"], "4.3": ["1.6"],
           "5.1": ["2.2"], "5.2": ["4.2"], "5.3": ["4.3"], "5.4": ["5.3"], "5.5": ["5.3"],
           "6.1": ["4.1"], "6.2": ["4.2"], "6.3": ["4.3"],
           "7.1": ["5.1"], "7.2": ["7.1"], "7.3": ["7.1"], "7.4": ["7.3", "6.1"], "7.5": ["2.4"], "7.6": ["2.5"],
           "8.1": ["2.1"], "8.2": ["3.1", "8.1"], "8.3": ["7.5"], "8.4": ["3.2", "8.3"], "8.5": ["7.6"], "8.6": ["3.3", "8.5"],
           "9.1": ["8.6", "5.4"], "9.2": ["8.2", "7.4"]}
REQ_CH = {"2": [1], "3": [1], "4": [1], "5": [4], "6": [4], "7": [2, 5], "8": [3, 7], "9": [8]}
RESOURCES = [{"id": "1", "title": "Terpenos principales de Boswellia sacra", "page": 91, "usedBy": ["3.3"]},
             {"id": "2", "title": "Terpenos principales de B. sacra y B. carterii comparados", "page": 91, "usedBy": ["3.3"]},
             {"id": "3", "title": "Terpenos de muestras de B. carterii y B. sacra comparados", "page": 134, "usedBy": ["8.6"]},
             {"id": "4", "title": "Terpenos principales de muestras de B. sacra de Omán", "page": 135, "usedBy": ["8.6"]}]

# Añadido tras la verificación: afirmación del gugulípido sobre los lípidos (M13).
ITEMS["u_hiperlipidemia"] = ("Gugulípido y colesterol", "Según el capítulo, el gugulípido de Commiphora mukul se ha estudiado y patentado para bajar el colesterol.")
REQ_IT["u_hiperlipidemia"] = ["p_guggul"]
for _c in CHAPTERS:
    for _s in _c["sections"]:
        if _s["num"] == "8.4":
            _s.setdefault("items", []).append("u_hiperlipidemia")
