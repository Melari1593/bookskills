---
name: nutraceuticos
description: Nutracéuticos para consulta clínica con recetas de gastronomía molecular dosificadas en gramos y evidencia de PubMed con DOI. Cubre curcumina, omega-3, probióticos, moringa, camu camu, aguaje, guayaba, zapote, mango, guanábana, cacao, espirulina, açaí, brócoli, cordyceps, melena de león, especias y semillas de calabaza, con seguridad e interacciones, más los grafos de los libros Flavonoids as Nutraceuticals (2024) , Applications of Functional Foods and Nutraceuticals for Chronic Diseases, Vol. I (2023) y Nutraceuticals for Prenatal, Maternal and Offspring's Nutritional Health. Úsala cuando pregunten por un nutracéutico, un alimento funcional amazónico, un flavonoide, el uso de alimentos funcionales en una enfermedad crónica o nutracéuticos en el embarazo, el posparto o la descendencia, pidan una receta con dosis o quieran saber qué evidencia y qué riesgos tiene, aunque no digan "nutracéutico".
---

<!-- argument-hint: [nutracéutico, alimento o flavonoide] -->

# Nutracéuticos: recetas dosificadas y evidencia

**Actualizada:** 2026-11-23 · **Uso:** consulta clínica de Espacio Clínico · Dra. Karla.

Esta skill tiene cuatro partes:

| Parte | Archivo | Contenido |
|---|---|---|
| Recetas y evidencia | `references/recetas-evidencia.md` | 25 preparaciones con gramos, proceso, fallas, evidencia por nivel de confianza, seguridad y log de búsqueda |
| Grafo del libro | `references/grafo_flavonoids.json`, `assets/grafo_flavonoids_as_nutraceuticals.html`, `scripts/ruta.py` | *Flavonoids as Nutraceuticals* (Kesharwani et al., Apple Academic Press, 2024): 13 capítulos, 184 secciones, 43 conceptos, 84 prerrequisitos |
| Grafo del libro | `references/grafo_functional_foods.json`, `assets/grafo_functional_foods_chronic_diseases.html`, `scripts/ruta.py --grafo cronicas` | *Applications of Functional Foods and Nutraceuticals for Chronic Diseases, Vol. I* (Mohan, Abdollahi y Pathak, eds., CRC Press, 2023): 15 capítulos, 189 secciones, 50 conceptos, 67 prerrequisitos |
| Grafo del libro | `references/grafo_prenatal.json`, `assets/grafo_nutraceuticos_prenatal_materno.html`, `scripts/ruta.py --grafo prenatal` | *Nutraceuticals for Prenatal, Maternal and Offspring's Nutritional Health* (Bhatt, Miraghajani, Pathak y otros, eds., CRC Press): 19 capítulos, 195 secciones, 56 conceptos, 71 prerrequisitos |

Responde en español. Usa frases cortas, una instrucción por frase y la condición primero.

## Qué hay en `recetas-evidencia.md`

| Sección | Compuesto | Técnica | Punto crítico de seguridad |
|---|---|---|---|
| 1 | Curcumina | Emulsión excipiente caliente con pimienta | Hepatotoxicidad rara; piperina inhibe CYP3A4 y P-gp |
| 2 | Omega-3 | Gel de emulsión con gelatina | Fibrilación auricular con más de 1 g/día |
| 3 | Probióticos | Esferificación inversa de yogur o kéfir | No usar en inmunosupresión ni con catéter venoso central |
| 4 | Moringa | Suspensión con xantana | Evidencia muy baja |
| 5 | Camu camu (pulpa) | Esferificación inversa en frío | Vitamina C del lote no confirmada |
| 6 | Aguaje (pulpa) | Microemulsión con aceite y proteína de suero | β-caroteno concentrado en fumadores |
| 7 | Guayaba | Espuma fría en sifón | N₂O solo para alimentos |
| 8 | Zapote (*Quararibea cordata*) | Esferificación directa (pH 6,5–7) | Sin ensayos en humanos |
| 9 | Mango | Gel firme de agar | Azúcares en diabetes |
| 10 | Guanábana | Aire de lecitina, baja exposición | Annonacina: no recomendada; semillas sin uso seguro |
| 11 | Cacao | Bebida fría suspendida | Cadmio y plomo del lote |
| 12 | Espirulina | Esferificación directa en frío | Microcistinas; no es fuente de B12 |
| 13 | Camu camu liofilizado | Shot frío de 1,5 g | Polvo higroscópico |
| 14 | Aguaje liofilizado | Polvo de grasa con maltodextrina | Sin dato de estabilidad casera |
| 15 | Açaí | Crema fría y plato combinado | Chagas oral: solo pulpa pasteurizada |
| 16 | Brócoli (sulforafano) | Crema tibia al vapor con mostaza parda añadida en frío | Alergia a mostaza; brotes crudos en inmunosupresión |
| 17 | Cordyceps con cacao | Bebida fría de cacao suspendida con xantana | Arsénico en *O. sinensis* silvestre; inmunosupresores y trasplante |
| 18 | Melena de león | Cubos de caldo gelificado con agar | Alergia a hongos; micelio sobre cereal (gluten) |
| 19 | Especias (jengibre, cardamomo, canela de Ceilán) | Leche tibia especiada suspendida con xantana | Jengibre con warfarina; cumarina de la cassia |
| 20 | Embarazo: hierro, calcio y folato | Salsa fría de guayaba sobre lentejas; panna cotta láctea; salsa verde cruda | No reemplaza ácido fólico ni hierro; lácteos pasteurizados (Listeria) |
| 21 | Bisglicinato ferroso | Shot frío de guayaba, una dosis por vaso | Intoxicación infantil: no hacer golosinas; dosis en mg de hierro elemental |
| 22 | Bisglicinato ferroso en brownie | Lote de 9 piezas: dilución geométrica en la harina, corte por peso, salsa fría de guayaba | El cacao reduce la absorción; cada pieza rotulada como medicamento, congelada y bajo llave; solo adultos, una al día |
| 23 | Semillas de calabaza | Tostado suave con mejorana a 110 °C; vinagreta fría con xantana 0,25 % | Alergia con anafilaxia frecuente; brote de *Salmonella* 2026; no calentar el aceite |
| 24 | Arepa de maíz integral con bisglicinato ferroso | Dilución geométrica, ácido láctico 6 mg/g de maíz, bolas pesadas; nivel A 3 mg o nivel B 25 mg por arepa | Nivel B con reglas de la sección 22; sin queso ni bebidas calientes; no en sobrecarga de hierro |
| 25 | Arepa con ácido fólico | Tabletas de 0,4 o 1 mg trituradas, dilución geométrica, bolas pesadas; 400 µg por arepa | Dosis alta solo en tableta; no duplicar con prenatal; descartar déficit de B12 |

Las secciones 26 y 27 traen la tabla de seguridad por situación del paciente, los datos no confirmados y el log de búsqueda de PubMed.

**Especias.** El perfil aromático, la evidencia de salud y la seguridad de 12 especias están en el documento [Especias: odorantes clave, salud y seguridad](https://claude.ai/artifact/4CDxKYH1jZVe7VdBJ5gYms). Sus odorantes están en `odorantes-db` (lote 12); consúltalos con `python3 odorantes-db/scripts/consulta.py jengibre cardamomo`.

**Complemento en el repositorio.** `grafos/monografias-ingredientes/` tiene monografías con alertas de evidencia de guanábana, guayaba, açaí y asaí, camu camu y aguaje. Si una pregunta va más allá de la receta (composición, usos tradicionales, afirmaciones contradichas), consúltalas.

## Cómo responder

1. **Si el compuesto está en el documento:** lee su sección completa antes de dar cifras. Copia gramos, porcentajes y citas tal como están. No des concentraciones de memoria.
2. **Si piden la receta:** entrega objetivo, tabla de ingredientes, proceso numerado, "por qué funciona", tabla de fallas y seguridad.
3. **Si piden evidencia:** separa los niveles de confianza (alta, moderada, baja, preclínica). Cita con enlace DOI. Marca *(interpretación)* lo que no viene de una fuente.
4. **Si la pregunta es clínica:** revisa primero la sección 26 (seguridad por situación del paciente). Di cuándo la receta da dosis de alimento y cuándo da dosis de ensayo.
5. **Si el compuesto no está en el documento:** sigue el método de abajo y ofrece agregarlo como sección nueva.

## Método para agregar un nutracéutico nuevo

1. Busca evidencia con la skill `biotech-research` (PubMed): metaanálisis o ensayos en humanos, biodisponibilidad, estabilidad (calor, pH, luz, oxígeno), toxicidad, contaminantes e interacciones. Registra cada query en el log.
2. Elige la técnica con la skill `gastronomia-molecular`. La técnica debe resolver el problema del compuesto: solubilidad, oxidación, supervivencia, sedimentación o degradación. Lee `hidrocoloides.md` y `tecnicas.md` antes de dar dosis.
3. Calcula en gramos: `g de agente = % × g de líquido / 100`. Verifica que los porcentajes sumen y que la porción tenga una cantidad conocida del compuesto.
4. Escribe la sección con el mismo formato del documento y añade una fila al resumen, a la seguridad y al log.
5. Si una cifra no está en las fuentes, dilo. No la inventes.

## Grafo de *Flavonoids as Nutraceuticals*

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py "término"`. Acepta un número de sección (`python scripts/ruta.py 8.15`) o el id de un concepto (`python scripts/ruta.py nfkb`).
2. Lee los resúmenes de los nodos en `references/grafo_flavonoids.json` antes de explicar una relación. Un arco `A → B` significa que B es antecedente de A. Los arcos son una interpretación pedagógica.
3. Para el mapa visual, entrega una copia de `assets/grafo_flavonoids_as_nutraceuticals.html`: tres vistas (capítulos, conceptos, completa), buscador, leyenda por bloque y "Trazar prerrequisitos".
4. Bloques: química y biosíntesis (cap. 2, 12); plantas y agricultura (3); nutracéuticos y salud humana (1, 5, 9, 11); inflamación e inmunidad (6, 7, 8); antivirales y COVID-19 (4, 13); tintes naturales (10).

**Advertencias del libro.** Es una obra colectiva. La mayor parte de la evidencia es in vitro, animal o in silico; el capítulo 4 reconoce que muy pocos flavonoides llegaron a ensayos clínicos. El capítulo 1 tiene redacción irregular. Para una conducta clínica, usa el documento de recetas y evidencia, no el libro.

## Grafo de *Functional Foods and Nutraceuticals for Chronic Diseases*, Vol. I

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py --grafo cronicas "término"`. Acepta un número de sección (`9.9`) o el id de un concepto (`esteroles`).
2. Lee los resúmenes de los nodos en `references/grafo_functional_foods.json` antes de explicar una relación. Los arcos son una interpretación pedagógica.
3. Para el mapa visual, entrega una copia de `assets/grafo_functional_foods_chronic_diseases.html`.
4. Bloques: carga e integración de las ECNT (cap. 1, 2); bases de seguridad, eficacia, regulación y vitamina D (3, 4); metabolismo, endocrino y cardiovascular (6, 7, 8, 9); vegetales y aceites de semilla (5, 10); órganos y sistemas: salud oral, urogenital, respiratorio y artritis (11–14); Alzheimer y polifenoles (15).
5. El capítulo 3 es la base de los demás: definiciones, toxicología, esteroles (eficacia máxima ≈ 1,6 g/día) y marco regulatorio.

**Advertencias del libro.** El libro no numera las secciones: la numeración `capítulo.orden` es propia del grafo. Las páginas son las impresas de cada índice de capítulo. El capítulo 11 no tiene encabezados propios; el grafo agrupa sus secciones por enfermedad. Varios capítulos revisan evidencia preclínica o estudios pequeños (por ejemplo, magnesio en dismenorrea). Para una conducta clínica, usa el documento de recetas y evidencia, no el libro.

## Grafo de *Nutraceuticals for Prenatal, Maternal and Offspring's Nutritional Health*

1. Para buscar un tema y sus antecedentes, ejecuta `python scripts/ruta.py --grafo prenatal "término"`. Acepta un número de sección (`10.3`) o el id de un concepto (`anemia_hb`).
2. Lee los resúmenes de los nodos en `references/grafo_prenatal.json` antes de explicar una relación. Los arcos son una interpretación pedagógica.
3. Para el mapa visual, entrega una copia de `assets/grafo_nutraceuticos_prenatal_materno.html`.
4. Bloques: bases y periconcepción (cap. 1–4); complicaciones maternas: ganancia de peso, aborto, preeclampsia, diabetes gestacional (5, 6, 10, 11); anemia, infección y hormonas (7, 8, 9); salud mental y posparto (12, 13); resultados fetales y de la descendencia: útero, hueso, dientes, piel y alergia, enfermedad crónica, respiración (14–19).
5. Para preguntas de embarazo, cruza con la skill `manual-obstetricia-ginecologia` y con la tabla de seguridad del documento de recetas.

**Advertencias del libro.** El libro numera solo algunas secciones: la numeración `capítulo.orden` es propia del grafo. El capítulo 7 no tiene subtítulos; el grafo lo divide por tema. Las dosis (hierro 27 mg/día, ácido fólico 600 µg/día, calcio ≥ 1 g/día en preeclampsia) vienen de las tablas del libro y no están verificadas en PubMed. Conceptos con alerta: exceso de vitamina A; cohosh azul, ginseng y mwanamphepo (hierbas para inducir el parto o sin seguridad establecida); la afirmación del capítulo 6 sobre clorofila y "guanidina" no tiene evidencia establecida.

## Alcance y límites

- No reemplaza un tratamiento indicado. Las recetas dan dosis de alimento salvo donde se indica.
- En menores de 1 año no apliques las dosis de hidrocoloides.
- Embarazo: no está buscado para la mayoría de compuestos; trátalo como no confirmado.
- Producto comercial: consulta INVIMA (Resolución 2606 de 2009 sigue vigente para aditivos).
- La versión viva del documento está en Claude Docs: "Nutracéuticos con gastronomía molecular: recetas y evidencia". Si cambia, vuelve a exportarla a `references/recetas-evidencia.md`.
