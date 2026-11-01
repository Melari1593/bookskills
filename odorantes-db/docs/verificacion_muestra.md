# Verificación independiente de la muestra de odorantes-db

Muestra: 30 filas (semilla 11), `docs/muestra_verificacion.json`. Fuente: PubMed. Se leyó el resumen de los 19 estudios. Se leyó el texto completo de los 6 estudios con PMCID (PMC12469716, PMC9562185, PMC8909151, PMC12785710, PMC7023010, PMC7758415). Para los demás solo hay resumen.

Antes de verificar contra las fuentes, se comprobó que las 30 filas de la muestra coinciden con `datos/odorantes.sqlite` (mismo rowid) y con `datos/extracciones/lote_*.json`. No hay diferencias entre las tres copias.

Criterio de nivel: `docs/instrucciones_extraccion.md` (A recombinado u omisión; B cuantificado con OAV ≥ 1; C GC-O/AEDA u OAV semicuantitativo; D solo GC-MS).

## Tabla

| rowid | alimento | compuesto | veredicto | detalle |
|---|---|---|---|---|
| 232 | naranja | ethyl 2-methylpropanoate | correcta | Buettner 2001 (resumen). Es uno de los ésteres afrutados más potentes por OAV. Los modelos de recombinación reprodujeron ambos jugos. Nivel A correcto. FD/OAV null: el resumen no da cifras. Descriptor correcto. |
| 444 | parmesano | 2,6-dimethyl-pyrazine | correcta | Qian 2002 (resumen). Osme la sitúa entre las pirazinas de la nota a nuez tostada. Nivel C correcto. El descriptor viene del grupo, no del compuesto aislado, pero es fiel. |
| 287 | tomate | 2-nonenal | correcta | Cheng 2020, Tabla 2 (texto completo). OAV impreso = 1; descriptor graso, verde. Está entre los 22 compuestos con OAV ≥ 1 que el estudio cuenta. Nivel B coherente con el método (calibración y umbrales en agua). Reserva sobre la fuente: concentración media 124,18 / umbral 190 ≈ 0,65. Además, el intervalo y la media son idénticos a los del nonanal. Es probable que la tabla tenga un error de copia. La fila reproduce bien la fuente, pero el dato de origen es dudoso. |
| 439 | parmesano | diacetyl | correcta | Qian 2002 (resumen). Figura entre los compuestos activos por Osme. Nivel C correcto. |
| 400 | mantequilla | (E)-2-octenal | correcta | Mallia 2009 (resumen). Es uno de los odorantes AEDA/SIDA que sube con la fotooxidación. El resumen no da OAV, así que C es el nivel prudente. |
| 239 | naranja | wine lactone | correcta | Sellami 2018 (resumen). Está entre los FD más altos del AEDA. El resumen no da el FD individual, así que null es correcto. Nivel C correcto. |
| 261 | tomate | (E,Z)-2,4-decadienal | correcta | Mayer 2008 (resumen). Es uno de los 19 odorantes del modelo de aroma validado sensorialmente. Nivel A correcto. |
| 438 | parmesano | heptanal | correcta | Qian 2002 (resumen). Activo por Osme. Nivel C correcto. |
| 301 | ajonjoli_tostado | 3-methyl-1-butene-1-thiols ((Z) and (E)) | correcta | Tamura 2011 (resumen). SIDA; OAV ≈ 2400 dado para el par de isómeros. Nivel B correcto. |
| 98 | te_negro | phenylacetaldehyde | correcta | Zhou 2023 (resumen). Hubo omisión, reducción y adición. Es uno de los 8 compuestos característicos con OAV > 100. Nivel A correcto. OAV null aceptable porque el resumen no da la cifra exacta. |
| 95 | te_negro | (E,Z)-2,6-nonadienal | correcta | Tao 2022, sección 3.3 (texto completo). OAV 49 en el té fresco. El texto lo describe como de olor a pepino. Nivel B correcto: el ensayo de adición no es una omisión, así que no llega a A. |
| 412 | parmesano | methional | correcta | Qian 2003 (resumen). Está entre los contribuyentes más importantes según OAV, con cuantificación por purga y trampa. Nivel B aceptable. |
| 263 | tomate | methional | correcta | Mayer 2008 (resumen). Forma parte del modelo de aroma validado. Nivel A correcto. |
| 244 | naranja | hexanal | error menor | Sellami 2018 (resumen). El hexanal aparece en el AEDA (C seguro). El resumen dice que los aldehídos bajan con el almacenamiento, pero no da un OAV ≥ 1 para el hexanal. Nivel B no demostrado con lo leído. Corregir a C (inflado 1 escalón). |
| 323 | mani_tostado | trans-4,5-epoxy-(E)-2-decenal | correcta | Chetschik 2008 (resumen). Está entre los odorantes principales del tostado. El resumen lo describe como metálico. Nivel C correcto. |
| 315 | ajonjoli_tostado | 2-methoxy-4-vinylphenol | correcta | Zheng 2026, sección 3.3 (texto completo). OAV 22 en la muestra de 170 °C / 20 min. El OAV es semicuantitativo, sin olfatometría, así que C es correcto. Nota: la matriz del estudio es aceite extraído de semilla tostada, no la semilla. |
| 407 | parmesano | 3-methylbutanal | correcta | Qian 2003 (resumen). Es el primer compuesto de la lista por OAV. Nivel B aceptable. |
| 96 | te_negro | (E)-2-nonenal | correcta | Tao 2022, sección 3.3 (texto completo). OAV 2 en el té fresco. El texto no da descriptor, así que el campo vacío es correcto. Nivel B correcto. |
| 49 | cacao | 2-phenylethanol | correcta | Frauendorfer 2008 (resumen). El resumen lo nombra como contribuyente al aroma tras SIDA/OAV. Nivel B aceptable. |
| 229 | banano | E-2-hexenal | correcta | Jordán 2001 (resumen). Solo aparece en la pulpa fresca y el panel GC-O lo detectó. Nivel C correcto. |
| 156 | frambuesa | 4-(p-hydroxyphenyl)-2-butanone | correcta | Klesk 2004 (resumen). Es uno de los 21 compuestos AEDA con impacto equivalente en ambos orígenes. No es una identificación tentativa. Nivel C correcto. |
| 73 | matcha | 3-ethyl-phenol | correcta | Luo 2022, sección 3.4.2 (texto completo). Es uno de los 10 compuestos con OAV > 1 exclusivos del grado alto. El OAV es semicuantitativo, sin GC-O, así que C es correcto. Descriptor musty = mohoso. |
| 47 | cacao | 3-methylbutanoic acid | correcta | Frauendorfer 2008 (resumen). Tiene el FD más alto en grano tostado, con olor a sudor, y la fuente lo cuantifica como contribuyente. Nivel B aceptable. |
| 276 | tomate | 2-octenal | correcta | Cheng 2020, Tabla 2 (texto completo). OAV 15 (450,97 / 30). Descriptor hongo, terroso. Nivel B correcto. |
| 415 | parmesano | ethyl hexanoate | correcta | Qian 2003 (resumen). Está en la lista de contribuyentes por OAV. Nivel B aceptable. |
| 356 | avellana_tostada | 4-hydroxy-2,5-dimethyl-3(2H)-furanone | correcta | Burdack-Freitag 2012 (resumen). Es uno de los 19 compuestos con OAV > 1 del modelo, que fue muy similar al original. Nivel A correcto. Detalle: el resumen lo sitúa en el segundo grupo de OAV, no entre los más altos. La `ubicacion` exagera un poco, pero ningún campo verificado es erróneo. |
| 325 | mani_tostado | 2-acetyltetrahydropyridine | correcta | Chetschik 2008 (resumen). Es nuevo en maní tostado y el resumen lo describe como de olor a palomitas. Nivel C correcto. |
| 22 | cafe_tostado | furfuryl methyl sulfide | correcta | Chen 2025, sección 3.5 (texto completo). FD 2187, exclusivo de la muestra de Colombia. No consta su OAV ni si entró en el recombinado, así que C es correcto. |
| 305 | ajonjoli_tostado | 3-mercapto-2-pentanone | correcta | Tamura 2011 (resumen). Es uno de los 11 tioles cuantificados por SIDA. El resumen no da su OAV, así que C es una elección conservadora y no infla el nivel. |
| 203 | mango | p-cymene | correcta | Liu 2020, secciones 3.3–3.4 (texto completo). OAV 7,19 y descriptor cítrico, verde. La fuente asigna el valor por error tipográfico a "HY", pero la lista de 17 compuestos es la de Tainong. La asignación de la fila es correcta. El FD del estudio es frecuencia de detección, no dilución, así que fd null es correcto. Nivel B correcto. |

## Recuento

| veredicto | n |
|---|---|
| correcta | 29 |
| error menor | 1 |
| error grave | 0 |
| no verificable | 0 |

- Tasa de error grave: 0/30 = 0 %. Con 0 eventos en 30 filas, el límite superior aproximado del IC95 % es 10 % (regla de 3/n).
- Tasa de error total (menor + grave): 1/30 = 3,3 %.

## Observaciones fuera de la tabla

1. **Base frágil de resumen.** 22 de las 30 filas (73 %) dependen solo del resumen. En esas filas FD/OAV son null salvo en la fila 301. Por eso casi no hay cifras individuales que contrastar. El nivel se apoya en frases generales del resumen (filas 49, 47, 407, 412 y 415). Son defendibles, pero son inferencias.
2. **Fuente dudosa (fila 287).** La Tabla 2 de Cheng 2020 parece duplicar los datos de concentración del nonanal en el (E)-2-nonenal. Conviene marcar esta fila como dato de baja confianza.
3. **Metadatos de estudio (no son filas de la muestra).** En `lote_3.json`, el estudio de mango (Liu 2020) lista `metodos: ["OAV","GC-MS"]`, pero el estudio también hizo GC-O (frecuencia de detección y OSME). En `lote_5.json`, Zheng 2026 analiza aceite de ajonjolí, no semilla tostada. La forma culinaria difiere de `ajonjoli_tostado`.
4. **Inconsistencia de criterio.** En Sellami (fila 244) se asignó B sin un OAV explícito. En Tamura (fila 305) se asignó C en la misma situación. Conviene unificar: sin un OAV ≥ 1 visible en lo leído, el nivel máximo es C.

## Conclusión

La muestra no contiene compuestos inventados, cifras inventadas ni niveles inflados en 2 o más escalones. Todas las cifras contrastadas coinciden con la fuente: 8 valores numéricos en total, 1 FD y 7 OAV (7 en texto completo y 1 en resumen). La fiabilidad para identificar compuestos y para transcribir cifras es alta. La debilidad principal es la asignación de nivel B desde resúmenes, con una sobreestimación de 1 escalón en 1/30 filas. También es baja la densidad de datos numéricos, porque el 73 % de las filas solo tiene resumen. Con n = 30, la tasa real de error grave puede llegar al ~10 %. Para afirmar una tasa < 5 % hace falta una muestra mayor o revisar los estudios sin texto completo.
