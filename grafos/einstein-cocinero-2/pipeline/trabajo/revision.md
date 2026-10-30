# Revisión independiente: grafo de Wolke, *Lo que Einstein le contó a su cocinero 2*

Material revisado: `salida/grafo.json` (26 conceptos, 141 secciones, 30 enlaces entre conceptos y 24 entre secciones), cotejado con `trabajo/lotes/lote_1..5.md` y con la química de alimentos establecida. Las correcciones aplicables están en `trabajo/correcciones.json`. Una prueba de `build_json.py` y `validate_graph.py` con esas correcciones pasa sin ciclos.

## 1. Conceptos

Veredictos: **12 correctos · 9 imprecisos · 5 incorrectos**. Cada concepto recibe el veredicto de su campo más débil.

| Concepto | Veredicto | Campo | Problema y corrección propuesta (≤ 40 palabras) |
|---|---|---|---|
| c_ph | impreciso | summary | "Cuántos iones hay libres" no indica la escala ni el sentido. Decir que es una escala logarítmica inversa: a menor pH, más ácido. |
| c_pigmentos | impreciso | summary | "Los carotenoides aparecen al soltarse de proteínas" solo vale para la astaxantina de los crustáceos. La mioglobina cambia también con el estado del hierro (ferroso o férrico, como explica 7.2) y con el CO (6.2). |
| c_proteinas | impreciso | summary | Mete el gluten entre los efectos de la desnaturalización. El gluten se forma al hidratar y amasar, cuando gliadinas y gluteninas se enlazan. Conviene presentarlo como una red análoga. |
| c_colageno | correcto | — | Opcional: el colágeno empieza a contraerse hacia 60–65 °C. Los "≥70 °C" son razonables para obtener gelatina. |
| c_huevo | impreciso | misconception | "Dependen de la raza y del pienso" no sirve para la fecundación. Separar: la cáscara depende de la raza, la yema del pienso, y la fecundación no cambia el valor nutritivo. |
| c_lacteos | impreciso | misconception | Mezcla dos ideas y tergiversa la del queso. Según 2.8, el porcentaje sobre extracto seco **exagera** la grasa real, no la oculta. Según 2.1, desnatar ahorra solo unas 63 kcal por taza. |
| c_enzimas | impreciso | misconception | "Ambos cambios son oxidaciones" no refuta que la fruta golpeada sea más dulce. Debe decir que el golpe solo pardea, sin ganar azúcar (4.2). |
| c_maillard | **incorrecto** | summary | Pone un umbral de 120–140 °C para Maillard y deja la caramelización "a mayor temperatura". El libro (7.6) dice que Maillard ocurre desde unos 50 °C, e incluso lentamente a temperatura ambiente, y que la caramelización empieza hacia 120 °C. |
| c_almidon | correcto | — | — |
| c_carbohidratos | impreciso | summary, formula | Los polioles no llegan intactos al colon: se absorben en parte (~2,4 kcal/g). "Restar la fibra" solo vale si la etiqueta la incluye en los carbohidratos (EE. UU., Colombia). En la UE ya viene excluida y se restaría dos veces. |
| c_grasas | **incorrecto** | summary | Dice que el cuerpo trata las grasas trans "como saturadas". Son peores: suben el LDL y bajan el HDL, y el propio libro lo dice en 4.6. Lo correcto es que se *apilan* como las saturadas. |
| c_oxidacion | correcto | — | Mezcla la hidrólisis con la oxidación, pero las presenta como procesos distintos. Aceptable. |
| c_dispersiones | correcto | — | Simplifica: la nata montada se estabiliza sobre todo con glóbulos de grasa parcialmente coalescidos. Admisible para el nivel del grafo. |
| c_cristalizacion | correcto | — | — |
| c_cambios_estado | correcto | — | — |
| c_transferencia_calor | correcto | — | La idea del peso frente a la forma viene de 9.13. El consejo sobre moldes sigue lo que dice 9.11. |
| c_magnitudes | correcto | — | — |
| c_osmosis | impreciso | summary, misconception, formula | "Solo unos milímetros" vale para ácidos y aromas. La sal avanza centímetros en horas o días (salmuera, salado en seco). Los fosfatos retienen agua uniéndose a las proteínas, no por ósmosis. Al salarlo, el pepino pierde turgencia: suelta agua, pero no "cruje más". |
| c_solubilidad | **incorrecto** | formula | "No esperar que un vino disuelva más sabor que el agua" contradice la alerta del propio grafo en 7.10 y la evidencia. El etanol al 10–15 % sí aumenta algo la solubilidad de los volátiles apolares. |
| c_fermentacion | **incorrecto** | summary | Los mohos como el koji (*Aspergillus oryzae*) son aerobios, así que no fermentan "sin oxígeno". El límite del 15 % es aproximado: hay levaduras de sake que llegan a ~20 %. |
| c_microbios | impreciso | summary | Dice que bacterias **y mohos** necesitan "poca acidez". Mohos y levaduras toleran bien el medio ácido (mermeladas, frutas). La acidez frena sobre todo a las bacterias peligrosas. |
| c_azufrados | correcto | — | — |
| c_gusto | **incorrecto** | summary | Da por hecho que los insectos no tienen esos receptores. En 8.9 es una conjetura del autor ("me jugaría…"), y es falsa para los isotiocianatos: el TRPA1 de los insectos los detecta, y por eso la mostaza los repele. Hay que quitar esa frase. |
| c_aroma | correcto | — | — |
| c_polifenoles | correcto | — | El eugenol es un monofenol. El texto lo agrupa bien bajo "algunos fenoles". |
| c_etiquetado | correcto | — | — |

Los demás errores comunes sí aparecen corregidos en el libro: gamba cruda rosada (6.9), vieiras con fosfatos (6.8), mantequilla en la puerta de la nevera (9.2), aceite light (4.8), azúcar que "se derrite" (10.1), forma frente a peso (9.13), plátano (4.3) y fibra en la batidora (5.10).

## 2. Muestra de 20 secciones (`random.seed(7)`, `random.sample` sobre los 141 ids en orden del TOC)

Muestra: 5.15, 2.22, 7.10, 1.13, 2.2, 10.5, 2.8, 7.2, 1.15, 9.11, 4.1, 1.10, 2.6, 8.8, 8.4, 2.1, 4.8, 2.7, 8.5, 1.16.

| Sección | ¿Fiel? | ¿Parafraseado? | ¿Conceptos adecuados? | Observación |
|---|---|---|---|---|
| 1.10 Sulfitos | sí | sí | sí | — |
| 1.13 Guerra entre estados | sí | sí | **mejorable** | c_fermentacion encaja poco: la sección trata de definición legal, destilación y filtrado por carbón. Mejor c_cambios_estado (destilar) y c_solubilidad (adsorción). |
| 1.15 Agitado y revuelto | sí | sí | sí | — |
| 1.16 Mida su alegría | sí | sí | sí | — |
| 2.1 Galimatías de los desnatados | sí | sí | sí | — |
| 2.2 La crème de la crème | sí | sí | sí | — |
| 2.6 Vivir del aire | sí | sí | sí | — |
| 2.7 A la sombra de Filadelfia | sí | sí | sí | — |
| 2.8 Re: Brie | sí | sí | sí | — |
| 2.22 A darle al merengue | sí | sí | sí | — |
| 4.1 Aguacate maduro | sí | sí | sí | — |
| 4.8 ¿Es light el aceite light? | sí | sí | **falta uno** | El resumen menciona "cómo guardarlo" y el texto explica que luz y calor oxidan el aceite insaturado. Falta c_oxidacion. |
| 5.15 Miel y azúcar | sí | sí | sí | El libro afirma que la miel es "caldo de cultivo" anaerobio. El resumen no lo repite, y la alerta corrige la parte del adulto. |
| 7.2 ¿Carne marrón? | sí | sí | sí | — |
| 7.10 ¿Por qué vino? | sí | sí | sí | Es coherente con la sección, pero ver la contradicción de c_solubilidad en la tabla 1. |
| 8.4 Amor verdadero | sí | sí | sí | — |
| 8.5 ¿Botulismo en una botella? | sí | sí | sí | — |
| 8.8 Especias desaboridas | sí | sí | sí | — |
| 9.11 El método del palillo | sí | sí | sí | — |
| 10.5 El alimento de los dioses | sí | sí | sí | — |

Ningún resumen de la muestra necesita reescribirse, así que `sections` queda vacío. Comprobé los 141 resúmenes buscando secuencias de 7 o más palabras copiadas del libro. Solo aparecen 5 coincidencias, de 7 a 9 palabras, y todas reformulan la pregunta del lector (2.13, 3.10, 5.2, 6.2, 10.1). No es copia sustancial.

Conceptos de sección que habría que cambiar a mano en `trabajo/sintesis.json`, porque el formato de correcciones no lo permite:
- **1.13**: quitar c_fermentacion y poner c_cambios_estado.
- **4.8**: añadir c_oxidacion.

## 3. Enlaces

No hay ciclos ni enlaces transitivos redundantes en `requires.items` (lo comprobé con un DFS).

| Enlace | Acción | Motivo |
|---|---|---|
| c_colageno → c_transferencia_calor | **quitar** | Es un "por qué" forzado. Que el colágeno se convierta en gelatina depende de la temperatura sostenida y del tiempo en medio húmedo, no de los modos de transmitir el calor. La parte de temperatura y tiempo ya está en c_proteinas. |
| c_polifenoles → c_enzimas (se apoya en) | **añadir** | El resumen de c_polifenoles explica el oscurecimiento del té negro, que es una oxidación enzimática (polifenoloxidasa, 1.3 y 4.2). Ahora el concepto no apunta a enzimas. Con este enlace, c_pigmentos → c_ph pasa a ser alcanzable por otra ruta, pero se mantiene porque su motivo es distinto (las antocianinas viran con el pH). |
| Los demás enlaces (28) | mantener | Tienen la dirección correcta y un motivo plausible. c_carbohidratos → c_enzimas y c_etiquetado → c_magnitudes son flojos, pero defendibles. |

**Enlaces entre secciones.** No se pueden expresar en `correcciones.json`, así que hay que cambiarlos a mano en `sintesis.json`:
- **s2.22 → s2.18**: la premisa es falsa. El motivo dice que 2.18 "muestra cómo el calor coagula la clara", pero 2.18 trata de que el ácido y la sal coagulan la clara que se escapa. Además, 2.22 trae su propia definición de desnaturalización. Propuesta: quitarlo, o cambiar el motivo por "2.18 muestra que la clara se coagula con facilidad".
- **s10.4 → s2.22**: es débil. 2.22 no explica cómo se forma ni cómo se estabiliza una espuma: solo dice que las claras pasteurizadas montan peor. Las nubes de 10.4 son espuma de gelatina. Propuesta: quitarlo.
- Los otros 22 enlaces entre secciones tienen un motivo correcto y la dirección adecuada.
