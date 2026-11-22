---
name: nutraceuticos
description: Nutracéuticos para consulta clínica con recetas de gastronomía molecular dosificadas en gramos y evidencia de PubMed con DOI. Cubre curcumina, omega-3, probióticos, moringa, camu camu, aguaje, guayaba, zapote, mango, guanábana, cacao, espirulina y açaí, con seguridad e interacciones, más el grafo del libro Flavonoids as Nutraceuticals (2024). Úsala cuando pregunten por un nutracéutico, un alimento funcional amazónico o un flavonoide, pidan una receta con dosis o quieran saber qué evidencia y qué riesgos tiene, aunque no digan "nutracéutico".
---

<!-- argument-hint: [nutracéutico, alimento o flavonoide] -->

# Nutracéuticos: recetas dosificadas y evidencia

**Actualizada:** 2026-11-22 · **Uso:** consulta clínica de Espacio Clínico · Dra. Karla.

Esta skill tiene dos partes:

| Parte | Archivo | Contenido |
|---|---|---|
| Recetas y evidencia | `references/recetas-evidencia.md` | 15 preparaciones con gramos, proceso, fallas, evidencia por nivel de confianza, seguridad y log de búsqueda |
| Grafo del libro | `references/grafo_flavonoids.json`, `assets/grafo_flavonoids_as_nutraceuticals.html`, `scripts/ruta.py` | *Flavonoids as Nutraceuticals* (Kesharwani et al., Apple Academic Press, 2024): 13 capítulos, 184 secciones, 43 conceptos, 84 prerrequisitos |

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

Las secciones 16 y 17 traen la tabla de seguridad por situación del paciente, los datos no confirmados y el log de búsqueda de PubMed.

**Complemento en el repositorio.** `grafos/monografias-ingredientes/` tiene monografías con alertas de evidencia de guanábana, guayaba, açaí y asaí, camu camu y aguaje. Si una pregunta va más allá de la receta (composición, usos tradicionales, afirmaciones contradichas), consúltalas.

## Cómo responder

1. **Si el compuesto está en el documento:** lee su sección completa antes de dar cifras. Copia gramos, porcentajes y citas tal como están. No des concentraciones de memoria.
2. **Si piden la receta:** entrega objetivo, tabla de ingredientes, proceso numerado, "por qué funciona", tabla de fallas y seguridad.
3. **Si piden evidencia:** separa los niveles de confianza (alta, moderada, baja, preclínica). Cita con enlace DOI. Marca *(interpretación)* lo que no viene de una fuente.
4. **Si la pregunta es clínica:** revisa primero la sección 16 (seguridad por situación del paciente). Di cuándo la receta da dosis de alimento y cuándo da dosis de ensayo.
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

## Alcance y límites

- No reemplaza un tratamiento indicado. Las recetas dan dosis de alimento salvo donde se indica.
- En menores de 1 año no apliques las dosis de hidrocoloides.
- Embarazo: no está buscado para la mayoría de compuestos; trátalo como no confirmado.
- Producto comercial: consulta INVIMA (Resolución 2606 de 2009 sigue vigente para aditivos).
- La versión viva del documento está en Claude Docs: "Nutracéuticos con gastronomía molecular: recetas y evidencia". Si cambia, vuelve a exportarla a `references/recetas-evidencia.md`.
