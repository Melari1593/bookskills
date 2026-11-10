# Fatiga: albahaca sagrada (tulsi), ortiga y paja de avena. Evidencia en humanos, aporte nutricional y seguridad

- **Fecha:** 2026-11-10
- **Contexto:** skill `healing-herbal-infusions` (Codekas 2018), capítulo 6 (`chapters/ch06-wellbeing.md`). Para la fatiga, la skill propone tres recetas: Sleep Well Tea (manzanilla, nébeda, valeriana), De-Stress Tea (albahaca sagrada o tulsi, pasiflora, salvia) e infusión larga de ortiga y paja de avena (4–12 h, fría, "nutritiva"). El capítulo no da cantidades en gramos. El formato sigue `evidencia/moringa.md`.
- **Pregunta:** ¿Qué evidencia en humanos tienen el tulsi, la ortiga y la paja de avena (y, de forma breve, la valeriana y la nébeda) para fatiga, energía, estrés, ansiedad, sueño y cognición? ¿Cuánto aporta de verdad una infusión "nutritiva"? ¿Qué riesgos omite el libro? ¿Se justifica una receta para fatiga?
- **Ya cubierto por la tabla "Seguridad clínica":** valeriana (ciclos), asteráceas (manzanilla), pasiflora, salvia y lactancia, taninos y hierro. No se repite.
- **Fuentes:** según PubMed (metadatos y resúmenes, con DOI); EMA/HMPC (monografías de *Urticae folium*, *Urticae herba*, *Urticae radix*, *Avenae herba* y páginas de estado de *Avenae fructus* y *Avenae herba*); MSD Manual Professional (Holy basil, revisión 07/2025); MSKCC About Herbs (Holy basil, actualizada 2026-09-21); American Family Physician 2023; The Edinburgh GP Handbook (resumen que cita NICE CKS); MedlinePlus y NIH ODS (ingestas de referencia); réplica secundaria de USDA (ortiga escaldada).
- **Fuentes bloqueadas:** LactMed (NCBI Bookshelf) mostró un reCAPTCHA. NICE CKS, MSKCC (primera URL), NIH ODS (hojas para profesionales de hierro, calcio y magnesio) y un adendo de EMA no estaban en la lista permitida. Se buscaron fuentes alternas (ver log). No se usó curl.
- **Escala de nivel de evidencia:** alta · moderada · baja · muy baja · sin evidencia en humanos.
- **Escala de veredicto:** respaldado · respaldado con matices · sin evidencia en humanos · contradicho · riesgo documentado · riesgo omitido.

---

## 1. Respuesta corta

1. Ninguna de estas plantas tiene un ensayo con la fatiga como desenlace principal. Primero hay que buscar la causa de la fatiga.
2. El tulsi tiene ensayos pequeños con **extractos en cápsulas**, no con té. En adultos con estrés, 250 mg/día de extracto durante 8 semanas bajaron el estrés percibido y el cortisol en cabello frente a placebo. El nivel de evidencia es **bajo**.
3. El único ensayo con **té** de tulsi (2 g de hoja por taza, 3 veces al día, 4 días) midió ansiedad en 44 pacientes con cáncer de tiroides. La ansiedad subió menos que con agua.
4. La avena verde (*Avenae herba*) tiene una monografía EMA de uso tradicional para "estrés mental leve" y "ayudar a dormir" (3 g por infusión). Los ensayos usan extractos y muestran efectos cognitivos agudos; con uso crónico, los resultados son mixtos. No hay datos de "energía".
5. La ortiga no tiene ensayos en fatiga, anemia ni sueño. Sus metaanálisis son en diabetes tipo 2: baja la glucemia en ayunas unos 17–18 mg/dl. Esto importa como **interacción**, no como beneficio para la fatiga.
6. La infusión "nutritiva" aporta poco. Solo el 4–12 % del hierro de la hierba pasa al agua. La media de los tés de hierbas es unos 18 µg de hierro por gramo de té. El potasio sí pasa bien (más del 55 %). La infusión no trata la anemia ni reemplaza un multivitamínico.
7. Riesgos que el libro omite: el tulsi puede bajar la T4, inhibir las plaquetas y afectar la fertilidad en animales. La EMA no recomienda la hoja de ortiga en embarazo, lactancia, menores de 12 años ni enfermedad cardiaca o renal grave, y la limita a 4 semanas. La avena pide precaución en celiaquía.
8. La evidencia **no justifica una receta para tratar la fatiga**. Sí permite una bebida de apoyo para estrés leve y sueño en adultos, con límites claros y después de descartar causas médicas (sección 8).

---

## 2. Primero, la causa

### 2.1 Causas de fatiga que se deben considerar

American Family Physician (Latimer 2023) agrupa las causas en estas categorías. La fatiga de 6 meses o más es crónica.

| Grupo | Ejemplos (según las fuentes) |
|---|---|
| Fisiológicas | Sueño insuficiente, exceso de ejercicio, hábitos de alimentación, embarazo, lactancia |
| Psiquiátricas y psicosociales | Depresión, ansiedad, duelo, estrés |
| Hematológicas | Anemia (incluye déficit de hierro, B12 o folato) |
| Endocrinas y metabólicas | Hipotiroidismo, diabetes |
| Infecciosas | Mononucleosis, VIH, hepatitis |
| Oncológicas | Cáncer |
| Cardiovasculares y pulmonares | Insuficiencia cardiaca, EPOC |
| Sueño | Apnea del sueño, insomnio |
| Gastrointestinales | Celiaquía (IgA y anticuerpos en el estudio inicial) |
| Reumatológicas y neurológicas | Enfermedades inflamatorias, esclerosis múltiple |
| Exposiciones | Fármacos, monóxido de carbono |

Fuentes: Latimer 2023 (AFP; PMID 37440739); The Edinburgh GP Handbook 2019 (resume NICE CKS "Tiredness/fatigue in adults"; NICE CKS no se pudo leer directamente).

### 2.2 Signos de alarma (consulta pronto)

Según el resumen de NICE CKS (Edinburgh GP Handbook):
- Pérdida de peso no intencional de unos 5 % en 6–12 meses.
- Adenopatía firme, no dolorosa, mayor de 2 cm, que crece, o supraclavicular o axilar.
- Hemoptisis, disfagia, sangrado rectal, nódulo mamario o sangrado posmenopáusico.
- Signos neurológicos focales.
- Sospecha de intoxicación por monóxido de carbono.

### 2.3 Estudio inicial

- Si la fatiga dura **1 mes o más**: hemograma, VSG o PCR, función hepática, urea y electrolitos, TSH, glucosa o HbA1c, e IgA (y serología de celiaquía según contexto) (Edinburgh GP Handbook, resumen de NICE CKS).
- AFP 2023 lista ferritina, hierro, folato y vitamina B12 entre las opciones. AFP 2023 advierte que el estudio sin indicación clínica rinde poco: guíalo por la historia y el examen.
- Si dura **3 meses o más**: añade uroanálisis, bioquímica ósea y CK (resumen de NICE CKS).
- AFP 2023 recomienda evaluar primero las causas fisiológicas (sueño, actividad, alimentación) (SORT C).

---

## 3. Tabla de evidencia en humanos

| Planta | Desenlace | Población | Preparado y dosis | Resultado (cifra) | Nivel | Veredicto | Fuente |
|---|---|---|---|---|---|---|---|
| Tulsi | Estrés percibido, sueño, cortisol | 100 adultos de 18–65 años con estrés (Australia) | Extracto estandarizado (Holixer) 125 mg 2 veces al día, 8 semanas, frente a placebo | Mejoró más la escala de estrés percibido (p = 0,003) y la escala de insomnio de Atenas (p = 0,025). Cortisol en cabello menor a la semana 8 (p = 0,025). Tras un estresor de laboratorio: cortisol salival menor (p = 0,001). Sin efectos adversos mayores. El resumen no da diferencias de medias ni IC. | baja (un ECA) | respaldado con matices (extracto, no té) | Lopresti 2022, doi:10.3389/fnut.2022.965130 |
| Tulsi | Síntomas de estrés general (incluye "agotamiento frecuente") | 150 adultos (India) | Extracto OciBest, 1200 mg/día, 6 semanas, frente a placebo | Puntaje total de síntomas menor (p ≤ 0,05). Mejoraron el olvido, el agotamiento y los problemas de sueño. Mejoría 39 % mayor que con placebo. | muy baja (escala autoevaluada, un ECA) | respaldado con matices | Saxena 2012, doi:10.1155/2012/894509 |
| Tulsi | Cognición, cortisol, ansiedad | Adultos sanos (n no confirmado en el resumen) | Extracto etanólico 300 mg/día, 30 días, frente a placebo | Mejores tiempos de reacción y errores en Sternberg y Stroop frente a placebo. Cortisol salival y ansiedad (STAI) mejoraron solo dentro del grupo; **sin diferencia entre grupos**. | muy baja | respaldado con matices (cognición); sin diferencia (cortisol) | Sampath 2015, PMID 26571987 (sin DOI en PubMed) |
| Tulsi | Ansiedad generalizada | 35 adultos con TAG | Extracto 500 mg 2 veces al día, 60 días; sin grupo placebo descrito | Bajó la ansiedad (p < 0,001) frente al inicio. | muy baja | respaldado con matices | Bhattacharyya 2008, PMID 19253862 |
| Tulsi | Ansiedad (único ensayo con **té**) | 44 pacientes con cáncer diferenciado de tiroides en terapia con yodo radiactivo | 180 ml de té con 2,0 g de hoja después de cada comida (3 al día), 4 días, frente a agua | El cambio en la ansiedad (STAI estado y rasgo) fue menor con té (p < 0,05). | muy baja | respaldado con matices | Nomura 2023, doi:10.1016/j.heliyon.2023.e20691 |
| Tulsi + rodiola + esquisandra | Estrés, sueño, fatiga | 186 adultos con estrés alto | Fórmula de 3 plantas, 60 días, frente a placebo | Estrés percibido (p < 0,0001) y sueño (PSQI, p = 0,0008) mejoraron. Sin cambio en el estado de alerta. El efecto **no** se puede atribuir al tulsi. | baja | sin evidencia en humanos (para tulsi solo) | McKinney 2026, doi:10.1186/s13063-026-09495-9 |
| Tulsi | Síntesis de 24 estudios clínicos | Varias poblaciones | Varios | Todos los estudios reportaron resultados favorables; ninguno, eventos adversos significativos. Sin metaanálisis ni evaluación de calidad en el resumen. | muy baja | respaldado con matices | Jamshidi 2017, doi:10.1155/2017/9217567 |
| Varias plantas (incluye tulsi) | Eje HPA y cortisol (revisión sistemática de ECA) | 52 ECA de 26 plantas | Varios | Para la mayoría de plantas, el efecto sobre el cortisol es "poco claro". El único hallazgo consistente fue con ashwagandha. | baja | contradicho (para "baja el cortisol" como efecto general) | Lopresti 2021, doi:10.1080/1028415X.2021.1892253 |
| Tulsi y otras plantas | Fatiga, sueño y ansiedad en cáncer | 8 ECA | Varios preparados orales | Certeza GRADE **muy baja** en todos los desenlaces. | muy baja | sin evidencia en humanos (de calidad) | Moreno-Ponce 2026, doi:10.3390/medsci14060597 |
| Ortiga (hoja) | Síntomas de enfermedad de la Guerra del Golfo (incluye fatiga) | 29 hombres; cruzado, seudoaleatorizado | Dosis baja y alta de ortiga, 30 días cada una (dosis no confirmada en el resumen) | Dosis alta: menor gravedad de síntomas frente a placebo (p = 0,048). El resumen no da el resultado de fatiga por separado. | muy baja | sin evidencia en humanos (para fatiga) | Younger 2021, doi:10.3390/ijerph18073671 |
| Ortiga | Anemia o hemoglobina | — | — | No hallé ensayos en humanos. | sin evidencia en humanos | sin evidencia en humanos | Búsquedas PubMed (log 4 y 23) |
| Ortiga | Sueño, ansiedad, energía | — | — | No hallé ensayos en humanos. | sin evidencia en humanos | sin evidencia en humanos | Log 4 |
| Ortiga (hoja) | Glucemia en DM2 (metaanálisis) | 8 ECA, 401 adultos con DM2 | Suplemento de ortiga | Glucemia en ayunas −18,01 mg/dl (IC 95 % −30,04 a −5,97; I² 94,6 %). HbA1c −0,77 % (IC −1,77 a 0,22; no significativa). | baja | respaldado con matices (relevante para interacciones) | Ziaei 2019, doi:10.1002/ptr.6535 |
| Ortiga | Perfil metabólico en DM2 (metaanálisis) | 13 ensayos | Varios | Glucemia −17,17 mg/dl (IC −26,60 a −7,73); HbA1c −0,93 (IC −1,66 a −0,17); PAS −5,03 mmHg (IC −8,15 a −1,91). Sin cambio en PAD. | baja | respaldado con matices (relevante para interacciones) | Tabrizi 2022, doi:10.2174/1389557521666210929143112 |
| Avena verde (extracto) | Cognición (revisión sistemática) | 6 ECA, 287 adultos sanos | Extractos; dosis variables | Dosis única: mejor exactitud y velocidad. Uso crónico corto: mejoró; uso crónico largo: no. Calidad "promedio". | baja | respaldado con matices (extracto, agudo) | Jibril 2022, doi:10.1016/j.clnesp.2022.12.011 |
| Avena verde (extracto) | Cognición, ánimo y respuesta a estrés | 132 adultos sanos de 35–65 años | 430, 860 o 1290 mg/día, 29 días, frente a placebo | Mejoró la memoria de trabajo y la multitarea. Dosis alta: menor respuesta electrodérmica al estresor. **Sin efecto en el ánimo.** | baja | respaldado con matices (cognición); contradicho (ánimo) | Kennedy 2020, doi:10.3390/nu12061598 |
| Avena verde (extracto) | Cognición crónica | 37 adultos de unos 67 años | 1500 mg/día, 12 semanas, cruzado | Sin efecto en ninguna medida cognitiva. | baja | contradicho (uso crónico) | Wong 2012, doi:10.3390/nu4050331 |
| Avena verde (extracto) | Cognición aguda | Adultos de 40–65 años con queja de memoria | 800 o 1600 mg, dosis única, cruzado | 800 mg: mayor velocidad global y mejor recuerdo diferido. | baja | respaldado con matices | Kennedy 2015, doi:10.1080/1028415X.2015.1101304 |
| Avena verde (extracto) | Estrés, sueño y calidad de vida al dejar de fumar | 145 fumadores | 900 mg/día, 8 semanas, frente a placebo | Mayor descenso del estrés percibido; mejor sueño; más reductores exitosos (66,7 % frente a 49,3 %; p = 0,034). El resumen no da las cifras de estrés ni sueño. | baja | respaldado con matices | Friling 2024, doi:10.3389/fnut.2024.1405156 |
| Avena (hierba) | Estrés mental leve y sueño (uso tradicional) | — | 3 g de hierba por infusión | Uso tradicional de 30 años o más; la EMA cita estudios en ratas, no ensayos clínicos. | sin evidencia en humanos (para el té) | respaldado con matices (uso tradicional) | EMA, EMEA/HMPC/202966/2007; página EMA *Avenae herba* |
| Avena | "Energía" | — | — | No hallé estudios. | sin evidencia en humanos | sin evidencia en humanos | Log 10 |
| Valeriana | Insomnio (revisión paraguas) | 8 revisiones sistemáticas | Varios | Sin evidencia de eficacia en el insomnio. Mejoría subjetiva de la calidad del sueño, no confirmada con medidas objetivas. Buen perfil de seguridad. | baja | contradicho (insomnio) | Valente 2024, doi:10.1016/j.euroneuro.2024.01.008 |
| Valeriana | Calidad subjetiva del sueño y ansiedad (metaanálisis) | 60 estudios (n = 6894); metaanálisis de 10 y 8 estudios | Raíz o extractos | Los autores atribuyen la inconsistencia a la calidad variable de los extractos. Sin eventos adversos graves (7–80 años). El resumen no da la cifra principal. | baja | respaldado con matices | Shinjyo 2020, doi:10.1177/2515690X20967323 |
| Valeriana | Insomnio en mayores de 65 | 1 estudio | — | Sin efecto en el sueño subjetivo ni objetivo. | baja | contradicho | Almond 2021, doi:10.4140/TCP.n.2021.83 |
| Nébeda | Sueño o ansiedad | — | — | No hallé ensayos clínicos. Solo un estudio de inhalación de aceites esenciales en mayores. | sin evidencia en humanos | sin evidencia en humanos | Log 22 |

**Nota sobre la fatiga:** ningún ensayo de la tabla usa la fatiga como desenlace principal. El ítem "agotamiento" del ensayo OciBest es el dato más cercano.

---

## 4. Aporte nutricional de las infusiones

### 4.1 Cuánto pasa al agua (tasa de extracción)

| Elemento | Tasa de extracción de la hierba al agua | Fuente |
|---|---|---|
| Hierro | 4,4–12,4 % (5 hierbas, entre ellas hoja de ortiga) | Suliburska 2011, doi:10.3109/09637486.2011.617359 |
| Hierro, calcio, manganeso | Poco extraíbles: menos del 20 % (7 hierbas, entre ellas ortiga) | Pytlakowska 2012, doi:10.1016/j.foodchem.2012.05.002 |
| Magnesio, zinc, cobre, fósforo | Moderadamente extraíbles: 20–55 % | Pytlakowska 2012 |
| Potasio | Muy extraíble: más del 55 % | Pytlakowska 2012 |
| Cobre | 26,7–50,7 % | Suliburska 2011 |
| Plomo, cadmio, cobalto, cromo | Paso al agua "nulo" en las infusiones estudiadas (incluye ortiga) | Başgel 2006, doi:10.1016/j.scitotenv.2005.04.016 |

Conclusión de Suliburska 2011: con un consumo promedio, las infusiones de hierbas **no son fuentes importantes** de calcio, magnesio, hierro, zinc ni cobre.

### 4.2 Cuánto aporta: datos en la infusión, no en la hoja seca

| Nutriente | Dato en la infusión | Por 10 g de hierba seca (cálculo) | % de la referencia diaria de una mujer de 19–50 años | Fuente |
|---|---|---|---|---|
| Hierro | Media de tés de hierbas: 18,45 ± 11,90 µg por g de té | ≈0,18 mg | ≈1 % de 18 mg (antes de descontar absorción) | Długaszek 2019, doi:10.1016/j.jtemb.2019.126428 |
| Calcio | Media: 5,73 ± 3,33 mg por g | ≈57 mg | ≈6 % de 1000 mg | Długaszek 2019 |
| Magnesio | Media: 1,79 ± 3,47 mg por g. Hoja de ortiga: 76 mg de Mg extraíble en 500 ml (los autores lo estiman en ≈20 % de la ingesta diaria; la cantidad de hierba no consta en el resumen) | ≈18 mg (media) | ≈6 % de 310 mg (media); ≈25 % de 310 mg (dato de ortiga) | Długaszek 2019; Konieczyński 2012, PMID 22574504 |
| Potasio | Media: 18,14 ± 9,50 mg por g | ≈181 mg | ≈7 % de 2600 mg | Długaszek 2019 |
| Vitamina C | Ortiga, 1 g en 100 ml: máximo ≈3 mg por 100 g de infusión (60 °C, 10 min). Baja a ≈1 mg a los 20 min. | — | ≈3–4 % de 75 mg por 100 ml (la referencia de 75 mg no se verificó en esta revisión) | Wolska 2016, PMID 27925706 |

**Notas de cálculo:**
1. Las cifras de Długaszek 2019 son la **media de varios tés de hierbas**. La ortiga está entre los que más minerales aportan, pero el resumen no da su valor propio. El valor real de la ortiga puede ser mayor que la media.
2. "Por 10 g" multiplica la media por 10. Supone la misma tasa de extracción que en el estudio. No hay datos de la infusión larga de 4–12 h (ver sección 13).
3. Referencias diarias (mujer de 19–50 años): hierro 18 mg (embarazo 27 mg), calcio 1000 mg (MedlinePlus, IDR de NASEM); magnesio 310–320 mg (MedlinePlus; NIH ODS, hoja para el consumidor); potasio 2600 mg (NIH ODS, IA 2019).
4. No hallé datos de minerales en la **infusión de paja de avena**.

### 4.3 Comparación: comer la ortiga cocida

| Por 100 g de ortiga escaldada (USDA, vía réplica secundaria) | Valor |
|---|---|
| Agua | 87,67 g |
| Calcio | 481 mg |
| Hierro | 1,64 mg |
| Magnesio | 57 mg |
| Potasio | 334 mg |
| Vitamina K | 498,6 µg |
| Folato | 14 µg |

Fuente: USDA, registro "Stinging Nettles, blanched (Northern Plains Indians)", leído en happyforks.com (réplica; sin número NDB en la página).

**Lectura:** 100 g de ortiga cocida dan unas 8 veces más calcio que la infusión de 10 g de hierba (cálculo con la media). Si el objetivo es nutrir, la ortiga cocida como verdura aporta más que la infusión. Con warfarina, la ortiga cocida sí aporta mucha vitamina K (ver sección 5).

---

## 5. Seguridad

### 5.1 Por planta

| Planta | Embarazo | Lactancia | Niños | Efectos adversos y alergias | Fuente |
|---|---|---|---|---|---|
| **Tulsi** | "Podría no ser segura" en embarazo ni si se busca embarazo. En animales, dosis altas redujeron la implantación y los embarazos a término. | No estudiada. LactMed no se pudo leer (bloqueo). | Sin datos. | Náusea, diarrea, cefalea, agitación. | MSD Manual 2025; MSKCC 2026 |
| **Tulsi: fertilidad (animales)** | Conejos machos: 2 g/día de hoja fresca, 30 días: menos espermatozoides; FSH y LH bajas. Ratas: extracto 250 mg/kg, 48 días: menor recuento y motilidad, **reversible** a las 2 semanas. Ratas hembra: 500 mg/kg, 15 días: más progesterona, menos ovulación. | — | — | — | Sethi 2010, doi:10.4103/0974-7788.76782; Ahmed 2002, doi:10.1515/jbcpp.2002.13.1.51; Poli 2019, doi:10.1097/JCMA.0000000000000034 |
| **Tulsi: tiroides (animales)** | Ratones: extracto 0,5 g/kg, 15 días: T4 sérica más baja; T3 sin cambio. | — | — | MSD: puede bajar la tiroxina y empeorar un hipotiroidismo. | Panda 1998, doi:10.1006/phrs.1998.0338; MSD 2025 |
| **Tulsi: toxicidad general (animales)** | Ratas, 200–800 mg/kg/día, 28 días: sin cambios en hemograma, bioquímica ni órganos. | — | — | — | Gautam 2014, doi:10.1155/2014/135654 |
| **Ortiga (hoja), EMA** | No recomendada: seguridad no establecida. | No recomendada: seguridad no establecida. | No en menores de 12 años. | Molestias digestivas leves (náusea, vómito, diarrea); picor, exantema y urticaria. Contraindicada si se recomienda restringir líquidos (enfermedad cardiaca o renal grave). Uso máximo 2–4 semanas (vías urinarias) o 4 semanas (dolor articular). Dosis 2–4 g por taza, 3–6 veces al día (8–12 g/día). | EMA/HMPC/508015/2007 (adoptada 2010-01-14; publicada 2011) |
| **Ortiga (herba), EMA** | No recomendada. | No recomendada. | No en menores de 12 años. | Molestias digestivas y alergia. 2–4 g por dosis, hasta 3 veces al día. La página la marca como **superada**. | EMEA/HMPC/170261/2006 (2008) |
| **Ortiga (raíz), EMA** | "No relevante" (indicación solo en hombres). | "No relevante". | "Sin uso relevante" en menores de 18 años. | Náusea, pirosis, plenitud, flatulencia, diarrea; picor, exantema, urticaria. Indicación: síntomas urinarios de la hiperplasia prostática **después** de que un médico descarte enfermedad grave. No es para fatiga. | EMA/HMPC/322646/2023, Rev. 1 (adoptada 2025-01-22) |
| **Ortiga: casos clínicos** | — | Recién nacido de 17 días con urticaria generalizada: la madre aplicó agua hervida con ortiga en los pezones; IgE específica alta en el bebé. | Ver lactancia. | Mujer de 30 años con galactorrea tras 1 mes de 500 mg/día de ortiga; se resolvió 1 semana después de suspenderla. | Uslu 2010, doi:10.1007/s00431-010-1327-z; Easton 2021, doi:10.12659/AJCR.933999 |
| **Ortiga fresca** | — | — | — | El contacto con los pelos urticantes causa picor, dermatitis y urticaria en minutos. Los pelos contienen acetilcolina, histamina y serotonina. Usa guantes al cosecharla. | Anderson 2003, doi:10.2310/6620.2003.38719; Ensikat 2021, doi:10.3390/toxins13020141 |
| **Avena (hierba), EMA** | No recomendada: seguridad no establecida. | No recomendada. | No en menores de 12 años. | Sin efectos adversos conocidos. Precaución en celiaquía: no hay datos del contenido de proteína. | EMEA/HMPC/202966/2007 (2008); revisión periódica en curso (convocatoria EMA/91151/2024) |
| **Avena (fruto), EMA** | — | — | Adultos y niños (uso cutáneo). | Uso cutáneo (avena coloidal) en inflamación leve de la piel y heridas menores. No es una indicación oral para fatiga. | EMEA/HMPC/368600/2007 (2008) |
| **Avena y celiaquía** | — | — | — | ECA con avena **pura**: 12 meses sin cambio en síntomas, histología ni serología. Pero 36 % de productos de avena "sin gluten" superaron 20 ppm (Codex), y 40 % superaron 5 ppm (Chile). | Pinto-Sánchez 2017, doi:10.1053/j.gastro.2017.04.009; Rodríguez 2022, doi:10.3389/fnut.2022.986282; Thompson 2004, doi:10.1056/NEJM200411043511924 (carta, sin resumen) |

### 5.2 Interacciones

| Planta | Fármaco | Dato | Tipo | Veredicto | Fuente |
|---|---|---|---|---|---|
| Tulsi | Levotiroxina | "Puede disminuir la eficacia" de la hormona tiroidea. | revisión (base animal) | riesgo omitido | MSD 2025; Panda 1998 |
| Tulsi | Anticoagulantes y antiagregantes | Inhibe la agregación plaquetaria y prolonga el tiempo de coagulación; más riesgo de sangrado, también en cirugía. Un extracto etanólico inhibió la agregación de plaquetas humanas in vitro (1–10 mg/ml). | revisión; in vitro | riesgo omitido | MSD 2025; Maaz 2026, doi:10.3390/molecules31162749 |
| Tulsi | Antidiabéticos | MSD cita un estudio cruzado de 40 pacientes con mejor glucemia y otro de 60 pacientes con algo más de descenso de glucosa y HbA1c junto con glibenclamida. No hallé estudios de hipoglucemia. Sumar hipoglucemia es una **inferencia**. | ensayos pequeños; inferencia | riesgo omitido (inferencia) | MSD 2025 |
| Tulsi | Barbitúricos | En animales, puede aumentar la sedación. | animal | riesgo omitido | MSD 2025 |
| Tulsi | Interacciones en general | MSKCC no lista interacciones. | revisión | — | MSKCC 2026 |
| Ortiga | Antidiabéticos | Baja la glucemia en ayunas unos 17–18 mg/dl en DM2. En un ECA se sumó a insulina y antidiabéticos orales sin efectos en creatinina ni transaminasas. | metaanálisis | riesgo omitido (vigilar glucosa) | Ziaei 2019; Tabrizi 2022; Kianbakht 2013, doi:10.7754/clin.lab.2012.121019 |
| Ortiga | Antihipertensivos | PAS −5,03 mmHg en DM2. Sumar hipotensión es una inferencia. | metaanálisis; inferencia | riesgo omitido (inferencia) | Tabrizi 2022 |
| Ortiga | Diuréticos y litio | La EMA no reporta interacciones. La indicación EMA es aumentar la diuresis. No hallé estudios con diuréticos ni litio. Sumar efecto diurético o alterar el litio es una **inferencia**. | inferencia | riesgo omitido (inferencia) | EMA/HMPC/508015/2007; log 21 |
| Ortiga | Warfarina | No hallé estudios ni casos de interacción. La hoja **cocida** tiene 498,6 µg de vitamina K por 100 g. No hallé el contenido de vitamina K en la infusión. | composición; sin datos clínicos | riesgo omitido (para la hoja como alimento) | USDA (réplica); log 21 |
| Avena (hierba) | — | La EMA no reporta interacciones. | monografía | — | EMEA/HMPC/202966/2007 |

### 5.3 Contaminantes

| Riesgo | Dato confirmado | Veredicto | Fuente |
|---|---|---|---|
| Metales pesados en tulsi de India | No hallé análisis de metales en productos comerciales de tulsi. Tulsi cultivado en macetas cerca de una zona industrial de Bengala Occidental acumuló metales en las hojas; la acumulación se correlacionó con el polvo atmosférico. | riesgo documentado (muy baja; no son productos comerciales) | Majee 2023, doi:10.1007/s10661-023-11573-3 |
| Metales en infusión de ortiga | Plomo, cadmio, cobalto y cromo: paso al agua nulo en infusiones de Turquía. | sin riesgo detectado (un estudio) | Başgel 2006 |
| Gluten en avena | Ver 5.1. | riesgo documentado | Rodríguez 2022 |

---

## 6. Afirmaciones verificadas

| # | Afirmación | Cifra verificada | Veredicto | Alerta (máx. 60 palabras) | Fuente |
|---|---|---|---|---|---|
| 1 | "El tulsi es un adaptógeno que reduce el cansancio" | Con extracto 250 mg/día, 8 semanas: menos estrés percibido (p = 0,003). Con 1200 mg/día, 6 semanas: menos "agotamiento" (p ≤ 0,05). Ningún ensayo usa la fatiga como desenlace principal. Ningún ensayo de fatiga usó té. | respaldado con matices (baja) | Hay ensayos pequeños con extractos para estrés, no para fatiga. El té no se ha probado para el cansancio. Antes de usarlo, descarta anemia, hipotiroidismo, depresión y apnea del sueño. No lo uses si buscas embarazo o tomas levotiroxina o anticoagulantes. | Lopresti 2022; Saxena 2012; MSD 2025 |
| 2 | "El tulsi baja el cortisol" | Un ECA: cortisol en cabello menor (p = 0,025) y cortisol salival menor tras estresor (p = 0,001). Otro ECA: sin diferencia entre grupos. Revisión de 52 ECA: efecto "poco claro". | respaldado con matices (baja) | Un solo ensayo con extracto mostró menos cortisol; otro no. La revisión sistemática lo califica de poco claro. No hay datos con té. No uses el tulsi para tratar alteraciones suprarrenales. Medir cortisol no sirve para evaluar la fatiga común. | Lopresti 2022; Sampath 2015; Lopresti 2021 |
| 3 | "La infusión de ortiga aporta hierro y sirve para la anemia" | Solo el 4,4–12,4 % del hierro pasa al agua. Media de tés de hierbas: 18,45 µg de hierro por g. Sin ensayos en anemia. | contradicho (por datos de composición; sin ensayos) | La infusión de ortiga aporta muy poco hierro: unos 0,2 mg por 10 g de hierba, el 1 % de la necesidad diaria de una mujer. No trata la anemia. Si hay anemia, busca la causa y usa hierro medicinal. Toma los tés 1 h antes o después de las comidas. | Suliburska 2011; Długaszek 2019 |
| 4 | "La ortiga es segura en el embarazo" | EMA: seguridad no establecida; no recomendada en embarazo ni lactancia. Caso: urticaria en recién nacido por ortiga en los pezones. | riesgo omitido (media) | No hay datos de seguridad de la ortiga en el embarazo. La EMA no la recomienda en embarazo ni lactancia. No la apliques en los pezones: causó urticaria en un recién nacido. La ortiga cocida como alimento ocasional es otra cosa; no hallé datos que la evalúen. | EMA/HMPC/508015/2007; Uslu 2010 |
| 5 | "La paja de avena calma los nervios y da energía" | EMA: uso tradicional para estrés mental leve y sueño (3 g por infusión). Extractos: mejor cognición aguda y menor estrés percibido en un ECA; sin efecto en el ánimo en otro. "Energía": sin estudios. | respaldado con matices (calma; baja) · sin evidencia en humanos (energía) | La EMA acepta la hierba de avena como uso tradicional para estrés leve y sueño. Los ensayos usan extractos, no la paja en infusión larga. No hay estudios de "energía". Si el cansancio dura más de 4 semanas, consulta. No en menores de 12 años, embarazo ni lactancia. | EMEA/HMPC/202966/2007; Kennedy 2020; Friling 2024 |
| 6 | "La paja de avena es apta para celíacos" | EMA: precaución en celiaquía. Avena pura: segura 12 meses en ECA. 36 % de productos "sin gluten" superaron 20 ppm. No hallé datos de gluten en la paja. | riesgo omitido (media) | La avena pura suele tolerarse, pero la contaminación con trigo o cebada es frecuente. La EMA pide precaución porque no conoce la proteína de la hierba. Si hay celiaquía, usa solo producto certificado sin gluten o evítala. | EMEA/HMPC/202966/2007; Pinto-Sánchez 2017; Rodríguez 2022 |
| 7 | "Las infusiones nutritivas reemplazan un multivitamínico" | Calcio ≈6 %, magnesio ≈6 %, potasio ≈7 % y hierro ≈1 % de la referencia diaria por 10 g de hierba (cálculo con medias). Las infusiones "no son fuentes importantes" de minerales. | contradicho (media) | Una infusión aporta una fracción pequeña de los minerales diarios y casi nada de hierro. No reemplaza un multivitamínico ni un suplemento indicado (hierro, B12, ácido fólico en embarazo). Para nutrir, la ortiga cocida como verdura aporta más que la infusión. | Suliburska 2011; Długaszek 2019; USDA (réplica) |

---

## 7. Qué puede ofrecer la skill y qué no

### 7.1 Veredicto general

La evidencia **no justifica una receta para tratar la fatiga**. Ninguna planta tiene ensayos con fatiga como desenlace principal. Los ensayos positivos usan extractos en cápsulas, no tés.

La skill sí puede ofrecer una **bebida de apoyo** para estrés leve y sueño. Condiciones: adulto, causas médicas descartadas y límites de la EMA.

### 7.2 Receta tipo (solo como apoyo, no como tratamiento)

**Té de avena verde (hierba de avena), opción principal**
- **Población:** adultos de 18 años o más. (La EMA permite desde 12 años; la skill usa 18 por prudencia.)
- **Excluir:** embarazo, lactancia, celiaquía sin producto certificado, fatiga con signos de alarma.
- **Cantidad:** 3 g de hierba de avena seca en 250 ml de agua hirviendo. Tapa y deja 10–15 min. Cuela.
- **Frecuencia:** 1 taza al día, en la tarde o antes de dormir. (La EMA da 3 g como dosis diaria de referencia.)
- **Duración máxima:** 2 semanas sin mejoría. Es un criterio de la skill; la EMA no fija un máximo.
- **Base:** monografía EMA, EMEA/HMPC/202966/2007.

**Complemento opcional: hoja de ortiga**
- **Solo** como bebida, no como fuente de hierro.
- **Población:** adultos sin embarazo, lactancia, enfermedad cardiaca o renal grave, ni restricción de líquidos.
- **Cantidad:** 2 g de hoja seca por taza de 250 ml. Máximo 8 g al día (límite inferior de la EMA, por prudencia). Infusión en frío o en caliente.
- **Infusión larga del libro:** si se hace de 4–12 h, la cantidad total de hoja en el día no debe superar 8 g. No hay datos de que la infusión larga extraiga más minerales útiles.
- **Duración máxima:** 4 semanas (EMA).
- **Precaución:** si toma antidiabéticos, antihipertensivos, diuréticos o litio, consulta antes.

**Tulsi:** la skill no debe recomendarlo como "adaptógeno para la fatiga". Si la persona ya lo usa como té culinario: no en embarazo, si busca embarazo, con levotiroxina, con anticoagulantes ni 2 semanas antes de una cirugía.

**Criterios de consulta (cualquiera):**
- La fatiga dura 4 semanas o más.
- Hay un signo de alarma (sección 2.2).
- Hay somnolencia diurna con ronquido o pausas respiratorias.
- Hay ánimo bajo o pérdida de interés casi todos los días durante 2 semanas.
- La persona está embarazada, lacta o toma medicamentos crónicos.

### 7.3 Lo que no debe hacer

- No prometer "energía" ni "reducir el cansancio".
- No presentar la infusión de ortiga como tratamiento de la anemia.
- No reemplazar el estudio de la fatiga por un té.
- No usar la valeriana para "dar energía"; en el insomnio no mostró eficacia en la revisión paraguas.
- No dar ortiga, tulsi ni avena en hierba a menores de 12 años.
- No aplicar ortiga en los pezones durante la lactancia.
- No usar la raíz de ortiga para la fatiga: su única indicación EMA es la próstata en hombres.

---

## 8. Alertas nuevas para la tabla "Seguridad clínica" de la skill

| Tema | Qué dice el libro | Veredicto (confianza) | Alerta |
|---|---|---|---|
| **Fatiga: busca la causa primero** | Propone tés para el bienestar y el sueño. | sin evidencia suficiente (alta) | Ningún té trata la fatiga. Si dura 4 semanas o más, pide hemograma, ferritina, TSH, glucosa o HbA1c y función renal y hepática. Consulta pronto si hay pérdida de peso ≥5 %, adenopatías, sangrado o signos neurológicos. Pregunta por sueño, ánimo, embarazo y fármacos (AFP 2023; resumen de NICE CKS). |
| **Albahaca sagrada (tulsi)** | Adaptógeno; evitar grandes cantidades en el embarazo. | riesgo omitido (media; datos animales) | No la uses en embarazo ni si se busca embarazo: en animales redujo la implantación y la fertilidad. Puede bajar la T4 y reducir el efecto de la levotiroxina. Inhibe las plaquetas: precaución con anticoagulantes y antes de cirugía. Puede sumar efecto a los antidiabéticos (MSD 2025; doi:10.1006/phrs.1998.0338). |
| **Hoja de ortiga: límites** | Infusión larga de 4–12 h, "nutritiva". | corregir (alta) | La EMA limita la hoja a 8–12 g/día y 4 semanas. No en menores de 12 años, embarazo ni lactancia. No si hay enfermedad cardiaca o renal grave con restricción de líquidos. Baja la glucemia en ayunas (−18 mg/dl en DM2): vigila con antidiabéticos (EMA/HMPC/508015/2007; doi:10.1002/ptr.6535). |
| **Infusión "nutritiva" y hierro** | La infusión larga extrae minerales. | corregir (media) | Solo el 4–12 % del hierro de la hierba pasa al agua: unos 0,2 mg por 10 g de hierba, el 1 % de la necesidad diaria. No trata la anemia ni reemplaza un multivitamínico. Para nutrir, la ortiga cocida aporta más (doi:10.3109/09637486.2011.617359; doi:10.1016/j.jtemb.2019.126428). |
| **Avena y celiaquía** | Paja de avena en infusión larga. | riesgo omitido (media) | La EMA pide precaución en celiaquía: no hay datos de proteína en la hierba. La avena pura fue segura 12 meses en ECA, pero 36 % de productos "sin gluten" superaron 20 ppm. Si hay celiaquía, usa solo producto certificado o evítala (EMEA/HMPC/202966/2007; doi:10.3389/fnut.2022.986282). |
| **Valeriana para el sueño** | Ciclos; el efecto tarda semanas. | confirmada con matices (media) | Una revisión paraguas de 8 revisiones sistemáticas no halló eficacia de la valeriana en el insomnio. Solo mejoró la calidad del sueño percibida. En el insomnio crónico, la primera línea es la terapia cognitivo-conductual. No la uses para dar energía (doi:10.1016/j.euroneuro.2024.01.008; doi:10.1111/jsr.13979). |

---

## 9. Huecos y limitaciones

1. **No hay ensayos de las recetas del libro.** Ningún ensayo probó el De-Stress Tea, el Sleep Well Tea ni la infusión larga de ortiga y avena.
2. **Extractos frente a té.** Casi toda la evidencia del tulsi y la avena usa extractos estandarizados (Holixer, OciBest, Neuravena, cognitaven). Su dosis de activos no equivale a una taza de té.
3. **Financiación.** Varios ensayos de extractos son de productos comerciales. No verifiqué la financiación de cada uno.
4. **Datos de la infusión de ortiga.** Los resúmenes dan tasas de extracción, pero no los mg de hierro y calcio por taza de ortiga sola. Los artículos completos no están en PMC. La media de Długaszek 2019 mezcla varios tés.
5. **Infusión larga.** No hallé estudios que comparen 4–12 h con 10–15 min para minerales. Para la vitamina C, más tiempo la **reduce** (Wolska 2016).
6. **Paja de avena.** No hallé datos de minerales ni de gluten en la paja o la hierba en infusión.
7. **LactMed** no se pudo leer (reCAPTCHA). La seguridad en lactancia se basa en la EMA y en casos.
8. **NICE CKS** no se pudo leer. Los signos de alarma vienen de un resumen secundario (Edinburgh GP Handbook 2019) que cita NICE CKS.
9. **Monografía de la hoja de ortiga.** Es de 2010. La revisión periódica (adendo 2022) no se pudo leer. No sé si cambió algo.
10. **Metales pesados en tulsi.** No hallé análisis de productos comerciales. El dato disponible es de plantas cultivadas cerca de industria.
11. **Referencias de ingesta.** Hierro y calcio se leyeron en MedlinePlus; magnesio y potasio en NIH ODS y MedlinePlus. No leí la fuente primaria de NASEM.

---

## 10. Referencias

**PubMed (según PubMed, con DOI cuando existe):**
1. Lopresti AL, Smith SJ, Metse AP, Drummond PD. *Front Nutr* 2022;9:965130. doi:[10.3389/fnut.2022.965130](https://doi.org/10.3389/fnut.2022.965130)
2. Saxena RC, et al. *Evid Based Complement Alternat Med* 2012:894509. doi:[10.1155/2012/894509](https://doi.org/10.1155/2012/894509)
3. Sampath S, et al. *Indian J Physiol Pharmacol* 2015. PMID 26571987 (sin DOI en PubMed).
4. Bhattacharyya D, et al. *Nepal Med Coll J* 2008. PMID 19253862 (sin DOI en PubMed).
5. Nomura M, et al. *Heliyon* 2023;9:e20691. doi:[10.1016/j.heliyon.2023.e20691](https://doi.org/10.1016/j.heliyon.2023.e20691)
6. McKinney J, et al. *Trials* 2026. doi:[10.1186/s13063-026-09495-9](https://doi.org/10.1186/s13063-026-09495-9)
7. Jamshidi N, Cohen MM. *Evid Based Complement Alternat Med* 2017:9217567. doi:[10.1155/2017/9217567](https://doi.org/10.1155/2017/9217567)
8. Lopresti AL, Smith SJ, Drummond PD. *Nutr Neurosci* 2022;25(8):1704-1730. doi:[10.1080/1028415X.2021.1892253](https://doi.org/10.1080/1028415X.2021.1892253)
9. Moreno-Ponce R, et al. *Med Sci (Basel)* 2026. doi:[10.3390/medsci14060597](https://doi.org/10.3390/medsci14060597)
10. Panda S, Kar A. *Pharmacol Res* 1998;38(2):107-10. doi:[10.1006/phrs.1998.0338](https://doi.org/10.1006/phrs.1998.0338)
11. Sethi J, et al. *Int J Ayurveda Res* 2010;1(4):208-10. doi:[10.4103/0974-7788.76782](https://doi.org/10.4103/0974-7788.76782)
12. Ahmed M, et al. *J Basic Clin Physiol Pharmacol* 2002;13(1):51-9. doi:[10.1515/jbcpp.2002.13.1.51](https://doi.org/10.1515/jbcpp.2002.13.1.51)
13. Poli V, Challa C. *J Chin Med Assoc* 2019;82(3):231-234. doi:[10.1097/JCMA.0000000000000034](https://doi.org/10.1097/JCMA.0000000000000034)
14. Gautam MK, Goel RK. *J Toxicol* 2014:135654. doi:[10.1155/2014/135654](https://doi.org/10.1155/2014/135654)
15. Maaz M, et al. *Molecules* 2026. doi:[10.3390/molecules31162749](https://doi.org/10.3390/molecules31162749)
16. Majee S, et al. *Environ Monit Assess* 2023. doi:[10.1007/s10661-023-11573-3](https://doi.org/10.1007/s10661-023-11573-3)
17. Younger J, et al. *Int J Environ Res Public Health* 2021;18(7):3671. doi:[10.3390/ijerph18073671](https://doi.org/10.3390/ijerph18073671)
18. Ziaei R, et al. *Phytother Res* 2019. doi:[10.1002/ptr.6535](https://doi.org/10.1002/ptr.6535)
19. Tabrizi R, et al. *Mini Rev Med Chem* 2022. doi:[10.2174/1389557521666210929143112](https://doi.org/10.2174/1389557521666210929143112)
20. Kianbakht S, et al. *Clin Lab* 2013. doi:[10.7754/clin.lab.2012.121019](https://doi.org/10.7754/clin.lab.2012.121019)
21. Easton L, et al. *Am J Case Rep* 2021;22:e933999. doi:[10.12659/AJCR.933999](https://doi.org/10.12659/AJCR.933999)
22. Uslu S, et al. *Eur J Pediatr* 2010 (en línea);170(3):401-3. doi:[10.1007/s00431-010-1327-z](https://doi.org/10.1007/s00431-010-1327-z)
23. Anderson BE, et al. *Am J Contact Dermat* 2003;14(1):44-6. doi:[10.2310/6620.2003.38719](https://doi.org/10.2310/6620.2003.38719)
24. Ensikat HJ, et al. *Toxins (Basel)* 2021;13(2):141. doi:[10.3390/toxins13020141](https://doi.org/10.3390/toxins13020141)
25. Suliburska J, et al. *Int J Food Sci Nutr* 2011 (en línea). doi:[10.3109/09637486.2011.617359](https://doi.org/10.3109/09637486.2011.617359)
26. Pytlakowska K, et al. *Food Chem* 2012. doi:[10.1016/j.foodchem.2012.05.002](https://doi.org/10.1016/j.foodchem.2012.05.002)
27. Długaszek M, et al. *J Trace Elem Med Biol* 2019 (en línea). doi:[10.1016/j.jtemb.2019.126428](https://doi.org/10.1016/j.jtemb.2019.126428)
28. Konieczyński P. *Acta Pol Pharm* 2012. PMID 22574504 (sin DOI en PubMed).
29. Başgel S, et al. *Sci Total Environ* 2006. doi:[10.1016/j.scitotenv.2005.04.016](https://doi.org/10.1016/j.scitotenv.2005.04.016)
30. Wolska J, et al. *Rocz Panstw Zakl Hig* 2016;67(4):367-371. PMID 27925706 (sin DOI en PubMed).
31. Jibril AT, et al. *Clin Nutr ESPEN* 2022 (en línea). doi:[10.1016/j.clnesp.2022.12.011](https://doi.org/10.1016/j.clnesp.2022.12.011)
32. Kennedy DO, et al. *Nutrients* 2020;12(6):1598. doi:[10.3390/nu12061598](https://doi.org/10.3390/nu12061598)
33. Kennedy DO, et al. *Nutr Neurosci* 2015 (en línea). doi:[10.1080/1028415X.2015.1101304](https://doi.org/10.1080/1028415X.2015.1101304)
34. Wong RH, et al. *Nutrients* 2012;4(5):331. doi:[10.3390/nu4050331](https://doi.org/10.3390/nu4050331)
35. Friling M, et al. *Front Nutr* 2024. doi:[10.3389/fnut.2024.1405156](https://doi.org/10.3389/fnut.2024.1405156)
36. Pinto-Sánchez MI, et al. *Gastroenterology* 2017. doi:[10.1053/j.gastro.2017.04.009](https://doi.org/10.1053/j.gastro.2017.04.009)
37. Rodríguez JM, et al. *Front Nutr* 2022;9:986282. doi:[10.3389/fnut.2022.986282](https://doi.org/10.3389/fnut.2022.986282)
38. Thompson T. *N Engl J Med* 2004;351(19):2021-2 (carta). doi:[10.1056/NEJM200411043511924](https://doi.org/10.1056/NEJM200411043511924)
39. Valente M, et al. *Eur Neuropsychopharmacol* 2024. doi:[10.1016/j.euroneuro.2024.01.008](https://doi.org/10.1016/j.euroneuro.2024.01.008)
40. Ell J, et al. *J Sleep Res* 2023. doi:[10.1111/jsr.13979](https://doi.org/10.1111/jsr.13979)
41. Shinjyo N, et al. *J Evid Based Integr Med* 2020. doi:[10.1177/2515690X20967323](https://doi.org/10.1177/2515690X20967323)
42. Almond S, et al. *Sr Care Pharm* 2021. doi:[10.4140/TCP.n.2021.83](https://doi.org/10.4140/TCP.n.2021.83)
43. Latimer KM, Gunther A, Kopec M. Fatigue in Adults: Evaluation and Management. *Am Fam Physician* 2023;108(1):58-69. PMID 37440739. https://www.aafp.org/pubs/afp/issues/2023/0700/fatigue-adults.html

**Fuentes oficiales y otras:**
44. EMA/HMPC. Community herbal monograph on *Urtica dioica* L.; *Urtica urens* L., folium. EMA/HMPC/508015/2007. https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-urtica-dioica-l-urtica-urens-l-folium_en.pdf ; estado: https://www.ema.europa.eu/es/medicines/herbal/urticae-folium
45. EMA/HMPC. Community herbal monograph on *Urtica dioica* L.; *Urtica urens* L., herba. EMEA/HMPC/170261/2006 (superada). https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-urtica-dioica-l-and-urtica-urens-l-herba_en.pdf
46. EMA/HMPC. European Union herbal monograph on *Urtica dioica* L.; *Urtica urens* L., radix. EMA/HMPC/322646/2023, Rev. 1 (2025-01-22). https://www.ema.europa.eu/system/files/documents/herbal-monograph/urticae-radix-mo_en.pdf
47. EMA/HMPC. Community herbal monograph on *Avena sativa* L., herba. EMEA/HMPC/202966/2007. https://www.ema.europa.eu/en/documents/herbal-monograph/final-community-herbal-monograph-avena-sativa-l-herba_en.pdf ; estado: https://www.ema.europa.eu/en/medicines/herbal/avenae-herba
48. EMA/HMPC. *Avenae fructus*: EMEA/HMPC/368600/2007; estado: https://www.ema.europa.eu/es/medicines/herbal/avenae-fructus
49. MSD Manual Professional. Holy Basil (Shane-McWhorter L; revisión 07/2025). https://www.msdmanuals.com/professional/special-subjects/dietary-supplements/holy-basil
50. MSKCC About Herbs. Holy Basil (actualizada 2026-09-21). https://www.mskcc.org/cancer-care/integrative-medicine/herbs/holy-basil-01
51. The Edinburgh GP Handbook. Tired All The Time / Chronic Fatigue Syndrome (2019-11-17; cita NICE CKS). https://medcal.mvm.ed.ac.uk/wp/gp-handbook/?p=106
52. MedlinePlus. Iron in diet: https://medlineplus.gov/ency/article/002422.htm ; Calcium in diet: https://medlineplus.gov/ency/article/002412.htm ; Magnesium in diet: https://medlineplus.gov/ency/article/002423.htm
53. NIH ODS. Potassium, Health Professional: https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/ ; Magnesium, Consumer: https://ods.od.nih.gov/factsheets/Magnesium-Consumer/
54. USDA, "Stinging Nettles, blanched (Northern Plains Indians)", vía réplica: https://happyforks.com/food/stinging-nettles/7728

---

## 11. Log de búsqueda

Todas las búsquedas se hicieron el 2026-11-10.

| # | Fuente | Consulta | Filtros | Resultados | Usados |
|---|---|---|---|---|---|
| 0 | Archivos locales | Lectura de `SKILL.md` (tabla "Seguridad clínica"), `chapters/ch06-wellbeing.md`, `evidencia/moringa.md`, `glossary.md`, `cheatsheet.md` | — | El capítulo no da gramos para las recetas | Contexto |
| 1 | PubMed | (Ocimum sanctum OR O. tenuiflorum OR tulsi OR holy basil) AND (systematic review[pt] OR meta-analysis[pt]) | tipo | 14 (varios irrelevantes) | 42930516, 33650944 |
| 2 | PubMed | tulsi … AND (stress OR anxiety OR sleep OR cortisol OR fatigue OR cognitive) AND (randomized controlled trial[pt] OR clinical trial[pt]) | tipo | 4 | 41656269, 26571987, 19253862 |
| 3 | PubMed | tulsi … AND (stress OR mood OR sleep OR clinical efficacy) AND (Lopresti OR Jamshidi OR Saxena) | ninguno | 8 | 36185698, 28400848, 21977056, 33650944 |
| 4 | PubMed | (Urtica dioica OR nettle) AND (fatigue OR anemia OR hemoglobin OR iron OR sleep OR anxiety) AND (randomized OR clinical trial OR meta-analysis) | ninguno | 15 | 33915962, 31802554, 34587883, 24273930 |
| 5 | PubMed | Avena sativa herb extract (cognitive OR stress OR mood OR sleep) randomized | ninguno | 3 | 34658781, 21711204, 21563962 |
| 6 | PubMed | tulsi … AND (glucose OR hypoglycemia OR diabetes) AND (randomized OR humans OR clinical) | ninguno | 51 (15 vistos; casi todos in silico u oftalmología) | ninguno |
| 7 | PubMed | tulsi … AND (fertility OR antifertility OR sperm OR thyroid OR anticoagulant OR platelet) | ninguno | 42 (20 vistos) | 42653832, 37829808, 30908416 |
| 8 | PubMed | tulsi … AND (heavy metal OR lead OR cadmium OR arsenic OR mercury) AND (herbal tea OR leaves OR products) | ninguno | 63 (15 vistos) | ninguno |
| 9 | PubMed | Ocimum sanctum[Title] AND (thyroid OR thyroxine OR spermatogenesis OR antifertility OR testis OR reproductive) | título | 15 | 9721597, 21455446, 12099405, 30908416, 24616736 |
| 10 | PubMed | (green oat OR wild green oat OR oat herb OR Avena sativa extract) AND (Kennedy[Author] OR stress OR mood OR cognition) AND (randomized OR placebo) | ninguno | 15 | 36657906, 32485993, 26618715, 22690320, 38962436, 28431885 |
| 11 | WebFetch | mskcc.org …/holy-basil | — | **Bloqueada** (no permitida) | Se buscó otra URL (log 13) |
| 12 | WebSearch | NCCIH holy basil tulsi safety pregnancy | — | 10 (ninguno de NCCIH) | ninguno; NCCIH no tiene ficha de tulsi en los resultados |
| 13 | WebSearch + WebFetch | mskcc.org About Herbs holy basil → …/holy-basil-01; msdmanuals.com …/holy-basil | — | 2 páginas leídas | MSKCC 2026; MSD 2025 |
| 14 | PubMed | tulsi … AND (heavy metals[tiab] OR lead[Title] OR cadmium[Title]) AND (accumulation OR contamination OR health risk) | campos | 6 | 37477710 |
| 15 | PubMed | Ayurvedic herbal medicine products lead mercury arsenic content internet United States India | ninguno | 0 | — |
| 16 | PubMed | (nettle OR Urtica dioica) AND (infusion OR tea OR decoction) AND (iron OR calcium OR magnesium OR potassium OR minerals) | ninguno | 16 | 31708254, 22868119, 22574504, 21916535, 15907975, 27925706 |
| 17 | PubMed | convert_article_ids de 6 estudios de minerales | — | Ninguno tiene texto completo en PMC | — |
| 18 | WebSearch + WebFetch | EMA Urtica folium/herba/radix; Avenae herba/fructus | — | Monografías y páginas de estado | EMA/HMPC/508015/2007; EMEA/HMPC/170261/2006; EMA/HMPC/322646/2023; EMEA/HMPC/202966/2007; páginas de estado |
| 19 | WebFetch | EMA, adendos de *Avena* (2025) y de *Urticae folium* (2022) | — | **Bloqueados** (no permitidos) | — |
| 20 | WebSearch + WebFetch | LactMed stinging nettle; LactMed holy basil → ncbi.nlm.nih.gov/books/NBK501777 y NBK501826 | — | **Bloqueados** (reCAPTCHA) | — |
| 21 | PubMed | (nettle OR Urtica) AND (warfarin OR anticoagulant OR "vitamin K") AND (interaction OR INR); (Urtica[Title] OR nettle[Title]) AND (warfarin OR lithium OR pregnancy …) | ninguno / título | 2; 172 (no leídos todos) | ninguno sobre warfarina o litio |
| 22 | PubMed | (Nepeta cataria OR catnip) AND (sleep OR anxiety OR sedative) AND humans | ninguno | 6 | ninguno clínico |
| 23 | PubMed | (Urtica dioica OR nettle) AND (anaemia OR anemia OR hemoglobin) AND (women OR adolescents OR humans) AND (trial OR randomized) | ninguno | 9 | ninguno en anemia |
| 24 | PubMed | (Urtica dioica OR nettle) AND (pregnancy OR uterine OR abortifacient OR teratogenic) AND (rats OR women OR survey) | ninguno | 15 (10 vistos) | 34876549 |
| 25 | PubMed | nettle sting urticaria | ninguno | 15 (8 vistos) | 20953796, 14744424, 33668609 |
| 26 | PubMed | (valerian OR Valeriana) AND (sleep OR insomnia) AND (meta-analysis[pt] OR systematic review[pt]) | desde 2019 | 21 (10 vistos) | 38359657, 37527850, 33086877, 33509331 |
| 27 | PubMed | gluten contamination commercial oat …; Thompson gluten contamination of commercial oat products in the United States | ninguno | 1; 1 | 36276819, 15525734 |
| 28 | WebSearch + WebFetch | Nettle infusion minerals; Wolska 2016 PDF; Özcan 2008 (AGRIS) | — | Wolska leído; Özcan sin datos de ortiga en el resumen | Wolska 2016 |
| 29 | WebSearch + WebFetch | USDA stinging nettles blanched → happyforks.com | — | 1 réplica | Composición por 100 g |
| 30 | WebFetch | cks.nice.org.uk/topics/tiredness-fatigue-in-adults | — | **Bloqueada** (no permitida) | Se usó AFP 2023 y el resumen de Edinburgh |
| 31 | WebSearch + WebFetch | AFP 2023 Fatigue in Adults; Edinburgh GP Handbook | — | 2 páginas leídas | Latimer 2023; Edinburgh 2019 |
| 32 | PubMed | Latimer fatigue in adults evaluation and management Am Fam Physician 2023 | ninguno | 1 | 37440739 |
| 33 | WebFetch | NIH ODS hojas para profesionales (hierro, calcio, magnesio) | — | **Bloqueadas**; se leyeron MedlinePlus y ODS (potasio; magnesio para consumidor) | Referencias de ingesta |

---

## 12. Datos no confirmados

1. Cantidad de hierro, calcio y magnesio por taza de infusión de **ortiga sola** (los resúmenes solo dan tasas de extracción o medias de varios tés).
2. Si la infusión larga de 4–12 h extrae más minerales que la infusión de 10–15 min.
3. Contenido de minerales y de gluten en la infusión de **paja de avena**.
4. Contenido de vitamina K en la **infusión** de ortiga.
5. Interacción de la ortiga con litio, diuréticos o warfarina en humanos.
6. Hipoglucemia clínica por tulsi junto con antidiabéticos.
7. Seguridad del tulsi y de la ortiga en lactancia según LactMed (bloqueado).
8. Metales pesados en productos comerciales de tulsi importados de India.
9. Dosis de ortiga usadas en el ensayo de la Guerra del Golfo y su efecto sobre la fatiga por separado.
10. Tamaño de muestra del ensayo de cognición con tulsi de Sampath 2015.
11. Las cifras de estrés y sueño del ensayo de avena verde en fumadores (Friling 2024).
12. Conclusiones de la revisión periódica 2020–2022 de la monografía EMA de la hoja de ortiga y de la revisión 2024 de *Avenae herba*.
13. Financiación de los ensayos de extractos comerciales.
14. Contenido actual de NICE CKS "Tiredness/fatigue in adults" (solo se leyó un resumen secundario de 2019).
