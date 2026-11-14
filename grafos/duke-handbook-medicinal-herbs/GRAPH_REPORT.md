# Reporte del grafo: Handbook of Medicinal Herbs

**Libro:** James A. Duke, Mary Jo Bogenschutz-Godwin, Judi duCellier y Peggy-Ann K. Duke. *Handbook of Medicinal Herbs*, 2.ª ed. CRC Press, 2002. ISBN 0-8493-1284-1. En inglés.
**Alcance procesado:** el catálogo completo de hierbas de la A a la Z (págs. 1–814) y la lista de abreviaturas de fuentes (págs. 815–820). No se procesaron la introducción ni los índices.
**Generado:** 2026-11-14 · **Verificación externa:** [`VERIFICACION.md`](VERIFICACION.md) · **Visor:** [`duke-grafo.html`](duke-grafo.html)

## Métricas

| Elemento | Cantidad |
|---|---|
| Nodos | 3761 |
| Hierba | 1083 |
| Actividad (p. ej., Antiemetic) | 1140 |
| Indicación (p. ej., Migraine) | 1534 |
| Seguridad (X, +, ++, +++) | 4 |
| Aristas | 65 742 |
| `calificacion_seguridad` | 1083 |
| `tiene_actividad` | 19 368 |
| `indicada_para` | 45 291 |

**Puntaje de eficacia de las aristas (escala de Duke):**

| Puntaje | Significado | Aristas | % |
|---|---|---|---|
| f | Folclor | 41 445 | 64,1 |
| 1 | Fitoquímico o estudio experimental | 21 201 | 32,8 |
| 2 | Extracto o té con estudios, o aprobación de Comisión E o TRAMIL | 1990 | 3,1 |
| 3 | Ensayos clínicos con la planta | 23 | 0,04 |

**Seguridad de las hierbas:** X 144 · + 350 · ++ 429 · +++ 160.

**Términos con más hierbas:** Fever (720), Cancer (684), Diuretic (625), Pain (601), Inflammation (581), Water Retention (569), Rheumatism (548), Dermatosis (529), Gastrosis (513), Diarrhea (501).

## Esquema

- **Nodo:** `id, label, type, description, source, chapter, section, page`. Las hierbas tienen además `scientific, safety, safety_raw, qualifier, dosages, downsides, extracts`.
- **Arista:** `source, target, relation, evidence, source_document, page, inferred, score, refs`.
  - `evidence` copia el ítem del libro, por ejemplo `Migraine (3; FNF; SHT)`.
  - `refs` lista las abreviaturas de las fuentes de Duke. Su significado está en `compact.json` → `abbr`.
  - `inferred` es `False` en todas las aristas: todas son afirmaciones expresas del libro.
- **page:** número impreso del libro. Es la página del PDF menos 23.

## Metodología

1. Extraje el texto con `pdftotext` (`src/raw.txt`).
2. `scripts/parse.py` detecta cada encabezado de monografía (`NOMBRE (Nombre científico Autor) puntaje`), incluidos los encabezados en dos líneas y los calificadores como "(Gel)" o "(external)". Luego separa las secciones Activities, Indications, Dosages, Contraindications, Extracts y Synonyms, y lee cada ítem con la forma `Nombre (puntaje; FUENTES)`. Resultado: `data.json`.
3. `scripts/build.py` crea los nodos y las aristas, valida el grafo y exporta los archivos.
4. `scripts/html.py` crea el visor interactivo con los datos incrustados y las insignias de la verificación.

Para reproducir:
```
python3 scripts/parse.py src/raw.txt data.json
python3 scripts/build.py data.json out/
python3 scripts/html.py out/compact.json out/duke-grafo.html
```

## Validación

- IDs duplicados: 0.
- Aristas sin extremo: 0.
- Aristas sin página: 0.
- Nodos huérfanos: 0.
- Hierbas sin ítems: Kelp y Wild Servicetree. Sus monografías no tienen secciones Activities ni Indications con puntaje. Solo tienen la arista de seguridad.

## Advertencias y limitaciones

- **El libro es de 2002.** Los puntajes de eficacia y seguridad son el criterio de Duke en ese año. No los uses como guía clínica. La verificación de 2026 contradice 3 de las 23 afirmaciones con eficacia 3 y halla alertas que el libro omite (hipérico, kava, fo-ti, cúrcuma, canela cassia). Ver [`VERIFICACION.md`](VERIFICACION.md).
- **La mayor parte del grafo es folclor.** El 97 % de las aristas tiene puntaje f o 1. Filtra por puntaje 2 o más para un uso informado.
- **Sinónimos sin fusionar.** Duke usa sus propios términos (Gastrosis, Rhinosis, Hepatosis). No los uní con términos clínicos. Hay variantes del mismo concepto (p. ej., las formas de cAMP).
- **Hierbas repetidas.** Algunas especies tienen dos monografías por la parte usada (Aloe y Aloes, gel y látex). Se conservan como nodos distintos, como en el libro.
- **Ítems descartados.** 43 ítems no se convirtieron en arista porque su nombre no era válido o superaba los 60 caracteres (64 702 ítems leídos; 64 659 aristas de actividad o indicación).
- **Texto libre.** Las secciones de dosis y contraindicaciones se guardan como texto, sin estructura.
- **Extracción automática.** Puede haber errores de lectura en ítems que cruzan columnas o páginas. Los conteos de validación no detectaron problemas estructurales.

## Archivos

| Archivo | Contenido |
|---|---|
| `nodes.csv` | Nodos (1,4 MB) |
| `edges.csv` | Aristas con evidencia y fuentes (11,8 MB) |
| `graph.json` | `{"metadata", "nodes", "edges"}` (21,8 MB) |
| `graph.graphml` | Para Gephi o Cytoscape (29,8 MB) |
| `compact.json` | Formato compacto del visor (3,4 MB) |
| `validation.json` | Resultados de la validación |
| `duke-grafo.html` | Visor interactivo autónomo (3,4 MB; d3 7.8.5 desde cdnjs) |
| `VERIFICACION.md` | Verificación con PubMed y fuentes regulatorias |
