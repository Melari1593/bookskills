---
name: nutricion-pediatrica-grafo
description: Explora el grafo de conocimiento del Manual of Pediatric Nutrition (3.ª ed., Hendricks, Duggan y Walker), en español. Úsala para localizar capítulos y secciones, encontrar conceptos como síndrome de realimentación, Holliday-Segar, crecimiento de recuperación, dieta cetogénica o nutrición parenteral, explicar cómo se conectan, trazar una ruta de estudio con prerrequisitos y ver qué recomendaciones del libro están superadas por guías vigentes; también para entregar el HTML interactivo del grafo.
---

# Grafo del Manual of Pediatric Nutrition

Usa `references/grafo.json` como mapa de estudio: 36 capítulos en 7 bloques, 254 secciones, 174 conceptos clave, 5 apéndices y unos 350 enlaces de prerrequisito (entre capítulos, secciones y conceptos). Las páginas son las impresas de la 3.ª edición. El HTML autocontenido está en `assets/grafo_nutricion_pediatrica.html`.

Los bloques son: evaluación y requerimientos; alimentación del niño sano; hospitalización y soporte nutricional; crítico, inmunocomprometido y prematuro; enfermedades de órganos y sistemas; endocrino-metabólicas; crecimiento, conducta y alergia. Los apéndices (`resources`) son: A conversiones, B interacciones fármaco-nutriente, C centros de referencia genético-metabólicos, D fabricantes de productos enterales y E curvas para síndromes específicos.

## Consultar

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py "término"`. También acepta un número de sección (`python scripts/ruta.py 17.3`) o el id de un concepto (`python scripts/ruta.py c15_sindrome_realimentacion`).
2. Antes de explicar una relación, lee en `references/grafo.json` los resúmenes de los nodos encontrados. Un arco `A → B` significa que B es antecedente de A. Los arcos son una interpretación pedagógica, no una cita literal de los autores.
3. Entrega la ruta de lectura con las secciones y páginas en orden e indica los saltos entre capítulos y entre bloques (por ejemplo, de la antropometría del capítulo 2 a la parenteral del 17). `ruta.py` también lista los apéndices que se consultan y las alertas de los conceptos de la ruta: inclúyelas siempre que la respuesta toque una cifra o una conducta.
4. Para el mapa visual, entrega una copia de `assets/grafo_nutricion_pediatrica.html`, que tiene buscador, leyenda filtrable por bloque, tres vistas (capítulos, conceptos, completa), el botón «Trazar prerrequisitos» y un recuadro «Atención» en los conceptos con alerta. Si piden modificar el grafo, edita el JSON y regenera el HTML con la skill de construcción de grafos (`grafo-nutricion-pediatrica` o `grafo-de-libro`).

## Alertas de guías vigentes

25 conceptos tienen el campo `caution`, revisado en octubre de 2026. Señala cuando una recomendación del libro está superada o una cifra no se pudo verificar. Las referencias que aparecen son, entre otras: Dietary Guidelines for Americans 2025–2030 (nueva pirámide, lácteos enteros en la infancia), DRI de energía 2023, patrones OMS y Resolución 2465 de 2016, Resolución 2350 de 2020 modificada por la 115 de 2026 (desnutrición aguda en Colombia), AAP 2024 (VIH y lactancia), ESPGHAN/ESPEN/ESPR/CSPEN 2018 (parenteral), ASPEN 2020 (realimentación), ESPGHAN 2022 (prematuro), AAP 2023 (obesidad), NHLBI 2011 (lípidos), ISPAD 2024 (diabetes), consenso de dieta cetogénica 2018 y DSM-5.

El grafo describe el libro: `formula` y `summary` dicen lo que dice el manual, y la actualización va solo en `caution`. Cuando cites una cifra de un concepto con alerta, di que el libro es de alrededor del año 2000 y remite a la guía vigente.

## Alcance y límites

- El libro no numera sus secciones. La numeración `capítulo.orden` es propia del grafo y sigue los encabezados principales de cada capítulo.
- El PDF fuente es un OCR de mala calidad. Las cifras clínicas ilegibles se omitieron en lugar de reconstruirse (por ejemplo, cortes de Gómez y Waterlow, longitudes intestinales y varias dosis); esos conceptos describen la relación sin la cifra. Los cortes de colesterol total del capítulo 29 se reconstruyeron de una figura dañada y están marcados para verificar en la página 434.
- Las remisiones del libro hacia capítulos posteriores («ver capítulo 27») se trataron como «ver también» y no como prerrequisitos.
- No incluye tablas completas, listas de productos ni problemas o casos del libro.
- No uses el grafo para decisiones clínicas. Para preguntas clínicas, contrasta con las guías vigentes que indican las alertas.
