---
name: hemodinamia-grafo
description: Explora el grafo de conocimiento del Manual de hemodinamia y aplicaciones clínicas en cardiología de José Rafael López Luciano. Úsala para localizar capítulos y secciones, encontrar conceptos como TIMI, angioplastia, IVUS o contraste, explicar cómo se conectan y trazar una ruta de lectura con prerrequisitos; también para entregar el HTML interactivo del grafo.
---

# Grafo del manual de hemodinamia

Utilizar `references/grafo.json` como mapa de estudio: 16 capítulos, 149 secciones, 63 conceptos y relaciones de prerrequisito. La numeración de páginas corresponde a la paginación impresa del manual. El HTML autocontenido está en `assets/grafo_hemodinamia.html`.

## Consultar

1. Para buscar un tema y sus antecedentes, ejecutar `python scripts/ruta.py "término"`. Se puede precisar un número de sección, por ejemplo `python scripts/ruta.py 4.12`, o un identificador de concepto, por ejemplo `python scripts/ruta.py reestenosis`.
2. Leer en `references/grafo.json` los resúmenes de los nodos encontrados antes de explicar la relación. Un arco `A → B` significa que B es antecedente de A; los arcos son una interpretación pedagógica, no una cita literal del autor.
3. Entregar una ruta de lectura con secciones y páginas impresas en orden, indicando los saltos entre capítulos. Al contestar preguntas clínicas, buscar además la fuente primaria pertinente y guías vigentes; este manual incluye recomendaciones y algoritmos históricos (por ejemplo, 2007 y 2010).
4. Para mostrar el mapa visual, proporcionar una copia de `assets/grafo_hemodinamia.html`. Contiene buscador, filtros, vistas de capítulos, conceptos y completa, y botón para trazar prerrequisitos. Si el usuario pide modificar el grafo, editar el JSON y regenerar el HTML con la skill `grafo-de-libro` cuando esté disponible.

## Alcance

Usar el grafo para orientación y aprendizaje. No extraer de sus resúmenes dosis, indicaciones actuales ni decisiones de atención a pacientes. El índice impreso tiene discrepancias de numeración en el capítulo 12; el grafo conserva 12.10 para enfermedad vascular periférica y 12.11 para diabetes, situando esta última en la página 331 según el cuerpo del PDF. No se incluyen tablas completas ni casos clínicos desarrollados.
