---
name: harrys-cosmeticology
description: "Knowledge base from Harry's Cosmeticology, 9th Ed. (Meyer R. Rosen, ed., Chemical Publishing, 2015): Vol. 1 (marketing, fragrance, global regulation & IP, skin/hair/nail/nose/oral/lip/feminine substrates), Vol. 2 (ingredients: surfactants, rheology modifiers, silicones, preservatives, antioxidants, botanicals, marine, hyaluronic acid, peptides, AHAs, retinoids, whiteners; anti-aging biology: senescence, glycation, sirtuins, epigenetics, chronobiology) and the Sustainability & Eco-responsibility focus book, plus a 2,100-concept knowledge graph. Use when formulating or troubleshooting a cosmetic or personal-care product, choosing or comparing actives and excipients (use levels, pH, mechanisms), explaining skin/hair/nail/oral biology or aging mechanisms behind a claim, checking US/EU/China/Russia/Saudi regulatory or nanomaterial requirements, or planning sustainable sourcing — also in Spanish (formulación cosmética, ingredientes, activos antiedad, despigmentantes, conservantes, regulación cosmética, cuidado capilar)."
---

<!-- argument-hint: [topic, ingredient, chapter part number, or "graph <concept>"] -->

# Harry's Cosmeticology (9th Edition)
**Editor-in-Chief**: Meyer R. Rosen | **Books**: Vol. 1, Vol. 2, *Sustainability and Eco-responsibility* (focus book) | **Chapters**: 59 chapter files | **Knowledge graph**: 2,129 concepts, 6,434 relations | **Generated**: 2026-10-08

## How to Use This Skill

- **Without arguments** — load the Core Frameworks below.
- **With a topic or ingredient** — find it in the Topic Index below or in [references/topic-index.md](references/topic-index.md) (650 topics), then read that chapter file before answering.
- **With a part number** — e.g. `4.3.5` → read `chapters/v2-p4-3-5-*.md`.
- **Cross-chapter questions** ("what treats X", "how does A relate to B", "which chapters mention Y") — query the knowledge graph:
  ```bash
  python3 scripts/graph_query.py search niacinamide        # find a concept
  python3 scripts/graph_query.py node "hyaluronic acid"     # what each chapter says + all relations
  python3 scripts/graph_query.py neighbors hyperpigmentation treats   # one relation type
  python3 scripts/graph_query.py path glycation wrinkles   # chain of relations between two concepts
  python3 scripts/graph_query.py chapter v2-p4-2-4          # concepts a chapter covers
  python3 scripts/graph_query.py top ingredient             # most connected ingredients
  ```
  Run the script from this skill's folder. Graph relations come from automated extraction: confirm specifics in the chapter file before stating them as fact.

When a question goes beyond the Core Frameworks, read the relevant chapter file(s) first. Answer in the user's language (the files are in English).

---

## Core Frameworks & Mental Models

**Market first, then chemistry** (Pt 1.1): under the Marketing Concept no product is developed unless a large enough group will buy it; 80–90% of new products fail, so chemists and marketers co-own a 7-step development process. Claims must be supportable at the use level; "dusting" an active below its effective level is an anti-pattern.

**Same principle, different paperwork** (Pt 2.2–2.3): US and EU both make the marketer responsible for safety with post-market surveillance, but the EU (Reg. 1223/2009) adds the Responsible Person, PIF/CPSR, CPNP notification and mandatory GMP (ISO 22716). Safety rests on Margin of Safety = NOAEL / SED, which must exceed 100. A product's legal class (cosmetic vs drug/quasi-drug) follows its *intended use and claims*. China (special vs non-special use, IECIC inventory), the Russia/Customs Union (TR TC 009/2011, EAC) and Saudi Arabia (SFDA, GSO 1943/2009) each add registration and labeling layers. Nanomaterials have their own EU 6-month pre-market notification and "(nano)" labeling.

**The stratum corneum is the gate** (Pt 3.1): ~10% of skin thickness, >80% of the barrier ("bricks and mortar": corneocytes + ceramide/cholesterol/fatty-acid lamellae, NMF from filaggrin). Four penetration routes exist; the outward flow of cells, water and lipids opposes delivery, so an active that never passes the SC can still help by protecting and repairing the barrier.

**Skin type is more than color** (Pt 3.2): Fitzpatrick predicts sunburn, not reaction to products; the EP Global Skin Classification (EP I–XI) adds ancestry. Skin of color reacts to irritation with post-inflammatory hyperpigmentation, so in darker skin, minimizing irritation is itself a depigmenting strategy.

**Aging = intrinsic + extrinsic, converging on a few hubs** (Pt 3.2.4, 4.3, Pt 5): UV → ROS → MAP kinase → AP-1 → MMPs (collagen breakdown) + reduced procollagen synthesis is the central photo-aging cascade. Pt 5 adds senescence (SASP, p53/p16), glycation (AGEs, crosslinked collagen), proteasome decline, telomere loss, sirtuin/NAD+ decline, epigenetic drift and circadian desynchronization. These are interlinked, which is why multi-target ("single-bullet" bundle) actives are favored over layering many products.

**Anti-aging actives by mechanism** (Pt 4.3):
| Target | Actives covered | Chapter |
|---|---|---|
| Gene transcription (RAR/RXR) | retinoic acid (Rx), retinol 0.1–2% (OTC) | 4.3.1 |
| Signal / carrier / neurotransmitter / enzyme-inhibitor peptides | palmitoyl peptides, GHK-Cu, acetyl hexapeptide | 4.3.2 |
| Desquamation + dermal matrix | AHAs 4–10% (efficacy depends on free acid: pH vs pKa), PHAs, bionic acids | 4.3.5 |
| Matrix repair signalling | growth factor/cytokine mixtures, stem-cell conditioned media | 4.3.6 |
| ROS/RNS, metals, oxidases | broad-spectrum antioxidant networks, combined with sunscreens | 4.3.7 |
| Glycation / proteasome / telomeres / sirtuins | carnosine-type anti-glycation, proteasome activators, sirtuin activators | 5.4–5.5 |

**Pigmentation has many levers** (Pt 3.2.2–3.2.3, 4.2.4): tyrosinase inhibition/copper chelation, MITF down-regulation, α-MSH/endothelin signalling, melanosome transfer (PAR-2), desquamation. Japan regulates "whitening" claims with approved quasi-drug actives; modern products combine several levers in a "bouquet." Hydroquinone remains the dermatology benchmark; alternatives include kojic acid, arbutin, niacinamide and botanical inhibitors.

**Hair is a shape-memory polymer** (Pt 3.3): every restyle (water set, hot iron, perm, relaxer, styling polymer) is soften → impose shape → fix. Damage comes from heat, alkali, reduction, bleach, UV and fatigue. The cuticle's covalently bound 18-MEA layer gives lubricity and hydrophobicity; weathering strips it, and hair-care actives aim to replenish it. Follicle cycling (anagen/catagen/telogen) drives growth disorders; graying is partly H2O2/oxidative.

**Formulation is a stress test** (Pt 4.1–4.2): choose rheology modifiers by the stresses the formula meets (pH, electrolyte, temperature, shear, packaging), not by label or price. Carbomers need neutralization; associative thickeners (HASE) respond to surfactant and salt. Silicones are insoluble in both water and oil with very low surface tension, so the authors use them as "the spice, not the meat." Preservative choice follows six growth factors (water activity, nutrients, pH, osmolarity, redox, packaging). Antioxidants slow, never stop, rancidity: pair primary (radical-quenching) with secondary (chelating) types.

**Biology-based ingredient discovery** (Pt 1.4, 3.5, 4.1.4, 4.3.3): gene and protein expression, miRNA profiling, odorant-receptor HTS and 3D skin models now substantiate actives. Expression data shows mechanism, not clinical efficacy. Fermentation, plant cell culture and probiotic-derived lysates provide uniform, sustainable bioactives.

**Sustainability as a design constraint** (Sustainability book): people–planet–profit; improve current practice (local cultivation, plant breeding, GAP, eco-extraction, green formulation) and adopt new tools (plant cell cultures, open innovation, ethnobotanical benefit-sharing, sustainable-harvest limits).

---

## Chapter Index

### Volume 1 — Marketing, Regulation & Substrates

| Part | Chapter | Key frameworks |
|---|---|---|
| 1.1 | [Marketing Concepts to Empower Technical People](chapters/v1-p1-1-marketing-concepts.md) | Marketing Concept, situation analysis & SWOT, Four P's, 7-step new product-development process, three forms of innovation, dusting & claims, patents, 80-90% failure rate |
| 1.2 | [Creating the Right Fragrance for Your Personal Care Product](chapters/v1-p1-2-fragrance-selection.md) | fragrance-house workflow, top/middle/base notes, volatility & log Kow & odor threshold, product-use cycle key evaluation point, concentration-cost math, carriers & troubleshooting, fragrance types (WS, WD, INCI blends, natural, GRAS), EU 26 allergens/IFRA/RIFM |
| 1.3 | [Fragrance Packaging Design: A Multi-Sensory Experience](chapters/v1-p1-3-fragrance-packaging-design.md) | initial/fragrance/creative briefs, sensory cues & sensory dissonance, qualitative vs quantitative consumer testing, component-isolation testing (Bombshell), color-scent associations, bottle ergonomics, story-driven fragrance brief |
| 1.4 | [Molecular Cell Biology and Gene Analysis for Next-Generation Cosmetics](chapters/v1-p1-4-molecular-biology-gene-expression.md) | cell signaling (reception/transduction/response), receptor classes, transcription factors, epigenetics (DNA methylation, histone modification), skin immunity & inflammasomes, Nrf2 pathway, AMPK pathway, limits of gene-expression data |
| 2.1 | [Regulatory Requirements, IP and Achieving Global Market Success (Co-Editors' Introduction)](chapters/v1-p2-1-global-regulatory-developments.md) | regulatory harmonization, ICCR hot topics, animal-testing alternatives, EU 2013 marketing ban, China 2014 non-special-use exemption, nanomaterial definitions, social-media-driven regulation |
| 2.2 | [Overview of the Changing Regulatory Landscape in the U.S. and the E.U.](chapters/v1-p2-2-us-eu-regulation.md) | adulterated vs misbranded, intended-use drug classification, US labeling (PDP, 21 CFR 701.3), EU Responsible Person, PIF/CPSR Annex I, MoS = NOAEL/SED >100, CPNP notification, REACH tonnage path |
| 2.3.1 | [Achieving Global Market Access – Focus on Russia](chapters/v1-p2-3-1-russia-customs-union.md) | Customs Union, TR TC 009/2011, State Registration vs Declaration of Conformity, 13 high-risk categories, EAC mark, category pH/micro/toxic-element limits, CU labeling |
| 2.3.2 | [KSA Cosmetics and Perfumery Products: Market Access and Regulations](chapters/v1-p2-3-2-saudi-arabia.md) | SFDA, GSO 1943/2009, SFDA classification guidance restrictions, per-shipment Certificate of Conformity, country-of-origin rule, SASO 585 perfumes, Arabic labeling, AHA limits |
| 2.3.3 | [Achieving Global Market Access – Focus on China](chapters/v1-p2-3-3-china.md) | special vs non-special use, CFDA registration dossier, mandatory animal testing/GPMT, impurity-focused safety assessment, IECIC inventory/new ingredients, MAC/MUCAP, Chinese label patch, organic ban |
| 2.3.4 | [Nanomaterials in Cosmetics: Regulatory and Safety Considerations](chapters/v1-p2-3-4-nanomaterials-regulation.md) | EU/US/Canada nano definitions, EU 6-month nano notification, "(nano)" labeling, SCCS 16 characterization parameters, three-state characterization, surface-area dose metric, assay interference, CEPA NSNR |
| 2.4 | [Intellectual Property Issues: Patents and Trade Secrets](chapters/v1-p2-4-intellectual-property.md) | IP type selection, patentability triad, PCT/EPC filing routes, provisional applications, trade secrets, trademarks/trade dress/copyright, freedom to operate, infringement types, partnering do/don'ts, patent search classes |
| 3.1 | [The Skin: Structure, Biochemistry, and Function](chapters/v1-p3-1-skin-structure.md) | epidermal strata & turnover, brick-and-mortar SC, lamellar bodies & lipid processing, filaggrin/NMF, four penetration pathways, liposome/transfersome/nanocarrier delivery, penetration vs protection, UV photodamage & skin cancer, genomics in skin care |
| 3.2.1 | [Classification Scale for Skin Complexions Around the World](chapters/v1-p3-2-1-global-skin-classification.md) | Fitzpatrick scale, EP Global Skin Classification Scale (EP I–XI), skin evaluation questionnaire, Wood's lamp & UV photography, ancestry-based precautions, mixed-race test-and-escalate |
| 3.2.2 | [Dermatologic Disorders in Skin of Color](chapters/v1-p3-2-2-skin-of-color-disorders.md) | melasma patterns, post-inflammatory hyperpigmentation, vitiligo, idiopathic guttate hypomelanosis, pseudofolliculitis barbae, hydroquinone & alternatives, NB-UVB phototherapy |
| 3.2.3 | [Asian Ethnic Skin: Specialty Corrective Cosmeceuticals](chapters/v1-p3-2-3-asian-ethnic-skin.md) | Asian lightening market data, pheomelanin/yellow undertones, three-step anti-pigment regimen, melasma peels/IPL protocols, peri-orbital hypermelanosis, PIH triggers, necessity products |
| 3.2.4 | [Compromised Skin in the Elderly](chapters/v1-p3-2-4-aging-elderly-skin.md) | intrinsic vs extrinsic aging, TEWL & barrier recovery with age, SC turnover, elderly dry skin/NMF, Cutometer parameters, photo-aging ROS–AP-1–MMP cascade, sunscreen/tretinoin/retinol/niacinamide/AHA/antioxidant evidence, cosmeceutical regulatory status |
| 3.3.1 | [An Overview of the Physical and Chemical Properties of Hair and Their Relation to Cosmetic Needs, Performance and Properties](chapters/v1-p3-3-1-hair-physical-chemical-properties.md) | Feughelman two-phase model, stress-strain regions, viscoelastic shape memory, water sorption isotherm/heat buffering, cuticle layers and 18-MEA, cell membrane complex failure, cuticle buckling, hair optics/shine, melanin, follicle cycle |
| 3.3.2 | [An Overview of Hair Follicle Anatomy and Biology](chapters/v1-p3-3-2-hair-follicle-biology.md) | permanent vs cycling follicle, bulge stem cells, dermal papilla signaling, anagen/catagen/telogen/exogen/kenogen, androgenetic alopecia & DHT, hair-loss therapeutic triad, follicle aging and graying, oxidative stress on follicle |
| 3.3.3 | [Hair Aging: Fundamentals, Protection and Repair](chapters/v1-p3-3-3-hair-aging.md) | intrinsic vs extrinsic hair aging, five aging attributes, H2O2/catalase graying theory, minoxidil, photo-aging, cuticle lipid loss & 18-MEA replenishment, scalp-type regimens, anti-aging hair ingredients |
| 3.3.4 | [Mechanisms of Changes in Hair Shape](chapters/v1-p3-3-4-hair-shape-changes.md) | hair as shape memory polymer, soften-impose-fix, water-setting, hot iron Tm/Tg vitrification, thioglycolate perm, alkaline relaxers/lanthionine, curl-tightness memory rule, friction vs bending, volume/frizz/body, styling polymer Tg and welding |
| 3.3.5 | [Eyelashes: Anatomy and Conditioners for Increasing Length and Fullness/Thickness](chapters/v1-p3-3-5-eyelashes.md) | lash anatomy, lash growth cycle, prostaglandin analogue conditioners, dechloro ethylcloprostenolamide RCT, periocular safety testing, peptide and stem-cell-derived conditioners, brow/scalp extension |
| 3.4 | [Substrate: The Nails](chapters/v1-p3-4-nails.md) | nail unit anatomy, matrix→plate layering, nail composition (cystine, water, Ca), growth rates, onycholysis from nail cosmetics, brittleness/splitting care, onychomycosis, paronychia, pigmented band referral |
| 3.5 | [Substrate: The Nose — Biology of Olfaction](chapters/v1-p3-5-nose-olfaction.md) | ~350 odorant receptors (GPCRs), piano-keyboard model, cell-based HTS with calcium dyes, Z′ factor ≥0.4, native full-length receptors, natural substitutes, fragrance enhancers/blockers, iterative sensory confirmation |
| 3.6.1 | [Substrate: The Mouth and Oral Care](chapters/v1-p3-6-1-mouth-oral-care.md) | cosmetic vs drug oral claims, enamel/dentin chemistry, critical pH 5.5, Stephan curve, plaque biofilm succession, calculus control, fluoride/remineralization, hydrodynamic sensitivity theory, whitening, malodor strategies, xerostomia, aphthous ulcers |
| 3.7 | [Substrate: The Lips — Lip Skin Structure and Function](chapters/v1-p3-7-lip-skin.md) | vermilion zone vs border, high lip TEWL, upper vs lower lip hydration, hairless sebaceous follicles, sebum composition, ceramide nomenclature and lip ceramide profile, age changes |
| 3.8 | [Substrate: Feminine Rejuvenation](chapters/v1-p3-8-feminine-rejuvenation.md) | vulvar anatomy and innervation, estrogen and vulvar sensation, vulvar atrophy cycle, irritants in OTC lubricants, topical estrogen/ospemifene, ADSC conditioned-media growth factors, cosmetic vulvar regimen goals |

### Volume 2 — Ingredients & Anti-Aging

| Part | Chapter | Key frameworks |
|---|---|---|
| 4.1.1 | [Surfactants: Intervention at the Interface of Multiphase Dispersed Systems](chapters/v2-p4-1-1-surfactants.md) | four charge classes, HLB system and required-HLB jar test, four emulsion stabilization mechanisms, liquid crystal emulsifiers, shampoo architecture, foam/solubilization/CMC, zwitterionic point, surfactant chemistry catalog |
| 4.1.2 | [Ingredients for Creating the Next Greatest Lipstick](chapters/v2-p4-1-2-lipstick-ingredients.md) | comfort-shine-wear trade-off, wax selection and 65–75°C melt window, sweating and clay master gels, silicone waxes/alkyl dimethicones/phenyl silicones, film formers for wear, spreading coefficient, pigment oil absorbance, snap test |
| 4.1.3 | [Hyaluronan (Hyaluronic Acid) – A Natural Moisturizer](chapters/v2-p4-1-3-hyaluronic-acid.md) | MW-to-function rule, fragment preparation and by-products, chemical modification/cross-linking, skin penetration by MW, DSC bound water, humidity-independent hydration, MW analytics (ESI-MS, MALDI, SEC-MALS) |
| 4.1.4.1 | [Ayurveda in Personal Care](chapters/v2-p4-1-4-1-ayurveda.md) | doshas, beauty from within, antioxidant/anti-inflammatory/antimicrobial botanicals, amla, curcuminoids, neem, Triphala, standardization need |
| 4.1.4.2 | [Probiotics in Topical Personal Healthcare](chapters/v2-p4-1-4-2-probiotics.md) | probiotic derived bioactives (non-live), beta-1,3-D-glucan, Toll-like receptors and Dectin-1, defensins, in vitro defensin ELISA screening, psoriasis caution |
| 4.1.4.3 | [Bioactives: Green and Sustainable Ingredients from Biotransformation and Biofermentation](chapters/v2-p4-1-4-3-fermentation-bioactives.md) | submerged vs solid-state fermentation, stress elicitation, live yeast cell derivative, marine algae actives, plant meristem cultures, recombinant peptides and HA, sustainability advantages |
| 4.1.5 | [Multi-Functional Botanicals for Topical Applications](chapters/v2-p4-1-5-multifunctional-botanicals.md) | natural vs naturally derived, extraction methods (solvent, freeze-drying, supercritical CO2), AHPA standardization, skin-lightening assay cascade, tetrahydrocurcumin vs hydroquinone, forskohlin cellulite, tetrahydropiperine penetration, oxyresveratrol, boswellic acids |
| 4.1.6 | [Ingredients to Strengthen Skin Barrier Integrity (Padina pavonica)](chapters/v2-p4-1-6-skin-barrier-padina.md) | calcium-dependent barrier, cytokeratins, desmosomes, tight junctions/DEJ/filaggrin, aging calcium bioavailability, HFP efficacy tests, anti-pollution explants |
| 4.1.7.1 | [Antimicrobial Preservatives for the Cosmetic and Personal Care Industry](chapters/v2-p4-1-7-1-antimicrobial-preservatives.md) | six growth factors, water activity thresholds, preservative selection criteria, active vs preservative, preservative frequency data, four-quadrant consumer model, global regulatory check |
| 4.1.7.2 | [Antioxidants: Extending the Shelf Life of Your Products](chapters/v2-p4-1-7-2-antioxidants-shelf-life.md) | initiation-propagation-termination, primary vs secondary antioxidants, tocopherol pro-oxidant effect, rosemary carnosic acid cascade, chelators, OSI/PV assays, polar paradox |
| 4.2.1 | [Natural and Synthetic Polymers: Designing Rheological Properties for Applications](chapters/v2-p4-2-1-rheological-additives.md) | aqueous vs non-aqueous thickeners, thixotropic vs pseudoplastic, shear-sensitive vs shear-loving, emulsion stabilization via external/internal phase, salt curve, appearance/texture-driven selection, organoclays, suspension mechanism |
| 4.2.2 | [Rheology Modifiers and Consumer Perception](chapters/v2-p4-2-2-rheology-modifiers-consumer-perception.md) | viscosity/yield stress/viscoelasticity, tan δ and cushion, AMPS polymers, carbomer pH-neutralization profile, ASE/HASE associative thickening, c* overlap concentration, NaCl-triggered breakdown on skin, QDA sensory correlation, hydroalcoholic neutralizer table, optical-effects cleanser suspension |
| 4.2.3.1 | [Silicones in Personal Care Products: Polydimethyl Siloxanes, Organosilicone Polymers, & Copolymers](chapters/v2-p4-2-3-1-silicones.md) | siliphilic/oleophilic solubility, M/D/T/Q nomenclature, cyclomethicone (D4/D5) replacement, silicone fluid viscosity grades, gums/elastomers/resins/MQ, dimethicone copolyol MW-function ladder, RF50, water tolerance, alkyl dimethicone & multi-domain, Green Star Rating |
| 4.2.3.2 | [Silicone Elastomer Applications](chapters/v2-p4-2-3-2-silicone-elastomers.md) | cross-link density vs swelling, Polysilicone-11, solvent-exchange mattifying, sebum absorption, 5–50 µm nano-free particles, elastomer vs linear dimethicone, pilling |
| 4.2.4 | [Skin Whitener Ingredients](chapters/v2-p4-2-4-skin-whiteners.md) | Japanese quasi-drug whitening approvals, tyrosinase inhibition/copper chelation, MITF down-regulation, α-MSH/endothelin/POMC signaling, neurowhitening (Substance P), PAR-2 melanin transfer, KLK desquamation, multi-target bouquet |
| 4.2.5 | [Marine Ingredients for Skin Care: An Ocean of Resources](chapters/v2-p4-2-5-marine-ingredients.md) | macroalgae polysaccharides, alginate oligosaccharides as EGF cofactor, microalgal exopolysaccharides, photolyase DNA repair, thioredoxin/Phormidium, rock samphire retinol-like, Salicornia AQP8, sea minerals/microdermabrasion |
| 4.2.6 | [Topical Reduction of Visible Skin Deterioration Due to Cellulite](chapters/v2-p4-2-6-cellulite.md) | estrogen–MMP-1 etiology, trabeculae destruction, alpha-2 receptors, anti-estrogens (genistein, chrysin, DIM), collagenase inhibition, PDE blocking/carnitine fat mobilization, collagen rebuilding, compression, efficacy measurement |
| 4.3.1 | [Topical Retinoids](chapters/v2-p4-3-1-topical-retinoids.md) | vitamin A oxidation ladder, RAR/RXR (RAR-gamma), four-factor acne model, triple-combination melasma therapy, retinol 0.1–2%, irritation and photosensitivity management |
| 4.3.2 | [Peptides for Anti-Aging Skin Care](chapters/v2-p4-3-2-peptides.md) | peptide size classes, signal/matrikine peptides, carrier (GHK-Cu), neurotransmitter-inhibitor peptides, enzyme-inhibitor peptides, antioxidant paradox, lipidation/cyclization/non-natural amino acids for delivery |
| 4.3.3 | [MicroRNAs in Skin Physiology](chapters/v2-p4-3-3-micrornas.md) | miR biogenesis (Drosha/DGCR8, Dicer, RISC/AGO2), miR nomenclature, miR-203 master regulator, pigmentation miRs, SA-miRs and p53/p16 pathways, exosomal miRs, 3D reconstructed skin for ingredient testing |
| 4.3.4 | [Amino Acids](chapters/v2-p4-3-4-amino-acids.md) | fermentation production, derivatization map (acyl glutamates, PCA, polyaspartate), NMF composition, Zinc PCA anti-AP-1, glycine:proline:alanine collagen boost, proline moisture retention, arginine AHA buffering, hair tensile-repair tests |
| 4.3.5 | [AHAs and Beyond](chapters/v2-p4-3-5-hydroxy-acids.md) | pH/pKa free-acid rule, AHA→PHA→bionic→NAG→N-acetylamino acid generations, AHA effects on all skin layers, amphoteric (arginine) complex, low-pH thickener/emulsifier/emollient selection, forearm and split-face clinical models |
| 4.3.6 | [Cytokines, Growth Factors, and Stem Cells](chapters/v2-p4-3-6-growth-factors-stem-cells.md) | intrinsic vs extrinsic aging, chronic-wound hypothesis, growth-factor cocktails (neonatal/fetal fibroblast), penetration and VEGF safety, adipose-derived stem-cell conditioned media, Swiss apple plant stem cells |
| 4.3.7 | [Antioxidants in Cosmetics for Anti-Aging](chapters/v2-p4-3-7-antioxidants.md) | ROS/RNS generation chain, NADPH oxidase, Fe/Cu/Ca catalysis, pro-oxidant antioxidants, broad-spectrum antioxidant criteria, MMP/ECM/DEJ two-front test, antioxidant combinations with sunscreens |
| 5.1 | [Theories of Aging — Skin Anti-Aging: At the Tipping Point](chapters/v2-p5-1-theories-of-aging.md) | DNA-damage vs programmed theories, 15 aging theories, free radical theory (Harman 1954), Hayflick limit, caloric restriction & sirtuins, glycation/cross-linking, inflammation cycle (PLA2/arachidonic acid), telomeres |
| 5.2 | [The Cellular Water Principle](chapters/v2-p5-2-cellular-water-principle.md) | ICW vs ECW compartments, edematous "wasted water", membrane hypothesis of aging (Nagy), BIA phase angle, Esposito classification, Strehler's 4 criteria, nutritional supplementation, Inclusive Health |
| 5.3 | [Anti-Senescence: Managing Cellular Functions](chapters/v2-p5-3-anti-senescence.md) | single-bullet treatment, replicative senescence vs apoptosis, ubiquitin-proteasome pathway, AGE/RAGE, MFRTA, hyperosmolarity >300 mOsm inflammation, osmoprotectants/anhydrobiosis, glutaminylglutamine amide peptides |
| 5.4 | [Glycation, Proteasome Activation, and Telomere Maintenance](chapters/v2-p5-4-glycation-proteasome-telomeres.md) | AGE formation (Schiff/Amadori/MGO), AGE-Reader autofluorescence, anti-glycation strategies, Albizia julibrissin preventive+curative, proteasome vs autophagy (LC3-II), proteasome caveat, telomeres/shelterin, SIPS model |
| 5.5 | [Sirtuins and Skin](chapters/v2-p5-5-sirtuins-and-skin.md) | SIRT1-7 localization, NAD+-dependent deacetylation & ADP-ribosylation, nicotinamide feedback inhibition, SIRT3/SIRT4 energy balance, SIRT3-SOD2, UVB & ozone suppress sirtuins, resveratrol activator, nicotinamide inhibitor for psoriasis |
| 5.6 | [Epigenetics of Skin Aging](chapters/v2-p5-6-epigenetics-of-skin-aging.md) | DNA methylation (DNMTs, CpG islands), histone modification (HAT/HDAC), methylation age clock, epigenetic drift in twins, DDR repair pathways, nutriepigenetics, epigenetic ingredients, 10 questions for epigenetic actives |
| 5.7 | [Chronobiology of the Skin: Circadian Rhythm and Clock Genes](chapters/v2-p5-7-skin-chronobiology.md) | SCN master clock, CLOCK/BMAL1-PER/CRY loop, day protect/night repair, night TEWL & penetration, DNA repair timing, UVB clock disruption, shift-work cancer risk, stem-cell clock |
| 5.8 | [Stress, Sleep and Epigenetic Orthodontics](chapters/v2-p5-8-stress-sleep-epigenetic-orthodontics.md) | sleep stages, HPA axis & cortisol, insomnia types, OSA/AHI, cortisol collagen loss, growth hormone, sleep hygiene, C-PAP/oral appliances, epigenetic orthodontics mechano-transduction |

### Sustainability & Eco-Responsibility (focus book)

| Part | Chapter | Key frameworks |
|---|---|---|
| 12.0–12.7 | [Sustainability and Eco-Responsibility (whole Part 12)](chapters/sus-p12-1-sustainability.md) | triple bottom line, open innovation for sustainability, six-element ethnobotanical approach, Peters sustainable harvest, local cultivation and plant breeding (chamomile −65% CO2), GAP and post-harvest drying, plant cell cultures (echinacoside), eco-responsible extraction and zeodration, green formulation |

## Topic Index (selected — full list in [references/topic-index.md](references/topic-index.md))

- **Acne** → v1-p3-2-3-asian-ethnic-skin, v2-p4-3-1-topical-retinoids
- **AHAs, PHAs, bionic acids, pH/pKa** → v2-p4-3-5-hydroxy-acids
- **Allergens (fragrance, EU 26), IFRA** → v1-p1-2-fragrance-selection, v1-p2-2-us-eu-regulation
- **Amino acids, NMF, PCA** → v2-p4-3-4-amino-acids, v1-p3-1-skin-structure
- **Animal-testing ban / alternatives** → v1-p2-1-global-regulatory-developments, v1-p2-3-3-china
- **Antioxidants for anti-aging** → v2-p4-3-7-antioxidants
- **Antioxidants for shelf life (rancidity)** → v2-p4-1-7-2-antioxidants-shelf-life
- **Cellulite** → v2-p4-2-6-cellulite
- **China market registration** → v1-p2-3-3-china
- **Circadian rhythm / night repair** → v2-p5-7-skin-chronobiology
- **Elderly / compromised skin** → v1-p3-2-4-aging-elderly-skin
- **Epigenetics, DNA methylation** → v2-p5-6-epigenetics-of-skin-aging, v1-p1-4-molecular-biology-gene-expression
- **Eyelash growth** → v1-p3-3-5-eyelashes
- **EU Cosmetics Regulation 1223/2009, CPSR, PIF, CPNP** → v1-p2-2-us-eu-regulation
- **Fermentation / biotech actives** → v2-p4-1-4-3-fermentation-bioactives
- **Fragrance selection, notes, log Kow** → v1-p1-2-fragrance-selection
- **Fragrance packaging & consumer testing** → v1-p1-3-fragrance-packaging-design
- **Glycation, AGEs, proteasome, telomeres** → v2-p5-4-glycation-proteasome-telomeres
- **Growth factors, stem-cell media** → v2-p4-3-6-growth-factors-stem-cells
- **Hair damage, 18-MEA, aging hair** → v1-p3-3-1-hair-physical-chemical-properties, v1-p3-3-3-hair-aging
- **Hair loss, follicle cycle** → v1-p3-3-2-hair-follicle-biology
- **Hair perm, relaxer, hot iron** → v1-p3-3-4-hair-shape-changes
- **Hyaluronic acid (MW effects)** → v2-p4-1-3-hyaluronic-acid
- **Hyperpigmentation, melasma, PIH** → v1-p3-2-2-skin-of-color-disorders, v1-p3-2-3-asian-ethnic-skin, v2-p4-2-4-skin-whiteners
- **Intellectual property, patents, trade secrets** → v1-p2-4-intellectual-property
- **Lipstick formulation** → v2-p4-1-2-lipstick-ingredients
- **Lips (biology)** → v1-p3-7-lip-skin
- **Marine / algae ingredients** → v2-p4-2-5-marine-ingredients, v2-p4-1-6-skin-barrier-padina
- **Marketing, new product development** → v1-p1-1-marketing-concepts
- **MicroRNAs** → v2-p4-3-3-micrornas
- **Nails** → v1-p3-4-nails
- **Nanomaterials** → v1-p2-3-4-nanomaterials-regulation
- **Olfaction, odorant receptors** → v1-p3-5-nose-olfaction
- **Oral care, fluoride, whitening, malodor** → v1-p3-6-1-mouth-oral-care
- **Peptides** → v2-p4-3-2-peptides
- **Preservatives, challenge testing** → v2-p4-1-7-1-antimicrobial-preservatives
- **Probiotics (topical)** → v2-p4-1-4-2-probiotics
- **Retinoids** → v2-p4-3-1-topical-retinoids
- **Rheology modifiers, carbomer, thickeners** → v2-p4-2-1-rheological-additives, v2-p4-2-2-rheology-modifiers-consumer-perception
- **Russia / Customs Union** → v1-p2-3-1-russia-customs-union
- **Saudi Arabia / GCC** → v1-p2-3-2-saudi-arabia
- **Senescence (cellular)** → v2-p5-3-anti-senescence, v2-p5-1-theories-of-aging
- **Silicones, elastomers** → v2-p4-2-3-1-silicones, v2-p4-2-3-2-silicone-elastomers
- **Sirtuins, NAD+** → v2-p5-5-sirtuins-and-skin
- **Skin barrier, stratum corneum, penetration** → v1-p3-1-skin-structure, v2-p4-1-6-skin-barrier-padina
- **Skin classification (Fitzpatrick, EP scale)** → v1-p3-2-1-global-skin-classification
- **Sleep, stress, cortisol** → v2-p5-8-stress-sleep-epigenetic-orthodontics
- **Surfactants, HLB, cleansing** → v2-p4-1-1-surfactants
- **Sustainability, sourcing, plant cell culture** → sus-p12-1-sustainability
- **Theories of aging** → v2-p5-1-theories-of-aging
- **Vulvar / feminine care** → v1-p3-8-feminine-rejuvenation
- **Water (cellular), hydration claims** → v2-p5-2-cellular-water-principle

## Supporting Files

- [glossary.md](glossary.md) — ~400 key terms with definitions and source chapter
- [patterns.md](patterns.md) — formulation, testing, regulatory and development techniques (when to use, how, trade-offs)
- [cheatsheet.md](cheatsheet.md) — decision rules and key numbers (pH, use levels, limits) by section
- [references/topic-index.md](references/topic-index.md) — full topic → chapter index
- [references/graph.json](references/graph.json) + [scripts/graph_query.py](scripts/graph_query.py) — knowledge graph and query tool (the interactive viewer lives in the repo at `Graphify/graph.html`)

---

## Scope & Limits

- Covers all substantive chapters of Vol. 1 (Parts 1–3), Vol. 2 (Parts 4–5) and the Sustainability focus book (Part 12). Editor's bio, preface and section intros are folded into this file rather than given chapter files.
- The book dates from 2015. Regulations have changed since: for example, US MoCRA (2022) is absent, China's CSAR (2021) replaced the 1990 rules, and the EU allergen list has grown beyond 26. Treat regulatory content as historical background and check current law before advising on compliance.
- Chapters are paraphrased summaries, not the book text. Use levels and clinical results are as reported by each chapter's authors, many of whom represent ingredient suppliers. Flag supplier-sourced efficacy claims as such.
- Not medical advice: drug-category topics (retinoic acid, hydroquinone, minoxidil, prostaglandin analogues, estrogen) are described as the book does, for formulation context.
