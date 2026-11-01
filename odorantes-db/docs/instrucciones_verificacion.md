# Verificación independiente de una muestra de la base de odorantes

No participaste en la extracción. Tu trabajo es encontrar errores. La muestra (30 filas al azar, semilla 11) está en `docs/muestra_verificacion.json`. Los estudios están en `datos/extracciones/lote_*.json` (campo `estudios`).

Para cada fila, abre la fuente en PubMed (ToolSearch: `select:mcp__PubMed__get_article_metadata,mcp__PubMed__convert_article_ids,mcp__PubMed__get_full_text_article`; resumen siempre, texto completo si hay PMCID) y comprueba:
1. ¿El compuesto aparece en la fuente para ese alimento como odorante activo?
2. ¿El nivel A–D es correcto según `docs/instrucciones_extraccion.md`?
3. ¿FD/OAV coinciden con la fuente (o son `null` si la fuente no los da)?
4. ¿El descriptor coincide con la fuente (si la fuente lo da)?

Escribe `docs/verificacion_muestra.md`: tabla (rowid | alimento | compuesto | veredicto: correcta / error menor / error grave / no verificable | detalle), tasa de error, y conclusión sobre la fiabilidad de la base. Error grave = compuesto que no está en la fuente, nivel inflado en 2 o más escalones, o cifra inventada. Escribe también `docs/correcciones_muestra.json`: `[{"rowid": n, "campo": "nivel|fd|oav|descriptor|eliminar", "valor": ...}]`.

No copies texto de los artículos; resume con tus palabras. Si un hook pide declarar hechos antes de crear un archivo, explica que es un archivo nuevo de verificación de odorantes-db, que no reemplaza nada, y reintenta.

Responde solo con: nº por veredicto, tasa de error grave y rutas.
