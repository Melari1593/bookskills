# Handbook of Medicinal Herbs (Duke, 2.ª ed., 2002)

Grafo de conocimiento del catálogo completo de *Handbook of Medicinal Herbs* (James A. Duke et al., CRC Press, 2002; ISBN 0-8493-1284-1), con una verificación externa hecha el 2026-11-14.

- **Visor:** [`duke-grafo.html`](duke-grafo.html). Es autónomo: carga d3 7.8.5 desde cdnjs y no necesita servidor. Permite buscar una hierba o una indicación, filtrar por seguridad y por puntaje mínimo de eficacia, y ver la ficha de cada hierba (dosis, contraindicaciones, extractos, sinónimos y página) con su red. Las hierbas verificadas muestran insignias y alertas de 2026.
- **Reporte del grafo:** [`GRAPH_REPORT.md`](GRAPH_REPORT.md). Incluye métricas, esquema, metodología, validación y limitaciones.
- **Verificación:** [`VERIFICACION.md`](VERIFICACION.md). Revisa las 23 afirmaciones con eficacia 3, las hierbas ++/+++ con alertas actuales y el cruce con `healing-herbal-infusions`.

## Cifras

- 3761 nodos: 1083 hierbas, 1140 actividades, 1534 indicaciones y 4 niveles de seguridad.
- 65 742 aristas. Cada una lleva la página impresa, el ítem textual y las fuentes de Duke.
- Eficacia de las aristas: f 64,1 %, 1 32,8 %, 2 3,1 %, 3 0,04 % (23 aristas).
- Seguridad de las hierbas: X 144, + 350, ++ 429, +++ 160.

## Hallazgos de la verificación

- De las 23 afirmaciones con eficacia 3, 8 están respaldadas con matices, 5 son inciertas, 7 no tienen evidencia clínica y 3 están contradichas: saw palmetto en la HBP y valeriana como hipnótico y en el insomnio.
- El libro omite alertas que hoy están establecidas en hierbas ++ y +++. Por ejemplo: interacciones del hipérico, hepatotoxicidad del kava, el fo-ti y los suplementos de cúrcuma, y la cumarina de la canela cassia.
- La calificación ++ del tanaceto contradice el propio texto del libro.

## Archivos

| Archivo | Contenido |
|---|---|
| `nodes.csv`, `edges.csv` | Nodos y aristas |
| `graph.json` | `{"metadata", "nodes", "edges"}` |
| `graph.graphml` | Para Gephi o Cytoscape |
| `compact.json` | Datos del visor |
| `validation.json` | Validación: sin IDs duplicados, sin huérfanos y sin aristas sin extremo |
| `scripts/parse.py` | Texto del PDF → `data.json` |
| `scripts/build.py` | `data.json` → exportaciones |
| `scripts/html.py` | `compact.json` → visor, con las insignias de la verificación |

El texto fuente del libro no está en el repositorio. Para reproducir el grafo, extrae el PDF con `pdftotext` y sigue los pasos de [`GRAPH_REPORT.md`](GRAPH_REPORT.md).

**Advertencia:** el libro es de 2002. Los puntajes son el criterio de Duke en ese año. No uses el grafo como guía clínica.
