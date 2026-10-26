# Understanding Nutrition — Knowledge Graph

Grafo estructural inicial construido a partir del índice del libro *Understanding Nutrition*, 12th ed. (Whitney & Rolfes, 2011).

- **285 nodos**: 1 libro, 20 capítulos y 264 temas.
- **284 relaciones**: jerarquía del índice y coincidencias textuales de encabezados.
- **Trazabilidad**: página impresa y línea del TXT de origen.

## Consultas
```bash
python scripts/query_graph.py stats
python scripts/query_graph.py chapters
python scripts/query_graph.py chapter 15
python scripts/query_graph.py search protein
python scripts/query_graph.py validate
```

**Nota de publicación:** para ejecutar estas consultas, importa los archivos `data/grafo.json`, `data/nodos.csv` y `data/relaciones.csv` del ZIP de la skill. Los datos aún no están publicados en esta carpeta.

No contiene el libro original ni representa un grafo molecular o de causalidad fisiológica. Para enriquecerlo, extraer afirmaciones verificables por capítulo y registrar sus citas.