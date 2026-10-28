---
name: "odorantes-clave"
description: "Busca en PubMed los odorantes clave de uno o más alimentos, encuentra los que comparten y traduce el resultado en maridajes con trazabilidad. Úsala para preguntas de foodpairing, aroma o química del sabor."
---

# Odorantes clave y maridaje

Identificas los **odorantes clave** (compuestos volátiles presentes por encima de su umbral de olor) de uno o varios alimentos a partir de literatura revisada por pares, encuentras los que comparten y los conviertes en ideas de maridaje con fuentes. Combinas dos marcos:

- **Química del aroma** (evidencia): qué moléculas son clave en cada alimento y con qué método se establecieron.
- **Método Foodpairing** (interpretación): si está disponible la skill `foodpairing` de bookskills, úsala para los 14 tipos de aroma, el overtoning y las reglas de equilibrio. Si no, aplica las reglas resumidas abajo.

Respondes en el idioma de la persona (por defecto, español).

## Cuándo usarla

- "¿Por qué combinan X e Y?", "¿qué moléculas comparten?", "odorantes de X".
- "¿Con qué marida X?" cuando la persona quiere una base química, no solo tradición culinaria.
- Diseñar una receta, bebida o producto a partir de puentes aromáticos.
- Revisar si una afirmación de maridaje ("comparten tal molécula") tiene respaldo.

No es para seguridad alimentaria ni toxicología de aromas; si aparece un riesgo (p. ej. contaminantes del tostado), menciónalo y remite a `biotech-research`.

## Paso 1. Definir el alimento con precisión

El perfil cambia mucho con el estado del alimento. Fija para cada uno: **especie o variedad, procesamiento (crudo, tostado y grado de tueste, fermentado, cocido, aceite, pasta) y matriz final (grano, bebida, aceite)**. Si la persona no lo dice, asume la forma culinaria más común y decláralo al inicio (p. ej. "café arábica tostado medio, en bebida"). Café verde y café tostado son alimentos distintos para esta skill.

## Paso 2. Buscar en PubMed

Usa las herramientas de PubMed (cárgalas con ToolSearch si hace falta). Lanza en paralelo, por alimento:

1. `<alimento en inglés> AND ("key odorants" OR "aroma extract dilution" OR "odor activity value" OR "aroma recombination" OR "odor-active" OR olfactometry)`
2. Si hay procesamiento: añade `AND (roasted OR fermented OR ...)`.
3. Para cada odorante candidato a compartido: `<odorante> AND (<alimento A> OR <alimento B>)` — confirma que aparece como clave en ambos, no solo como volátil detectado.

Obtén los metadatos (título, resumen, DOI). Si la salida es grande, procésala con Python sobre el archivo guardado y extrae solo las frases que nombran compuestos, FD, OAV o "key".

Para revisiones clásicas (Grosch, Schieberle y su grupo, Escuela de Múnich de química del sabor), búscalas por autor si el tema lo pide; son la referencia de los métodos AEDA/SIDA.

## Paso 3. Jerarquía de evidencia de un odorante

Un compuesto detectado no es lo mismo que un odorante clave. Clasifica cada hallazgo:

| Nivel | Método en el estudio | Qué demuestra |
|---|---|---|
| A (más fuerte) | Recombinación y pruebas de omisión | El compuesto es necesario para el aroma |
| B | Cuantificación por dilución isotópica (SIDA) + OAV ≥ 1 | Está por encima de su umbral en ese alimento |
| C | GC-olfatometría con AEDA (factor de dilución alto) o OAV con cuantificación semicuantitativa | Contribuye al olor en el extracto |
| D | Solo GC-MS / SPME sin olfatometría ni umbrales | Está presente; no prueba que huela |

Un odorante es **compartido con confianza alta** cuando aparece con nivel A–C en ambos alimentos, en al menos un estudio cada uno. Media: nivel C en uno y D en otro, o un solo estudio pequeño. Baja: solo nivel D o solo en un modelo (p. ej. reacción de Maillard en laboratorio, no en el alimento).

## Paso 4. Normalizar nombres

Los mismos compuestos aparecen con nombres distintos. Unifica antes de comparar y menciona el sinónimo en la tabla. Ejemplos frecuentes:

- 2-furfuriltiol = 2-furanmetanotiol = furfuril mercaptano (FFT)
- Furaneol = HDMF = 4-hidroxi-2,5-dimetil-3(2H)-furanona
- Sotolón = 3-hidroxi-4,5-dimetil-2(5H)-furanona
- 4-vinilguayacol = 2-metoxi-4-vinilfenol
- Guayacol = 2-metoxifenol
- Metional = 3-(metiltio)propanal
- 2-acetil-1-pirrolina (2-AP)
- 3-metilbutanal = isovaleraldehído; 2-metilbutanal; 2-metilpropanal = isobutiraldehído (aldehídos de Strecker)

Si dudas de una equivalencia, no la fuerces: escribe ambos nombres y "equivalencia no confirmada".

## Paso 5. Construir la tabla de odorantes compartidos

Para cada odorante compartido: nombre (y sinónimo), descriptor de olor, evidencia en A (estudio, método o FD/OAV si el resumen lo da), evidencia en B, nivel de confianza. Añade debajo **lo que los diferencia**: los odorantes clave propios de cada alimento, porque sirven para contrastes.

Asigna cada odorante a uno de los 14 tipos de aroma de Foodpairing (frutal, cítrico, floral, verde, herbal, vegetal, caramelo, tostado, frutos secos, leñoso, especiado, quesero, animal, químico). Guía rápida:

- Pirazinas, tioles furánicos (FFT), aldehídos de Strecker de malta → tostado / frutos secos
- Furaneol, maltol, sotolón (baja concentración) → caramelo
- Guayacoles, fenoles → leñoso/ahumado o especiado (clavo para 4-vinilguayacol)
- Ésteres etílicos → frutal; lactonas → frutal/coco
- Aldehídos C6–C9 → verde; terpenos → cítrico, floral o herbal
- Metional, metanotiol → vegetal; 2,3-butanodiona → quesero/mantecoso
- Tioles con notas de grosella o cárnicas → frutal o animal según el compuesto

## Paso 6. Traducir a maridaje (interpretación)

Separa siempre evidencia (tabla) de interpretación (ideas). Reglas:

1. **Puente fuerte**: dos o más odorantes compartidos con confianza alta → maridaje de "punto grande"; buen candidato para **overtoning** (sumar ingredientes que comparten esos tipos de aroma, p. ej. café + ajonjolí + caramelo).
2. **Contraste**: usa los odorantes propios de uno (p. ej. ésteres frutales del café) para elegir un tercer ingrediente de otro tipo de aroma.
3. **Equilibrio** (reglas del libro): al menos 2 de los 5 sabores básicos, un elemento blando y uno crocante, cinco ingredientes o menos mientras se aprende.
4. **Matriz y estabilidad**: los odorantes hidrofóbicos se perciben mejor en grasa; los muy volátiles o reactivos (tioles) se pierden con el reposo, el calor prolongado o la unión a la matriz. Si un estudio lo describe, conviértelo en consejo práctico (p. ej. "café recién preparado").
5. **Procesamiento**: si un odorante aparece solo con tostado o fermentación, indica que el maridaje depende de esa preparación.

## Paso 7. Entrega

Estructura de la respuesta (en el chat, salvo que pidan un documento):

```
Respuesta corta: sí/no comparten odorantes clave y cuáles pesan más.

## Odorantes compartidos
| Odorante (sinónimo) | Olor | En A | En B | Confianza |

## Lo que los diferencia

## Qué implica para el maridaje (interpretación)

## Limitaciones

## Log de búsqueda
| Fuente | Fecha | Query | Resultados |

Fuentes: autor año con enlace DOI.
```

Si la persona quiere guardarlo, ofrece una tabla en Sheets/Docs o un grafo de maridajes.

## Reglas

- **Trazabilidad**: cada fila de la tabla lleva al menos una fuente con DOI. Nunca pongas un odorante "compartido" de memoria; si lo conoces pero no lo confirmaste en esta búsqueda, márcalo "no verificado".
- Cuando uses PubMed, atribúyelo ("según PubMed") e incluye los DOI como enlaces.
- **No compares FD ni OAV entre estudios** como si fueran la misma escala: dependen del método, la extracción y la matriz. Usa los valores solo para jerarquizar dentro de un mismo estudio.
- Advierte sesgos: muchos estudios usan variedades o procesados concretos (p. ej. ajonjolí blanco chino, aceite prensado), y un perfil puede no aplicar a otra forma del alimento.
- Distingue un compuesto que huele de forma distinta según concentración (p. ej. sotolón: caramelo a baja, curry/fenogreco a alta).
- Los descriptores de olor vienen del estudio; no inventes notas sensoriales.
- Esta skill describe química del aroma; no hace afirmaciones de salud.

## Ejemplo verificado (28/10/2026): café tostado + ajonjolí tostado

Odorantes compartidos encontrados en PubMed:

| Odorante | Olor | Café tostado | Ajonjolí tostado | Confianza |
|---|---|---|---|---|
| 2-furfuriltiol | Café tostado, azufrado | Clave al tostar (Poisson 2009, doi:10.1021/jf901683v; Gigl 2021, doi:10.1021/acs.jafc.1c06163) | Entre los FD más altos en semilla tostada (Tamura 2010, doi:10.1021/jf100623a) | Alta |
| Furaneol (HDMF) | Caramelo | FD/OAV altos (Chen 2025, doi:10.3390/foods14183192) | FD alto (Tamura 2010); OAV alto en aceite (Jia 2019, doi:10.1111/jfbc.12786) | Alta |
| 4-vinilguayacol | Clavo | OAV alto (Chen 2025); aumenta al tostar (Czerny 2000, doi:10.1021/jf990609n) | FD alto (Tamura 2010); clave en pasta (Yang 2024, doi:10.1016/j.foodchem.2024.139809) | Alta |
| Guayacol, 4-etilguayacol | Ahumado | Chen 2025; Czerny 2000 | Clave del ahumado del aceite (Zhao 2025, doi:10.1016/j.foodres.2025.117567) | Alta |
| Alquilpirazinas (2-etil-3-metil-, 2-etil-3,5-dimetil-) | Tostado, frutos secos | FD 2048 en café turco (Turan Ayseli 2020, doi:10.1016/j.foodchem.2020.127821) | 2-etil-3-metilpirazina clave en pasta (Yang 2024) | Media-alta |

Diferencias: el café aporta ésteres frutales, dicetonas, sotolón y β-damascenona; el ajonjolí, tiazoles y 2-acetil-1,4,5,6-tetrahidropiridina (Kuang 2025, doi:10.1016/j.foodchem.2025.146671). Implicaciones: overtoning tostado–caramelo (café + ajonjolí + caramelo), café recién preparado porque el 2-furfuriltiol se une a melanoidinas y se pierde (Gigl 2021), ajonjolí tostado al momento, contraste frutal (naranja, frutos rojos) a través de los ésteres del café.