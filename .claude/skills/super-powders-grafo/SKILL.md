---
name: super-powders-grafo
description: Explora el grafo de conocimiento de Super Powders (Katrine van Wyk, 2018), en español, con alertas de evidencia verificadas en PubMed y agencias. Úsala para localizar un adaptógeno, hongo o superpolvo (ashwagandha, reishi, melena de león, maca, mucuna, He Shou Wu, cúrcuma, matcha…), ver qué recetas lo usan, trazar qué fichas leer antes de una receta (Golden Latte, tónicos, dulces), revisar qué afirma el libro y qué está superado o es riesgoso, y entregar el HTML interactivo; también cuando pregunten si un latte, tónico o polvo adaptógeno es seguro o tiene respaldo, aunque no nombren el libro.
---

# Grafo de Super Powders

Usa `references/grafo.json` como mapa del libro *Super Powders: Adaptogenic Herbs and Mushrooms for Energy, Beauty, Mood, and Well-Being* (Katrine van Wyk, 2018). Tiene 15 capítulos en 6 bloques, 104 secciones, 48 nodos de polvo o concepto (25 adaptógenos y hongos, 10 superpolvos y 13 conceptos de la Parte I), 47 recetas y 259 enlaces de prerrequisito. El HTML autocontenido está en `assets/grafo_super_powders.html`.

Los bloques son:
- Fundamentos (Parte I, caps. 0–5): estrés, "fatiga suprarrenal", qué es un adaptógeno, cómo elegirlo y qué saber antes de empezar.
- Hongos medicinales (cap. 6): chaga, cordyceps, melena de león, reishi y cola de pavo.
- Raíces, hierbas y hojas (cap. 7): ashwagandha, astrágalo, eleutero, He Shou Wu, tulsi, regaliz, maca, moringa, mucuna, ginseng, rhodiola, shatavari y ashitaba.
- Bayas, polen y perla (cap. 8): goji, espino, schisandra, polen de pino y perla.
- Otros superpolvos (cap. 9): baobab, remolacha, blue majik (espirulina azul), cacao, carbón activado, clorela, canela, colágeno hidrolizado, matcha y cúrcuma, más una guía para comprar polvos de calidad.
- Recetas (Parte III, caps. 10–14): lattes y bebidas, tónicos, dulces, recetas para la mañana, caldos, salsas y mezclas.

## Consultar

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py "término"`. Acepta el nombre de un polvo (`ashwagandha`), el título de una receta (`"golden latte"`), un número de sección (`10.11`), un número de capítulo (`7`) o el id de un nodo (`he_shou_wu`).
2. Antes de explicar una relación, lee en `references/grafo.json` los resúmenes de los nodos encontrados. Un arco `A → B` significa que B es antecedente de A: una receta tiene como antecedentes las fichas de los polvos que usa. Los arcos son una interpretación pedagógica, no una cita de la autora.
3. Entrega la ruta de lectura con las secciones en orden. Para una receta, la ruta lista las fichas de sus polvos. `ruta.py` también imprime las alertas de esos polvos: **inclúyelas siempre que la respuesta toque eficacia, dosis o seguridad.**
4. Para el mapa visual, entrega una copia de `assets/grafo_super_powders.html`. Tiene buscador, leyenda filtrable por bloque, vistas, el botón «Trazar prerrequisitos» y un recuadro «Atención» en los nodos con alerta. Si piden modificar el grafo, edita el JSON y regenera el HTML con la skill `grafo-de-libro`.

## Alertas de evidencia

33 nodos tienen el campo `caution`. Las verificaciones son del 2026-10-28, con PubMed y agencias (EMA, EFSA, BfR, LactMed, LiverTox, NIH ODS, Endocrine Society). La alerta de goji se amplió el 2026-11-17 con la alergia por LTP. Cada alerta empieza con un veredicto:

| Veredicto | Significado |
|---|---|
| Respaldada | La evidencia confirma la afirmación o la advertencia del libro |
| Debatida | Los estudios se contradicen o la calidad cambia el resultado |
| Imprecisa | El libro exagera o simplifica lo que muestran los estudios |
| Superada | La evidencia actual la contradice |
| Sin evidencia humana | Solo hay datos in vitro o en animales |
| Riesgo omitido | El libro no menciona un riesgo documentado |

Archivos de soporte:
- `references/alertas.json`: el texto de cada alerta, por id de nodo.
- `references/verif_A.md` (conceptos, hongos y otros polvos) y `references/verif_B.md` (raíces, hierbas y bayas): veredicto, fuentes con DOI o URL y confianza de cada alerta.
- `references/log_busqueda.md`: cada búsqueda con fecha, query y PMID.

Los riesgos principales que el libro omite son:
- **He Shou Wu:** hepatotoxicidad.
- **Ashwagandha:** daño hepático y tirotoxicosis. Dinamarca la retiró de los complementos en 2023.
- **Mucuna:** contiene levodopa.
- **Canela cassia:** cumarina. La ingesta tolerable es 0,1 mg/kg al día.
- **Cúrcuma con pimienta negra:** daño hepático con suplementos de mayor absorción.
- **Reishi en polvo:** casos de hepatitis.

Las afirmaciones sin respaldo más claras son la «fatiga suprarrenal» y la B12 de la ashitaba.

El grafo describe el libro: `formula` y `summary` dicen lo que dice la autora, y la evidencia va solo en `caution`. Cuando cites una afirmación de salud del libro, da también su veredicto.

## Cómo responder sobre salud

1. Si la pregunta es de eficacia o seguridad, lee la alerta y la ficha de `verif_A.md` o `verif_B.md`, y cita sus fuentes.
2. Si la pregunta va más allá de la alerta, o si han pasado varios meses desde la verificación, busca en PubMed con la skill `biotech-research` y di la fecha de la búsqueda.
3. Para preparar un latte o un tónico casero con estos polvos, usa también `healing-herbal-infusions`. Su carpeta `evidencia/` trae revisiones de goji, jujube e higo seco, limonaria y bebidas con evidencia.
4. Para la técnica (espumas, emulsiones, texturas), usa `gastronomia-molecular`. Para combinar aromas, usa `foodpairing` u `odorantes-clave`.

## Alcance y límites

- El EPUB no tiene páginas ni numera las secciones. La numeración `capítulo.orden` es propia del grafo. Solo las recetas llevan la página impresa, tomada de las referencias cruzadas del libro.
- Los polvos se agruparon por tipo; el libro los presenta en orden alfabético.
- Cada receta del grafo dice para qué la propone el libro y qué polvos usa, pero no trae las cantidades. Para prepararla, consulta el libro.
- Las alertas resumen la evidencia publicada. No sustituyen la valoración clínica, sobre todo en embarazo, lactancia, enfermedad hepática o tiroidea, y en personas que toman anticoagulantes, antidiabéticos, levodopa o inmunosupresores.
