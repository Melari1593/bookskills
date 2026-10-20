---
name: grafo-de-libro
description: Extrae y estructura un grafo de conocimiento a partir de un libro o PDF proporcionado por el usuario, con conceptos, relaciones, citas de procedencia y exportaciones para análisis de grafos.
---

# Grafo de libro

## Activación
Usar cuando el usuario escriba `$grafo-de-libro` y adjunte o identifique un libro, PDF o documento fuente.

## Objetivo
Convertir el contenido del libro en un grafo de conocimiento **trazable a la fuente**. No inventar capítulos, conceptos, relaciones, páginas ni citas.

## Procedimiento
1. Identificar el archivo, título, edición, idioma y alcance. Si no hay documento accesible, solicitarlo.
2. Extraer índice, capítulos, encabezados y contenido relevante; conservar números de página cuando estén disponibles.
3. Crear nodos con identificadores estables, etiqueta, tipo, definición y referencia de origen (capítulo, sección, página).
4. Crear aristas dirigidas con relación explícita: `define`, `parte_de`, `causa`, `relacionado_con`, `prerrequisito_de`, `aplica_a`. Añadir evidencia textual breve y localización. Distinguir relaciones expresas de inferencias.
5. Normalizar sinónimos, resolver duplicados y evitar aristas sin sustento. Indicar vacíos o ambigüedades.
6. Validar nodos huérfanos, identificadores repetidos, referencias faltantes y consistencia de las relaciones.
7. Exportar `nodes.csv`, `edges.csv`, `graph.json` y opcionalmente `graph.graphml`; incluir `GRAPH_REPORT.md` con estadísticas y limitaciones.
8. Si el usuario pide un grafo interactivo, crear visualización HTML autónoma con búsqueda, filtros y detalle de evidencia.
9. Si el usuario solicita aprendizaje automático, preparar matrices de características y división de datos sin fuga; diferenciar claramente grafo documental y grafo de observaciones empíricas.

## Esquema mínimo
- Nodo: `id, label, type, description, source, chapter, section, page`.
- Arista: `source, target, relation, evidence, source_document, page, inferred`.
- JSON: `{"metadata": {...}, "nodes": [...], "edges": [...]}`.

## Reglas
- Basarse primero en el material proporcionado. Señalar por separado cualquier información externa.
- No asumir que una relación causal existe por simple coocurrencia.
- No presentar hipótesis o vínculos pedagógicos como afirmaciones del autor.
- En documentos médicos o científicos, respetar edición y contexto temporal; no interpretar recomendaciones antiguas como guías vigentes.
- No afirmar que se ha subido nada a GitHub sin confirmación de escritura exitosa.

## Entrega
Resumir libro y alcance procesado, métricas del grafo, metodología, advertencias y rutas de archivos exportados. Si faltan insumos, especificar qué falta.
