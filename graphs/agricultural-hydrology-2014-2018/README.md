# Grafo de hidrología agrícola Colombia (2014–2018)

Extensión del grafo de física hacia agua en suelos, hidrología y rendimiento agrícola.

## Resultado local validado
- 45.054 registros de laboratorio de suelos incluidos (2014–2018).
- 6.658 agregados departamento–municipio–cultivo–año.
- 7.850 nodos; 71.431 relaciones.
- 6 ecuaciones conceptuales: Darcy, Richards, van Genuchten, balance hídrico, continuidad, FAO-56 Penman–Monteith.
- Artefactos locales: build_hydro_graph.py, nodes.csv, edges.csv, observed_features.csv, hydrology.graphml, hydrology.json, validation_report.json.

## Semántica
- OBSERVED_IN, FOR_CROP, LOCATED_IN: evidencia del CSV.
- HAS_AGGREGATE_MEASUREMENT: mediana numérica de registros por grupo, unidades aún no validadas.
- DESCRIBES: conocimiento físico externo.
- POTENTIAL_PROXY_FOR: hipótesis científica no calibrada.

## Limitaciones
No hay etiquetas de rendimiento agrícola ni datos de lluvia, ET, conductividad hidráulica o retención de agua. No se ha entrenado una GNN. Evitar fuga temporal/espacial y no interpretar promedios territoriales como mediciones de parcelas individuales.

## Reproducibilidad
El paquete completo, incluidos los archivos grandes y script, está disponible como ZIP en la conversación de ChatGPT que generó este registro. Esta publicación documenta la extensión; no incluye los archivos de datos ni el código ejecutable.
