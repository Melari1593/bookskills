---
name: guyton-fisiologia-grafo
description: Explora el grafo de conocimiento del Tratado de fisiología médica de Guyton y Hall (14.ª ed., español). Úsala para localizar capítulos y secciones, encontrar conceptos como Frank-Starling, Nernst, multiplicador de contracorriente o renina-angiotensina, explicar cómo se conectan y trazar una ruta de estudio con prerrequisitos; también para entregar el HTML interactivo del grafo.
---

# Grafo de fisiología de Guyton y Hall

Usa `references/grafo.json` como mapa de estudio: 85 capítulos en 8 bloques, 714 secciones, 391 conceptos clave y unos 1400 enlaces de prerrequisito (entre capítulos, secciones y conceptos). Las páginas son las impresas de la 14.ª edición. El HTML autocontenido está en `assets/grafo_guyton.html`.

## Consultar

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py "término"`. También acepta un número de sección (`python scripts/ruta.py 27.4`) o el id de un concepto (`python scripts/ruta.py multiplicador_contracorriente`).
2. Antes de explicar una relación, lee en `references/grafo.json` los resúmenes de los nodos encontrados. Un arco `A → B` significa que B es antecedente de A. Los arcos son una interpretación pedagógica, no una cita literal de los autores.
3. Entrega la ruta de lectura con las secciones y páginas en orden e indica los saltos entre capítulos y entre bloques (por ejemplo, de la circulación capilar del capítulo 16 al riñón del 27).
4. Para el mapa visual, entrega una copia de `assets/grafo_guyton.html`, que tiene buscador, leyenda filtrable por bloque, tres vistas (capítulos, conceptos, completa) y el botón «Trazar prerrequisitos». Si piden modificar el grafo, edita el JSON y regenera el HTML con la skill `grafo-de-libro`.

## Alcance y límites

- Las secciones no están numeradas en el libro. La numeración `capítulo.orden` es propia del grafo y sigue los encabezados principales de cada capítulo.
- Las páginas de las secciones pueden desviarse ±1 página. Se dedujeron de los pies de página del texto fuente.
- El archivo fuente no incluía las páginas impresas 794–846. Los capítulos 64–67 y el principio del 68 (motilidad, secreciones, digestión y absorción, trastornos gastrointestinales y metabolismo de los hidratos de carbono) figuran con el título de la edición y una estructura basada en su contenido conocido, sin páginas. Están marcados con `"missing": true` y su resumen empieza por «(Ausente del archivo fuente)».
- Las fórmulas de los conceptos son relaciones fisiológicas estándar escritas en texto plano. No llevan número de ecuación del libro.
- No uses el grafo para decisiones clínicas. Para preguntas clínicas, contrasta con fuentes y guías vigentes.
