# Lichi y mamoncillo — maridaje y técnica molecular

Generado: 2026-11-16 · Skills aplicadas: `odorantes-clave` (base `odorantes-db`, lote 10), `foodpairing`, `gastronomia-molecular` (`references/hidrocoloides.md`), `biotech-research`.
Relación con el libro: el capítulo 9 usa lichi (Lychee Harmony, ensalada tropical) y rambután. El mamoncillo (*Melicoccus bijugatus*, Sapindaceae) no está en el libro; se añade por ser de la misma familia y común en Colombia.

## 1. Seguridad primero (ver `evidence.md` S7)

- Según PubMed, el **arilo** de lichi, longan y mamoncillo contiene hipoglicina A (HGA) y MCPG ([Isenberg 2016](https://doi.org/10.1021/acs.jafc.6b02478)). Las **semillas** también: primera cuantificación de HGA en semilla de lichi y de ambas toxinas en semilla de mamoncillo y longan ([Sanford 2018](https://doi.org/10.1016/j.foodchem.2018.04.093)).
- El contenido cambia con el cultivar y el almacenamiento ([Yang 2020](https://doi.org/10.1016/j.foodchem.2020.127013)).
- No se encontró evidencia de que el calor destruya estas toxinas.

Reglas para cualquier receta de este archivo:
1. Use solo fruta madura y fresca. Descarte fruta verde o caída.
2. No use la semilla en ninguna forma (cruda, tostada, molida, infusión).
3. Sirva porciones de postre. Sirva con una comida.
4. Si el comensal es un niño, no sirva cantidades grandes en ayunas.

## 2. Aroma (evidencia, `odorantes-db`)

| Odorante | Olor | Evidencia en lichi | Nivel |
|---|---|---|---|
| Metional | papa cocida | FD 1024 ([Feng 2017](https://doi.org/10.1016/j.jfda.2017.07.013)) | C |
| Geraniol | floral dulce | FD 512 (Feng 2017); OAV 764 en jugo ([Wang 2023](https://doi.org/10.1016/j.crfs.2023.100481)) | C |
| Linalol | floral | OAV 7504 en jugo (Wang 2023) | C |
| Óxido de rosa | floral, "lichi" | OAV 4265 en jugo (Wang 2023); presente en 3 cultivares ([Mahattanatawee 2007](https://doi.org/10.1021/jf062925p)) | C |
| Furaneol | caramelo | Feng 2017 | C |
| Trisulfuro de dimetilo | azufrado | Feng 2017; Mahattanatawee 2007 | C |

Nota de apoyo: en la uva Muscaris, la nota "a lichi" se reprodujo con óxido de rosa + geraniol en pruebas de recombinación y omisión ([Wang 2024](https://doi.org/10.1021/acs.jafc.3c08298)). Es evidencia nivel A del par, pero en uva, no en lichi.

**Dato técnico:** la pasteurización del jugo de lichi bajó los alcoholes un 28,5 %, sobre todo geraniol y citronelol (Wang 2023). Regla: **trabaje el lichi en frío.**

**Mamoncillo:** no se encontraron estudios de odorantes clave en PubMed (query del 16/11/2026, 71 resultados, ninguno de aroma). Todo maridaje del mamoncillo es interpretación por sabor (dulce y ácido).

## 3. Maridaje

| Pareja | Puente | Tipo | Fuente |
|---|---|---|---|
| Lichi + frambuesa | 6 odorantes compartidos: geraniol, linalol, β-ionona, β-damascenona, furaneol, metional | Overtoning floral-frutal | `consulta.py lichi frambuesa` |
| Lichi + té negro | 8 compartidos (incl. geraniol, linalol, 2-feniletanol) | Overtoning floral | `consulta.py lichi` |
| Lichi + fresa | 5 compartidos | Overtoning frutal | `consulta.py lichi` |
| Lichi + naranja | geraniol, linalol | Puente cítrico-floral | `consulta.py lichi` |
| Lichi + rosa, jengibre, coco | Rosa: no verificado en la base. Jengibre y coco: contraste (pungencia, grasa) | Interpretación | — |
| Mamoncillo + sal + ají + lima | Contraste de sabor (salado, picante, ácido) | Interpretación | — |

## 4. Recetas

### 4.1 Gelatina de lichi en frío

Objetivo: gel suave que se funde en boca, sin calentar el jugo por encima de 50 °C, para conservar geraniol y linalol.

| Ingrediente | % | g |
|---|---|---|
| Jugo de lichi (pulpa licuada y colada) | — | 400 |
| Gelatina | 1,2 | 4,8 |

Proceso:
1. Hidrate la gelatina en agua fría 5 min. Escúrrala.
2. Caliente 50 g del jugo a ~50 °C. Disuelva la gelatina en él.
3. Mezcle con los 350 g de jugo restante, a temperatura ambiente.
4. Vierta en moldes. Cuaje por debajo de 15 °C durante varias horas.

Por qué funciona: la gelatina forma hélices de colágeno al enfriarse y funde a 25–40 °C, cerca de la temperatura de la boca. No hay que hervir, a diferencia del agar (> 90 °C), y así el jugo no pierde sus alcoholes terpénicos.

Si falla: no cuaja → poca gelatina o mezcla aún tibia; espere más horas en frío o suba a 1,5 %.

Montaje sugerido (foodpairing): gelatina de lichi + coulis de frambuesa crudo + crumble de mantequilla. Dos sabores básicos (dulce, ácido), una textura blanda y una crocante, tres componentes.

### 4.2 Perlas de mamoncillo (esferificación inversa)

Objetivo: esferas con centro líquido de un jugo ácido.

| Ingrediente | % | g |
|---|---|---|
| Jugo de mamoncillo | — | 200 |
| Lactato de calcio | 2,4 | 4,8 |
| Goma xantana (opcional, cuerpo) | 0,3 | 0,6 |
| Baño: agua | — | 1000 |
| Baño: alginato de sodio | 0,5 | 5 |

Proceso:
1. El día anterior, licúe el alginato en el agua. Refrigere para que salga el aire.
2. Extraiga la pulpa: pele la fruta, remójela en poca agua, frote la pulpa y cuele. **No rompa ni muela la semilla.**
3. Disuelva el lactato de calcio (y la xantana, si la usa) en el jugo.
4. Deje caer cucharadas del jugo en el baño. Espere 2–3 min.
5. Enjuague las esferas en agua limpia. Sirva en el momento.

Por qué la inversa: el jugo es ácido (sin pH medido). La esferificación directa necesita pH ≥ 3,65. En la inversa, el calcio va en el jugo y el gel se forma afuera, en contacto con el alginato.

Si falla: la esfera se deshace → poco tiempo en el baño o baño con aire; la esfera sigue engrosando → enjuague mejor.

Montaje sugerido: perlas de mamoncillo sobre hielo raspado con sal de mar, ají en polvo y ralladura de lima.

## 5. Huecos

- Sin estudios de aroma del mamoncillo.
- Sin pH medido del jugo de mamoncillo ni de lichi.
- Sin umbral de porción segura para HGA o MCPG.
- Sin datos sobre la estabilidad de las toxinas al calor.

## 6. Log de búsqueda

| Fuente | Fecha | Query | Resultados |
|---|---|---|---|
| PubMed | 2026-11-16 | (litchi OR lychee) AND ("key odorants" OR "aroma extract dilution" OR "odor activity value" OR olfactometry) | 6; usados PMID 29567218, 17266328, 37033736, 38216146 |
| PubMed | 2026-11-16 | Melicoccus bijugatus OR mamoncillo OR "Spanish lime" OR quenepa | 71; ninguno de aroma |
| PubMed | 2026-11-16 | (Melicoccus OR mamoncillo OR longan OR rambutan) AND hypoglycin | 61; usado PMID 29853400 |
| PubMed | 2026-11-16 | litchi AND (hypoglycin OR methylenecyclopropylglycine) AND encephalopathy | 14; usados PMID 27367968, 32454275 |
| odorantes-db | 2026-11-16 | `consulta.py lichi`; `consulta.py lichi frambuesa` | 13 odorantes; 6 compartidos con frambuesa |
