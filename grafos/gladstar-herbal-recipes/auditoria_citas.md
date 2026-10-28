# Auditoría de citas: alertas.json

Fecha: 2026-10-28. Se revisaron las referencias que los agentes A–F citaron de memoria, sin abrirlas. Herramientas: PubMed (lookup_article_by_citation, get_article_metadata, search_articles) y WebSearch/WebFetch para los organismos.

Resultado: **15 confirmadas · 7 corregidas · 1 no confirmada** (23 citas).

## Tabla

| Cita | Estado | Identificador | Cambio hecho |
|---|---|---|---|
| Kearns 2003, N Engl J Med (farmacología del desarrollo) | confirmada | PMID 13679531 · doi:10.1056/NEJMra035092 | Ninguno. Solo aparece en verif_C, no en el texto de ninguna alerta. |
| Dworkin 2007, Clin Infect Dis (manejo del herpes zóster) | corregida | PMID 17143845 · doi:10.1086/510206 | La guía no exige iniciar en 72 h: dice que todos los ensayos empezaron en ese plazo, y que los antivirales reducen el dolor agudo y prolongado. h_oats se reescribió así. |
| Collinson 2020, Cochrane CD003048.pub4 (probióticos en diarrea aguda) | confirmada | PMID 33295643 · doi:10.1002/14651858.CD003048.pub4 | Ninguno. Respalda «beneficio dudoso» en r_slippery_elm_gruel: probablemente poca o ninguna diferencia en la diarrea de 48 h o más. |
| Freedman 2018, N Engl J Med (PROGUT) | confirmada | PMID 30462939 · doi:10.1056/NEJMoa1802597 | Ninguno. Probiótico combinado sin efecto en niños. Se cita en verif_C, no en la alerta. |
| Schnadower 2018, N Engl J Med (LGG frente a placebo) | confirmada | PMID 30462938 · doi:10.1056/NEJMoa1802598 | Ninguno. LGG sin beneficio en niños. Se cita en verif_C, no en la alerta. |
| Monografía EMA de regaliz (*Glycyrrhizae radix*) | corregida | EMA/HMPC/108399/2024, Rev. 1, adoptada el 04-03-2026: https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-glycyrrhiza-glabra-l-glycyrrhiza-inflata-bat-glycyrrhiza-uralensis-fisch-radix-revision-1_en.pdf | Se confirman: máximo de 4 semanas; no recomendado en hipertensión, enfermedad renal, hepática o cardiovascular ni hipopotasemia; no recomendado en embarazo ni lactancia; no combinar con diuréticos, glucósidos cardíacos, corticoides ni laxantes estimulantes. La edad estaba mal: la EMA no lo recomienda en **menores de 18 años**, no en menores de 12. Se corrigió en r_formula_for_lung_and_chest_congestion (ahora «menores de 18 años», EMA/HMPC 2026) y en la versión fusionada de h_licorice. |
| Monografía EMA de equinácea (*E. purpurea herba recens*) | confirmada | EMA/HMPC/48704/2014 Corr 1: https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-echinacea-purpurea-l-moench-herba-recens_en.pdf | Dice que no se recomienda en menores de 12 años, que está contraindicada si hay hipersensibilidad a las compuestas y que puede causar reacciones graves en atópicos (broncoespasmo, anafilaxia). Se añadió «EMA 2014» a h_echinacea. |
| Aviso MHRA 2012 (equinácea oral, menores de 12 años) | confirmada | 20-08-2012, según fuente secundaria: https://www.nutraingredients.com/Article/2012/08/20/UK-Echinacea-not-suitable-for-under-12s/ | Ninguno. No se pudo abrir la página de gov.uk. La EMA 2014 dice lo mismo. |
| LiverTox, usnea / ácido úsnico | no confirmada | La entrada (NBK548493) aparece en las búsquedas, pero el enlace está bloqueado o pide captcha. Fuentes alternativas: Durazo 2004, PMID 15128366, doi:10.1111/j.1572-0241.2004.04165.x; aviso de la FDA de 2001 sobre LipoKinetix (https://www.mskcc.org/cancer-care/treatments/symptom-management/integrative-medicine/herbs/news-alerts/fda-warning-regarding-lipokinetix-weight-loss-supplement) | Se quitó «LiverTox» de h_usnea y de r_ear_infection_tincture, y se puso Durazo 2004 (fallo hepático fulminante con trasplante por ácido úsnico puro). La afirmación clínica se mantiene. |
| LiverTox, chaparral | corregida | https://www.ncbi.nlm.nih.gov/books/NBK548355/ (actualizada el 25-05-2022) | Se confirman la hepatitis, la cirrosis, la insuficiencia hepática aguda y el trasplante (puntuación B). LiverTox no habla del uso tópico, así que se suavizó «no hay casos sobre piel intacta» a «no consta daño hepático… aunque no se ha estudiado» en r_antifungal_powder y h_chaparral. Sheikh 1997 (PMID 9129552) también se confirma: 13 hepatotoxicidades, 4 cirrosis y 2 trasplantes. |
| DeKosky 2008, JAMA (GEM) | confirmada | PMID 19017911 · doi:10.1001/jama.2008.683 | Ninguno. Sin efecto en la incidencia de demencia (HR 1,12) ni en la progresión del DCL. |
| Holubarsch 2008, Eur J Heart Fail (SPICE) | confirmada | PMID 19019730 · doi:10.1016/j.ejheart.2008.10.004 | Ninguno. Sin efecto en el desenlace principal; seguro junto al tratamiento óptimo. |
| Zick 2009, Eur J Heart Fail (HERB CHF) | confirmada | PMID 19789403 · doi:10.1093/eurjhf/hfp116 | Ninguno. Sin beneficio funcional y con más eventos adversos. Esto se añadió al texto fusionado de h_hawthorn, porque F decía «bien tolerado». |
| Tankanow 2003, J Clin Pharmacol | confirmada | PMID 12817526 | Ninguno. El espino no alteró la farmacocinética de la digoxina. |
| Vanderperren 2005, Ann Pharmacother | corregida | PMID 15956233 · doi:10.1345/aph.1E670 | Es un solo caso con causalidad «posible». «El abuso se ha asociado a daño hepático y renal» pasó a «Se ha descrito un caso de fallo hepático con daño renal por abuso de sen» (h_senna). |
| Bowman 2021, BMC Complement Med Ther | confirmada | PMID 33563275 · doi:10.1186/s12906-021-03230-4 | Ninguno. Evidencia débil; sin daño ni beneficio demostrados. |
| Rosti 1994, Acta Paediatr | corregida | PMID 7919774 · doi:10.1111/j.1651-2227.1994.tb13115.x | La tisana no era solo de hinojo. Las madres tomaban más de 2 L al día de una mezcla de regaliz, hinojo, anís y galega (según LactMed). Se reescribió en h_fennel. |
| LactMed (hinojo; búsqueda de hierbas en la lactancia) | confirmada | LactMed «Fennel» (texto reproducido en https://drugs.com/breastfeeding/fennel.html); NBK501922 | Ninguno. El efecto sobre la leche no está establecido y no sube la prolactina. |
| ACOG (duchas vaginales) | confirmada | Guía ACOG de vaginitis 2006, resumida en AFP: https://aafp.org/pubs/afp/issues/2006/1101/p1639a.html | Ninguno en el texto. La fuente corta de h_goldenseal pasa a ser «ACOG 2006». |
| Monografía EMA de cáscara sagrada (*Rhamni purshianae cortex*) | confirmada | EMA/HMPC/726270/2016, Rev. 1 (2020): https://www.ema.europa.eu/en/medicines/herbal/rhamni-purshianae-cortex | Ninguno. Solo para mayores de 12 años, máximo 1 semana, no en embarazo ni lactancia. |
| Brendler 2022, Front Pharmacol (buchu) | corregida | PMID 35197854 · doi:10.3389/fphar.2022.813142 | Se confirma que no hay ensayos en infección urinaria. La pulegona (31–73 %) está en el **aceite esencial** de *A. crenulata* y apenas pasa al extracto acuoso. h_buchu se precisó en ese sentido. |
| Estimación propia de cafeína de las Zoom Balls (lote A) | corregida | Schimpl 2013, PMID 23981847, doi:10.1016/j.jep.2013.08.023 (guaraná hasta 6 %); receta en texto.txt: 5 oz de guaraná, 2 oz de cola, 60 bolitas | Ahora se presenta como **estimación** propia. Con guaraná al 2,5–6 % y cola al 1,5–2,5 % salen unos 70–165 mg por bolita; el lote A daba 85–165. No incluye el chocolate. «Superan» pasó a «pueden superar» (r_zoom_balls). |
| Restricciones de ashwagandha (fuente secundaria, lote A) | corregida | ANSES 2024: https://www.nutraingredients.com/Article/2024/06/17/French-agency-warns-ashwagandha-unsafe-in-specific-populations ; Dinamarca y RIVM: https://www.nutraingredients.com/Article/2026/07/06/timeline-will-authorities-de-throne-the-king-of-herbs/ | Dinamarca prohibió la ashwagandha en complementos tras el informe DTU de 2020; no se confirmó el año exacto, así que se quitó «2023». Francia no la desaconseja en general, sino en el embarazo, la lactancia, los menores de 18 años, los trastornos tiroideos, hepáticos o cardíacos y con depresores del SNC. Países Bajos (RIVM, 2024) desaconseja su uso. Fuente corta: «DVFA 2023» pasó a «ANSES 2024». |

Otros cambios en la consolidación (no son citas de la lista): en h_crampbark se quitaron las fuentes vagas «PubMed 2026; Cochrane 2025» del lote F y se dejó Dante 2013. En h_comfrey, la EMA se cita sin año, porque los lotes daban 2015 y 2021 para documentos distintos.

## Log de búsqueda

| Fuente | Query / acción | Resultados | Usados |
|---|---|---|---|
| PubMed lookup_article_by_citation | Kearns NEJM 2003; Dworkin CID 2007; Freedman y Schnadower NEJM 2018; DeKosky JAMA 2008; Holubarsch EJHF 2008; Zick EJHF 2009; Tankanow J Clin Pharmacol 2003; Vanderperren Ann Pharmacother 2005; Bowman BMC 2021; Rosti Acta Paediatr 1994; Brendler Front Pharmacol 2022 | 12 citas (2 ambiguas) | 12 |
| PubMed get_article_metadata | 15 PMID (los anteriores más los candidatos ambiguos); salida guardada y procesada con Python | 15 | 13 |
| PubMed search_articles | Collinson S[Author] probiotics acute infectious diarrhoea Cochrane | 1 | 1 |
| PubMed search_articles | Sheikh NM chaparral-associated hepatotoxicity 1997 | 1 | 1 |
| PubMed search_articles | usnic acid fulminant liver failure weight loss supplement | 7 | 0 |
| PubMed search_articles | Durazo FA fulminant liver failure usnic acid | 1 | 1 |
| PubMed search_articles | guarana Paullinia cupana seed caffeine content review | 2 | 1 |
| WebSearch / WebFetch | MHRA 2012 oral echinacea children under 12 | 10 | 1 (nutraingredients) |
| WebSearch / WebFetch | Brendler 2022 buchu pulegone (PMC y frontiersin bloqueados; PDF de frontiersin abierto) | 10 | 1 |
| WebSearch / WebFetch | LiverTox usnic acid / NBK548493 (captcha o fuera de la lista permitida) | 20 | 0 |
| WebSearch | FDA 2001 LipoKinetix usnic acid | 10 | 1 |
| WebSearch / WebFetch | LiverTox chaparral (NBK548355) | 10 | 1 |
| WebSearch / WebFetch | EMA Glycyrrhizae radix Rev. 1 2026 (PDF de la monografía) | 10 | 1 |
| WebSearch / WebFetch | EMA Echinacea purpurea herba recens (PDF de la monografía) | 10 | 1 |
| WebSearch / WebFetch | EMA Rhamni purshianae cortex | 10 | 1 |
| WebSearch / WebFetch | Dworkin 2007, 72 h (PDF de la guía) | 10 | 1 |
| WebSearch / WebFetch | LactMed fennel (texto en drugs.com) | 10 | 1 |
| WebSearch / WebFetch | ACOG douching (AFP 2006) | 10 | 1 |
| WebSearch / WebFetch | DVFA, ANSES y RIVM sobre ashwagandha (nutraingredients 2023, 2024 y 2026) | 37 | 2 |
| texto.txt | Receta de Zoom Balls (cantidades de guaraná y cola, 60 bolitas) | 1 | 1 |
