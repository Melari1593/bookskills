# Verificar afirmaciones del libro de Wolke (2005) frente a la ciencia de 2026

Entrada: `trabajo/afirmaciones.md` (V1–V24, cada una con la sección del libro). Te toca el rango que indique el encargo.

Para cada afirmación:
- Busca en PubMed (carga con ToolSearch `select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata`) y en fuentes oficiales con WebSearch/WebFetch (EFSA, FDA, USDA FSIS, OMS/IARC, Codex, revisiones de química de alimentos). Prioriza revisiones, guías y regulación vigente.
- Si la salida de una herramienta es enorme, guárdala y procésala con Python.
- **Veredicto**: vigente · vigente con matices · superado · en disputa.
- **Alerta** (español, ≤ 55 palabras, frases cortas, neutra): qué sabemos hoy y qué cambia para quien cocina. Termina con la fuente corta entre paréntesis. Solo para veredictos distintos de "vigente".

## Salida
1. `trabajo/verif_X.md` (X = A o B): por afirmación, veredicto, qué dice la evidencia (2–4 frases), alerta, fuentes (autor año, revista u organismo, DOI o URL) y confianza (alta, media, baja). Al final, un **log de búsqueda** en tabla (fuente | query | resultados | usados).
2. `trabajo/alertas_X.json`: `{ "n.k": "texto de la alerta" }` con el id de sección de la afirmación. Si dos afirmaciones caen en la misma sección, únelas (≤ 80 palabras). Valida con json.load.

Cuando cites PubMed, incluye el DOI. No inventes referencias: si no pudiste abrir o confirmar una fuente, no la cites.

Si un hook pide declarar hechos antes de crear un archivo, responde: "archivo nuevo de trabajo del grafo de Wolke en bookskills; no reemplaza nada; lo lee build_json.py; instrucción del usuario: 'Incluye también el 7'" y reintenta.

Responde solo con: veredictos por tipo, nº de alertas y rutas.
