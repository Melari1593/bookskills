# bookskills

Skills de Claude basadas en libros y obras de referencia.

| Skill | Descripción |
|---|---|
| [`ideas-a-animacion`](.claude/skills/ideas-a-animacion/SKILL.md) | Convierte ideas de grafos de libros y archivos PDF, TXT o EPUB en guiones, storyboards y prompts de video con fuentes trazables y estilo de animación seleccionado por el usuario. |
| [`acupuntura-puntos`](.claude/skills/acupuntura-puntos/SKILL.md) | Los 361 puntos clásicos de acupuntura (MTC) por meridiano, con índice por síntoma, categorías (Shu, Yuan, Luo, Xi, Mu, Hui…) y guía de diagnóstico por patrón (lengua, pulso, ocho reglas) con evidencia de fiabilidad. |
| [`harrys-cosmeticology`](.claude/skills/harrys-cosmeticology/SKILL.md) | *Harry's Cosmeticology* 9.ª ed. (Vol. 1, Vol. 2 y Sostenibilidad): 59 fichas de capítulo sobre formulación, ingredientes, sustratos, regulación y antienvejecimiento, con glosario, patrones, cheatsheet y consulta del grafo de conocimiento. |
| [`hemodinamia-grafo`](.claude/skills/hemodinamia-grafo/SKILL.md) | Mapa de estudio del *Manual de hemodinamia y aplicaciones clínicas en cardiología*: 16 capítulos, 149 secciones, 63 conceptos y rutas de prerrequisitos. |
| [`empresa-agentica-grafo`](.claude/skills/empresa-agentica-grafo/SKILL.md) | *La empresa agéntica* (Hodjat y Blondeau, 2026) en dos modos: explorar el grafo (introducción y 9 capítulos, 68 secciones, 63 conceptos, rutas de prerrequisitos) y asesorar un proyecto multiagente con los marcos del libro (encaje, preparación, autonomía, riesgos, ROI, lock-in). |
| [`guyton-fisiologia-grafo`](.claude/skills/guyton-fisiologia-grafo/SKILL.md) | Mapa de estudio del *Tratado de fisiología médica* de Guyton y Hall, 14.ª ed.: 85 capítulos, 714 secciones, 391 conceptos clave y rutas de prerrequisitos, correlacionado con los 44 capítulos de *Berne & Levy Physiology*, 8.ª ed. |
| [`nutricion-pediatrica-grafo`](.claude/skills/nutricion-pediatrica-grafo/SKILL.md) | Mapa de estudio del *Manual of Pediatric Nutrition*, 3.ª ed. (Hendricks, Duggan y Walker), en español: 36 capítulos, 254 secciones, 174 conceptos clave, 5 apéndices, rutas de prerrequisitos y alertas de guías vigentes (octubre de 2026). |
| [`nutraceuticos`](.claude/skills/nutraceuticos/SKILL.md) | Nutracéuticos para consulta clínica: 25 recetas de gastronomía molecular dosificadas en gramos (curcumina, omega-3, probióticos, moringa, camu camu, aguaje, guayaba, zapote, mango, guanábana, cacao, espirulina, açaí, brócoli, cordyceps, melena de león, especias, semillas de calabaza, preparaciones prenatales, bisglicinato ferroso en shot, brownie y arepa de maíz integral dosificados, arepa con ácido fólico, y liofilizados) con evidencia de PubMed por nivel de confianza, seguridad y log de búsqueda; incluye los grafos de *Flavonoids as Nutraceuticals* (2024), *Nutraceuticals for Prenatal, Maternal and Offspring's Nutritional Health* y *Applications of Functional Foods and Nutraceuticals for Chronic Diseases*, Vol. I (2023). |
| [`origami-biotech`](.claude/skills/origami-biotech/SKILL.md) | Origami en dos módulos: diseño (boxpleating, circle/river packing, método del árbol, kirigami, teselaciones y origami rígido con espesor) y biotecnología (origami de ADN y de ARN, dispositivos plegables). Literatura de PubMed con DOI y nivel de confianza, lecciones de la playlist *Origami Design Class* marcadas como verificadas o pendientes, y registro de búsquedas. |

## Atlas de Meridianos

`atlas/atlas-meridianos.html` es un mapa interactivo de los puntos de `acupuntura-puntos`: vistas anterior, posterior y de cabeza lateral, fichas completas y recetas por síntoma. Se abre directamente en el navegador.

Se genera a partir de las fichas de la skill, así que después de corregir una ficha hay que regenerarlo:

```bash
python3 atlas/build.py
```

`atlas/template.html` contiene la página (estilos y lógica) y `atlas/build.py` extrae los datos de `references/` y asigna a cada punto una posición esquemática en la figura.

## Grafos de acupresión y ojos (Dalet y Rosenfarb)

[`grafos/dalet-acupressure-self-care/grafo_dalet_acupressure.html`](grafos/dalet-acupressure-self-care/grafo_dalet_acupressure.html) es el mapa de *Acupressure Self-Care Handbook* (Roger Dalet, 2023): introducción y 12 partes, 77 afecciones y 86 puntos recurrentes. El libro no nombra los puntos; los códigos son una interpretación y están verificados con las fichas de [`acupuntura-puntos`](.claude/skills/acupuntura-puntos/SKILL.md). Cada afección indica cuántos de sus puntos coinciden con el índice de síntomas de la skill (127 de 207 usos, 61 %). Detalle en [`comparacion.md`](grafos/dalet-acupressure-self-care/comparacion.md).

[`grafos/rosenfarb-healing-your-eyes/grafo_rosenfarb_healing_eyes.html`](grafos/rosenfarb-healing-your-eyes/grafo_rosenfarb_healing_eyes.html) es el mapa de *Healing Your Eyes with Chinese Medicine* (Andy Rosenfarb, 2007): 8 capítulos, 81 secciones, 56 conceptos y 3 apéndices, con alertas marcadas con ⚠ y evidencia de PubMed en [`evidencia.md`](grafos/rosenfarb-healing-your-eyes/evidencia.md). La numeración de secciones es propia del grafo; el EPUB no tiene páginas impresas.

## Grafo de Medicina tradicional china para mujeres (Patzek y Hertzer)

[`grafos/patzek-mtc-para-mujeres/grafo_patzek_mtc_mujeres.html`](grafos/patzek-mtc-para-mujeres/grafo_patzek_mtc_mujeres.html) es el mapa de *Medicina tradicional china para mujeres* (Sabine Patzek y Karin Hertzer, Arkano Books, 2003): 4 partes, 56 apartados y 62 conceptos (síndromes, hierbas, puntos y evidencia). Los puntos de cada afección, escritos en notación española (E, BP, VC…), se pasaron a códigos OMS y se cruzaron con [`acupuntura-puntos`](.claude/skills/acupuntura-puntos/SKILL.md). Las alertas de seguridad (acónito en el embarazo, Melia toosendan, mu tong, urgencias obstétricas) y la evidencia de PubMed están en [`comparacion_y_evidencia.md`](grafos/patzek-mtc-para-mujeres/comparacion_y_evidencia.md). La numeración de apartados es propia del grafo; las páginas son las del índice.

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

## Grafo de La empresa agéntica

[`grafos/la-empresa-agentica/grafo_la_empresa_agentica.html`](grafos/la-empresa-agentica/grafo_la_empresa_agentica.html) es el mapa interactivo de *La empresa agéntica* (Babak Hodjat y Antoine Blondeau, O'Reilly, edición en español, 2026): introducción y 9 capítulos, 68 secciones, 63 conceptos clave, 12 figuras y 184 prerrequisitos, en 5 bloques (introducción; Parte I · por qué importa; Parte II · tecnología de agentes; Parte III · confianza; Parte IV · el futuro). Cada concepto (AAOSA, sly_data, RACI de segunda capa, pasarela neutral de modelos, MCP y A2A…) lleva su esquema en una línea. Los datos están en [`grafo_la_empresa_agentica.json`](grafos/la-empresa-agentica/grafo_la_empresa_agentica.json). La skill [`empresa-agentica-grafo`](.claude/skills/empresa-agentica-grafo/SKILL.md) usa este grafo para trazar rutas desde la terminal y para asesorar proyectos multiagente.

Las páginas son las impresas del índice del libro. Los resúmenes están redactados con palabras propias. El capítulo 7 no numera sus secciones ni sus viñetas: esa numeración es propia del grafo. Quedaron fuera el prólogo, el prefacio, los agradecimientos y el índice analítico. Las conexiones son una interpretación pedagógica.

## Grafo de Strategic Analytics (HBR Insights You Need)

[`grafos/hbr-strategic-analytics/grafo_hbr_strategic_analytics.html`](grafos/hbr-strategic-analytics/grafo_hbr_strategic_analytics.html) es el mapa interactivo de *Strategic Analytics: The Insights You Need from Harvard Business Review* (Harvard Business Review Press, 2020): la introducción de Thomas H. Davenport y 13 artículos, 65 secciones, 48 ideas clave, 7 figuras o tablas y 131 prerrequisitos, en 4 bloques (introducción; fundamentos de la analítica; organización guiada por la analítica; aplicar la analítica). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_hbr_strategic_analytics.json`](grafos/hbr-strategic-analytics/grafo_hbr_strategic_analytics.json).

Los títulos de artículos y secciones van en inglés, como en el libro; los resúmenes están en español y redactados con palabras propias. El EPUB no tiene páginas. Varios artículos no tienen subtítulos: sus secciones y toda la numeración son propias del grafo. Los artículos son independientes entre sí: las conexiones son una interpretación pedagógica de cómo se complementan los temas.

## Grafo de Unprepared to Entrepreneur

[`grafos/unprepared-to-entrepreneur/grafo_unprepared_to_entrepreneur.html`](grafos/unprepared-to-entrepreneur/grafo_unprepared_to_entrepreneur.html) es el mapa interactivo de *Unprepared to Entrepreneur: A Method to the Madness of Starting Your Own Business* (Sonya Barlow, Kogan Page, 2021): 11 capítulos, 90 secciones (casos de estudio incluidos), 64 herramientas, 13 figuras o tablas y 136 prerrequisitos, en 6 bloques (punto de partida; idea, cliente y modelo; visibilidad y comunidad; equipo y liderazgo; salud y dinero; ventas y reflexiones finales). Cada herramienta (Lean Canvas, regla 3-2-1, tipos de impostor, regla 50:30:20…) lleva su esquema en una línea. Los datos están en [`grafo_unprepared_to_entrepreneur.json`](grafos/unprepared-to-entrepreneur/grafo_unprepared_to_entrepreneur.json).

Los títulos y los resúmenes están en español y redactados con palabras propias. El EPUB no tiene páginas y el libro no numera sus secciones: la numeración es propia del grafo. Quedaron fuera las secciones «Afterthoughts», los cuadernos de trabajo, las referencias y el índice. Las conexiones son una interpretación pedagógica.

## Grafo de The Five Elements Cookbook

[`grafos/five-elements-cookbook/grafo_five_elements_cookbook.html`](grafos/five-elements-cookbook/grafo_five_elements_cookbook.html) es el mapa interactivo de *The Five Elements Cookbook: A Guide to Traditional Chinese Medicine with Recipes for Everyday Healing* (Zoey Xinyi Gong): 25 capítulos, 165 secciones, 26 conceptos clave, 2 tablas y 703 prerrequisitos, en 5 bloques (fundamentos de la MTC; propiedades de los alimentos; estaciones y constituciones; las 50 hierbas; las 55 recetas). Cada hierba lleva su naturaleza, sabor, meridianos y dosis máxima diaria según el libro, y cada receta sus funciones, energética, clima y las hierbas que usa. Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_five_elements_cookbook.json`](grafos/five-elements-cookbook/grafo_five_elements_cookbook.json).

Desde el 2026-11-21, 27 secciones (21 hierbas y 6 recetas) llevan una alerta de evidencia que se ve en el recuadro «Atención» del visor. Hay 7 dosis del libro que chocan con la evidencia: kombu (15 g/día eleva la TSH), semilla de albaricoque (cianuro; límite de la EFSA), regaliz (hasta 30 g/día), canela cassia (cumarina), nuez moscada, nuez de ginkgo (convulsiones) y azafrán. La skill [`five-elements-cookbook-grafo`](.claude/skills/five-elements-cookbook-grafo/SKILL.md) consulta el grafo con `scripts/ruta.py`, y su [`verificacion.md`](.claude/skills/five-elements-cookbook-grafo/references/verificacion.md) trae las fuentes con DOI, la confianza, los huecos y el log de búsqueda.

La fuente fue un texto plano sin páginas, así que el grafo no tiene páginas. El libro no numera sus secciones: la división de la Parte I en 12 capítulos y la numeración son propias del grafo. Las hierbas, en orden alfabético en el libro, se agruparon en 6 capítulos según la función que les asigna la tabla de hierbas del propio libro. Las hierbas de cada receta se detectaron buscando sus nombres en el texto y pueden incluir alguna que solo se menciona como sustituto. Los resúmenes están en español y redactados con palabras propias; las conexiones son una interpretación pedagógica.

## Grafo de Understanding Nutrition

[`grafos/understanding-nutrition/grafo_understanding_nutrition.html`](grafos/understanding-nutrition/grafo_understanding_nutrition.html) es el mapa interactivo de *Understanding Nutrition*, 12.ª ed. (Whitney y Rolfes, Cengage, 2011), en español: 20 capítulos con sus Highlights, 175 secciones, 151 conceptos clave, 11 apéndices y 463 prerrequisitos, en 6 bloques (fundamentos y planificación; digestión y macronutrientes; metabolismo, energía, peso y actividad; vitaminas, agua y minerales; ciclo vital; salud, inocuidad y ambiente). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_understanding_nutrition.json`](grafos/understanding-nutrition/grafo_understanding_nutrition.json).

El libro es de 2011. 57 conceptos llevan un recuadro «Atención» con la guía o el dato que hoy lo reemplaza (Dietary Guidelines 2025–2030, DRI de energía 2023, de sodio y potasio 2019 y de calcio y vitamina D 2011, etiqueta de la FDA de 2016, guía de colesterol AHA/ACC 2018, hipertensión AHA/ACC 2025, DSM-5, AAP 2023 sobre obesidad pediátrica, entre otras). El grafo describe el libro; la actualización va solo en esas alertas. [`alertas.json`](grafos/understanding-nutrition/alertas.json) registra, por concepto, qué dice el libro y qué dice la referencia vigente, y [`log_busqueda.md`](grafos/understanding-nutrition/log_busqueda.md) documenta la verificación de cada referencia (fecha, consulta y fuente).

La fuente fue un texto extraído de un PDF a varias columnas: las cifras de tablas y figuras desarmadas se omitieron en lugar de reconstruirse. La numeración de secciones es propia del grafo; las páginas son las impresas. Las conexiones son una interpretación pedagógica.

## Grafo de La crianza rebelde

[`grafos/crianza-rebelde/grafo_crianza_rebelde.html`](grafos/crianza-rebelde/grafo_crianza_rebelde.html) es el mapa interactivo de *La consciencia y la empatía. La crianza rebelde: educar desde el respeto* (Ana Acosta Rodríguez, 2019): 16 capítulos (prólogo incluido), 74 secciones, 65 ideas clave y 147 prerrequisitos, en 5 bloques (punto de partida y necesidades; desarrollo emocional y cerebral; el modelo C.E.R.; técnicas y autorregulación; pareja y sanación). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_crianza_rebelde.json`](grafos/crianza-rebelde/grafo_crianza_rebelde.json).

Las ideas que se apoyan en una afirmación científica se contrastaron con evidencia en psicología del desarrollo y neurociencia. 15 llevan un recuadro «Atención» porque la afirmación está superada o simplificada (por ejemplo, el cerebro triuno de MacLean, la lateralización «izquierdo lógico / derecho emocional», la equiparación del tiempo fuera con castigo dañino o los cambios cerebrales permanentes por mindfulness). [`alertas.json`](grafos/crianza-rebelde/alertas.json) contiene las 49 valoraciones, incluidas las respaldadas (por ejemplo, el daño del castigo físico: Gershoff y Grogan-Kaylor 2016; AAP 2018), y [`log_busqueda.md`](grafos/crianza-rebelde/log_busqueda.md) documenta la verificación de las referencias citadas en las alertas. Las alertas valoran afirmaciones empíricas, no las opciones de crianza del libro.

El EPUB no tiene páginas y el libro no numera sus secciones: la numeración es propia del grafo. Es un mapa de estudio, no el grafo de afirmaciones trazables que propone [`grafo-crianza/SPEC.md`](grafo-crianza/SPEC.md); sus alertas pueden servir de insumo para la fase de evidencia de esa especificación.

## Grafo de Super Powders

[`grafos/super-powders/grafo_super_powders.html`](grafos/super-powders/grafo_super_powders.html) es el mapa interactivo de *Super Powders: Adaptogenic Herbs and Mushrooms for Energy, Beauty, Mood, and Well-Being* (Katrine van Wyk, 2018): 15 capítulos, 104 secciones, 48 nodos de polvo o concepto (25 adaptógenos y hongos, 10 superpolvos y 13 conceptos de la Parte I), 47 recetas y 259 prerrequisitos, en 6 bloques (fundamentos; hongos medicinales; raíces, hierbas y hojas; bayas, polen y perla; otros superpolvos; recetas). Cada receta está enlazada con los polvos que usa, así que trazar los prerrequisitos de una receta muestra qué fichas leer antes. Los datos están en [`grafo_super_powders.json`](grafos/super-powders/grafo_super_powders.json).

33 nodos llevan una alerta de evidencia, contrastada en PubMed y en agencias (EMA, EFSA, BfR, LactMed, LiverTox, NIH ODS). Entre los riesgos que el libro omite están la hepatotoxicidad del He Shou Wu, la levodopa de la mucuna, el daño hepático y la tirotoxicosis asociados a la ashwagandha, la cumarina de la canela cassia y el daño hepático por suplementos de cúrcuma con mayor absorción; entre las afirmaciones sin respaldo, la «fatiga suprarrenal» y la B12 de la ashitaba. [`alertas.json`](grafos/super-powders/alertas.json) reúne los textos de las alertas, [`verif_A.md`](grafos/super-powders/verif_A.md) y [`verif_B.md`](grafos/super-powders/verif_B.md) traen el veredicto, las fuentes con DOI y la confianza de cada una, y [`log_busqueda.md`](grafos/super-powders/log_busqueda.md) documenta las búsquedas.

El EPUB no tiene páginas ni numera las secciones: la numeración es propia del grafo y solo las recetas llevan la página impresa, tomada de las referencias cruzadas del libro. Los polvos se agruparon por tipo; el libro los presenta en orden alfabético. Las alertas resumen evidencia publicada y no sustituyen la valoración clínica.

La skill [`.claude/skills/super-powders-grafo/`](.claude/skills/super-powders-grafo/SKILL.md) consulta este grafo: `scripts/ruta.py` busca un polvo, una receta o una sección, traza las fichas previas e imprime las alertas de evidencia. El 2026-11-17 se comprobó que los 98 DOI de `verif_A.md` y `verif_B.md` existen en PubMed, y se añadió a la alerta de goji la alergia por LTP.


## Grafo de Herbal Recipes for Vibrant Health

[`grafos/gladstar-herbal-recipes/grafo_gladstar.html`](grafos/gladstar-herbal-recipes/grafo_gladstar.html) es el mapa interactivo de *Rosemary Gladstar's Herbal Recipes for Vibrant Health: 175 Teas, Tonics, Oils, Salves, Tinctures, and Other Natural Remedies for the Entire Family* (Rosemary Gladstar, Storey, 2008; ed. 2015): 9 capítulos y 2 apéndices, 102 secciones, 152 recetas, 98 fichas de plantas de la botica A–Z y 4 conceptos, en 5 bloques (fundamentos y vida sana; nervios y remedios caseros; belleza natural; niños, mujeres, hombres y mayores; botica y técnicas). Cada receta está enlazada con las plantas que usa y con la técnica del apéndice II que requiere (té, jarabe, aceite, ungüento, tintura…). Los datos están en [`grafo_gladstar.json`](grafos/gladstar-herbal-recipes/grafo_gladstar.json).

99 nodos llevan una alerta de evidencia. Se verificaron 125 afirmaciones en PubMed y en agencias (LiverTox, EMA, FDA, NCCIH, Cochrane, AAP, LactMed): ninguna quedó plenamente respaldada; 58 tienen riesgo documentado, 26 están contradichas, 18 carecen de evidencia suficiente y 23 tienen respaldo parcial. Entre los riesgos que el libro minimiza están la consuelda, el tusílago, el chaparral, el kava y el fo-ti por vía oral (daño hepático), el safrol del sasafrás, el regaliz diario, los enemas de nébeda, las tinturas con alcohol y los aceites esenciales en bebés, el cohosh azul y negro en el embarazo, y las interacciones del hipérico, el ginkgo y el espino. Las afirmaciones están en [`afirmaciones_A.md`](grafos/gladstar-herbal-recipes/afirmaciones_A.md) … [`afirmaciones_F.md`](grafos/gladstar-herbal-recipes/afirmaciones_F.md); los veredictos con fuentes y confianza, en [`verif_A.md`](grafos/gladstar-herbal-recipes/verif_A.md) … [`verif_F.md`](grafos/gladstar-herbal-recipes/verif_F.md); los textos finales, en [`alertas.json`](grafos/gladstar-herbal-recipes/alertas.json); la revisión de 23 citas (15 confirmadas, 7 corregidas, 1 sustituida), en [`auditoria_citas.md`](grafos/gladstar-herbal-recipes/auditoria_citas.md), y las búsquedas, en [`log_busqueda.md`](grafos/gladstar-herbal-recipes/log_busqueda.md).


## Grafo de Lo que Einstein le contó a su cocinero 2

[`grafos/einstein-cocinero-2/grafo_einstein_cocinero_2.html`](grafos/einstein-cocinero-2/grafo_einstein_cocinero_2.html) es el mapa de *Lo que Einstein le contó a su cocinero 2* (Robert L. Wolke): 141 preguntas en 10 capítulos y 26 conceptos de química y física culinaria, cada uno con su mecanismo, el error común que corrige y su uso en la cocina. Los enlaces explican por qué un concepto se apoya en otro, y 24 alertas señalan qué explicaciones del libro (2005) quedaron superadas o matizadas. El pipeline reproducible, las pruebas de contenido, la revisión independiente y la verificación están en [`grafos/einstein-cocinero-2/`](grafos/einstein-cocinero-2/README.md).


## Grafo de Apharsemon, mirra y olíbano

[`grafos/mirra-olibano-apharsemon/grafo_mirra_olibano.html`](grafos/mirra-olibano-apharsemon/grafo_mirra_olibano.html) es el mapa del capítulo "Apharsemon, Myrrh and Olibanum: Ancient Medical Plants" (Ben-Yehoshua y Hanuš, 2014) de *Medicinal and Aromatic Plants of the Middle-East*: 9 partes, 39 secciones y 31 nodos sobre el bálsamo de Judea, la mirra y el incienso. Lleva 11 alertas de evidencia de 14 afirmaciones verificadas: ninguna afirmación médica queda respaldada sin matices; el Mirazid y el gugulípido quedan contradichos, la Boswellia en Crohn superada y el capítulo omite el riesgo del humo de incienso y las precauciones de la mirra en embarazo y niños. Detalle en [`grafos/mirra-olibano-apharsemon/`](grafos/mirra-olibano-apharsemon/README.md).


## Grafos de capítulos de Nuts and Seeds in Health and Disease Prevention

[`grafos/nuts-seeds/`](grafos/nuts-seeds/README.md) reúne cuatro capítulos de *Nuts and Seeds in Health and Disease Prevention* (Elsevier, 2011 y 2020) como grafos interactivos con alertas de evidencia: ácidos grasos (39 alertas en total), minerales y tóxicos, semilla de orégano y semilla de tamarindo. Entre los hallazgos: riesgos omitidos de la semilla de ginkgo, el cáñamo, el bario de la nuez de Brasil y el uso del tamarindo como "alternativa al antiveneno"; valores de referencia ya retirados para plomo y arsénico; y errores del capítulo de tamarindo.

## Aflatoxinas

[`grafos/aflatoxinas/`](grafos/aflatoxinas/README.md) tiene un grafo de evidencia y un informe completo sobre las aflatoxinas, construidos desde PubMed y fuentes oficiales. El grafo tiene 9 partes, 37 secciones, 32 ítems y 11 alertas. Cubre toxicología, la sinergia con la hepatitis B, embarazo y lactancia, límites de la UE, el Codex, la FDA y Colombia, la situación en Colombia, la mitigación y la detección por volátiles de *Aspergillus*. 5 de las 11 afirmaciones están contradichas, entre ellas que cocinar las elimina y que la ausencia de olor a moho indica un alimento seguro.

## Grafo de Origami Design Secrets (Lang)

[`grafos/origami-design-secrets/grafo_origami_design_secrets.html`](grafos/origami-design-secrets/grafo_origami_design_secrets.html) es el mapa interactivo de *Origami Design Secrets: Mathematical Methods for an Ancient Art* (Robert J. Lang, A K Peters/CRC Press, 2011): 14 capítulos, 85 secciones, 70 conceptos clave, 2 anexos (Referencias y Glosario) y 193 prerrequisitos, en 6 bloques (fundamentos; bases y puntos; injertos y texturas; teselas y circle packing; moléculas, árbol y algoritmos; box pleating y bases híbridas). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_origami_design_secrets.json`](grafos/origami-design-secrets/grafo_origami_design_secrets.json). La skill [`origami-biotech`](.claude/skills/origami-biotech/SKILL.md) incluye una copia del grafo y `scripts/ruta.py`, que lista la ruta de lectura de una sección, un capítulo o un concepto desde la terminal.

Los títulos de secciones van en español y los términos técnicos conservan su forma en inglés. Los resúmenes están en español y redactados con palabras propias. Las páginas son las impresas; las del glosario vienen del propio libro. Solo 5 conceptos del capítulo 14 llevan fórmula con número de ecuación verificado; las ecuaciones de los otros capítulos no se pudieron extraer del PDF. Los prerrequisitos son una interpretación pedagógica de cómo abre cada sección, no una lista del autor. Quedan fuera las instrucciones de plegado de los modelos.

## Grafo de Flavonoids as Nutraceuticals

[`grafos/flavonoids-as-nutraceuticals/grafo_flavonoids_as_nutraceuticals.html`](grafos/flavonoids-as-nutraceuticals/grafo_flavonoids_as_nutraceuticals.html) es el mapa interactivo de *Flavonoids as Nutraceuticals* (Kesharwani, Saini, Keservani y Sharma, eds., Apple Academic Press, 2024): 13 capítulos, 184 secciones, 43 conceptos clave y 84 prerrequisitos, en 6 bloques (química y biosíntesis; plantas y agricultura; nutracéuticos y salud humana; inflamación e inmunidad; antivirales y COVID-19; tintes naturales). Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_flavonoids_as_nutraceuticals.json`](grafos/flavonoids-as-nutraceuticals/grafo_flavonoids_as_nutraceuticals.json). La skill [`nutraceuticos`](.claude/skills/nutraceuticos/SKILL.md) incluye una copia del grafo y `scripts/ruta.py`.

Títulos y resúmenes en español, con palabras propias. Las páginas son las impresas. Los prerrequisitos son una interpretación pedagógica: el libro es una obra colectiva y sus capítulos casi no se citan entre sí. La mayor parte de la evidencia del libro es in vitro, animal o in silico. Quedan fuera las tablas de compuestos, las figuras y las referencias.

## Grafo de Nutraceuticals for Prenatal, Maternal and Offspring's Nutritional Health

[`grafos/nutraceuticos-prenatal-materno/grafo_nutraceuticos_prenatal_materno.html`](grafos/nutraceuticos-prenatal-materno/grafo_nutraceuticos_prenatal_materno.html) es el mapa interactivo de *Nutraceuticals for Prenatal, Maternal and Offspring's Nutritional Health* (Bhatt, Miraghajani, Pathak y otros, eds., CRC Press): 19 capítulos, 195 secciones, 56 conceptos clave y 71 prerrequisitos, en 5 bloques (bases y periconcepción; complicaciones maternas; anemia, infección y hormonas; salud mental y posparto; resultados fetales y de la descendencia). La numeración `capítulo.orden` es del grafo. Los datos están en [`grafo_nutraceuticos_prenatal_materno.json`](grafos/nutraceuticos-prenatal-materno/grafo_nutraceuticos_prenatal_materno.json). La skill [`nutraceuticos`](.claude/skills/nutraceuticos/SKILL.md) incluye una copia y `scripts/ruta.py --grafo prenatal`.

## Grafo de Functional Foods and Nutraceuticals for Chronic Diseases

[`grafos/functional-foods-chronic-diseases/grafo_functional_foods_chronic_diseases.html`](grafos/functional-foods-chronic-diseases/grafo_functional_foods_chronic_diseases.html) es el mapa interactivo de *Applications of Functional Foods and Nutraceuticals for Chronic Diseases*, Vol. I (Mohan, Abdollahi y Pathak, eds., CRC Press, 2023): 15 capítulos, 189 secciones, 50 conceptos clave y 67 prerrequisitos, en 6 bloques (carga e integración de las ECNT; bases de seguridad, eficacia y regulación; metabolismo, endocrino y cardiovascular; vegetales y aceites; órganos y sistemas; neurodegeneración). El libro no numera las secciones: la numeración `capítulo.orden` es del grafo. Los datos están en [`grafo_functional_foods_chronic_diseases.json`](grafos/functional-foods-chronic-diseases/grafo_functional_foods_chronic_diseases.json). La skill [`nutraceuticos`](.claude/skills/nutraceuticos/SKILL.md) incluye una copia y `scripts/ruta.py --grafo cronicas`.

## Grafos de libros de agentes de IA

Cuatro mapas interactivos de libros sobre agentes de IA, en español. Cada uno tiene buscador, tres vistas y trazado de prerrequisitos. Los datos de cada grafo están en el `.json` de su carpeta.

| Grafo | Libro | Contenido |
|---|---|---|
| [`albada-desarrollo-agentes-ia`](grafos/albada-desarrollo-agentes-ia/grafo_albada_desarrollo_agentes_ia.html) | *Desarrollo de Aplicaciones con Agentes de IA* (Michael Albada) | 13 capítulos, 137 secciones, 56 conceptos, 1 recurso (repositorio del libro) y 194 prerrequisitos, en 5 bloques: fundamentos y diseño; construcción del agente; aprendizaje y escalado; evaluación y operación; seguridad y colaboración humana. |
| [`lanham-agentes-ia-en-accion`](grafos/lanham-agentes-ia-en-accion/grafo_lanham_agentes_ia_en_accion.html) | *Agentes de IA en Acción*, 2.ª ed. (Micheal Lanham) | 11 capítulos, 153 secciones, 53 patrones, 2 apéndices (entorno de Python; Node.js y npx para MCP) y 285 prerrequisitos, en 7 bloques: fundamentos; herramientas y MCP; sistemas multiagente; razonamiento y memoria; evaluación y producción; bucles y agente cognitivo; consejos prácticos. |
| [`graphrag-agentico`](grafos/graphrag-agentico/grafo_graphrag_agentico.html) | *GraphRAG agéntico* (Anthony Alcaraz y Sam Julien) | 8 capítulos y la Conclusión, 107 secciones, 41 conceptos y 185 prerrequisitos, en 7 bloques: fundamentos; representación del conocimiento; memoria de grafos; razonamiento y planificación; orquestación de herramientas; autoevolución y evaluación; optimización y producción. |
| [`ahmad-30-agentes`](grafos/ahmad-30-agentes/grafo_ahmad_30_agentes.html) | *30 Agentes que Todo Ingeniero de IA Debe Construir* (Imran Ahmad) | 17 capítulos, 68 secciones, 70 ítems (los 30 agentes y 40 conceptos) y 206 prerrequisitos, en 8 bloques: fundamentos y prompts; despliegue responsable y ética; arquitecturas cognitivas; orquestación y razonamiento; software, conversación y contenido; percepción y mundo físico; dominios especializados; epílogo. |

Los resúmenes están redactados con palabras propias. Las fuentes son EPUB sin páginas impresas, y ningún libro numera sus secciones: la numeración `capítulo.orden` es del grafo. En Ahmad, el libro no da una lista numerada de los 30 agentes; el recuento es del grafo. Los prerrequisitos son una interpretación pedagógica. Quedan fuera el código, los ejercicios, las tablas y el material preliminar. Los HTML cargan d3 desde cdnjs, así que necesitan conexión.

## Monografías de ingredientes

[`grafos/monografias-ingredientes/`](grafos/monografias-ingredientes/README.md) reúne 11 grafos construidos desde PubMed y fuentes oficiales, no desde un libro. Diez son monografías con la estructura de 9 partes del grafo de mirra y olíbano: guanábana, guayaba, corozo, aguacate, café, gulupa, açaí y asaí, murumuru, camu camu y aguaje. El undécimo, [`almendras-gestantes`](grafos/monografias-ingredientes/almendras-gestantes/), es un grafo de pregunta clínica sobre almendras en la gestación y la lactancia. En total hay 147 afirmaciones verificadas y 137 alertas. 53 afirmaciones no tienen evidencia en humanos, 18 están contradichas y 31 señalan un riesgo documentado u omitido. Los riesgos que se repiten son el Chagas oral por frutos de palma y la falta de datos de seguridad en el embarazo. El índice visual está en [`index.html`](grafos/monografias-ingredientes/index.html).

## Handbook of Medicinal Herbs (Duke)

[`grafos/duke-handbook-medicinal-herbs/duke-grafo.html`](grafos/duke-handbook-medicinal-herbs/duke-grafo.html) es el grafo del catálogo completo de *Handbook of Medicinal Herbs*, 2.ª ed. (James A. Duke et al., CRC Press, 2002): 1083 hierbas, 1140 actividades, 1534 indicaciones y 65 742 aristas con página, puntaje de eficacia (f, 1, 2, 3) y fuentes de Duke. El visor permite buscar por hierba o por indicación, filtrar por seguridad (X, +, ++, +++) y por eficacia, y ver dosis y contraindicaciones. Se verificaron en PubMed las 23 afirmaciones con eficacia 3: 8 están respaldadas con matices y 3 están contradichas (saw palmetto en la HBP; valeriana en el insomnio). También se revisaron las hierbas ++ y +++ con alertas que el libro omite (hipérico, kava, fo-ti, cúrcuma, canela cassia). Detalle en [`grafos/duke-handbook-medicinal-herbs/`](grafos/duke-handbook-medicinal-herbs/README.md).

## Grafo de El perfume (Vidal Valls)

[`grafos/el-perfume/grafo_el_perfume.html`](grafos/el-perfume/grafo_el_perfume.html) es el mapa interactivo de *El perfume. Los secretos de la elaboración del perfume* (Agustí Vidal Valls, Parramón Paidotribo, ed. epub 2022): 4 capítulos (olfato y química; materias primas y familias olfativas; creación de un perfume; anexo de seguridad), 39 secciones, 44 conceptos clave, 3 anexos y 91 prerrequisitos. Tiene buscador, tres vistas y trazado de prerrequisitos. Los datos están en [`grafo_el_perfume.json`](grafos/el-perfume/grafo_el_perfume.json).

Los resúmenes están redactados con palabras propias. El epub no tiene páginas impresas ni numera las secciones: la numeración sigue el orden del sumario. Las conexiones son una interpretación pedagógica. El anexo de seguridad describe IFRA y alérgenos según la normativa vigente al escribir el libro; hoy rige el Reglamento (UE) 2023/1545, que amplía la lista de alérgenos. Complementa la skill `crear-perfumes`.

## Skill de odorantes clave

[`skills/odorantes-clave/`](skills/odorantes-clave/SKILL.md) busca en PubMed los odorantes clave de uno o más alimentos (estudios con recombinación, SIDA/OAV, AEDA u olfactometría), clasifica cada hallazgo por nivel de evidencia, unifica sinónimos de compuestos y arma una tabla de odorantes compartidos con DOI. Después traduce el resultado a maridajes con el método de [`foodpairing/`](foodpairing/SKILL.md) (14 tipos de aroma, overtoning, reglas de equilibrio), separando evidencia de interpretación. Incluye como ejemplo verificado el caso café tostado + ajonjolí tostado (2-furfuriltiol, furaneol, 4-vinilguayacol, guayacoles y alquilpirazinas compartidos).

## Skill de gastronomía molecular

[`skills/gastronomia-molecular/`](skills/gastronomia-molecular/SKILL.md) reúne técnicas y química de la gastronomía molecular, construidas desde PubMed, JECFA, EFSA, FDA, USDA FSIS y normas de Colombia. Incluye una tabla maestra de 21 hidrocoloides con concentraciones, temperaturas, sensibilidades y estado regulatorio; 10 técnicas (esferificación, geles, espumas, emulsiones, sous vide con tablas de pasteurización, nitrógeno líquido, óxido nitroso, transglutaminasa y otras); y la química de Maillard, caramelización, proteínas, almidón, emulsiones, pH y altitud. Cada referencia trae fuentes, log de búsqueda y datos no confirmados.

## Skill de Healing Herbal Infusions

[`healing-herbal-infusions/`](healing-herbal-infusions/SKILL.md) convierte los capítulos 1 a 6 de *Healing Herbal Infusions* (Colleen Codekas, 2018) en una skill. Incluye la elección del medio de infusión (agua, alcohol, vinagre, miel, oximiel, glicerina, aceite), la regla de hierba fresca o seca, los métodos para aceite y la receta base de ungüento. También tiene un cheatsheet de 53 recetas con edad mínima, un glosario con nombres científicos y una tabla de seguridad clínica. Esa tabla agrega los riesgos que el libro omite: miel en menores de 1 año, interacciones del hipérico, consuelda en piel abierta, salicilatos y síndrome de Reye, y el tejo como conífera tóxica. Los capítulos 7 a 9 no están extraídos.

## Aplicación Python de Graphify

[`apps/graphify-py/`](apps/graphify-py/) instala la distribución oficial `graphifyy==0.9.91` con soporte para PDF y Office, y expone el comando `bookskills-graphify`. Incluye instrucciones para generar un grafo de código local y consultarlo. El código del proyecto original permanece en su distribución oficial bajo licencia Apache 2.0.

## Instalación

Las skills viven en `.claude/skills/` y Claude Code las carga automáticamente al abrir este repo. Cada carpeta es una skill independiente (`SKILL.md` + `references/`). Para instalarla en claude.ai, comprime la carpeta como `.skill` (zip) y súbela en *Settings → Capabilities → Skills*, o cópiala a `~/.claude/skills/` para Claude Code.

> ⚠️ El contenido se redactó a partir de fuentes estándar (Deadman, localización OMS 2008) sin cotejo página a página. Verifica ubicaciones y profundidades de puntos de riesgo antes del uso clínico.
