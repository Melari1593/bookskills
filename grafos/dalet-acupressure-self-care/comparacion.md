# Dalet frente a la skill acupuntura-puntos

Generado: 2026-11-26. Script: cruce de `grafo_dalet_acupressure.json` con `.claude/skills/acupuntura-puntos/references/`.

## Método

1. El libro de Dalet no nombra los puntos; solo los describe. Claude asignó un código OMS a cada descripción.
2. Cada código se comparó con su ficha (ubicación y precauciones) y con la lista de contraindicados en el embarazo de `categorias.md`.
3. Cada afección se cruzó con su entrada del `indice-sintomas.md`. Una coincidencia significa que el punto del libro también aparece en esa entrada.

## Resultado

- 86 puntos verificados; todos tienen ficha o fila de punto extra.
- Coincidencia global: 127 de 207 usos de puntos (61 %).
- Discrepancias de ubicación: LU11 (el libro dice lado del índice; estándar radial), GV26 (el libro dice dos tercios bajo la nariz), Qiuhou (tercio externo frente a cuarto lateral), CV15 y ST42 (aproximados).
- Puntos del libro contraindicados clásicamente en el embarazo: LI4, SP6, BL60, BL67, GB21; abdomen inferior: CV3, CV4, CV6, ST25, KI11.

## Por afección

| Afección | Entrada del índice | Coinciden | Solo en el libro |
|---|---|---|---|
| 1.1 | Conjuntivitis | 2/4 | BL1, yuyao |
| 1.3 | Vista cansada | 4/4 | — |
| 1.6 | Acúfenos e hipoacusia | 2/4 | CV23, GV15 |
| 1.7 | Acúfenos e hipoacusia | 3/4 | GV15 |
| 1.8 | Mareo y vértigo | 1/3 | SI19, TE3 |
| 1.9 | Resfriado Viento-Frío + Rinitis | 3/4 | GV13 |
| 1.10 | Sinusitis | 3/4 | ST2 |
| 1.11 | Resfriado Viento-Frío + Resfriado Viento-Calor | 2/6 | GB21, GV13, LI20, yintang |
| 1.12 | Aftas | 1/4 | CV23, ST45, ST6 |
| 1.13 | Dolor de muelas | 3/6 | CV23, GV26, LI1 |
| 1.14 | Dolor de garganta | 2/4 | ST45, ST6 |
| 2.2 | Diabetes | 2/3 | BL17 |
| 2.3 | Obesidad | 1/2 | GB25 |
| 3.1 | Síndrome Bi | 1/3 | TE8, dingchuan |
| 3.2 | Tortícolis | 2/2 | — |
| 3.3 | Hombro doloroso | 1/1 | — |
| 3.4 | Epicondilitis lateral | 3/3 | — |
| 3.5 | Túnel carpiano | 2/3 | HT7 |
| 3.7 | Dorsalgia | 0/1 | TE3 |
| 3.8 | Lumbalgia aguda | 3/3 | — |
| 3.9 | Ciática | 1/3 | BL67, LR1 |
| 3.10 | Dolor de cadera | 1/2 | SP9 |
| 3.11 | Dolor de rodilla | 1/1 | — |
| 3.12 | Esguince de tobillo | 0/2 | GB39, SP6 |
| 3.13 | Talalgia | 0/2 | ST42, bafeng |
| 4.1 | Náusea y vómito | 1/2 | sifeng |
| 4.2 | Dolor de hipocondrio y biliar | 2/3 | yaoyan |
| 4.4 | Dolor epigástrico | 3/3 | — |
| 4.5 | Estreñimiento | 2/4 | LR1, SP9 |
| 4.6 | Diarrea | 3/3 | — |
| 4.7 | Hemorroides | 3/4 | GV26 |
| 5.1 | Hipertensión | 4/4 | — |
| 6.1 | Cólico renal | 1/4 | BL57, KI3, yaoyan |
| 6.2 | Cistitis | 1/3 | LR8, yaoyan |
| 6.3 | Retención urinaria + Incontinencia urinaria | 0/2 | BL67, KI11 |
| 6.4 | Enuresis | 4/4 | — |
| 7.1 | Cefalea | 2/4 | LU9, SI3 |
| 7.2 | Neuralgia del trigémino | 2/3 | LU9 |
| 7.3 | Dolor intercostal + Dolor torácico | 0/3 | GB25, SP9, TE8 |
| 8.2 | Eccema | 4/4 | — |
| 8.3 | Urticaria | 2/4 | BL13, GV16 |
| 8.4 | Herpes zóster | 1/5 | BL67, GB20, PC4, ST45 |
| 9.1 | Asma | 3/3 | — |
| 9.2 | Tos aguda + Tos crónica | 5/6 | dingchuan |
| 9.3 | Tos aguda + Tos crónica | 3/4 | sifeng |
| 10.1 | Síncope y primeros auxilios | 2/2 | — |
| 10.2 | Epilepsia | 2/3 | GV16 |
| 10.3 | Parálisis facial | 2/4 | BL1, LU9 |
| 10.4 | Secuelas de ACV | 5/8 | GB21, GV16, TE8 |
| 10.5 | Adicciones y tabaquismo | 1/4 | GB20, GB8, GV25 |
| 10.6 | Depresión | 1/1 | — |
| 10.7 | Agitación y manía | 2/4 | CV15, yintang |
| 11.1 | Impotencia | 3/3 | — |
| 11.3 | Mastitis | 2/4 | CV17, LI10 |
| 11.4 | Náusea del embarazo | 2/2 | — |
| 11.5 | Amenorrea | 1/3 | CV6, yaoyan |
| 11.6 | Dismenorrea + Síndrome premenstrual + Menstruación irregular | 5/6 | KI11 |
| 11.7 | Menorragia y metrorragia | 2/3 | SP3 |
| 11.8 | Prolapso uterino | 2/3 | KI11 |
| 11.9 | Leucorrea | 2/3 | GV26 |
| 12.1 | Fatiga | 2/2 | — |
| 12.2 | Insomnio | 1/2 | SP3 |

## Límites

- La asignación de códigos es una interpretación; las descripciones del libro son aproximadas (traveses de dedo).
- "Solo en el libro" no significa error: el índice recoge una selección de puntos, no todas las escuelas.
