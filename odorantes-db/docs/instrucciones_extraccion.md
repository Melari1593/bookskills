# Extracción de odorantes clave: instrucciones para un lote

Base de datos de odorantes clave de alimentos (bookskills/odorantes-db). Te tocan los alimentos de `datos/alimentos.json` con `"lote": N` (N te lo da el encargo).

## Pasos por alimento
1. Busca en PubMed (carga con ToolSearch: `select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__convert_article_ids,mcp__PubMed__get_full_text_article,mcp__PubMed__get_copyright_status`):
   `<nombre en inglés> AND ("key odorants" OR "aroma extract dilution" OR "odor activity value" OR "aroma recombination" OR "stable isotope dilution" OR "odor-active")`.
   Si hace falta, busca por autores de referencia (Grosch, Schieberle, Hofmann, Buettner, Steinhaus) con el alimento.
2. Elige **2 a 4 estudios** por alimento, priorizando el método más fuerte (recombinación/omisión > SIDA + OAV > AEDA > solo GC-MS) y la forma culinaria indicada en `alimentos.json`.
3. Para cada estudio, intenta el texto completo: convierte PMID a PMCID; si tiene PMCID, usa `get_full_text_article` (si la salida es grande, guárdala en `cache/` —que no se versiona— y procésala con Python). Si no hay texto completo, usa solo el resumen y marca `texto_completo: false`.
4. Extrae **solo los compuestos que el estudio declara activos en olor** (en recombinado, OAV ≥ 1, FD alto o detectados por olfatometría). No extraigas listas de volátiles sin olfatometría salvo en estudios de nivel D. Máximo 25 compuestos por estudio, los de mayor FD/OAV.

## Nivel de evidencia de cada compuesto (el más alto que alcanza en ese estudio)
- **A**: forma parte de un recombinado validado sensorialmente, o su omisión cambia el aroma de forma significativa.
- **B**: cuantificado (idealmente SIDA) con OAV ≥ 1.
- **C**: GC-olfatometría / AEDA (FD alto) u OAV semicuantitativo.
- **D**: solo GC-MS o SPME sin olfatometría ni umbrales.

## Salida: `datos/extracciones/lote_N.json`
```json
{
 "estudios": [
  {"doi": "10.xxxx/...", "pmid": "…", "pmcid": "PMC… o null", "autor": "Apellido", "anio": 2020,
   "alimento": "id de alimentos.json", "muestra": "variedad, origen y procesado del estudio",
   "metodos": ["AEDA", "SIDA", "OAV", "recombinacion", "omision", "GC-MS"],
   "texto_completo": true, "licencia": "CC BY 4.0 / sin datos / …",
   "nota": "paráfrasis propia, ≤ 60 palabras: qué hizo el estudio y qué encontró"}
 ],
 "odorantes": [
  {"doi": "10.xxxx/...", "alimento": "id", "nombre": "nombre tal como lo da el estudio, en inglés",
   "descriptor": "descriptor de olor del estudio, traducido al español",
   "fd": 1024, "oav": 350.5, "nivel": "A", "ubicacion": "Tabla 3 / resumen / Figura 2"}
 ]
}
```
`fd` y `oav` son `null` si el estudio no los da. Varios estudios del mismo alimento pueden repetir compuestos: anótalos en cada estudio.

## Reglas
- **No copies texto de los artículos.** Solo datos (nombres, cifras, métodos) y notas con tus palabras. No pegues frases ni tablas enteras.
- **No inventes**: si un número o un descriptor no está en lo que leíste, déjalo `null` o vacío. Si solo viste el resumen, extrae solo lo que el resumen nombra.
- Valida el JSON con `python3 -c "import json;json.load(open('datos/extracciones/lote_N.json'))"`.
- Si un hook pide declarar hechos antes de crear un archivo, responde: "archivo nuevo de datos extraídos para odorantes-db en bookskills; no reemplaza nada; lo lee scripts/build_db.py; instrucción del usuario: 'Hazlo' (construir la base de odorantes)" y reintenta.

Responde solo con: por alimento, nº de estudios (cuántos con texto completo) y nº de odorantes por nivel; ruta del archivo.
