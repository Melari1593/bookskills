---
name: gastronomia-molecular
description: "Técnicas y química de la gastronomía molecular con dosis verificadas: hidrocoloides (alginato, agar, gelana, xantana, metilcelulosa, lecitina), esferificación, geles, espumas, emulsiones, sous vide, nitrógeno líquido y transglutaminasa, y las reacciones que las explican (Maillard, caramelización, proteínas, almidón, pH). Úsala siempre que pidan diseñar o corregir una textura, calcular gramos de un aditivo, explicar por qué una preparación funciona o falla, o revisar la seguridad de una técnica de cocina moderna, aunque no digan \"gastronomía molecular\"."
---

<!-- argument-hint: [técnica, agente, reacción o problema de textura] -->

# Gastronomía molecular

**Generada:** 2026-11-10 · **Fuentes:** PubMed, JECFA, EFSA, FDA (21 CFR, Food Code, GRAS), USDA FSIS, FSA, Codex, normas de Colombia, y *Texture* de Lersch (v2.2) para dosis técnicas.

Esta skill tiene dos capas:
- **Técnica:** qué agente usar, a qué concentración, a qué temperatura y qué hacer si falla.
- **Química:** qué pasa en las moléculas y por qué la técnica funciona.

Responde en el idioma de la persona. Por defecto, responde en español, con unidades métricas, °C y gramos.

## Archivos de referencia

Lee el archivo que corresponde antes de dar cifras. No des concentraciones de memoria.

| Archivo | Cuándo leerlo | Contenido |
|---|---|---|
| [`references/hidrocoloides.md`](references/hidrocoloides.md) | Elegir o dosificar un agente; diagnosticar un gel o una salsa que falla; regulación y alergenos | Tabla maestra de 21 agentes (concentración, hidratación, gelificación, fusión, sensibilidades, estado JECFA/EFSA/Colombia), 14 sinergias, 22 fallas con su corrección |
| [`references/tecnicas.md`](references/tecnicas.md) | Preparar una técnica paso a paso; sous vide; nitrógeno líquido; N₂O; transglutaminasa | 10 técnicas con receta base, puntos críticos y seguridad; tablas de pasteurización USDA FSIS y FDA Food Code; tabla resumen de 24 filas |
| [`references/reacciones.md`](references/reacciones.md) | Explicar por qué pasa algo; diseñar sabor, color o textura con química | Maillard y acrilamida, caramelización, proteínas, almidón, emulsiones, agua y calor (con altitud), pH y color, fermentación y umami |

Cada archivo termina con referencias (DOI o URL), log de búsqueda y **datos no confirmados**. Si una cifra está en "datos no confirmados", dilo y no la inventes.

Para el aroma (pirazinas, furanonas, aldehídos de Strecker, maridajes), usa la skill `odorantes-clave` y la base `odorantes-db`. Para verificar una afirmación de salud, usa `biotech-research`.

---

## Cómo responder

1. **Define el objetivo.** Qué textura, forma, temperatura de servicio y sabor busca la persona. Anota el líquido base: su pH, su calcio, su alcohol, su azúcar y si tiene fruta cruda con enzimas (piña, papaya, kiwi).
2. **Elige la técnica y el agente.** Usa la tabla rápida de abajo y confirma en `hidrocoloides.md`. Revisa las sensibilidades del agente frente al líquido base.
3. **Calcula en gramos.** Usa porcentaje en peso sobre el líquido: `g de agente = % × g de líquido / 100`. Con concentraciones menores de 1 %, pide una báscula de 0,01 g. Una cucharadita no es una medida válida a estas dosis.
4. **Da el proceso.** Pasos numerados, con temperatura de dispersión, de hidratación y de gelificación, y tiempos.
5. **Di los puntos críticos y las fallas típicas.** Usa la tabla de fallas de `hidrocoloides.md` y los "errores típicos" de `tecnicas.md`.
6. **Aplica la seguridad.** Revisa la sección de seguridad de abajo. Si aplica, dila junto a la receta, no al final.
7. **Explica la química en 2–4 frases.** Usa `reacciones.md`. Separa lo que está en las fuentes de tu interpretación.

### Formato de una receta

```
Objetivo: <textura, forma, servicio>
Ingredientes (para <X> g de líquido):
| Ingrediente | % | g |
Proceso:
1. ...
Por qué funciona: <química en 2–4 frases>
Si falla: <síntoma → causa → corrección>
Seguridad: <solo lo que aplica>
Fuentes: <archivo de referencia y fuente original>
```

---

## Tabla rápida de agentes

Valores de `references/hidrocoloides.md` (Lersch, *Texture* v2.2; JECFA; FDA). Úsalos como punto de partida y ajusta con prueba.

| Objetivo | Agente | Concentración (% p/p) | Clave del proceso |
|---|---|---|---|
| Esferas (directa) | Alginato de sodio en el líquido + baño de cloruro de calcio | Alginato 0,5–1; baño 0,5 de CaCl₂ (o 1 de lactato de calcio) | El líquido debe tener pH ≥ 3,65 y poco calcio. Si el pH es menor, corrige con citrato de sodio. Enjuaga las esferas en agua. |
| Esferas (inversa) | Calcio en el líquido + baño de alginato | Lactato o gluconolactato de calcio 2,4–3,75 en el líquido; baño de alginato 0,5 | Sirve para líquidos ácidos, con calcio o con alcohol. La esfera deja de gelificar al enjuagarla. |
| Gel firme, servido caliente o frío | Agar | 0,2 cuaja; 0,5 gel firme | Hierve para hidratar (> 90 °C). Gelifica a 35–45 °C. Funde a 80–90 °C. |
| Gel suave que se funde en la boca | Gelatina | 0,6–1,7 | Hidrata en agua fría y disuelve a ~50 °C. Gelifica por debajo de 15 °C en horas. Funde a 25–40 °C. No cuaja con piña, papaya o kiwi crudos. |
| Gel quebradizo | Carragenano kappa | ~1,5 | Hidrata a más de 70 °C. Sinergia con garrofín. |
| Gel elástico | Carragenano iota; gelana alta acilación | Iota 1–1,5; gelana AA 0,4–0,7 | Iota gelifica con calcio. Gelana AA gelifica y funde a 70–80 °C. |
| Gel que soporta calor y ácido | Gelana baja acilación | 0,4–0,7 | Hidrata a 90–95 °C con pH > 3,9. Las sales impiden la hidratación. |
| Gel que cuaja al calentar | Metilcelulosa | 1–2 | Hidrata en frío toda la noche. Gelifica a 50–60 °C y se ablanda al enfriar. |
| Espesar sin calor | Goma xantana | 0,25 salsa fluida; 0,7–1,5 salsa espesa | Dispersa con azúcar, aceite o licuadora. Estable en ácido, sal y alcohol. |
| Aire ligero | Lecitina de soja | 0,3–0,9 | Licuadora de inmersión en la superficie. Recoge la espuma de arriba. |
| Polvo de grasa | Maltodextrina de tapioca | Según receta (la grasa queda atrapada) | Mezcla aceite y maltodextrina hasta polvo. |
| Queso fundido liso | Citrato de sodio | ≤ 3 del queso (límite FDA para queso procesado) | Retira el calcio de la caseína y evita que la grasa se separe. |

---

## Seguridad (aplícala siempre)

Las cifras vienen de `references/tecnicas.md` y `references/reacciones.md`.

| Tema | Regla |
|---|---|
| **Nitrógeno líquido (−196 °C)** | Hay al menos 9 casos de perforación gástrica publicados, uno en Bogotá (2019). Nunca sirvas un alimento o bebida mientras quede nitrógeno líquido visible o humo. Espera la evaporación completa. Usa guantes y gafas. Trabaja en un lugar ventilado: el nitrógeno desplaza el oxígeno (un litro de líquido da unos 694 litros de gas). FDA (2018) y FSA (2012) emitieron alertas. |
| **Óxido nitroso (sifón)** | Usa solo cargas para alimentos y solo en el sifón. El uso recreativo causa deficiencia funcional de vitamina B12 y mielopatía. Es sustancia controlada en el Reino Unido desde 2023. |
| **Sous vide** | Usa las tablas de tiempo y temperatura de `tecnicas.md` (USDA FSIS, FDA Food Code). El tiempo empieza cuando el **centro** alcanza la temperatura. Pollo: no uses menos de 60 °C (a 60 °C, 25,7–32 min según la grasa). Res: 60 °C por 12 min en el centro, o 54,4 °C por 112 min. Enfría rápido: de 57 a 21 °C en 2 h y a 5 °C en 6 h en total. Guarda a ≤ 5 °C un máximo de 7 días. En embarazo, inmunosupresión, niños pequeños y mayores, usa las temperaturas completas del Food Code. |
| **Transglutaminasa** | Las piezas pegadas llevan la superficie al interior. Cocínalas como carne molida (63 °C por 3 min o 70 °C instantáneo). Declara su uso. En celiaquía, EFSA (2026) dice que no se puede descartar una contribución al riesgo; la evidencia es mecanística, sin ensayos clínicos. |
| **Ceviche y ácidos** | El limón desnaturaliza la proteína, pero **no pasteuriza**. Redujo *Salmonella* solo 1–2 log y no mata *Anisakis*. Para pescado crudo, congela antes a −20 °C por 7 días o a −35 °C por 15 h. |
| **Acrilamida** | Se forma por encima de 120 °C con baja humedad. En papa: remoja 30 min a 2 h, fríe por debajo de 175 °C y busca un color dorado claro, no café. No guardes la papa por debajo de 6 °C. |
| **Ahumado y asado fuerte** | Generan hidrocarburos aromáticos policíclicos y aminas heterocíclicas. Evita el contacto directo con la llama y la carne carbonizada. |
| **Alergenos y origen** | La lecitina de soja se declara como alergeno en la UE. La gelatina es de cerdo, res o pescado (restricciones religiosas). El origen de la maltodextrina importa en celiaquía. |
| **Lactantes** | Varios hidrocoloides tienen límites o restricciones en alimentos para lactantes. Consulta `hidrocoloides.md` §4.3 antes de usarlos para niños menores de 1 año. |

## Altitud (Bogotá y otras ciudades altas)

- En Bogotá (~2600 m), el agua hierve a unos 91 °C. Es un cálculo con la presión estándar, no una medición publicada.
- La pasta, las legumbres y los huevos tardan más en cocinarse. Una cocción "en agua hirviendo" no llega a 100 °C.
- La olla a presión recupera la temperatura alta.
- El sous vide no cambia con la altitud: el baño controla la temperatura por debajo del punto de ebullición.

## Regulación en Colombia

- La Resolución 2606 de 2009 sigue vigente para aditivos. La Resolución 2362 de 2023 no la deroga.
- La 2606 no trae una lista de aditivos permitidos agente por agente. Para un producto comercial, consulta al INVIMA y al Codex GSFA.
- No encontré normas del INVIMA sobre nitrógeno líquido, óxido nitroso ni transglutaminasa en cocina.

## Alcance y límites

- Las dosis técnicas vienen sobre todo de *Texture* v2.2 de Lersch, leído por extracción automática. Algunas columnas de su tabla salieron desalineadas; `hidrocoloides.md` lo indica.
- Sin cifra confirmada: datos técnicos de la HPMC y de los almidones modificados, dosis culinaria de la transglutaminasa, tablas de pasteurización de pescado por grosor (Baldwin), umbral de Maillard (~140 °C), temperaturas exactas de coagulación de la clara y la yema, y pH seguro de las fermentaciones lácticas. Si te piden estas cifras, dilo.
- La seguridad de las técnicas es para cocina. No es asesoría regulatoria para un producto comercial.
