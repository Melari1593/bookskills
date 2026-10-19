# bookskills

Skills de Claude basadas en libros y obras de referencia.

| Skill | Descripción |
|---|---|
| [`acupuntura-puntos`](.claude/skills/acupuntura-puntos/SKILL.md) | Los 361 puntos clásicos de acupuntura (MTC) por meridiano, con índice por síntoma y categorías (Shu, Yuan, Luo, Xi, Mu, Hui…). |
| [`harrys-cosmeticology`](.claude/skills/harrys-cosmeticology/SKILL.md) | *Harry's Cosmeticology* 9.ª ed. (Vol. 1, Vol. 2 y Sostenibilidad): 59 fichas de capítulo sobre formulación, ingredientes, sustratos, regulación y antienvejecimiento, con glosario, patrones, cheatsheet y consulta del grafo de conocimiento. |
| [`hemodinamia-grafo`](.claude/skills/hemodinamia-grafo/SKILL.md) | Mapa de estudio del *Manual de hemodinamia y aplicaciones clínicas en cardiología*: 16 capítulos, 149 secciones, 63 conceptos y rutas de prerrequisitos. |
| [`guyton-fisiologia-grafo`](.claude/skills/guyton-fisiologia-grafo/SKILL.md) | Mapa de estudio del *Tratado de fisiología médica* de Guyton y Hall, 14.ª ed.: 85 capítulos, 714 secciones, 391 conceptos clave y rutas de prerrequisitos, correlacionado con los 44 capítulos de *Berne & Levy Physiology*, 8.ª ed. |

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

## Aplicación Python de Graphify

[`apps/graphify-py/`](apps/graphify-py/) instala la distribución oficial `graphifyy==0.9.91` con soporte para PDF y Office, y expone el comando `bookskills-graphify`. Incluye instrucciones para generar un grafo de código local y consultarlo. El código del proyecto original permanece en su distribución oficial bajo licencia Apache 2.0.

## Instalación

Las skills viven en `.claude/skills/` y Claude Code las carga automáticamente al abrir este repo. Cada carpeta es una skill independiente (`SKILL.md` + `references/`). Para instalarla en claude.ai, comprime la carpeta como `.skill` (zip) y súbela en *Settings → Capabilities → Skills*, o cópiala a `~/.claude/skills/` para Claude Code.

> ⚠️ El contenido se redactó a partir de fuentes estándar (Deadman, localización OMS 2008) sin cotejo página a página. Verifica ubicaciones y profundidades de puntos de riesgo antes del uso clínico.
