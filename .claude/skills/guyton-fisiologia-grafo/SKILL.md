---
name: guyton-fisiologia-grafo
description: Explora el grafo de conocimiento del Tratado de fisiología médica de Guyton y Hall (14.ª ed., español). Úsala para localizar capítulos y secciones, encontrar conceptos como Frank-Starling, Nernst, multiplicador de contracorriente o renina-angiotensina, explicar cómo se conectan, trazar una ruta de estudio con prerrequisitos y ubicar el capítulo equivalente de Berne & Levy Physiology (8.ª ed.); también para entregar el HTML interactivo del grafo.
---

# Grafo de fisiología de Guyton y Hall

Usa `references/grafo.json` como mapa de estudio: 85 capítulos en 8 bloques, 714 secciones, 391 conceptos clave y unos 1400 enlaces de prerrequisito (entre capítulos, secciones y conceptos). Las páginas son las impresas de la 14.ª edición. El HTML autocontenido está en `assets/grafo_guyton.html`.

El grafo está correlacionado con *Berne & Levy Physiology* (8.ª ed., en inglés). En `resources` están sus 44 capítulos: `id` es el número del capítulo en B&L, `page` su página de inicio en B&L y `usedBy` las secciones de Guyton que trata. Además vienen título y resumen en español, `bl_section` y `subtemas` con página. En el HTML aparecen como cuadrados grises, y el panel de cada sección de Guyton tiene un apartado «Complemento en Berne & Levy».

## Consultar

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py "término"`. También acepta un número de sección (`python scripts/ruta.py 27.4`) o el id de un concepto (`python scripts/ruta.py multiplicador_contracorriente`).
2. Antes de explicar una relación, lee en `references/grafo.json` los resúmenes de los nodos encontrados. Un arco `A → B` significa que B es antecedente de A. Los arcos son una interpretación pedagógica, no una cita literal de los autores.
3. Entrega la ruta de lectura con las secciones y páginas en orden e indica los saltos entre capítulos y entre bloques (por ejemplo, de la circulación capilar del capítulo 16 al riñón del 27). `ruta.py` también lista los capítulos de Berne & Levy que complementan el tema: inclúyelos cuando pidan una segunda fuente, un enfoque más molecular o integrado, o un tema digestivo de los capítulos 64–68 (B&L 27–32 cubre ese hueco con texto real).
4. Para el mapa visual, entrega una copia de `assets/grafo_guyton.html`, que tiene buscador, leyenda filtrable por bloque, tres vistas (capítulos, conceptos, completa) y el botón «Trazar prerrequisitos». Si piden modificar el grafo, edita el JSON y regenera el HTML con la skill `grafo-de-libro`.

## Alcance y límites

- Las secciones no están numeradas en el libro. La numeración `capítulo.orden` es propia del grafo y sigue los encabezados principales de cada capítulo.
- Las páginas de las secciones pueden desviarse ±1 página. Se dedujeron de los pies de página del texto fuente.
- El archivo fuente no incluía las páginas impresas 794–846. Los capítulos 64–67 y el principio del 68 (motilidad, secreciones, digestión y absorción, trastornos gastrointestinales y metabolismo de los hidratos de carbono) figuran con el título de la edición y una estructura basada en su contenido conocido, sin páginas. Están marcados con `"missing": true` y su resumen empieza por «(Ausente del archivo fuente)».
- Las fórmulas de los conceptos son relaciones fisiológicas estándar escritas en texto plano. No llevan número de ecuación del libro.
- La correspondencia con Berne & Levy se hizo por contenido, capítulo a capítulo, y es una interpretación. B&L no tiene sección de sangre ni capítulos de buceo o energética celular, así que los capítulos 36 (grupos sanguíneos), 37 (hemostasia), 45 (buceo) y 73 (energética) de Guyton, y algunas secciones de otros capítulos, quedan sin complemento.
- No uses el grafo para decisiones clínicas. Para preguntas clínicas, contrasta con fuentes y guías vigentes.
