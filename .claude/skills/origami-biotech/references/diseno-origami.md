# Diseño de origami — conceptos

Cada punto lleva una etiqueta de origen:
- `[verificado]`: viene de una descripción de video de la playlist (ver `lecciones-playlist.md`).
- `[curso MIT]`: viene de materiales públicos del curso MIT 6.849 (Geometric Folding Algorithms). No es el contenido de la playlist.
- `[general]`: conocimiento general de origami. No atribuyas esto al canal.
- `[externo]`: viene de una fuente pública fuera de la playlist y del curso MIT. Cita siempre la fuente.

## Tabla de contenido
1. Boxpleating
2. Packing
3. Método del árbol
4. Glosario mínimo
5. Lo que falta por verificar
6. Referencia externa: Inkjet 4D Print (autoplegado de teselados)
7. Tipos y técnicas de origami
8. Kirigami
9. Teselaciones
10. Origami rígido con espesor

## 1. Boxpleating

- Método de diseño muy usado. Permite modelos de complejidad teóricamente infinita. `[verificado]` (lección 4.1)
- Se contrasta con el método de bases tradicionales. `[verificado]` (lección 4.1)
- Se caracteriza por pliegues solo en múltiplos de 45°. `[curso MIT]` (diapositivas L05 del curso)
- La playlist dedica una serie larga al tema. `[verificado]` (lección 4.1)

## 2. Packing

- El packing convierte el árbol deseado en un patrón de pliegues. `[verificado]` (lección 4.2)
- Cada apéndice de la figura necesita una porción de papel. En el método de círculos, esa porción es un círculo. `[curso MIT]`
- El *circle/river packing* se describe como una asignación de espacio sobre el papel. `[curso MIT]`

## 3. Método del árbol

- El curso MIT 6.849 presenta el método del árbol como un algoritmo de diseño. Relaciona un árbol, un empaquetado de círculos y ríos, y el lugar posible de los pliegues de bisagra en una base uniaxial. `[curso MIT]`
- La lección 4.2 de la playlist usa la palabra "árbol". Confirma con la transcripción si usa la misma convención. `[por verificar]`

## 4. Glosario mínimo

| Término | Definición | Origen |
|---|---|---|
| Boxpleating (Bp) | Método de diseño con pliegues en múltiplos de 45° | `[curso MIT]` |
| Crease pattern (CP) | Mapa de todos los pliegues del papel desplegado | `[general]` |
| Packing | Paso que convierte el árbol en un crease pattern | `[verificado]` |
| Base uniaxial | Base cuyos apéndices salen en un solo eje | `[curso MIT]` |

## 5. Lo que falta por verificar

- Procedimiento paso a paso del packing de la lección 4.2.
- Criterios numéricos (por ejemplo, tamaños de cuadrícula) usados en las lecciones.
- Contenido de las otras 18 lecciones.

Referencia externa mencionada: Robert J. Lang, *Origami Design Secrets* (2.ª ed.). La edición incluye capítulos de boxpleating, boxpleating uniaxial y empaquetado de polígonos. `[general]`

## 6. Referencia externa: Inkjet 4D Print (autoplegado de teselados)

Fuente: Narumi K, Koyama K, Suto K, Noma Y, Sato H, Tachi T, Sugimoto M, Igarashi T, Kawahara Y. *Inkjet 4D Print*. ACM Transactions on Graphics 42(4), agosto de 2023 (SIGGRAPH 2023). DOI: [10.1145/3592409](https://doi.org/10.1145/3592409). Página del proyecto: https://narumi.me/inkjet4dprint (consultada el 2026-11-16). Solo se leyó la página del proyecto, no el artículo.

Qué describe la página `[externo]`:
- Método para fabricar teselados de origami 3D que se pliegan solos.
- Se imprimen patrones 2D en ambas caras de una lámina base termorretráctil con una impresora UV de inyección de tinta comercial.
- El plegado ocurre al calentar la lámina.
- El método cubre teselados conocidos y de forma libre.
- Los autores declaran más de 1200 veces más caras autoplegables que el 4D printing basado en plegado con impresoras FDM (Thermorph, CHI 2018).
- Los autores declaran una velocidad de impresión 2,8 veces mayor.
- La decoración a todo color es opcional.

Qué NO aparece en la página (no lo afirmes):
- Valores de las condiciones de calentamiento.
- La composición comercial de la lámina.
- Las cifras de las evaluaciones de resolución, velocidad y precisión de forma.
- Las aplicaciones concretas y las limitaciones.

Cuándo usar esta referencia:
- Cuando el usuario pregunte por teselados, autoplegado o fabricación de origami con impresión.
- No la uses como evidencia biomédica. Es un trabajo de fabricación e interacción persona-computador. No está indexado en la búsqueda de PubMed de `biotech-literatura.md`.

## 7. Tipos y técnicas de origami

Fuente: Origami Resource Center, https://origami-resource-center.com/types-of-origami (consultada el 2026-11-16) `[externo]`. La página nombra los tipos. No los define. No afirmes una definición de un tipo sin otra fuente.

Tipos principales, como los nombra la página:
- Action Origami (acción)
- Business Card (tarjeta de presentación)
- Candy Wrapper (envoltorio de caramelo)
- Crease Pattern (patrón de pliegues)
- Dollar Bill (billete)
- GVF (Golden Venture Folding)
- Modular Origami (modular)
- Tessellations (teselaciones)
- Palm Weaving (tejido de palma)
- Pure & Pureland
- Origami Quilts (colchas)
- Strip Folding (plegado en tiras)
- Toilet Paper (papel higiénico)
- Wet Folding (plegado en húmedo)

Sección "Origami Fringe" de la misma página (técnicas afines al papel): Tea Bag Folding, Fabric Folding, Quilling, Kirigami, Origamic Architecture, Iris Folding.

Definiciones con otra fuente:
- Origami modular: formas geométricas hechas con varias unidades repetidas. `[curso MIT]` (descripción de la clase 5)
- Teselaciones: plegado en un patrón que se repite. `[curso MIT]` (descripción de la clase 5)
- Plegado en húmedo: se humedece el papel para darle forma curva. `[general]`
- Boxpleating: ver la sección 1. La página no lo menciona.

## 8. Kirigami

- Origen de la palabra: "ori" es plegar, "kiru" es cortar y "kami" es papel. `[PubMed]` (Blees et al. 2015, [DOI](https://doi.org/10.1038/nature14588))
- Origami Resource Center lo lista como técnica afín al origami. `[externo]`
- Jin y Yang (2023) lo describen como un oficio tradicional de cortar y plegar. `[PubMed]` ([DOI](https://doi.org/10.1002/adma.202308560)) La diferencia con el origami no es absoluta.
- Nota de prensa de Harvard SEAS (24 feb 2017), https://seas.harvard.edu/news/new-pop-strategy-inspired-cuts-not-folds `[externo]`:
  - Define el kirigami como un arte japonés antiguo que usa cortes, y no pliegues, para cambiar la estructura y la función de un material.
  - El estudio parte de una lámina delgada perforada. Al estirarla lo suficiente, el pandeo forma una estructura 3D con crestas y valles, parecida al plegado Miura-ori.
  - Con más estiramiento, las deformaciones temporales se vuelven pliegues permanentes.
  - La orientación de los cortes controla el patrón de apertura y las propiedades mecánicas.
  - Autores: Ahmad Rafsanjani (primer autor) y Katia Bertoldi. Revista: *Physical Review Letters*.
  - Solo se leyó la nota de prensa, no el artículo.
- Para aplicaciones biomédicas del kirigami, usa `references/biotech-literatura.md`, sección 5.

## 9. Teselaciones

- Definición: plegado en un patrón que se repite. `[curso MIT]` (descripción de la clase 5)
- Definición de los abstracts: un patrón de pliegues con simetrías de traslación. Se usa para diseñar propiedades mecánicas de objetos. `[PubMed]` (Chaos 2023, PMID 38060800, [DOI](https://doi.org/10.1063/5.0160803))
- Ejemplo: "Miura ori" se describe como una teselación de origami. `[PubMed]` (Phys Rev Lett 2024, PMID 38518354, [DOI](https://doi.org/10.1103/PhysRevLett.132.108201))
- Origami Resource Center las lista como tipo de origami (sección 7). `[externo]`
- Autoplegado de teselados con impresión de inyección de tinta: ver la sección 6 (Inkjet 4D Print). `[externo]`
- Teselaciones en el sentido de mosaicos (teselados platónicos, de Laves y arquimedianos) aparecen en origami de ADN. Es otro uso de la palabra: aquí las teselas se ensamblan en un plano. `[PubMed]` (Tang 2023, [DOI](https://doi.org/10.1021/jacs.3c03044)). Detalles en `references/biotech-literatura.md`, sección 6.
- Qué no está verificado: los pasos para diseñar una teselación (por ejemplo, el cálculo del patrón de pliegues de un Miura-ori). La playlist no está verificada para este tema. No los inventes. `[por verificar]`

## 10. Origami rígido con espesor

Fuente: Chen Y, Peng R, You Z. *Origami of thick panels*. *Science* 349(6246):396-400, 2015. PMID 26206928. DOI [10.1126/science.aab2870](https://doi.org/10.1126/science.aab2870). `[PubMed]` Consultado el 2026-11-18. Se leyó el texto completo del artículo (pp. 396-399 y la lista de referencias), en el PDF que aportó la usuaria. No se leyó el material suplementario (figuras S1 a S14, película S1), donde están las demostraciones.

Qué dice el abstract:
- Los patrones de origami, incluido el origami rígido (láminas planas e inflexibles unidas por pliegues), se crean sobre todo para láminas de espesor cero.
- Para aplicarlos a techos, paneles solares y espejos espaciales hay que considerar el espesor. Los métodos previos suelen añadir material o desplazar los paneles, sin cambiar el modelo cinemático.
- Los autores desarrollan una síntesis cinemática para origami rígido de paneles gruesos. Su modelo difiere del existente y puede reproducir movimientos idénticos a los del origami de espesor cero.
- Los autores indican que el método funciona con origami típico y puede aplicarse a estructuras de ingeniería reales.

Cómo usar esta referencia:
- Úsala cuando el usuario pregunte por papel con espesor, origami rígido o estructuras desplegables de ingeniería.
- No es biomédico. El abstract no menciona dispositivos médicos. La relación con stents o dispositivos plegables es una analogía de diseño `[general]`: un material con espesor real no se pliega como una lámina ideal.
- Qué no aparece en el artículo (no lo afirmes): aplicaciones biomédicas, materiales y espesores concretos de los modelos, y cifras de rendimiento. El artículo no trata esos temas en el texto principal.

Qué dice el texto completo `[PubMed]` (pp. 396-399):
- Supuesto: el panel grueso tiene espesor distinto de cero. Las líneas de pliegue solo van en las caras del panel, no en su profundidad.
- Problema: en el origami rígido de espesor cero, cada vértice se modela como un eslabonamiento esférico. Con espesor, los pliegues ya no se cruzan en un punto. Unos quedan en la cara superior y otros en la inferior.
- Dos condiciones de plegabilidad: cada lazo de cuerpos rígidos debe ser un eslabonamiento mecánico, y el conjunto debe conservar movilidad.
- Método: se busca un eslabonamiento espacial cinemáticamente equivalente al esférico y se demuestra que tienen el mismo movimiento. En patrones con varios vértices, se unen las líneas de pliegue compartidas. Esto es posible por la simetría de rotación del patrón (por ejemplo, la torsión cuadrada).

Equivalencias que presentan los autores (el número de ecuación es el del artículo):
- Cuatro pliegues → eslabonamiento de Bennett (4R). Los ángulos de sector cumplen α12 + α34 = α23 + α41 = π (Ec. 2), que es la condición de plegado plano de espesor cero. Además α12 = α34 y α23 = α41 (Ec. 3). Las distancias cumplen a12/a23 = sen α12 / sen α23 (Ec. 4). Modelos: torsión cuadrada y Miura-ori (Hoberman ya había publicado el caso simétrico).
- Cinco pliegues → eslabonamiento de Myard (5R). Condiciones: a12 = a51, a23 = a45, a34 = 0 (Ec. 6) y a12/a23 = sen α12 / sen α23 (Ec. 7). Modelo: patrón de caja (con ángulos de sector π/6, π/2, 2π/3, π/2 y π/6 en la Fig. 2).
- Seis pliegues → eslabonamiento de Bricard con simetría de plano (6R). Condiciones: a12 = a61, a23 = a56, a34 = a45 (Ec. 9) y a12 + a23 = a34 para plegado compacto (Ec. 10). Modelo: patrón de diamante.
- Waterbomb: el vértice W usa Bricard con a23 = a56, a34 = a45 = μ·a23 y a12 = a61 = (1 + μ)·a23 (Ec. 12). El vértice D es un caso especial del diamante. También muestran un patrón con vértices de cuatro y de seis pliegues a la vez.

Resultados que afirman los autores:
- En el caso de cuatro pliegues, solo los patrones plegables planos tienen equivalente de panel grueso. La razón: Bennett es el único eslabonamiento espacial 4R conocido.
- Con cinco y seis pliegues, el eslabonamiento esférico suele tener dos o tres grados de libertad y el espacial equivalente solo uno. La equivalencia exige reducir los grados de libertad, por ejemplo con simetría. Los autores dicen que esto puede ayudar en la práctica, porque el plegado se controla más fácil.
- Con μ ≠ 1 en el waterbomb, el movimiento difiere del esférico. El patrón sigue plegándose plano y puede expandirse plano. Los autores señalan que se puede diseñar el panel grueso con la teoría de mecanismos, sin partir del origami rígido de espesor cero.
- Los autores plegaron modelos físicos de torsión cuadrada, caja, diamante, waterbomb y un patrón mixto (Figs. 1 a 4).
- Los autores dicen que el número de eslabonamientos espaciales sobrerrestringidos es bastante limitado.