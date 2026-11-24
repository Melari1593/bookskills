---
name: agentes-ia-grafos
description: Grafos de cuatro libros de agentes de IA en español (Albada, Lanham, GraphRAG agéntico de Alcaraz y Julien, 30 agentes de Ahmad). Úsala para ubicar un concepto (ReAct, MCP, memoria, GraphRAG, orquestador, evaluación, guardrails), trazar qué leer antes, comparar cómo lo trata cada libro, armar un plan de estudio o de diseño de un agente y entregar el HTML interactivo.
---

# Grafos de libros de agentes de IA

La skill reúne 4 grafos de conocimiento. Cada grafo tiene capítulos, secciones, ítems clave y prerrequisitos.

| Clave | Libro | Contenido | Ítems |
|---|---|---|---|
| `albada` | *Desarrollo de Aplicaciones con Agentes de IA* (Michael Albada) | 13 capítulos, 137 secciones, 1 recurso (repositorio del libro) | 56 conceptos y patrones |
| `lanham` | *Agentes de IA en Acción*, 2.ª ed. (Micheal Lanham) | 11 capítulos, 153 secciones, 2 apéndices (Python; Node.js y npx para MCP) | 53 patrones |
| `graphrag` | *GraphRAG agéntico* (Anthony Alcaraz y Sam Julien) | 8 capítulos y Conclusión (`C`), 107 secciones | 41 conceptos y patrones |
| `ahmad` | *30 Agentes que Todo Ingeniero de IA Debe Construir* (Imran Ahmad) | 17 capítulos, 68 secciones | 30 agentes y 40 conceptos |

Archivos:
- `references/grafo_<clave>.json`: datos de cada grafo.
- `assets/grafo_<clave>.html`: mapa interactivo de cada grafo.
- `scripts/ruta.py`: búsqueda y ruta de lectura desde la terminal.

## Qué libro usar

- Si la pregunta es de arquitectura, diseño, evaluación, operación o seguridad de un agente en producción, empieza por `albada`.
- Si la pregunta es práctica (código, MCP, multiagente, memoria, bucles, agente cognitivo), empieza por `lanham`.
- Si la pregunta es de grafos de conocimiento, memoria en grafo, razonamiento sobre rutas u orquestación de herramientas con grafos, usa `graphrag`.
- Si la pregunta es de un tipo concreto de agente (por dominio o por tarea), usa `ahmad`. Sus ítems con resumen "Agente N." son los 30 agentes.
- Si no sabes qué libro tiene el tema, busca en los 4 a la vez.

## Consultar

1. Para buscar un tema en los 4 libros, ejecuta `python scripts/ruta.py "término"`.
2. Para la ruta de lectura en un libro, ejecuta `python scripts/ruta.py --grafo <clave> "término o número"`. Ejemplos: `--grafo graphrag PathRAG`, `--grafo ahmad 7.4`, `--grafo lanham react`.
3. Antes de explicar una relación, lee en el JSON los resúmenes de los nodos de la ruta. Un arco `A → B` en `requires` significa que B es antecedente de A.
4. Entrega la ruta en orden del libro. Indica los saltos entre capítulos.
5. Si el tema aparece en varios libros, compara cómo lo trata cada uno. Di qué libro lo desarrolla más y en qué secciones.

## Usos frecuentes

- **Plan de estudio:** junta las rutas de los temas pedidos. Quita las secciones repetidas. Ordena por libro y por número.
- **Diseño de un agente:** para cada componente del agente (herramientas, memoria, planificación, evaluación, guardrails, despliegue), da la sección de referencia de cada libro. Después da un orden de construcción.
- **Mapa visual:** entrega una copia de `assets/grafo_<clave>.html`. Tiene buscador, 3 vistas (capítulos, ítems, completa), leyenda filtrable y el botón "Trazar prerrequisitos". Necesita internet para cargar d3 desde cdnjs.
- **Cambiar un grafo:** edita el JSON. Después regenera el HTML con la skill `grafo-de-libro` (`build_graph.py`). Copia el resultado también a `grafos/` del repositorio.

## Límites

- Los libros son EPUB sin páginas impresas. El grafo no tiene números de página.
- Ningún libro numera sus secciones. La numeración `capítulo.orden` es del grafo. No la cites como numeración del libro.
- En `ahmad`, el libro no da una lista numerada de los 30 agentes. El recuento es del grafo (por ejemplo, 3 agentes en el capítulo 7).
- Los campos `formula` son esquemas cortos del grafo, no fórmulas del libro.
- Los prerrequisitos son una interpretación pedagógica, no una lista de los autores.
- El grafo no incluye código, ejercicios, tablas ni material preliminar.
- Los resúmenes son paráfrasis. No reproduzcas pasajes de los libros.
- Los frameworks y las APIs cambian rápido. Si la respuesta depende de la versión actual de una herramienta (MCP, A2A, un SDK), verifica en la documentación oficial.

## Skills relacionadas

- `empresa-agentica-grafo`: grafo de *La empresa agéntica* (Hodjat y Blondeau), con el enfoque de organización y negocio.
- `grafo-de-libro`: construye o regenera grafos de libros.
