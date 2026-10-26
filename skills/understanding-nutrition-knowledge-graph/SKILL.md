---
name: understanding-nutrition-knowledge-graph
description: Consulta un grafo temático trazable de Understanding Nutrition (Whitney y Rolfes, 12.ª edición) para explorar capítulos y conceptos de nutrición.
---
# Understanding Nutrition — Grafo de conocimiento

## Activación
Usar ante preguntas de navegación, identificación de temas y organización del contenido del libro. Consultar primero `data/grafo.json` o `scripts/query_graph.py`.

## Procedimiento
1. Ejecutar `python scripts/query_graph.py chapters` para listar capítulos.
2. Ejecutar `python scripts/query_graph.py chapter 15` para nutrición en embarazo y lactancia.
3. Ejecutar `python scripts/query_graph.py search vitamin` para localizar conceptos.
4. Ejecutar `python scripts/query_graph.py validate` para comprobar integridad.
5. Cuando se requieran mecanismos, dosis, interacciones o afirmaciones clínicas, consultar el texto original y adjuntar evidencia verificable: el grafo solo contiene encabezados del índice.

## Modelo
- `Book` → `HAS_CHAPTER` → `Chapter` → `HAS_TOPIC` → `Topic`.
- `SAME_HEADING` relaciona encabezados iguales; **no** implica causalidad ni equivalencia clínica.
- Los campos `page` corresponden a paginación impresa y `source_line` a la línea del TXT original.

## Seguridad y calidad
- Libro publicado en 2011: valores de referencia, recomendaciones y guías clínicas pueden estar desactualizados.
- No usar como fuente única de recomendaciones médicas actuales ni personalizar suplementación sin evaluación profesional.
- No reproducir capítulos ni fragmentos extensos protegidos por derechos de autor.
- Diferenciar explícitamente datos extraídos, inferencias y evidencia externa.