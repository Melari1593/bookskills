# Verificación de alertas 9 a 16 — "Seguridad clínica" (healing-herbal-infusions)

Fecha de verificación: 2026-11-03.
Alcance: alertas 9 a 16 de `/home/claude/verif-hhi/tabla.md`.
Método: búsqueda en PubMed (con DOI) y en fuentes oficiales (EMA/HMPC, NCCIH, CDC, ACOG, LactMed, SPS-NHS).
Regla de atribución: los datos marcados "según PubMed" vienen de artículos recuperados de PubMed. El DOI va en cada referencia.

## Resumen

| # | Alerta | Veredicto | Confianza |
|---|---|---|---|
| 9 | Clavo para el dolor de muela | Confirmada con matices | Alta |
| 10 | Cúrcuma con pimienta | Corregir | Alta |
| 11 | Espino blanco e hibisco | Corregir | Media |
| 12 | Equinácea y saúco | Confirmada con matices | Alta (equinácea) · Baja (saúco/autoinmunes) |
| 13 | Asteráceas | Confirmada | Alta |
| 14 | Cannabis | Confirmada con matices | Alta |
| 15 | Amapola de California y pasiflora | Confirmada con matices | Media |
| 16 | Embarazo y lactancia | Corregir | Media |

---

## 9. Clavo para el dolor de muela

**Veredicto:** confirmada con matices. **Confianza:** alta.

**Afirmaciones:**
- "El aceite de clavo (eugenol) es tóxico si un niño lo ingiere." **Confirmada.** La EMA describe casos en niños menores de 2 años tras ingerir 5–10 ml. Los efectos fueron depresión del SNC, coma, convulsiones, hipoglucemia, acidosis metabólica, CID e insuficiencia hepática fulminante. Se usó N-acetilcisteína como antídoto. Según PubMed hay casos publicados (Lane 1991: lactante de 7 meses; Kim 2018: NAC precoz).
- "Guárdalo fuera de su alcance." **Confirmada** como medida razonable.
- "El dolor dental necesita odontólogo." **Confirmada.** La EMA limita la indicación tradicional a "alivio temporal" del dolor por caries.
- **Matiz que falta:** la EMA no recomienda el aceite de clavo dental en menores de 18 años (faltan datos). También pide evitar el contacto con las encías. El aceite concentrado irrita la mucosa.

**Texto propuesto (Alerta):**
> El aceite de clavo (eugenol) ingerido por un niño pequeño puede causar coma, convulsiones e insuficiencia hepática (5–10 ml en menores de 2 años). Guárdalo fuera de su alcance. La EMA no lo recomienda en menores de 18 años. Evita el contacto con la encía. Es solo un alivio temporal: el dolor dental necesita odontólogo (EMA/HMPC/534924/2010).

**Referencias:**
- EMA/HMPC. Community herbal monograph on *Syzygium aromaticum*, floris aetheroleum. EMA/HMPC/534924/2010 (efectiva 13/09/2011). https://www.ema.europa.eu/en/medicines/herbal/caryophylli-floris-aetheroleum
- EMA/HMPC. Assessment report on *Syzygium aromaticum* flos et floris aetheroleum. EMA/HMPC/534946/2010, sección 5.5 (casos Hartnoll 1993, Brown 1992, Eisen 2004, Janes 2005). https://ema.europa.eu/en/documents/herbal-report/final-assessment-report-syzygium-aromaticum-l-merill-et-lm-perry-flos-syzygium-aromaticum-l-merill_en.pdf
- Lane BW et al. Clove oil ingestion in an infant. Hum Exp Toxicol. 1991. doi:10.1177/096032719101000410 (según PubMed)
- Kim A et al. Early administration of N-acetylcysteine in the treatment of clove oil ingestion. J Pediatr Gastroenterol Nutr. 2018. doi:10.1097/MPG.0000000000001988 (según PubMed)

---

## 10. Cúrcuma con pimienta

**Veredicto:** corregir. **Confianza:** alta.

**Afirmaciones:**
- "La piperina también aumenta la absorción de algunos medicamentos." **Confirmada.** Según PubMed, en humanos 20 mg/día de piperina aumentaron la exposición a fenitoína, carbamazepina (AUC +48 %, Cmáx +69 %) y nevirapina (AUC ~+170 %). El mecanismo probable es la inhibición de CYP3A4 y mayor absorción. Son estudios pequeños, con dosis de suplemento, no de condimento.
- "La cúrcuma potencia los anticoagulantes." **Exagerada.** Según PubMed, el único estudio clínico encontrado (Meriva®, 10 días) no cambió el INR con warfarina ni con dabigatrán. Tampoco cambió el tiempo de sangría con antiagregantes. En ratas, la curcumina alteró la farmacocinética de la warfarina sin cambiar el tiempo de protrombina. La monografía EMA dice "interacciones: ninguna notificada", y la adenda EMA de 2025 no menciona la warfarina. El riesgo es teórico (efecto antiagregante in vitro) y se basa en casos aislados. Debe decir "puede", no "potencia".
- "Hay casos de hepatotoxicidad con preparados de cúrcuma de alta biodisponibilidad." **Confirmada y reforzada.** Según PubMed, la red DILIN reporta 10 casos (1 muerte), con latencia de 1–4 meses y fuerte asociación con HLA-B*35:01. Tres productos contenían piperina. En Toscana hubo 7 casos, todos con formulaciones de alta biodisponibilidad y dosis altas. La adenda EMA 2025 confirma el riesgo con formulaciones de alta biodisponibilidad o dosis altas. No hay toxicidad descrita con las dosis de la monografía.
- **Matiz que falta:** la EMA no recomienda la cúrcuma en obstrucción biliar, colangitis, enfermedad hepática ni cálculos biliares. Tampoco en menores de 18 años, embarazo ni lactancia.

**Texto propuesto (Alerta):**
> La piperina aumenta la absorción de algunos fármacos (fenitoína, carbamazepina, nevirapina). Con anticoagulantes o antiagregantes, la cúrcuma puede sumar riesgo de sangrado; los datos humanos son escasos. Los suplementos concentrados o con pimienta causan hepatitis (latencia 1–4 meses). Evítala con enfermedad hepática o biliar (DILIN 2022, doi:10.1016/j.amjmed.2022.09.026; EMA 2018/2025).

**Referencias:**
- Halegoua-DeMarzio D et al. Liver injury associated with turmeric — ten cases from DILIN. Am J Med. 2023;136:200-6. doi:10.1016/j.amjmed.2022.09.026 (según PubMed)
- Lombardi N et al. Acute liver injury following turmeric use in Tuscany. Br J Clin Pharmacol. 2021;87:741-53. doi:10.1111/bcp.14460 (según PubMed)
- Garaizabal Azkue ÍJ et al. Turmeric associated liver injury with susceptible HLA. Rev Esp Enferm Dig. 2024. doi:10.17235/reed.2024.10763/2024 (según PubMed; caso con 60 mg curcumina + 10 mg pimienta)
- Bedada SK et al. Piperine and carbamazepine in healthy volunteers. Drug Res. 2017. doi:10.1055/s-0042-118173 (según PubMed)
- Kasibhatta R, Naidu MUR. Piperine and nevirapine. Drugs R D. 2007. doi:10.2165/00126839-200708060-00006 (según PubMed)
- Pattanaik S et al. Piperine and phenytoin in epilepsy. Phytother Res. 2006. doi:10.1002/ptr.1937 (según PubMed)
- Velpandian T et al. Piperine in food and phenytoin. Eur J Drug Metab Pharmacokinet. 2001. doi:10.1007/BF03226378 (según PubMed)
- Hu S, Belcaro G, Dugall M et al. Interaction study between antiplatelet agents, anticoagulants, thyroid replacement therapy and a bioavailable formulation of curcumin (Meriva®). Eur Rev Med Pharmacol Sci. 2018;22:5042-6. doi:10.26355/eurrev_201808_15647 (según PubMed)
- Liu AC et al. Curcumin and warfarin/clopidogrel in rats. Planta Med. 2013. doi:10.1055/s-0032-1328652 (según PubMed)
- EMA/HMPC. EU herbal monograph on *Curcuma longa* L., rhizoma, Rev. 1. EMA/HMPC/329755/2017 (adoptada 25/09/2018). https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-curcuma-longa-l-rhizoma-revision-1_en.pdf
- EMA/HMPC. Addendum to assessment report on *Curcuma longa*. EMA/HMPC/81467/2025 (19/11/2025). https://www.ema.europa.eu/en/documents/herbal-report/final-addendum-assessment-report-curcuma-longa-l-rhizoma_en.pdf

---

## 11. Espino blanco e hibisco

**Veredicto:** corregir. **Confianza:** media.

**Afirmaciones:**
- "El espino puede interactuar con la digoxina." **Corregir (sin evidencia clínica).** Según PubMed, un ensayo cruzado (n = 8, extracto WS 1442, 900 mg/día, 3 semanas) no cambió la farmacocinética de la digoxina. La monografía EMA de *Crataegus* dice "interacciones: ninguna notificada". El informe de evaluación EMA cita una posible suma farmacodinámica en modelos celulares e interferencia con un inmunoensayo de digoxina. La alerta debe hablar de suma de efecto teórica con fármacos cardiacos, no de interacción probada.
- **Matiz que falta (espino):** la EMA exige que un médico descarte enfermedad cardiaca grave antes de usarlo. No lo recomienda en menores de 18 años para síntomas cardiacos. Pide consulta urgente si hay edema de piernas, dolor torácico irradiado o disnea.
- "El hibisco baja la presión arterial." **Confirmada.** Según PubMed, un metaanálisis de 17 ECA mostró −7,1 mmHg de PAS frente a placebo. Una revisión paraguas (26 ECA, 1797 participantes) muestra un efecto dependiente de la dosis, similar a algunos antihipertensivos. **Matiz:** el riesgo clínico es la suma con antihipertensivos (hipotensión). No se halló un ensayo de interacción directo.

**Texto propuesto (Alerta):**
> El hibisco baja la presión arterial (−7 mmHg sistólica en metaanálisis); con antihipertensivos, vigila hipotensión. El espino no cambió la digoxina en un estudio pequeño, pero puede sumar efecto a fármacos cardiacos. Úsalo solo si un médico descartó enfermedad cardiaca. Consulta urgente si hay dolor torácico, disnea o edema (doi:10.1093/nutrit/nuab104; EMA/HMPC/159075/2014).

**Referencias:**
- Tankanow R et al. Interaction study between digoxin and a preparation of hawthorn. J Clin Pharmacol. 2003;43:637-42. PMID 12817526 (según PubMed; DOI no devuelto por PubMed)
- EMA/HMPC. EU herbal monograph on *Crataegus* spp., folium cum flore. EMA/HMPC/159075/2014 (borrador 13/10/2014; versión adoptada 2016; revisión 1 en consulta 2025). https://www.ema.europa.eu/en/medicines/herbal/crataegi-folium-cum-flore
- EMA/HMPC. Assessment report on *Crataegus* spp., folium cum flore. EMA/HMPC/159076/2014 (05/04/2016), sección 3.1.4. https://ema.europa.eu/en/documents/herbal-report/final-assessment-report-crataegus-spp-folium-cum-flore_en.pdf
- Ellis LR et al. Hibiscus sabdariffa on blood pressure and cardiometabolic markers: SR/MA. Nutr Rev. 2022;80:1723-37. doi:10.1093/nutrit/nuab104 (según PubMed)
- Efficacy and safety of *Hibiscus sabdariffa* in cardiometabolic health: overview of reviews and dose-response MA. Complement Ther Med. 2025. doi:10.1016/j.ctim.2025.103135 (según PubMed)
- Serban C et al. Sour tea on arterial hypertension: SR/MA. J Hypertens. 2015. doi:10.1097/HJH.0000000000000585 (según PubMed)

---

## 12. Equinácea y saúco

**Veredicto:** confirmada con matices. **Confianza:** alta (equinácea) · baja (saúco en enfermedades autoinmunes).

**Afirmaciones:**
- "La evidencia en humanos es inconsistente (Cochrane)." **Confirmada.** Según PubMed, la revisión Cochrane 2014 (24 ECA, 4631 participantes) no mostró beneficio en el tratamiento. En prevención, un análisis post hoc sugiere una reducción relativa del 10–20 %, de relevancia clínica dudosa. Los productos difieren mucho entre sí.
- "Preséntalos como opción de bajo riesgo." **Confirmada con matices.** La EMA describe reacciones de hipersensibilidad graves (incluido Stevens-Johnson). Hay riesgo mayor en atopia. La EMA no recomienda la equinácea en menores de 12 años. Tampoco la recomienda en enfermedades sistémicas progresivas, enfermedades autoinmunes, inmunodeficiencia o inmunosupresión.
- **Saúco y evidencia:** según PubMed, un metaanálisis (n = 180) informa beneficio, pero es pequeño. El NCCIH (2024) lo califica como "investigación preliminar". La EMA no pudo establecer monografía para el fruto (falta posología tradicional). La flor (*Sambuci flos*) tiene monografía tradicional para resfriado inicial.
- "El saúco no es adecuado en enfermedades autoinmunes." **Sin evidencia suficiente, pero plausible.** Ni la EMA (flor ni fruto) ni el NCCIH lo mencionan. Una única cohorte retrospectiva (Faden 2024, n = 673) asoció el saúco a brotes de dermatomiositis y lupus cutáneo. Es una asociación temporal, no causal. La contraindicación oficial en autoinmunes es de la **equinácea** (EMA).
- **Matiz que falta (saúco):** las bayas crudas o verdes, las hojas y los tallos tienen glucósidos cianogénicos. Causan náuseas, vómito y diarrea. Hay que cocinar las bayas (NCCIH).

**Texto propuesto (Alerta):**
> La evidencia es débil e inconsistente: Cochrane no halla beneficio de la equinácea en el tratamiento del resfriado. No la uses en enfermedades autoinmunes, inmunosupresión ni menores de 12 años. El saúco se asoció a brotes de dermatomiositis y lupus (dato observacional). Cocina siempre las bayas de saúco (Cochrane 2014, doi:10.1002/14651858.CD000530.pub3; EMA/HMPC/48704/2014).

**Referencias:**
- Karsch-Völk M et al. Echinacea for preventing and treating the common cold. Cochrane Database Syst Rev. 2014;(2):CD000530. doi:10.1002/14651858.CD000530.pub3 (según PubMed)
- EMA/HMPC. EU herbal monograph on *Echinacea purpurea* (L.) Moench, herba recens. EMA/HMPC/48704/2014 Corr 1 (adoptada 24/11/2014). https://www.ema.europa.eu/en/documents/herbal-monograph/final-european-union-herbal-monograph-echinacea-purpurea-l-moench-herba-recens_en.pdf
- Hawkins J et al. Black elderberry supplementation: MA of RCTs. Complement Ther Med. 2019;42:361-5. doi:10.1016/j.ctim.2018.12.004 (según PubMed)
- NCCIH. Elderberry. Última actualización: noviembre 2024. https://www.nccih.nih.gov/health/elderberry
- EMA/HMPC. Public statement on *Sambucus nigra* L., fructus. EMA/HMPC/32465/2013. https://www.ema.europa.eu/en/medicines/herbal/sambuci-fructus
- EMA/HMPC. Community herbal monograph on *Sambucus nigra* L., flos. EMEA/HMPC/283166/2007 (03/07/2008).
- Faden DF et al. Supplement use and disease exacerbation in dermatomyositis and cutaneous lupus. ACR Open Rheumatol. 2024. doi:10.1002/acr2.11735 (fuente secundaria Healio; **no verificado en PubMed**)

---

## 13. Asteráceas

**Veredicto:** confirmada. **Confianza:** alta.

**Afirmaciones:**
- "Si hay alergia a la ambrosía o a otras asteráceas, hay riesgo de reacción cruzada." **Confirmada.** La EMA contraindica la equinácea y el aceite de manzanilla si hay hipersensibilidad a otras asteráceas. La EMA describe anafilaxia por contacto mucoso con preparados líquidos de manzanilla. El NCCIH (2025) señala más riesgo de alergia a la manzanilla si hay alergia a ambrosía, crisantemos o margaritas. Según PubMed, hay un caso de anafilaxia por equinácea en una paciente atópica. El 19–20 % de los atópicos tenía IgE contra equinácea. También hay reacción cruzada en dermatitis de contacto.
- **Matiz que falta:** la atopia (no solo la alergia conocida) aumenta el riesgo. La reacción puede ocurrir con el primer uso. El riesgo incluye el uso tópico (caléndula, árnica, manzanilla).

**Texto propuesto (Alerta):**
> Si hay alergia a la ambrosía, a la margarita o a otras asteráceas, no uses estas plantas. Hay riesgo de reacción cruzada, incluso anafilaxia y con el primer uso. Las personas con atopia tienen más riesgo. Esto incluye el uso tópico (EMA/HMPC/48704/2014; Mullins 1998, doi:10.5694/j.1326-5377.1998.tb126773.x).

**Referencias:**
- EMA/HMPC. EU herbal monograph on *Echinacea purpurea*, herba recens. EMA/HMPC/48704/2014 Corr 1, secciones 4.3, 4.4, 4.8.
- EMA/HMPC. EU herbal monograph on *Matricaria recutita* L., aetheroleum. EMA/HMPC/278814/2010 (07/07/2015), secciones 4.3, 4.8. Copia: https://www.e-lactancia.org/media/papers/ManzanillaComun-EMA2015.pdf
- NCCIH. Chamomile: Science and Safety (boletín 06/03/2025). https://content.govdelivery.com/accounts/USNIHNCCIH/bulletins/3d59816
- Mullins RJ. Echinacea-associated anaphylaxis. Med J Aust. 1998;168:170-1. doi:10.5694/j.1326-5377.1998.tb126773.x (según PubMed)
- Paulsen E, Andersen KE. Colophonium and Compositae mix as markers of fragrance allergy. Contact Dermatitis. 2005. doi:10.1111/j.0105-1873.2005.00704.x (según PubMed)

---

## 14. Cannabis

**Veredicto:** confirmada con matices. **Confianza:** alta.

**Afirmaciones:**
- "No lo uses en embarazo." **Confirmada.** Según PubMed, un metaanálisis JAMA Pediatrics 2025 (51 estudios, ajustado por tabaco) mostró más bajo peso al nacer (OR 1,75), parto pretérmino (OR 1,52) y PEG (OR 1,57). La certeza es moderada. Una revisión paraguas BMJ 2023 califica de "convincente" la asociación con PEG y bajo peso. ACOG (Consenso Clínico n.º 10, sept. 2025) dice que no hay indicaciones médicas en embarazo ni lactancia.
- "No lo uses en lactancia." **Confirmada.** El CDC (2024) aconseja no usar marihuana ni CBD durante la lactancia. **Matiz:** según un resumen secundario, ACOG 2025 no considera el uso de cannabis una contraindicación para amamantar. Recomienda apoyar la lactancia y reducir la exposición (no verificado en el texto original de ACOG).
- "Puede potenciar los sedantes." **Confirmada.** Según PubMed, una revisión JAMA 2026 recomienda evitar el uso con alcohol, benzodiacepinas u otros depresores del SNC. También pide no conducir. La revisión BMJ 2023 confirma somnolencia y efectos adversos del SNC.
- **Matiz que falta:** el cannabis aumenta el riesgo de choque vehicular y de psicosis. También tiene interacciones farmacocinéticas por CYP (THC y CBD).

**Texto propuesto (Alerta):**
> No lo uses en el embarazo: se asocia a bajo peso, parto pretérmino y PEG. No lo uses durante la lactancia (CDC). Suma sedación con alcohol, benzodiacepinas y opioides. No conduzcas después de usarlo. Evítalo si hay antecedente de psicosis (JAMA Pediatr 2025, doi:10.1001/jamapediatrics.2025.0689; ACOG 2025).

**Referencias:**
- Lo JO et al. Prenatal cannabis use and neonatal outcomes: SR/MA. JAMA Pediatr. 2025;179:738-46. doi:10.1001/jamapediatrics.2025.0689 (según PubMed)
- Sainz K et al. Meta-analysis of maternal and neonatal outcomes of cannabis use in pregnancy. Matern Health Neonatol Perinatol. 2025. doi:10.1186/s40748-025-00216-9 (según PubMed)
- Solmi M et al. Balancing risks and benefits of cannabis use: umbrella review. BMJ. 2023;382:e072348. doi:10.1136/bmj-2022-072348 (según PubMed)
- Hsu M et al. Therapeutic use of cannabis and cannabinoids: a review. JAMA. 2026;335:345-59. doi:10.1001/jama.2025.19433 (según PubMed)
- CDC. Marijuana and breastfeeding (revisado 26/02/2024). https://cdc.gov/breastfeeding-special-circumstances/hcp/vaccine-medication-drugs/marijuana.html
- ACOG. Clinical Consensus No. 10: Cannabis Use During Pregnancy and Lactation (sept. 2025). Consultado vía resumen secundario: https://www.epocrates.com/online/article/acog-calls-for-universal-cannabis-screening-in-pregnancy-and-postpartum

---

## 15. Amapola de California y pasiflora

**Veredicto:** confirmada con matices. **Confianza:** media.

**Afirmaciones:**
- "Pueden sumar sedación con benzodiacepinas." **Confirmada como precaución oficial para la pasiflora.** La EMA no recomienda usarla con sedantes sintéticos (p. ej., benzodiacepinas) sin indicación médica. No hay datos clínicos de interacción. Para la amapola de California, la EMA dice "interacciones: ninguna notificada". Según PubMed, en ratones el flumazenil revierte su efecto sedante (acción sobre el receptor benzodiacepínico). Su alcaloide (S)-reticulina modula receptores GABA-A. La suma es plausible, pero no está demostrada en humanos.
- "Con alcohol u opioides." **Sin evidencia directa.** No se hallaron estudios. Se mantiene por plausibilidad farmacodinámica; debe decir "pueden".
- "No conduzcas después de tomarlas." **Confirmada.** La EMA dice que ambas "pueden alterar la capacidad de conducir y usar máquinas".
- **Matiz que falta:** según PubMed, el extracto etanólico (tintura) de amapola de California inhibe CYP3A4, 2C9, 2C19 y 2D6 in vitro. La infusión acuosa no mostró ese efecto. La EMA no recomienda la amapola en menores de 18 años (borrador) ni la pasiflora en menores de 12. Tampoco recomienda ninguna de las dos en embarazo ni lactancia.

**Texto propuesto (Alerta):**
> Pueden alterar la capacidad de conducir: no conduzcas después de tomarlas. Pueden sumar sedación con benzodiacepinas, alcohol u opioides; no las combines sin indicación médica. La tintura de amapola de California inhibe enzimas CYP in vitro. No las uses en embarazo ni lactancia (EMA/HMPC/669740/2013; EMA/HMPC/680372/2013; doi:10.1055/s-0042-103689).

**Referencias:**
- EMA/HMPC. Community herbal monograph on *Passiflora incarnata* L., herba. Versión 2007 (EMEA/HMPC/230962/2006), secciones 4.5, 4.6, 4.7; Rev. 1 vigente EMA/HMPC/669740/2013 (18/06/2014). https://www.ema.europa.eu/en/medicines/herbal/passiflorae-herba
- EMA/HMPC. EU herbal monograph on *Eschscholzia californica* Cham., herba. EMA/HMPC/680372/2013 (publicada 06/05/2015); adenda EMA/HMPC/648153/2022 (sin nuevos datos de seguridad). https://www.ema.europa.eu/medicines/herbal/eschscholziae-herba
- Rolland A et al. Neurophysiological effects of an extract of *Eschscholzia californica*. Phytother Res. 2001. doi:10.1002/ptr.884 (según PubMed)
- Fedurco M et al. *Eschscholzia californica* alkaloids on GABA-A receptors. Biochem Res Int. 2015. doi:10.1155/2015/617620 (según PubMed)
- Manda VK et al. Modulation of CYPs, P-gp and PXR by *Eschscholzia californica*. Planta Med. 2016. doi:10.1055/s-0042-103689 (según PubMed)

---

## 16. Embarazo y lactancia

**Veredicto:** corregir. **Confianza:** media.

**Afirmaciones:**
- "Ninguna receta tiene datos de seguridad en el embarazo." **Confirmada con matices.** Todas las monografías EMA revisadas dicen "seguridad en embarazo y lactancia no establecida": *Crataegus*, *Curcuma*, *Passiflora*, *Eschscholzia*, *Echinacea* y *Sambucus* flos. "Ninguna" es una generalización: no se revisaron todas las plantas del libro. Se propone "la mayoría".
- "Si está embarazada, no recomiendes tinturas ni dosis medicinales sin valoración." **Confirmada.** Coincide con la fórmula EMA "no recomendado en ausencia de datos suficientes". **Matiz:** las tinturas además contienen etanol.
- "La salvia y la menta reducen la leche" (lo que dice el libro; la alerta no lo corrige). **Corregir.** LactMed (15/07/2025) dice que la salvia "supuestamente" reduce la lactancia. Añade que no hay estudios científicos de su efecto sobre la producción de leche. Para la menta, SPS-NHS (08/03/2024) describe informes contradictorios (aumenta o reduce). Añade que no hay evidencia publicada. LactMed menta no cargó (bloqueo reCAPTCHA).

**Texto propuesto (Alerta):**
> La mayoría de estas plantas no tiene datos de seguridad en embarazo ni lactancia (EMA). Si la persona está embarazada o lacta, no recomiendes tinturas ni dosis medicinales sin valoración. Que la salvia y la menta reducen la leche es tradición: no hay estudios que lo prueben (LactMed 2025; SPS-NHS 2024).

**Referencias:**
- LactMed. Sage. NBK501816, revisado 15/07/2025. https://www.ncbi.nlm.nih.gov/books/NBK501816/
- SPS (NHS Specialist Pharmacy Service). Using gastrointestinal antispasmodics during breastfeeding (08/03/2024). https://www.sps.nhs.uk/articles/using-gastrointestinal-antispasmodics-during-breastfeeding/
- LactMed. Peppermint. NBK501851. https://ncbi.nlm.nih.gov/books/NBK501851/ (**no cargó**)
- Monografías EMA citadas en las alertas 10, 11, 12 y 15 (sección 4.6 de cada una).

---

## Log de búsqueda (2026-11-03)

| Fuente | Query o URL | Resultado |
|---|---|---|
| PubMed | clove oil eugenol ingestion child toxicity hepatotoxicity | 0 |
| PubMed | clove oil poisoning child | 2 (PMID 29601442, 1679654) |
| PubMed | eugenol clove oil ingestion hepatic necrosis N-acetylcysteine | 0 |
| EMA | Caryophylli floris aetheroleum (página, monografía borrador, informe final) | Cargó; casos pediátricos sección 5.5 |
| PubMed | piperine drug interaction bioavailability pharmacokinetics review | 14 (1 retirado: PMID 38910277, no usado) |
| PubMed | piperine[Title] AND (phenytoin OR nevirapine OR theophylline OR propranolol OR carbamazepine)[Title] | 10; 5 estudios humanos usados |
| PubMed | curcumin warfarin interaction INR bleeding | 1 (PMID 30070343) |
| PubMed | turmeric warfarin case report | 0 |
| PubMed | Curcuma[MeSH] AND Warfarin[MeSH] | 2 (estudios en rata) |
| PubMed | turmeric curcumin liver injury DILIN case series | 0 |
| PubMed | Halegoua-DeMarzio turmeric liver injury | 2 (PMID 36252717, 39136211) |
| PubMed | turmeric liver injury HLA-B*35:01 | 1 (PMID 39297606) |
| PubMed | Lombardi turmeric liver injury Italian phytovigilance | 1 (PMID 32656820) |
| EMA | Curcuma longa monografía Rev. 1 y adenda 2025 | Cargó |
| NIH LiverTox | Turmeric NBK548561 (HTML y PDF) | **Bloqueado (reCAPTCHA)** |
| PubMed | Crataegus hawthorn digoxin pharmacokinetic interaction | 1 (PMID 12817526) |
| EMA | Crataegi folium cum flore (página, informe, monografía vía e-lactancia) | Cargó |
| PubMed | Hibiscus sabdariffa blood pressure meta-analysis | 8; 3 usados |
| PubMed | Echinacea for preventing and treating the common cold Cochrane | 7; Cochrane 2014 usado |
| PubMed | elderberry supplementation upper respiratory symptoms meta-analysis | 1 |
| PubMed | Sambucus nigra elderberry respiratory viral infection systematic review | 0 |
| PubMed | elderberry autoimmune disease cytokine safety concern | 0 |
| Web | NCCIH elderberry | Cargó (actualizado nov. 2024) |
| Web | Healio: elderberry autoimmune skin disease (Faden 2024) | Cargó (fuente secundaria) |
| EMA | Echinacea purpurea herba recens; Sambuci fructus; Sambuci flos | Cargó |
| PubMed | Compositae allergy cross-reactivity | 182; 3 revisados |
| PubMed | echinacea adverse reactions anaphylaxis atopy | 1 (PMID 9507713) |
| PubMed | chamomile tea anaphylaxis | 9; ninguno clínico útil en los 5 primeros |
| Web | NCCIH chamomile (nccih.nih.gov) | **No permitido (allowlist)**; usado boletín govdelivery |
| EMA | Matricaria recutita aetheroleum (vía e-lactancia) | Cargó |
| PubMed | cannabis use during pregnancy outcomes meta-analysis low birth weight (2022–) | 10; 3 usados |
| PubMed | cannabis drug interactions CNS depressants review clinicians | 7; JAMA 2026 usado |
| Web | CDC marijuana and breastfeeding | Cargó (revisado 26/02/2024) |
| Web | ACOG Clinical Consensus 10 | Solo resúmenes secundarios (epocrates, CNN) |
| PubMed | Eschscholzia californica sedative | 5; 3 usados |
| PubMed | Passiflora incarnata benzodiazepine interaction sedation | 0 |
| EMA | Passiflorae herba (página y monografía 2007) | Cargó; PDF vigente 2014 **no permitido (allowlist)** |
| EMA | Eschscholziae herba (página, borrador, adenda 2022) | Cargó |
| PubMed | peppermint OR sage lactation milk supply evidence | 2716 (query demasiado amplia, no útil) |
| PubMed | herbal galactagogues antigalactagogues sage peppermint breastfeeding review | 0 |
| LactMed | Sage NBK501816 | Cargó (rev. 15/07/2025) |
| LactMed | Peppermint NBK501851 (HTML y PDF) | **Bloqueado (reCAPTCHA)** |
| Web | SPS-NHS antispasmodics breastfeeding | Cargó (08/03/2024) |

## Datos no confirmados

1. **LiverTox (turmeric):** no cargó. No se confirmó su puntuación de probabilidad ni su texto sobre piperina.
2. **LactMed (peppermint):** no cargó. La afirmación sobre la menta se apoya solo en SPS-NHS.
3. **ACOG Consenso Clínico n.º 10:** no se leyó el texto original. La frase "el uso de cannabis no contraindica la lactancia" viene de un resumen secundario.
4. **Faden 2024 (saúco y brotes autoinmunes):** no se verificó en PubMed. El dato viene de Healio.
5. **Saúco en enfermedades autoinmunes:** ninguna fuente oficial (EMA, NCCIH) lo contraindica. La afirmación del libro queda sin evidencia sólida.
6. **Pasiflora/amapola con alcohol u opioides:** no hay estudios. La alerta se mantiene por plausibilidad.
7. **Monografía vigente de *Passiflora* (Rev. 1, 2014):** el PDF no cargó. Se usó la versión 2007, que la página EMA declara superada. La revisión 2 está en curso.
8. **Monografía de *Eschscholzia*:** se leyó el borrador 2014; el texto final adoptado (2015) no se abrió. El borrador es incoherente en la edad (12 frente a 18 años).
9. **Matricariae flos:** se citó la monografía del aceite esencial, no la de la flor. No se verificó la contraindicación por asteráceas en la monografía de la flor.
10. **DOI de Tankanow 2003:** PubMed no devolvió DOI; se cita el PMID.
11. **Estudio Meriva® 2018:** es un estudio abierto, sin grupo control, con la formulación de un fabricante. Su resultado negativo no excluye la interacción.
12. **Alerta 16 "ninguna receta":** no se revisaron todas las plantas del libro. Algunas (p. ej., jengibre) podrían tener datos en el embarazo.
