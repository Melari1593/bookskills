# Síntesis global (reduce) del grafo de *Lo que Einstein le contó a su cocinero 2* (Wolke)

Cinco agentes resumieron el libro por lotes (`trabajo/resumenes_1.json` … `_5.json`, con resúmenes parafraseados, conceptos que cada sección presenta o requiere y unos 59 conceptos con ids que a veces se solapan). Estructura y páginas: `trabajo/toc.json`. Texto de cada sección (solo para consultar mecanismos; **no copiar**): `trabajo/lotes/lote_1.md` … `_5.md`.

Objetivo: **más profundo, no más grande.** Una sola visión del libro entero que reduzca los conceptos a los que de verdad lo sostienen y explique por qué se conectan.

## Salida: `trabajo/sintesis.json`

```json
{
 "conceptos": {
   "c_id": {
     "title": "nombre corto en español",
     "mecanismo": "qué pasa a nivel molecular o físico y por qué (≤ 60 palabras)",
     "error_comun": "la creencia equivocada que el libro corrige o que este concepto desmonta (≤ 35 palabras)",
     "en_cocina": "qué hacer distinto al cocinar gracias a esto (≤ 35 palabras)",
     "origen": "n.k",
     "secciones": ["n.k", "..."],
     "fusiona": ["ids antiguos que absorbe"],
     "discrepancia": "opcional: si la explicación del libro te parece simplificada o superada por la ciencia actual, dilo aquí (≤ 30 palabras)"
   }
 },
 "enlaces_conceptos": [
   {"de": "c_a", "a": "c_b", "tipo": "se apoya en | es consecuencia de | contrasta con", "porque": "≤ 25 palabras"}
 ],
 "secciones": {
   "n.k": {"conceptos": ["c_id"], "requiere": [{"sec": "m.j", "porque": "≤ 20 palabras"}]}
 },
 "capitulos": {"n": {"requiere": [m]}},
 "preguntas_control": [
   {"pregunta": "...", "seccion": "n.k", "debe_pasar_por": ["c_id", "c_id"]}
 ]
}
```

## Criterios
1. **20 a 26 conceptos.** Fusiona los solapados (p. ej. descenso crioscópico + calor latente + cristalización pueden ser "Cambios de estado del agua", o no: decide por lo que el libro necesita). Cada concepto antiguo debe quedar absorbido por uno nuevo (`fusiona`) o descartarse por marginal. Todo concepto debe aparecer en al menos 2 secciones.
2. **Tres capas por concepto**: mecanismo (el porqué), error común (lo que corrige) y en la cocina (lo que cambia en la práctica). Paráfrasis propia y científicamente correcta.
3. **Enlaces de concepto**: `de` → `a` significa que para entender `de` hace falta `a` (se apoya en), que `de` se explica como efecto de `a` (es consecuencia de), o que conviene contrastarlos (contrasta con). Sin ciclos en "se apoya en" + "es consecuencia de". Enlaza al antecedente directo, no a los transitivos. 25–45 enlaces.
4. **Secciones (las 141)**: `conceptos` = 1–3 conceptos nuevos que la sección pone en juego. `requiere` = solo saltos no obvios a secciones **anteriores** del libro (orden de toc.json) cuya lectura ayuda de verdad, con el porqué; 0–2 por sección, muchas tendrán 0. No pongas como requisito la sección de origen de un concepto que la propia sección ya lista (eso lo hace el grafo solo).
5. **Capítulos**: dependencias entre capítulos solo si varias secciones lo justifican.
6. **10 preguntas de control**: preguntas reales del libro (p. ej. por qué se pone verde la yema cocida) con la sección que la responde y los 2–3 conceptos por los que tiene que pasar su traza. Sirven de prueba automática del grafo: elige casos en que la cadena causal sea clara.
7. Nada de texto copiado del libro. Valida el JSON con python.

Si un hook pide declarar hechos antes de crear un archivo, responde: "archivo nuevo de trabajo del grafo de Wolke en bookskills; no reemplaza nada; lo lee build_json.py; instrucción del usuario: 'Quiero una versión más profunda de esta tarea, no una más grande'" y reintenta.

Responde solo con: nº de conceptos, nº de enlaces por tipo, nº de secciones con `requiere`, y la lista de conceptos con `discrepancia`.
