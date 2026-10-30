# Instrucciones para resumir un lote de *Lo que Einstein le contó a su cocinero 2* (Robert L. Wolke)

El libro se convierte en un grafo interactivo en español: capítulos → secciones (cada sección es una pregunta o tema breve con título ingenioso) → conceptos científicos clave. Tu lote está en `trabajo/lotes/lote_N.md` (N te lo da el encargo), con bloques `======== CAPÍTULO n` y `==== SECCIÓN id=n.k (p. X): título`. El texto viene de un PDF y puede tener cortes; si una sección contiene dos temas (porque una sección vecina no se detectó, p. ej. "¡No me beses!" dentro de 8.2), asigna a cada sección el resumen que corresponde a su título.

Lista cerrada de conceptos (ids): `trabajo/conceptos.md`. Úsala para etiquetar.

## Salida: `trabajo/resumenes_N.json`

```json
{
 "chapters": {"1": {"summary": "..."}},
 "sections": {"1.1": {"summary": "...", "presenta": ["c_cristalizacion"], "requiere": ["c_gases_disueltos"]}},
 "conceptos": {"c_cristalizacion": {"summary": "...", "section": "1.1"}},
 "conceptos_nuevos": {"c_algo": {"title": "...", "summary": "...", "section": "n.k"}}
}
```

Reglas:
- **Con tus propias palabras.** Nunca copies frases ni pasajes del libro (derechos de autor). Español neutro, frases cortas.
- `summary` de capítulo: 1–2 frases (máx. 40 palabras) sobre qué temas cubre.
- `summary` de sección: 1 frase (máx. 30 palabras) que diga la pregunta que responde y la explicación científica, parafraseada (p. ej. "Por qué el hielo casero sale opaco: el aire disuelto y las impurezas se concentran en el centro al congelarse de fuera hacia dentro.").
- `presenta`: conceptos de la lista que esa sección **explica** (0–3). `requiere`: conceptos que la sección **usa** sin explicarlos y que el lector necesita entender (0–4). No repitas un concepto en ambas listas.
- `conceptos`: para cada concepto que tu lote explica, 1 frase (máx. 35 palabras) con la explicación, parafraseada, y la sección donde mejor se explica (si en varias, la primera).
- `conceptos_nuevos`: solo si un tema científico central del lote no cabe en la lista (máx. 3), con id `c_` en minúsculas y sin acentos.
- Incluye TODOS los ids de capítulo y sección del lote. Valida con `python3 -c "import json;json.load(open('trabajo/resumenes_N.json'))"`.

Si un hook pide declarar hechos antes de crear un archivo, responde: "archivo nuevo de trabajo del grafo del libro de Wolke; no reemplaza nada; lo lee build_json.py; instrucción del usuario: '/grafo-de-libro' con el PDF del libro" y reintenta.

Al terminar responde solo: nº de secciones cubiertas, conceptos presentados y nuevos propuestos, ruta del archivo.
