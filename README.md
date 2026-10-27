# bookskills

Skills de Claude basadas en libros y obras de referencia.

| Skill | Descripción |
|---|---|
| [`acupuntura-puntos`](.claude/skills/acupuntura-puntos/SKILL.md) | Los 361 puntos clásicos de acupuntura (MTC) por meridiano, con índice por síntoma y categorías (Shu, Yuan, Luo, Xi, Mu, Hui…). |
| [`harrys-cosmeticology`](.claude/skills/harrys-cosmeticology/SKILL.md) | *Harry's Cosmeticology* 9.ª ed. (Vol. 1, Vol. 2 y Sostenibilidad): 59 fichas de capítulo sobre formulación, ingredientes, sustratos, regulación y antienvejecimiento, con glosario, patrones, cheatsheet y consulta del grafo de conocimiento. |
| [`hemodinamia-grafo`](.claude/skills/hemodinamia-grafo/SKILL.md) | Mapa de estudio del *Manual de hemodinamia y aplicaciones clínicas en cardiología*: 16 capítulos, 149 secciones, 63 conceptos y rutas de prerrequisitos. |
| [`guyton-fisiologia-grafo`](.claude/skills/guyton-fisiologia-grafo/SKILL.md) | Mapa de estudio del *Tratado de fisiología médica* de Guyton y Hall, 14.ª ed.: 85 capítulos, 714 secciones, 391 conceptos clave y rutas de prerrequisitos, correlacionado con los 44 capítulos de *Berne & Levy Physiology*, 8.ª ed. |
| [`nutricion-pediatrica-grafo`](.claude/skills/nutricion-pediatrica-grafo/SKILL.md) | Mapa de estudio del *Manual of Pediatric Nutrition*, 3.ª ed. (Hendricks, Duggan y Walker), en español: 36 capítulos, 254 secciones, 174 conceptos clave, 5 apéndices, rutas de prerrequisitos y alertas de guías vigentes (octubre de 2026). |

## Atlas de Meridianos

`atlas/atlas-meridianos.html` es un mapa interactivo de los puntos de `acupuntura-puntos`: vistas anterior, posterior y de cabeza lateral, fichas completas y recetas por síntoma. Se abre directamente en el navegador.

Se genera a partir de las fichas de la skill, así que después de corregir una ficha hay que regenerarlo:

```bash
python3 atlas/build.py
```

`atlas/template.html` contiene la página (estilos y lógica) y `atlas/build.py` extrae los datos de `references/` y asigna a cada punto una posición esquemática en la figura.

## Graphify — Harry's Cosmeticology

`Graphify/graph.html` es un grafo de conocimiento interactivo de *Harry's Cosmeticology* (Vol. 1, Vol. 2 y Sostenibilidad): 2129 conceptos y 6434 relaciones entre ingredientes, anatomía, mecanismos, afecciones y regulación. El reporte está en `Graphify/GRAPH_REPORT.md`; detalles en [`Graphify/README.md`](Graphify/README.md). La skill `harrys-cosmeticology` incluye una copia del grafo y `scripts/graph_query.py` para consultarlo; `python3 Graphify/build.py` regenera ambos.

## Grafo de hemodinamia

[`Graphify/hemodinamia-grafo.html`](Graphify/hemodinamia-grafo.html) es el mapa interactivo autocontenido del manual de José Rafael López Luciano. Incluye buscador, tres vistas y trazado de prerrequisitos. La skill [`hemodinamia-grafo`](.claude/skills/hemodinamia-grafo/SKILL.md) contiene el JSON de datos y `scripts/ruta.py` para consultar rutas desde la terminal. Las conexiones son una interpretación pedagógica; las recomendaciones clínicas históricas del manual deben contrastarse con fuentes vigentes.

## Grafo de fisiología de Guyton y Hall

[`grafos/guyton-fisiologia/grafo_guyton.html`](grafos/guyton-fisiologia/grafo_guyton.html) es el mapa interactivo autocontenido del *Tratado de fisiología médica* de Guyton y Hall (14.ª ed., en español). Organiza los 85 capítulos en 8 bloques (célula y músculo; corazón y circulación; riñón; sangre e inmunidad; respiración; sistema nervioso; digestión, metabolismo y temperatura; endocrinología, reproducción y deporte) y tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_guyton.json`](grafos/guyton-fisiologia/grafo_guyton.json). La skill [`guyton-fisiologia-grafo`](.claude/skills/guyton-fisiologia-grafo/SKILL.md) incluye una copia y `scripts/ruta.py` para consultar rutas desde la terminal.

El grafo incluye además la correlación con *Berne & Levy Physiology* (8.ª ed.). Cada uno de sus 44 capítulos es un nodo cuadrado, con su página, un resumen en español y subtemas, enlazado a las secciones de Guyton que trata (530 enlaces). El panel de cada sección muestra qué leer en Berne & Levy para complementarla, y `ruta.py` lo lista junto a la ruta.

Al texto fuente le faltaban las páginas 794–846. Por eso los capítulos 64–67 y el principio del 68 se reconstruyeron con la estructura conocida de la edición, van sin páginas y están marcados como ausentes. Las páginas de las secciones son aproximadas (±1). Las conexiones son una interpretación pedagógica.

## Grafo de nutrición pediátrica

[`grafos/nutricion-pediatrica/grafo_nutricion_pediatrica.html`](grafos/nutricion-pediatrica/grafo_nutricion_pediatrica.html) es el mapa interactivo autocontenido del *Manual of Pediatric Nutrition* (3.ª ed., Hendricks, Duggan y Walker), traducido al español. Organiza los 36 capítulos en 7 bloques (evaluación y requerimientos; niño sano; hospitalización y soporte; crítico, inmunocomprometido y prematuro; enfermedades de órganos y sistemas; endocrino-metabólicas; crecimiento, conducta y alergia) y tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_nutricion_pediatrica.json`](grafos/nutricion-pediatrica/grafo_nutricion_pediatrica.json). La skill [`nutricion-pediatrica-grafo`](.claude/skills/nutricion-pediatrica-grafo/SKILL.md) incluye una copia y `scripts/ruta.py`, que lista la ruta de lectura, los apéndices que se consultan y las alertas de los conceptos implicados.

El libro es de alrededor del año 2000. 25 conceptos llevan un recuadro «Atención» con la guía que hoy reemplaza la recomendación del manual (Dietary Guidelines 2025–2030, AAP 2024 sobre VIH y lactancia, ESPGHAN/ESPEN 2018, ASPEN 2020, ISPAD 2024, Resolución 115 de 2026, entre otras). El grafo describe el libro; la actualización va solo en esas alertas.

El PDF fuente es un OCR de mala calidad: las cifras clínicas ilegibles se omitieron en lugar de reconstruirse. El libro no numera sus secciones, así que la numeración es propia del grafo. Las conexiones son una interpretación pedagógica.

## Grafo de HBR's 10 Must Reads for Business Students

[`grafos/hbr-10-must-reads/grafo_hbr_10_must_reads.html`](grafos/hbr-10-must-reads/grafo_hbr_10_must_reads.html) es el mapa interactivo de *HBR's 10 Must Reads for Business Students* (Harvard Business Review Press, 2023): 12 artículos (10 más 2 bonus), 55 secciones, 45 ideas clave y 44 prerrequisitos, en 4 bloques (gestionarte a ti mismo; comunicación e influencia; fortalezas, feedback e identidad; liderazgo, ética y propósito). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_hbr_10_must_reads.json`](grafos/hbr-10-must-reads/grafo_hbr_10_must_reads.json).

Los títulos de artículos y secciones van en inglés, como en el libro; los resúmenes están en español y redactados con palabras propias. El libro no numera las secciones, así que la numeración es propia del grafo; las páginas son las de inicio de cada artículo según el índice analítico. Los artículos son independientes entre sí: las conexiones son una interpretación pedagógica de cómo se complementan los temas.

## Grafo de The Five Elements Cookbook

[`grafos/five-elements-cookbook/grafo_five_elements_cookbook.html`](grafos/five-elements-cookbook/grafo_five_elements_cookbook.html) es el mapa interactivo de *The Five Elements Cookbook: A Guide to Traditional Chinese Medicine with Recipes for Everyday Healing* (Zoey Xinyi Gong): 25 capítulos, 165 secciones, 26 conceptos clave, 2 tablas y 703 prerrequisitos, en 5 bloques (fundamentos de la MTC; propiedades de los alimentos; estaciones y constituciones; las 50 hierbas; las 55 recetas). Cada hierba lleva su naturaleza, sabor, meridianos y dosis máxima diaria según el libro, y cada receta sus funciones, energética, clima y las hierbas que usa. Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_five_elements_cookbook.json`](grafos/five-elements-cookbook/grafo_five_elements_cookbook.json).

La fuente fue un texto plano sin páginas, así que el grafo no tiene páginas. El libro no numera sus secciones: la división de la Parte I en 12 capítulos y la numeración son propias del grafo. Las hierbas, en orden alfabético en el libro, se agruparon en 6 capítulos según la función que les asigna la tabla de hierbas del propio libro. Las hierbas de cada receta se detectaron buscando sus nombres en el texto y pueden incluir alguna que solo se menciona como sustituto. Los resúmenes están en español y redactados con palabras propias; las conexiones son una interpretación pedagógica.

## Grafo de Understanding Nutrition

[`grafos/understanding-nutrition/grafo_understanding_nutrition.html`](grafos/understanding-nutrition/grafo_understanding_nutrition.html) es el mapa interactivo de *Understanding Nutrition*, 12.ª ed. (Whitney y Rolfes, Cengage, 2011), en español: 20 capítulos con sus Highlights, 175 secciones, 151 conceptos clave, 11 apéndices y 463 prerrequisitos, en 6 bloques (fundamentos y planificación; digestión y macronutrientes; metabolismo, energía, peso y actividad; vitaminas, agua y minerales; ciclo vital; salud, inocuidad y ambiente). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_understanding_nutrition.json`](grafos/understanding-nutrition/grafo_understanding_nutrition.json).

El libro es de 2011. 57 conceptos llevan un recuadro «Atención» con la guía o el dato que hoy lo reemplaza (Dietary Guidelines 2025–2030, DRI de energía 2023, de sodio y potasio 2019 y de calcio y vitamina D 2011, etiqueta de la FDA de 2016, guía de colesterol AHA/ACC 2018, hipertensión AHA/ACC 2025, DSM-5, AAP 2023 sobre obesidad pediátrica, entre otras). El grafo describe el libro; la actualización va solo en esas alertas. [`alertas.json`](grafos/understanding-nutrition/alertas.json) registra, por concepto, qué dice el libro y qué dice la referencia vigente, y [`log_busqueda.md`](grafos/understanding-nutrition/log_busqueda.md) documenta la verificación de cada referencia (fecha, consulta y fuente).

La fuente fue un texto extraído de un PDF a varias columnas: las cifras de tablas y figuras desarmadas se omitieron en lugar de reconstruirse. La numeración de secciones es propia del grafo; las páginas son las impresas. Las conexiones son una interpretación pedagógica.

## Grafo de La crianza rebelde

[`grafos/crianza-rebelde/grafo_crianza_rebelde.html`](grafos/crianza-rebelde/grafo_crianza_rebelde.html) es el mapa interactivo de *La consciencia y la empatía. La crianza rebelde: educar desde el respeto* (Ana Acosta Rodríguez, 2019): 16 capítulos (prólogo incluido), 74 secciones, 65 ideas clave y 147 prerrequisitos, en 5 bloques (punto de partida y necesidades; desarrollo emocional y cerebral; el modelo C.E.R.; técnicas y autorregulación; pareja y sanación). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_crianza_rebelde.json`](grafos/crianza-rebelde/grafo_crianza_rebelde.json).

Las ideas que se apoyan en una afirmación científica se contrastaron con evidencia en psicología del desarrollo y neurociencia. 15 llevan un recuadro «Atención» porque la afirmación está superada o simplificada (por ejemplo, el cerebro triuno de MacLean, la lateralización «izquierdo lógico / derecho emocional», la equiparación del tiempo fuera con castigo dañino o los cambios cerebrales permanentes por mindfulness). [`alertas.json`](grafos/crianza-rebelde/alertas.json) contiene las 49 valoraciones, incluidas las respaldadas (por ejemplo, el daño del castigo físico: Gershoff y Grogan-Kaylor 2016; AAP 2018), y [`log_busqueda.md`](grafos/crianza-rebelde/log_busqueda.md) documenta la verificación de las referencias citadas en las alertas. Las alertas valoran afirmaciones empíricas, no las opciones de crianza del libro.

El EPUB no tiene páginas y el libro no numera sus secciones: la numeración es propia del grafo. Es un mapa de estudio, no el grafo de afirmaciones trazables que propone [`grafo-crianza/SPEC.md`](grafo-crianza/SPEC.md); sus alertas pueden servir de insumo para la fase de evidencia de esa especificación.

## Aplicación Python de Graphify

[`apps/graphify-py/`](apps/graphify-py/) instala la distribución oficial `graphifyy==0.9.91` con soporte para PDF y Office, y expone el comando `bookskills-graphify`. Incluye instrucciones para generar un grafo de código local y consultarlo. El código del proyecto original permanece en su distribución oficial bajo licencia Apache 2.0.

## Instalación

Las skills viven en `.claude/skills/` y Claude Code las carga automáticamente al abrir este repo. Cada carpeta es una skill independiente (`SKILL.md` + `references/`). Para instalarla en claude.ai, comprime la carpeta como `.skill` (zip) y súbela en *Settings → Capabilities → Skills*, o cópiala a `~/.claude/skills/` para Claude Code.

> ⚠️ El contenido se redactó a partir de fuentes estándar (Deadman, localización OMS 2008) sin cotejo página a página. Verifica ubicaciones y profundidades de puntos de riesgo antes del uso clínico.
