---
name: five-elements-cookbook-grafo
description: Explora el grafo de conocimiento de The Five Elements Cookbook (Zoey Xinyi Gong), en español, con alertas de evidencia verificadas en PubMed y EFSA. Úsala para ubicar un concepto de la terapia alimentaria china (Yin y Yang, Qi, Humedad, Cinco Elementos, naturaleza térmica, cinco sabores, constituciones), ver la ficha y la dosis de una de sus 50 hierbas (goji, dátil, astrágalo, dang gui, kombu, nuez de ginkgo, semilla de albaricoque, reishi…), trazar qué leer antes de una de sus 55 recetas (congees, caldos, tés, postres) y entregar el HTML interactivo; también cuando pregunten si una sopa, té o congee medicinal chino es seguro, qué comer según la estación o la constitución en MTC, o si una dosis de una hierba china es razonable, aunque no nombren el libro.
---

# Grafo de The Five Elements Cookbook

Usa `references/grafo.json` como mapa de *The Five Elements Cookbook: A Guide to Traditional Chinese Medicine with Recipes for Everyday Healing* (Zoey Xinyi Gong). Tiene 25 capítulos en 5 bloques, 165 secciones, 26 conceptos clave, 2 tablas y 703 enlaces de prerrequisito. El HTML autocontenido está en `assets/grafo_five_elements_cookbook.html`. Si estos archivos no están en la sesión, clona o lee el repositorio GitHub `Melari1593/bookskills`, carpeta `.claude/skills/five-elements-cookbook-grafo/`.

Los bloques son:
- Fundamentos de la MTC (caps. 0–6): terapia alimentaria, Yin y Yang, las cinco sustancias vitales, los seis factores ambientales, órganos y meridianos, y los Cinco Elementos (Wu Xing).
- Propiedades de los alimentos (caps. 7–10): naturaleza térmica, cinco sabores, cuatro direcciones y métodos de cocción.
- Estaciones y constituciones (caps. 11–12): comer según la estación y 9 constituciones (deficiencia de Yang, Yin o Qi; estancamiento de Qi o de Sangre; Flema-Humedad; Humedad-Calor; alérgica; neutra).
- Hierbas (caps. 13–18): 50 hierbas. Cada ficha trae función, naturaleza, sabor, meridianos y la dosis máxima diaria según el libro.
- Recetas (caps. 19–24): 55 recetas de entradas, sopas, platos principales, congees, bebidas y postres. Cada una trae funciones, energética, clima y hierbas.

## Consultar

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py "término"`. Acepta el nombre de una hierba (`kombu`), el título de una receta en inglés (`"wu zhi yin"`), un número de sección (`15.6`), un número de capítulo (`22`) o el id de un concepto (`shi`).
2. Antes de explicar una relación, lee en `references/grafo.json` los resúmenes de las secciones encontradas. Un arco `A → B` significa que B es antecedente de A: una receta tiene como antecedentes las fichas de sus hierbas y los conceptos de MTC que usa. Los arcos son una interpretación pedagógica, no una cita de la autora.
3. Entrega la ruta de lectura en orden. `ruta.py` también imprime las alertas de las hierbas y recetas de la ruta: **inclúyelas siempre que la respuesta toque eficacia, dosis o seguridad.**
4. Para el mapa visual, entrega una copia de `assets/grafo_five_elements_cookbook.html`. Tiene buscador, leyenda filtrable por bloque, tres vistas, el botón «Trazar prerrequisitos» y un recuadro «Atención» en las secciones con alerta. Si piden modificar el grafo, edita el JSON y regenera el HTML con la skill `grafo-de-libro`.

## Alertas de evidencia

27 secciones tienen el campo `caution`: 21 hierbas y 6 recetas. La verificación es del 2026-11-21. Las alertas de 14 hierbas se reusaron de `super-powders-grafo` y de `healing-herbal-infusions`; las de las 7 hierbas de mayor riesgo se verificaron en esta revisión. Cada alerta empieza con un veredicto:

| Veredicto | Significado |
|---|---|
| Respaldada | La evidencia apoya el uso como alimento o la afirmación del libro |
| Imprecisa | El libro advierte o afirma algo, pero simplifica o se queda corto |
| Riesgo omitido | El grafo no recoge un riesgo documentado |
| Sin datos de seguridad a esa dosis | No hay estudios que respalden la dosis del libro |
| Matiz | Precaución práctica, sobre todo para niños, embarazo o fármacos |

Archivos de apoyo:
- `references/alertas.json`: el texto de cada alerta, por número de sección.
- `references/verificacion.md`: veredicto, fuentes con DOI, confianza, origen, cálculos, huecos y log de búsqueda.

### Dosis del libro que chocan con la evidencia

| Sección | Hierba | Dosis del libro | Problema |
|---|---|---|---|
| 15.11 | Kombu | 15 g secos al día | Con esa misma cantidad, la TSH subió por encima de lo normal en adultos sanos (Miyai 2008). Úsalo para dar sabor al caldo, no como hierba diaria. |
| 15.12 | Semilla de albaricoque | 3 a 10 g al día | La EFSA pone el límite agudo de un adulto en 3 semillas pequeñas crudas (370 mg); un niño pequeño llega con media semilla. La cocción no elimina el riesgo de cianuro. |
| 13.4 | Regaliz chino | hasta 30 g al día | Con 100 mg o más de ácido glicirrícico al día sube la presión y baja el potasio (Penninkilampi 2017). |
| 17.2 | Corteza de canela (cassia) | 2 g molidos al día | Da de 3,8 a 6,5 mg de cumarina: un adulto de 60 kg llega a la ingesta tolerable y un niño la supera. |
| 15.7 | Nuez moscada | 9 g enteros o 3 g molidos al día | Hay intoxicaciones con dosis grandes. La dosis del libro supera la cantidad culinaria. |
| 15.6 | Nuez de ginkgo | 5 a 10 nueces al día | La ginkgotoxina causa convulsiones, sobre todo en niños. Siempre cocida y nunca para niños. |
| 18.8 | Azafrán y cártamo | 1,5 g y 10 g al día | No hay datos que respalden esa dosis. Usa cantidades culinarias. |

Otras alertas importantes:
- **Miel (13.2):** no en menores de 12 meses. La llevan 15 recetas.
- **Warfarina:** goji (13.6), dang gui (13.9), ginseng americano (14.3) y jengibre (16.7).
- **Hongo de nieve (22.6):** riesgo de ácido bongkrékico si se remoja mucho tiempo.
- **Saffron Mulled Wine (23.6):** lleva alcohol.

El grafo describe el libro: `summary` dice lo que dice la autora, y la evidencia va solo en `caution`. Cuando cites una dosis o una afirmación de salud del libro, da también su veredicto.

## Cómo responder sobre salud

1. Si la pregunta es de eficacia o seguridad, lee la alerta y su fila de `verificacion.md`, y cita sus fuentes.
2. Si la hierba no tiene alerta, no supongas que es segura: `verificacion.md` lista las que no se revisaron. Busca en PubMed con la skill `biotech-research` y di la fecha de la búsqueda.
3. Separa el marco de la MTC (naturaleza, sabor, meridianos, patrones) de la evidencia clínica. Explica el marco como lo describe el libro y no lo presentes como fisiología demostrada.
4. Para preparar un té, un jarabe o un caldo con estas hierbas, usa también `healing-herbal-infusions`. Para adaptógenos y hongos (reishi, goji, astrágalo), usa `super-powders-grafo`. Para MTC y salud mental, usa `chinese-medicine-for-the-mind`. Para la técnica (geles, espumas), usa `gastronomia-molecular`. Para combinar aromas, usa `foodpairing` u `odorantes-clave`.

## Alcance y límites

- El grafo no trae páginas impresas. La numeración `capítulo.sección` es propia del grafo.
- Las recetas tienen su título original en inglés. El grafo da funciones, energética, clima y hierbas, pero no cantidades ni pasos. Para prepararlas, consulta el libro.
- Las alertas comparan con el resumen del grafo, no con el texto completo del libro. El libro puede traer advertencias que el grafo no recoge.
- Las alertas resumen la evidencia publicada. No sustituyen la valoración clínica, sobre todo en embarazo, lactancia, niños, enfermedad tiroidea, hepática, renal o cardiaca, y en personas que toman anticoagulantes, antihipertensivos, diuréticos, digoxina, corticoides o inmunosupresores.
