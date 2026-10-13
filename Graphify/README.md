# Graphify — Harry's Cosmeticology

Grafo de conocimiento de tres libros de *Harry's Cosmeticology* (9.ª ed., Chemical Publishing, 2015), construido con el método de [graphify](https://github.com/Graphify-Labs/graphify): extraer conceptos y relaciones por capítulo, fusionarlos en un grafo, detectar comunidades y generar un reporte y un visor.

- *Vol. 1* — marketing y fragancia, regulación global y propiedad intelectual, y los sustratos (piel, cabello, uñas, nariz, boca, labios, zona íntima).
- *Vol. 2* — ingredientes (tensioactivos, siliconas, reología, botánicos, conservantes, antioxidantes, péptidos, AHAs…) y fundamentos del antienvejecimiento.
- *Sustainability and Eco-responsibility* (focus book).

**2129 nodos · 6434 aristas · 59 comunidades · 65 capítulos.**

## Archivos

| Archivo | Qué es |
|---|---|
| `graph.html` | Visor interactivo autocontenido (ábrelo en el navegador). Busca un concepto, tócalo para ver lo que dice cada capítulo y sus relaciones; filtra por tipo o enfoca una comunidad. |
| `GRAPH_REPORT.md` | Nodos dios, conceptos puente, comunidades, conexiones sorprendentes, hiperaristas y lista de capítulos. |
| `graph.json` | El grafo completo: nodos (tipo, comunidad, resúmenes por capítulo, alias), aristas (relación, confianza, evidencia) e hiperaristas. |
| `extraction/chunk_*.json` | Extracción por capítulo hecha por los subagentes (fuente del grafo). |
| `labels.json` | Nombres de las comunidades, indexados por su concepto principal. |
| `build.py`, `template.html` | Constructor (Python estándar, sin dependencias) y plantilla del visor. |

Para regenerar tras editar una extracción o `labels.json`:

```bash
python3 Graphify/build.py
```

## Cómo se hizo

1. Cada EPUB se convirtió a texto por capítulo (el texto de los libros no se incluye en el repo).
2. Nueve subagentes leyeron los capítulos completos y extrajeron nodos tipados (`ingredient`, `anatomy`, `mechanism`, `condition`, `product`, `technique`, `regulation`, `concept`…) y aristas con relación (`treats`, `inhibits`, `causes`, `used_in`, `regulates`…), confianza `EXTRACTED`/`INFERRED`/`AMBIGUOUS` y una frase de evidencia. A diferencia del graphify original, los ids de concepto son globales (`hyaluronic_acid`, no `capitulo_hyaluronic_acid`) para que un mismo concepto conecte capítulos y libros.
3. `build.py` fusiona por id, plurales, siglas (VEGF ↔ vascular endothelial growth factor) y una lista de sinónimos revisada a mano; agrupa con Louvain (sin contar las aristas capítulo→tema) y escribe las salidas.

> El paquete `graphifyy` no pudo instalarse en este entorno, así que el pipeline se reimplementó sin dependencias. Las relaciones provienen de una extracción automática: verifica en el libro antes de citar un dato.
