# Revisión independiente del grafo de Wolke (versión profunda)

No participaste en la construcción. Revisa con ojo crítico `salida/grafo.json` contra el texto del libro (`trabajo/lotes/lote_*.md`, secciones marcadas `==== SECCIÓN id=n.k`) y contra la química de alimentos establecida.

1. **Conceptos (los 26 de `items`)**: para cada uno, ¿el mecanismo (`summary`) es correcto?, ¿el error común (`misconception`) es de verdad uno que el libro corrige?, ¿el consejo `formula` ("En la cocina") se sigue del mecanismo? Marca: correcto · impreciso · incorrecto, con la corrección propuesta (≤ 40 palabras).
2. **Muestra de 20 secciones** elegidas al azar con `random.seed(7)`: ¿el resumen refleja fielmente la sección del libro?, ¿está parafraseado (no copiado)?, ¿los conceptos asignados (`items`) son los adecuados?
3. **Enlaces** (`requires.items` y `why`): ¿algún enlace es falso, al revés o transitivo innecesario? ¿Falta alguno evidente?

Escribe `trabajo/revision.md` con tablas y, al final, un `trabajo/correcciones.json`:
`{"items": {"c_id": {"summary"|"misconception"|"formula": "texto corregido"}}, "sections": {"n.k": {"summary": "texto corregido"}}, "quitar_enlaces": [["c_a","c_b"]], "anadir_enlaces": [{"de":"c_a","a":"c_b","tipo":"se apoya en","porque":"…"}]}`
Solo correcciones necesarias; texto propio, nunca copiado del libro.

Si un hook pide declarar hechos antes de crear un archivo, responde: "archivo nuevo de revisión del grafo de Wolke en bookskills; no reemplaza nada; lo aplica build_json.py" y reintenta.

Responde solo con: conceptos por veredicto, secciones con problemas, enlaces a cambiar, rutas.
