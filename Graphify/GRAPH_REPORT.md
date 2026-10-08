# Graph Report — Harry's Cosmeticology (9.ª ed.)

Grafo de conocimiento construido con el método de [graphify](https://github.com/Graphify-Labs/graphify) a partir de tres libros: *Harry's Cosmeticology* Vol. 1 y Vol. 2, y el *focus book* *Sustainability and Eco-responsibility*.

## Resumen

- **2129 nodos**, **6434 aristas**, **59 comunidades**, 151 hiperaristas
- 65 capítulos procesados
- Tipos de nodo: ingredient 512, anatomy 396, concept 252, technique 222, ingredient_class 166, mechanism 160, condition 128, regulation 113, product 72, chapter 65, organization 33, region 10
- Confianza de las aristas: EXTRACTED 6116, INFERRED 316, AMBIGUOUS 2

## Nodos dios (los conceptos más conectados)

| # | Concepto | Tipo | Grado | Capítulos |
|---|---|---|---|---|
| 1 | Skin Aging | condition | 87 | 19 |
| 2 | UV Radiation | mechanism | 64 | 20 |
| 3 | Collagen | anatomy | 64 | 19 |
| 4 | Wrinkles | condition | 62 | 17 |
| 5 | Reactive Oxygen Species | mechanism | 52 | 13 |
| 6 | Cellular Senescence | mechanism | 46 | 9 |
| 7 | Hyperpigmentation | condition | 46 | 8 |
| 8 | Photoaging | condition | 44 | 10 |
| 9 | Sunscreen | product | 41 | 16 |
| 10 | Antioxidants | ingredient_class | 41 | 11 |
| 11 | Tyrosinase | anatomy | 41 | 13 |
| 12 | Hyaluronic Acid | ingredient | 40 | 7 |
| 13 | Keratinocyte | anatomy | 38 | 14 |
| 14 | Oxidative Stress | mechanism | 38 | 13 |
| 15 | Matrix Metalloproteinase | anatomy | 38 | 11 |
| 16 | Skin Barrier | anatomy | 35 | 9 |
| 17 | FDA | regulation | 34 | 13 |
| 18 | Inflammation | mechanism | 34 | 5 |
| 19 | Stratum Corneum | anatomy | 32 | 9 |
| 20 | Intrinsic Aging | mechanism | 32 | 6 |

## Conceptos puente (aparecen en más capítulos)

- **UV Radiation** — 20 capítulos (v1, v2)
- **Skin Aging** — 19 capítulos (v1, v2)
- **Collagen** — 19 capítulos (v1, v2)
- **Wrinkles** — 17 capítulos (v1, v2)
- **Sunscreen** — 16 capítulos (v1, v2)
- **Keratinocyte** — 14 capítulos (v1, v2)
- **FDA** — 13 capítulos (v1, v2)
- **Reactive Oxygen Species** — 13 capítulos (sus, v1, v2)
- **Oxidative Stress** — 13 capítulos (v1, v2)
- **Tyrosinase** — 13 capítulos (v1, v2)
- **Fibroblast** — 12 capítulos (v1, v2)
- **Acne** — 12 capítulos (v1, v2)
- **Antioxidants** — 11 capítulos (sus, v1, v2)
- **Melanocyte** — 11 capítulos (v1, v2)
- **Matrix Metalloproteinase** — 11 capítulos (v1, v2)

## Comunidades

### 0. Regulación global y seguridad

188 conceptos · cohesión 0.89  
Principales: FDA, Preservatives, EU Cosmetics Regulation 1223/2009, Nanomaterials, TR CU 009/2011 Safety of Perfumery and Cosmetic Products, Trace Impurities, China Food and Drug Administration, Cosmetic Labeling Requirements, Cosmeceuticals, Animal Testing, Federal Food, Drug, and Cosmetic Act, Cosmetic Safety Assessment
  
Capítulos: Regulatory Requirements, IP and Global Market Success; Changing Regulatory Landscape in the U.S. and E.U.; Global Market Access: Russia; Saudi Arabia Cosmetics Market Access and Regulations; Global Market Access: China; Nanomaterials in Cosmetics: Regulatory and Safety; Antimicrobial Preservatives for Cosmetics

### 1. Envejecimiento cutáneo: senescencia y epigenética

174 conceptos · cohesión 0.74  
Principales: Skin Aging, Cellular Senescence, Inflammation, Sirtuins, Epigenetics, Nrf2 Signaling Pathway, MicroRNA, Resveratrol, NF-kB, DNA Methylation, Polyphenols, Proteasome
  
Capítulos: Molecular Cell Biology and Gene Analysis for Cosmetics; MicroRNAs in Skin Physiology; Fundamentals of Skin Anti-Aging Overview; Theories of Aging: Skin Anti-Aging at the Tipping Point; Sirtuins and Skin; Epigenetics of Skin Aging; Chronobiology of the Skin: Circadian Rhythm and Clock Genes

### 2. Epidermis y función barrera

163 conceptos · cohesión 0.78  
Principales: Keratinocyte, Skin Barrier, Stratum Corneum, Psoriasis, Transepidermal Water Loss, Ceramide, Desquamation, Fermentation, Natural Moisturizing Factor, Circadian Clock, Desmosome, Filaggrin
  
Capítulos: The Skin: Structure, Biochemistry, and Function; Lip Skin: Structure and Function; Probiotics in Topical Personal Healthcare; Green and Sustainable Bioactives from Biofermentation; Ingredients to Strengthen Skin Barrier Integrity; Marine Ingredients for Skin Care

### 3. Emolientes, siliconas y reología

148 conceptos · cohesión 0.86  
Principales: Sebum, Silicones, Rheology Modifiers, Silicone Elastomers, Dimethicone, Emulsion, Emulsion Stabilization, Carbomer, Viscosity, Alkyl Dimethicone, Cyclomethicone, Ethanol
  
Capítulos: Natural and Synthetic Polymers: Designing Rheological Properties; Rheology Modifiers and Consumer Perception; Silicones in Personal Care Products; Silicone Elastomer Applications

### 4. Radiación UV, estrés oxidativo y antioxidantes

146 conceptos · cohesión 0.7  
Principales: UV Radiation, Reactive Oxygen Species, Antioxidants, Oxidative Stress, Free Radicals, Ascorbic Acid, Hydrogen Peroxide, Amla, Tocopherol, Hair Graying, UVB Radiation, Carotenoids
  
Capítulos: Antioxidants: Extending Product Shelf Life; Antioxidants in Cosmetics for Anti-Aging; Anti-Senescence: Managing Cellular Functions

### 5. Dermis, colágeno y arrugas

142 conceptos · cohesión 0.67  
Principales: Collagen, Wrinkles, Photoaging, Matrix Metalloproteinase, Intrinsic Aging, Alpha Hydroxy Acids, Fibroblast, Retinoids, Elastin, Glycolic Acid, Tretinoin, Growth Factors
  
Capítulos: Compromised Skin in the Elderly; Topical Retinoids; Peptides for Anti-Aging Skin Care; AHAs and Beyond: Anti-Aging Ingredients; Cytokines, Growth Factors, and Stem Cells

### 6. Pigmentación, despigmentantes y acné

140 conceptos · cohesión 0.76  
Principales: Hyperpigmentation, Tyrosinase, Acne, Melanocyte, Melanogenesis, Melasma, Melanin, Japanese Quasi-Drug, Skin Penetration, Hydroquinone, Post-Inflammatory Hyperpigmentation, EP Global Skin Classification Scale
  
Capítulos: Classification Scale for Skin Complexions Around the World; Dermatologic Disorders in Skin of Color; Specialty Corrective Cosmeceuticals for Asian Ethnic Skin; Multi-Functional Botanicals for Topical Applications; Skin Whitener Ingredients

### 7. Tensioactivos y limpieza

116 conceptos · cohesión 0.84  
Principales: Shampoo, Surfactants, Anionic Surfactants, Nonionic Surfactants, PEG/PPG Dimethicone, Sodium Lauryl Sulfate, Polysorbates, Soap, Styling Polymers, Microbial Product Spoilage, Cationic Surfactants, Hair Conditioner
  
Capítulos: Preface; Surfactants

### 8. Fibra capilar: química y forma

100 conceptos · cohesión 0.86  
Principales: Hair, Disulfide Bond, Keratin, Hair Relaxer, Hair Cuticle, Apoptosis, Hot Iron Styling, Hair Damage, Hair Shape Memory, Cuticle Cell Buckling, Frizz, Gel Structure of the Amorphous Phase
  
Capítulos: The Hair: Editor's Overview; Physical and Chemical Properties of Hair; Hair Aging: Protection and Repair; Mechanisms of Changes in Hair Shape; The Nails

### 9. Hidratación: ácido hialurónico, aminoácidos y péptidos

77 conceptos · cohesión 0.67  
Principales: Hyaluronic Acid, Amino Acids, Peptides, Hyaluronan Fragments, Skin Elasticity, Arginine, Skin Hydration, Glycerol, Osmoprotection, Humectants, Proline, Sodium PCA
  
Capítulos: Hyaluronan: A Natural Moisturizer; Amino Acids

### 10. Maquillaje, labial y colorantes

75 conceptos · cohesión 0.79  
Principales: Sunscreen, Lipstick, Color Additives, Waxes, Certification-Exempt Color Additives, Titanium Dioxide, EU Positive Lists (Annexes IV-VI), Lips, Esters, Hair Breakage, Phytosteryl/Octyldodecyl Lauroyl Glutamate, Rainforest Ingredients
  
Capítulos: Ingredients for Creating the Next Greatest Lipstick

### 11. Folículo piloso y ciclo del cabello

72 conceptos · cohesión 0.82  
Principales: Hair Follicle, Hair Growth Cycle, Hair Loss, Dermal Papilla, Sebaceous Gland, Anagen, Androgenetic Alopecia, Eyelash, Dihydrotestosterone, Hair Follicle Aging, Hair Follicle Stem Cell, Lash Conditioner
  
Capítulos: Hair Follicle Anatomy and Biology; Eyelashes: Anatomy and Lash Conditioners

### 12. Cuidado oral

65 conceptos · cohesión 0.91  
Principales: Dental Caries, Fluoride, Gingivitis, Oral Malodor, Toothpaste, Dental Calculus, Dental Plaque, Dentin Hypersensitivity, Chlorhexidine, Mouthwash, Oral Care Products, Aphthous Ulcer
  
Capítulos: The Mouth and Oral Care

### 13. Fragancia: materias primas y evaporación

64 conceptos · cohesión 0.86  
Principales: Fragrance, Essential Oils, Fragrance Carriers, Natural Fragrance, Volatility, Botanical Extracts, Natural Isolates, Stability Testing, Water-Soluble Fragrance, Absolutes, Base Notes, Concretes
  
Capítulos: Creating the Right Fragrance for Your Personal Care Product

### 14. Hormonas, celulitis y percepción sensorial

64 conceptos · cohesión 0.79  
Principales: Estrogen, Cellulite, UV DNA Damage, Genistein, Sensory Perception, Forskolin, Lipolysis, Vulvar Atrophy, Algae, Cyclic AMP, Histone Deacetylase, Laminaria Digitata Extract
  
Capítulos: Feminine Rejuvenation; Ayurveda in Personal Care; Topical Reduction of Cellulite

### 15. Sostenibilidad y biodiversidad

57 conceptos · cohesión 0.86  
Principales: Plant Cell Culture, Sustainability, Open Innovation, Overharvesting, Pesticides, Sustainable Farming, Carbon Footprint, Herboretum Network, Open Innovation for Sustainability, Zeodration, Biodiversity, Local Cultivation
  
Capítulos: Sustainability Book Authors; Sustainability and Eco-Responsibility: A Global Approach

### 16. Desarrollo de producto y marketing de fragancias

51 conceptos · cohesión 0.94  
Principales: New Product-Development Process, Consumer Testing, Fragrance Brief, Fragrance House, Fragrance Packaging Design, Innovation, Marketing Mix (Four P's), Perfumer, Fragrance Evaluator, Market Research, New Product Failure, Sensory Cues
  
Capítulos: Marketing Concepts to Empower Technical People; Fragrance Packaging Design

### 17. Propiedad intelectual y mercados

49 conceptos · cohesión 0.88  
Principales: Patent, China, Intellectual Property, Japan, Trademark, Patent Infringement, Traditional Herbal Knowledge, United States, Utility Model, Utility Patent, India, United States Patent and Trademark Office
  
Capítulos: Intellectual Property: Patents and Trade Secrets

### 18. Glicación y ojeras

38 conceptos · cohesión 0.76  
Principales: Glycation, Advanced Glycation End Products, Dark Under-Eye Circles, Albizia Julibrissin Extract, Amadori Product, Epigenetic Orthodontics, Methylglyoxal, Protein Cross-Linking, Craniofacial Bone Remodeling, Carboxymethyl-Lysine, Glyoxalase, Glycotoxins
  
Capítulos: Glycation, Proteasome Activation, and Telomere Maintenance

### 19. Receptores olfativos y cribado

28 conceptos · cohesión 0.89  
Principales: High-Throughput Screening, Natural Fragrance Ingredient, Odorant Receptor, Human Sensory Testing, Cell Signaling, Cell-Based Assay, G-Protein-Coupled Receptor, Cell-Surface Receptors, Epidermal Growth Factor, Fragrance Blocker, Fragrance Enhancer, Calcium Influx
  
Capítulos: The Nose: Biology of Human Olfaction

### 20. Estrés, sueño y eje HPA

21 conceptos · cohesión 0.79  
Principales: Obstructive Sleep Apnea, Cortisol, Hypothalamic-Pituitary-Adrenal Axis, Insomnia, Adrenocorticotropic Hormone, Human Growth Hormone, Nitric Oxide, Deep Sleep (Stage N3), Epinephrine, Peroxynitrite, REM Sleep, Sleep Stages
  
Capítulos: Stress, Sleep and Epigenetic Orthodontics

### 21. Agua celular y nutrición

13 conceptos · cohesión 0.92  
Principales: Dietary Supplementation, Intracellular Water, Phase Angle, Basal Metabolic Rate, Bioelectrical Impedance Analysis, Cellular Water Principle, Extracellular Water, Sirtuin Activators, Total Body Water, Edematous Water, Glucosamine, Lecithin
  
Capítulos: The Cellular Water Principle

### 22. Ingredientes prohibidos por la FDA

11 conceptos · cohesión 0.92  
Principales: FDA Prohibited Cosmetic Ingredients, Bithionol, Halogenated Salicylanilides, Photocontact Sensitization, Prohibited Cattle Materials, Zirconium-Containing Complexes, Chlorofluorocarbon Propellants, Chloroform, Granuloma, Methylene Chloride, Vinyl Chloride

### 23. Anatomía genital femenina

6 conceptos · cohesión 1.0  
Principales: Vulva, Clitoris, Labia Majora, Labia Minora, Mons Veneris, Pudendal Nerve

### 24. Teorías neuroendocrinas del envejecimiento

4 conceptos · cohesión 1.0  
Principales: Death Hormone Theory, Hypothalamus, Neuro-Endocrine Theory of Aging, Thyroxin

### 25. Intelligent Targeting Carrier / Poly(lactic-co-glycolic acid) / Polyvinyl Alcohol

3 conceptos · cohesión 1.0  
Principales: Intelligent Targeting Carrier, Poly(lactic-co-glycolic acid), Polyvinyl Alcohol

### 26. Lichen Planus / Anonychia / Onychorrhexis

3 conceptos · cohesión 1.0  
Principales: Anonychia, Lichen Planus, Onychorrhexis

### 27. Eco-Responsibility / Eco-Design / Corporate Social Responsibility

3 conceptos · cohesión 1.0  
Principales: Eco-Responsibility, Corporate Social Responsibility, Eco-Design

### 28. Omega-7 Fatty Acids / Macadamia Nut Oil / Sea Buckthorn Oil

3 conceptos · cohesión 1.0  
Principales: Omega-7 Fatty Acids, Macadamia Nut Oil, Sea Buckthorn Oil

### 29. In Vitro Epithelial Cell Models / Alternatives to Animal Testing / Rosette Test

3 conceptos · cohesión 1.0  
Principales: In Vitro Epithelial Cell Models, Alternatives to Animal Testing, Rosette Test

### 30. Marine Algae / Phlorotannins / Sulfated Polysaccharides

3 conceptos · cohesión 1.0  
Principales: Marine Algae, Phlorotannins, Sulfated Polysaccharides

### 31. Enzyme Biology-Based Skin Care Marketing / Papain / Bromelain

3 conceptos · cohesión 1.0  
Principales: Enzyme Biology-Based Skin Care Marketing, Bromelain, Papain

_Además, 27 comunidades de menos de 3 conceptos (nodos aislados o pares)._

## Conexiones sorprendentes

Aristas que cruzan comunidades entre conceptos que, por lo demás, aparecen en capítulos distintos.

- **UV Radiation** → `activates` → **Inflammasome** (EXTRACTED, 1.0) — _UV activates inflammasomes in keratinocytes_
- **Gene Expression Analysis** → `conceptually_related_to` → **Skin Aging** (EXTRACTED, 1.0) — _Gene expression studies give insight into skin aging_
- **UV Radiation** → `causes` → **Photo-Aging of Hair** (EXTRACTED, 1.0) — _Long-term UV exposure causes chemical degradation of hair proteins and lipids_
- **Hydroxyl Radical** → `causes` → **Skin Aging** (EXTRACTED, 1.0) — _hydroxyl radicals and peroxynitrite are initiators of aging_
- **UV Radiation** → `increases` → **Carboxymethyl-Lysine** (EXTRACTED, 1.0) — _UV oxidation accelerates CML formation_
- **UV Radiation** → `increases` → **Epigenetic Drift** (EXTRACTED, 1.0) — _UV exacerbates epigenetic drift_
- **Skin Aging** → `decreases` → **Sensory Perception** (EXTRACTED, 1.0) — _advancing age most significant effect on sensory perception_
- **Ursolic Acid** → `increases` → **Collagen** (EXTRACTED, 1.0) — _Increases collagen in fibroblasts_
- **Skin Aging** → `decreases` → **Calcium** (EXTRACTED, 1.0) — _Loss of bioavailable calcium_
- **Skin Aging** → `decreases` → **Cytokeratins** (EXTRACTED, 1.0) — _Cytokeratin synthesis decreases_
- **Skin Aging** → `decreases` → **Intercellular Communication** (EXTRACTED, 1.0) — _Less communication between keratinocytes_
- **Padina Pavonica Extract** → `protects_against` → **Skin Aging** (EXTRACTED, 1.0) — _Prevents premature aging_
- **Pollution** → `contributes_to` → **Skin Aging** (EXTRACTED, 1.0) — _Linked to premature aging in cities_
- **Sphacelaria Scoparia Extract** → `increases` → **Collagen** (EXTRACTED, 1.0) — _stimulates collagen I and IV synthesis_
- **Laminaria Digitata Extract** → `increases` → **Collagen** (EXTRACTED, 1.0) — _collagen synthesis returns to young condition_

## Hiperaristas (grupos de 3+ conceptos)

- **Top, middle and base notes of the fragrance pyramid**: Base Notes, Fragrance Pyramid, Middle Notes, Top Notes, Volatility
- **Natural fragrance material categories**: Absolutes, Concretes, Essential Oils, Natural Isolates
- **Three hurdles to perceiving a fragrance material**: Octanol-Water Partition Coefficient, Odor Detection Threshold, Raoult's Law, Volatility
- **Brief documents in fragrance development**: Fragrance Brief, Mood Board, Olfactive Families, Product Brief
- **Multi-sensory cues of fragrance packaging (hearing, seeing, touching, smelling)**: Bottle Ergonomics, Color-Scent Association, Consumer Testing, Fragrance Storytelling, Sensory Cues
- **Three stages of cell signaling**: Cell Signaling, Cell-Surface Receptors, Gene Expression, GTPase, Protein Kinases
- **Epigenetic mechanisms regulating gene expression**: Chromatin, DNA Methylation, Epigenetics, Histones, Histone Modification, Nucleosome
- **Phytochemical activators of Nrf2 and AMPK in skin**: AMPK, Berberine, Curcumin, Epigallocatechin Gallate, Nrf2 Signaling Pathway, Quercetin, Resveratrol, Sulforaphane
- **ICCR priority regulatory topics**: Allergens, Alternatives to Animal Testing, Endocrine Disruptors, International Cooperation on Cosmetics Regulation, In Silico Prediction Models, Nanomaterials, Trace Impurities
- **Steps toward EU compliance**: Cosmetic Labeling Requirements, Cosmetic Products Notification Portal, ISO 22716 Cosmetics GMP, Product Information File, Responsible Person, Safety Assessor
- **SCCS four-step risk assessment and MoS**: Margin of Safety, No Observed Adverse Effect Level, Four-Step Risk Assessment, SCCS Notes of Guidance, Systemic Exposure Dosage
- **FDA prohibited cosmetic ingredients**: Bithionol, Chlorofluorocarbon Propellants, Chloroform, Halogenated Salicylanilides, Methylene Chloride, Prohibited Cattle Materials, Vinyl Chloride, Zirconium-Containing Complexes
- **CU higher-risk categories requiring State Registration**: Children's Cosmetics, CU State Registration, Fluoride, Hair Color, Hydrogen Peroxide, Nanomaterials
- **CU pathogen limits in cosmetics**: Candida albicans, Escherichia coli, Microbiological Contamination, Pseudomonas aeruginosa, Staphylococcus aureus, TR CU 009/2011 Safety of Perfumery and Cosmetic Products
- **SFDA additional ingredient bans and limits**: Alpha Hydroxy Acids, Hydroquinone, Retinol, Salicylic Acid, SFDA Guidance for Products Classification, Sulfur, Tretinoin, Triclosan, Urea, Zinc Oxide
- **KSA market access process**: Arabic Labeling Requirement, Certificate of Conformity (KSA), Country of Origin Labeling, GSO 1943/2009 Cosmetic Products Safety Requirements, Saudi Food and Drug Authority
- **Routine impurities tested in Chinese safety assessment**: Acrylamide, 1,4-Dioxane, Margin of Safety, Methanol, N-Nitrosodiethanolamine, Phenol, Trace Impurities
- **Skin sensitization testing in China**: China Food and Drug Administration, Guinea Pig Maximization Test, Local Lymph Node Assay, Skin Sensitization, 3R Principle
- **Nanomaterial characterization parameters**: Dose Metrics for Nanomaterials, Nanomaterials, Nanomaterial Physicochemical Characterization, SCCS Guidance on Safety Assessment of Nanomaterials in Cosmetics
- **Nanomaterial interference with toxicity assays**: Nanomaterial Assay Interference, Carbon Nanoparticles, ELISA, LDH Assay, Metal Oxide Nanoparticles, MTT Assay, Reactive Oxygen Species
- **Nanomaterial cosmetic regulation by jurisdiction**: EU Cosmetics Regulation 1223/2009, FDA Draft Guidance on Safety of Nanomaterials in Cosmetic Products, Health Canada, [nano] Ingredient Labeling, EU Nanomaterial Pre-Market Notification, New Substances Notification Regulations
- **Forms of IP used in cosmetics**: Copyright, Design Patent, Plant Patent, Service Mark, Trade Dress, Trade Secret Protection, Trademark, Utility Model, Utility Patent
- **Patentability criteria**: Industrial Applicability, Nonobviousness, Novelty, Patent
- **Types of patent infringement**: Direct Infringement, Doctrine of Equivalents, Indirect Infringement, Literal Infringement, Patent Infringement, Willful Infringement
- **Layers of the epidermis**: Stratum Basale, Stratum Corneum, Stratum Granulosum, Stratum Lucidum, Stratum Spinosum
- **Melanin formation pathway**: Eumelanin, Melanin, Melanosome, Pheomelanin, Tyrosinase, Tyrosine
- **Stratum corneum penetration pathways**: Follicular Penetration Pathway, Intercellular Penetration Pathway, Polar Penetration Pathway, Transcellular Penetration Pathway
- **EP Global Skin Classification classes I-XI**: EP Class I (Caucasian I), EP Class II (Caucasian II), EP Class III (Caucasian III), EP Class IV (Hispanic/Latino), EP Class IX (Native American/Alaskan), EP Class V (Mediterranean/Asian I), EP Class VI (Asian II), EP Class VII (Asian III), EP Class VIII (Pacific Islander), EP Class X (Black/African American), EP Class XI (Mixed Race)
- **EP scale assessment categories**: EP Global Skin Classification Scale, Skin Evaluation Questionnaire, Skin Type (Oily/Dry), Skin Undertone, Sun Exposure
- **Natural alternatives to hydroquinone for hyperpigmentation**: Arbutin, Dioic Acid, Ellagic Acid, Kojic Acid, Licorice Extract, Mulberry Extract, Niacinamide, Resveratrol, Rucinol, Soy
- **Vitiligo treatment options**: Cosmetic Camouflage, Excimer Laser, Monobenzone, Narrow-Band UVB Phototherapy, Topical Calcineurin Inhibitors, Topical Corticosteroids, Vitamin D3 Analogs
- **Treatments for melasma**: Fractional Laser, Glycolic Acid, Intense Pulsed Light, Kojic Acid, Lactic Acid, Microdermabrasion, Sunscreen, Trichloroacetic Acid Peel
- **Preventive regimen for hyperpigmentation**: Exfoliation, Skin Whitening Products, Sunscreen
- **UV-induced photo-aging signaling cascade**: AP-1, Collagen, Cytokines, MAP Kinase Pathway, Matrix Metalloproteinase, Reactive Oxygen Species, UV Radiation
- **Contributing factors to elderly dry skin**: Dry Skin, Glycerol, Lactic Acid, Pyrrolidone Carboxylic Acid, Sebum, Stratum Corneum Turnover
- **Cosmeceutical treatments for aging skin**: Alpha Hydroxy Acids, Anti-Glycation Compounds, Antioxidants, Beta Hydroxy Acids, Niacinamide, Peptides, Retinol
- **Layers of the hair cuticle cell**: Cell Membrane Complex, Endocuticle, Epicuticle, Exocuticle, 18-Methyl Eicosanoic Acid
- **Three cell types of the hair fiber**: Cortical Cell, Cuticle Cell, Hair Medulla
- **Follicle life cycle phases**: Anagen, Catagen, Hair Growth Cycle, Telogen
- **Compartments of the anagen hair follicle**: Arrector Pili Muscle, Dermal Papilla, Hair Bulb, Hair Follicle Bulge, Inner Root Sheath, Matrix Keratinocyte, Outer Root Sheath
- **Extended hair cycle phases**: Anagen, Catagen, Exogen, Kenogen, Telogen
- **Molecular regulators of catagen entry**: Basic Fibroblast Growth Factor, Catagen, Insulin-Like Growth Factor 1, Interleukin-1 Alpha, Transforming Growth Factor Beta, Tumor Necrosis Factor Alpha, Vascular Endothelial Growth Factor
- **Signs of aging hair**: Frizz, Hair Breakage, Hair Graying, Hair Loss, Hair Manageability, Hair Shine, Perceived Hair Dryness
- **Oxidative mechanism of hair graying**: Catalase, Hair Graying, Hydrogen Peroxide, Melanocyte, Methionine Sulfoxide Reductase, Tyrosinase
- **Chemical changes of hair photo-aging**: Cysteic Acid, Disulfide Bond, Hair Porosity, Photo-Aging of Hair, Tryptophan, UV Radiation
- **Three steps of hair shape change (soften, impose, lock)**: Disulfide Bond, Hair Relaxer, Hot Iron Styling, Hydrogen Bond, Permanent Waving, Vitrification, Water-Setting
- **Proposed mechanisms of alkaline straightening**: Disulfide Bond, Hair Relaxer, Lanthionine, Protein Denaturation, Supercontraction
- **Factors setting hair shape in motion**: Hair Drying Rate, Hair Volume, Hydrogen Bond, Inter-Fiber Friction, Hair Shape Memory
- **Generations of lash conditioners**: Adipose-Derived Stem Cell Peptides, Dechloro Ethylcloprostenolamide, Lash Conditioner, Peptides, Prostaglandin Analogues
- **Safety assessment of dechloro ethylcloprostenolamide**: Ames Test, Dechloro Ethylcloprostenolamide, Local Lymph Node Assay, Repeat Insult Patch Test
- **Glands around eyelash follicles**: Eyelash, Meibomian Gland, Moll Gland, Zeis Gland
- **Components of the Nail Unit**: Cuticle, Epionychium, Hyponychium, Lunula, Nail Matrix, Nail Plate, Nailbed, Proximal Nail Fold
- **Causes of onycholysis**: Artificial Nails, Candida, Contact Dermatitis, Formaldehyde, Onycholysis, Onychomycosis, Psoriasis
- **Sebum composition**: Cholesterol, Sebum, Squalene, Triglycerides, Wax Monoesters
- **Stratum corneum barrier lipids**: Ceramide, Cholesterol, Free Fatty Acids, Skin Barrier
- **Cell-based fragrance discovery pipeline**: Cell-Based Assay, High-Throughput Screening, Iterative Screening, Odorant Receptor, Human Sensory Testing, Z' Factor
- **Tooth structure layers**: Cementum, Dental Enamel, Dental Pulp, Dentin, Dentinal Tubule
- **Caries process**: Critical pH, Demineralization, Dental Caries, Dental Plaque, Fluoride, Remineralization, Saliva, Streptococcus Mutans, Sucrose
- **Clinically proven antigingivitis agents**: Cetylpyridinium Chloride, Chlorhexidine, Essential Oils, Gingivitis, Stannous Fluoride, Triclosan
- **Vulvar anatomy**: Clitoris, Labia Majora, Labia Minora, Mons Veneris, Vulva
- **Cutaneous mechanoreceptors**: Meissner Corpuscle, Merkel Cell, Pacinian Corpuscle, Ruffini Receptor, Sensory Perception
- **ADSC conditioned media factors**: Growth Factors, Human Adipocyte Conditioned Media Extract, Superoxide Dismutase, Transforming Growth Factor Beta, Vascular Endothelial Growth Factor
- **Six traits of OIS companies**: Collaboration, Open Innovation for Sustainability, Six Traits of Sustainable Companies, Transparency, Triple Bottom Line
- **Plant cell culture phenylpropanoid production**: Chlorogenic Acid, Echinacoside, Elicitation, NF-kB, Nrf2 Signaling Pathway, Phenylpropanoids, Plant Cell Culture, Verbascoside
- **Eco-responsible plant ingredient chain**: Carbon Footprint, Ethanol, Plant Extraction, Glycerol, Good Agricultural Practices, Local Cultivation, Plant Drying, Zeodration
- **Breakthrough ingredient technologies highlighted in 9th edition**: Biotechnology/Fermentation Ingredient Production, Hyaluronic Acid, Marine Ingredients, Plant Stem Cell Technology, Skin Whitening
- **Four surfactant charge classes**: Amphoteric Surfactants, Anionic Surfactants, Cationic Surfactants, Nonionic Surfactants
- **Four emulsion stabilization mechanisms**: Charge Stabilization, Liquid Crystalline Lamellar Phase, Polymeric Stabilization, Steric Stabilization
- **Typical shampoo surfactant system**: Alkanolamides, Betaines, Shampoo, Sulfates
- **Lipstick comfort-shine-wear tradeoff**: Color Additives, Film Formers, Holy Grail of Lipsticks, Lipstick, Polybutene
- **Lipstick wax backbone**: Beeswax, Candelilla Wax, Carnauba Wax, Castor Oil, Lipstick Crystalline Structure
- **Lipstick feel-enhancing powders**: Boron Nitride, Calcium Aluminum Borosilicate, Lauroyl Lysine, Nylon-12, Polymethyl Methacrylate, Polytetrafluoroethylene, Spherical Silica
- **HA molecular-weight tiers and their cosmetic effects**: Hyaluronan Fragments, Hyaluronic Acid, Skin Hydration, Skin Penetration, Transepidermal Water Loss
- **Analytical techniques for HA molecular weight**: Electrospray Ionization Mass Spectrometry, Hyaluronan Fragments, MALDI-TOF, Size-Exclusion Chromatography with Multi-Angle Light Scattering
- **HA chemical modification strategies**: Carbodiimide Coupling, Divinyl Sulfone, Hyaluronan Chemical Modification, Hyaluronan Cross-Linking, Hydrophobized Hyaluronan
- **ROS-inflammation-aging cascade**: Collagen, Elastin, Inflammation, Matrix Metalloproteinase, Reactive Oxygen Species, Skin Aging, UV Radiation
- **Triphala three-plant blend**: Amla, Terminalia Bellirica, Terminalia Chebula, Triphala
- **Probiotic molecule to TLR to defensin innate defense pathway**: Defensins, Innate Immunity, Keratinocyte, Probiotic Derived Bioactive, Toll-Like Receptor
- **Probiotic cell-wall immune bioactives**: Beta-1,3-D-Glucan, Lipoteichoic Acid, Peptidoglycan, Zymosan
- **In vitro PDB efficacy testing**: Defensins, ELISA, In Vitro Epithelial Cell Models, Quantitative Real-Time PCR
- **Cosmetic fermentation organism platforms**: Aspergillus oryzae, Lactobacillus, Microalgae, Plant Cell Culture, Saccharomyces cerevisiae
- **UV-oxidative stress-MMP collagen degradation cascade**: Collagen, Matrix Metalloproteinase, Oxidative Stress, Skin Aging, UV Radiation
- **Algal skin-care actives**: Chlorella Extract, Corallina pilulifera Extract, Fucoxanthin, Phlorotannins, Ulkenia Extract
- **Botanical extraction methods**: Lyophilization, Solvent Extraction, Botanical Extract Standardization, Supercritical CO2 Extraction
- **Melanogenesis signaling and inhibitors**: Alpha-MSH, Cyclic AMP, Melanin, Melanocyte, MITF, Tyrosinase
- **Natural skin lighteners vs benchmarks**: Amla, Arbutin, Ellagic Acid, Hydroquinone, Kojic Acid, Oxyresveratrol, Tetrahydrocurcumin
- **Layers of the epidermis**: Corneocyte, Epidermal Layers, Keratinocyte, Keratinocyte Differentiation, Stratum Corneum
- **Calcium-dependent epidermal structures**: Calcium, Calcium Signaling, Cytokeratins, Desmosome, Intercellular Communication
- **Dermal-epidermal junction components**: Collagen IV, Dermal-Epidermal Junction, Fibronectin, Hemidesmosomes, Integrins, Laminins
- **Six factors encouraging microbial growth**: Osmotic Pressure, pH, Microbial Product Spoilage, Surfactants, Water Activity
- **Most frequently used preservatives (US/Canada)**: Butylparaben, DMDM Hydantoin, Methylisothiazolinone, Methylparaben, Phenoxyethanol, Propylparaben
- **Societal-quadrant regulators**: Environmental Protection Agency, FDA, Four-Quadrant Model, Federal Trade Commission, Personal Care Products Council
- **Steps of lipid auto-oxidation**: Lipid Hydroperoxides, Initiation, Propagation, Termination, Secondary Oxidation Products
- **Carnosic acid antioxidant cascade**: Carnosic Acid, Carnosol, Phenolic Diterpenes, Rosemary Extract
- **Oxidation and antioxidant assays**: DPPH Assay, ORAC Assay, Oxidative Stability Index, Peroxide Value, Secondary Oxidation Product Assays
- **Rheological additives for aqueous systems**: Cellulose Derivatives, Clays, Fatty Alcohols, Natural Gums, Polyethylene Glycol, Starch Derivatives, Synthetic Polymer Thickeners
- **Rheological additives for nonaqueous systems**: Aluminum Magnesium Hydroxide Stearate, Castor Oil Derivatives, Fatty Acids, Organoclays, Polyethylene, Silica, Stearic Acid Derivatives
- **Rheology-linked sensory attributes of emulsions**: Osmosis, Pseudoplasticity, Quantitative Descriptive Analysis, Human Sensory Testing, Hair Viscoelasticity, Yield Stress
- **Main synthetic polymeric rheology modifiers**: Acrylates/C10-30 Alkyl Acrylate Crosspolymer, AMPS Polymers, ASE/HASE Polymers, Carbomer
- **Critical rheological parameters**: Hair Viscoelasticity, Viscosity, Yield Stress
- **Silicone structure classes**: Alkyl Dimethicone, Alkyl PEG/PPG Dimethicone, Cyclomethicone, Dimethicone, PEG/PPG Dimethicone, Silicone Elastomers, Silicone Gum, Silicone Resins
- **Cyclomethicone (D5) replacement approaches**: Alkyl Dimethicone, Cyclopentasiloxane, Dimethicone, Ethyl Methicone, Soybean Oil
- **Dimethicone copolyol function vs molecular weight**: Emulsion, Eye Irritation, PEG/PPG Dimethicone, Wetting
- **Functions of silicone elastomers**: Controlled Release Delivery, Mattifying, Sebum, Silicone Elastomers, Soft-Focus Effect
- **Melanin synthesis and delivery pathway**: Alpha-MSH, Endothelin, Keratinocyte, Melanin Transfer, Melanocyte, Melanosome, MITF, Protease-Activated Receptor 2, Proopiomelanocortin, Tyrosinase, UV Radiation
- **Japanese whitening quasi-drug actives**: Adenosine Monophosphate Disodium Salt, Arbutin, Ascorbic Acid, 4-n-Butylresorcinol, Chamomile Extract, Ellagic Acid, Kojic Acid, Linoleic Acid, Magnolignan, Placental Extract, 4-Methoxy Potassium Salicylate, Rhododendrol, Tranexamic Acid, Tranexamic Acid Cetyl Ester Hydrochloride
- **Whitening strategies by cellular target**: Corneocyte, Desquamation, Keratinocyte, Melanocyte, Substance P
- **Marine cosmetic resources**: Algae, Exopolysaccharides, Halophytes, Marine Polysaccharides, Photolyase, Sea Minerals
- **Blue algae DNA protection and repair**: UV DNA Damage, DNA Repair, Phormidium Extract, Photolyase, Thioredoxin, UV Radiation
- **Marine slimming pathway**: Adipocyte, Cyclic AMP, Laminaria Digitata Extract, Lipolysis, Sphacelaria Scoparia Extract
- **Proposed hormonal etiology of cellulite**: Adipose Tissue, Cellulite, Collagen Degradation, Estrogen, Fibroblast, Interleukin-1 Alpha, MMP-1, Progesterone, Collagen Trabeculae
- **Topical anti-cellulite strategy**: Ascorbic Acid, Asiatic Acid, Caffeine, Carnitine, Chrysin, Diindolylmethane, Genistein, Grape Seed Extract
- **Fat mobilization pathway**: Beta-Oxidation, Carnitine, Cyclic AMP, Lipolysis, Phosphodiesterase
- **Forms of vitamin A**: Retinal, Retinol, Retinyl Esters, Tretinoin
- **Acne pathogenesis and retinoid targets**: Acne, Microcomedo, Propionibacterium acnes, Toll-Like Receptor 2
- **Categories of cosmetic peptides**: Antioxidant Peptides, Carrier Peptides, Enzyme Inhibitor Peptides, Matrikines, Neuropeptides
- **Extracellular matrix components**: Collagen, Elastin, Extracellular Matrix, Fibronectin, Glycosaminoglycan, Integrins
- **MicroRNA biogenesis machinery**: DICER1, Drosha, Exportin-5, MicroRNA, RNA-Induced Silencing Complex
- **miR-203 epidermal targets**: ABL1, c-Jun, miR-203, p63 (DNp63), SOCS3
- **Senescence regulatory network**: Cellular Senescence, miR-34a, p16-pRB Pathway, p53-p21 Pathway, Senescence-Associated MicroRNAs, SIRT1
- **Composition of natural moisturizing factor**: Amino Acids, Natural Moisturizing Factor, Pyrrolidone Carboxylic Acid, Sodium Lactate
- **UV-AP-1-collagenase wrinkle cascade**: AP-1, Collagen, Collagenase, UV Radiation, Wrinkles, Zinc PCA
- **Glycine:proline:alanine collagen cocktail**: Alanine, Collagen, Glycine, Proline
- **Generations of hydroxy acids**: Alpha Hydroxy Acids, Bionic Acids, N-Acetyl Amino Acids, N-Acetylglucosamine, Polyhydroxy Acids
- **AHA effects across skin layers**: Alpha Hydroxy Acids, Collagen, Desquamation, Glycosaminoglycan, Keratinocyte, Melanogenesis
- **Low-pH AHA formulation toolkit**: Acid-Swellable Associative Thickeners, Amphoteric AHA Complex, Nonionic Emulsifiers, pKa, Polyacrylic Acid Polymers, Smectite Clays
- **Free radical-MMP ECM degradation in aging**: Collagen, Extracellular Matrix, Free Radicals, Matrix Metalloproteinase, Tissue Inhibitors of Metalloproteinases
- **Biologic cosmeceutical classes**: Adipose-Derived Stem Cell, Cytokines, Growth Factors, Plant Stem Cell, Stem Cells
- **Zones of the dermal-epidermal junction**: Collagen IV, Collagen VII, Dermal-Epidermal Junction
- **Skin antioxidant network**: Antioxidant Network, Ascorbic Acid, Catalase, Glutathione, Glutathione Peroxidase, Superoxide Dismutase, Tocopherol, Ubiquinone, Uric Acid
- **UV-induced ROS generation pathways**: Fenton Reaction, Free Iron and Copper, Hydroxyl Radical, NADPH Oxidase, Endogenous Photosensitizers, Singlet Oxygen, UV Radiation
- **Mainstream theories of aging**: Deficient Immune System/Autoimmune Theory, Caloric Restriction, Cross-Linking Theory, Death Hormone Theory, Free Radical Theory of Aging, Genetic Control Theory, Glycation Theory, Hayflick Limit Theory, Inflammation Theory of Aging, Mitochondrial Theory of Aging, Mutation Accumulation and DNA/RNA Damage Theory, Neuro-Endocrine Theory of Aging, Telomere Theory of Aging, Waste Accumulation Theory, Wear and Tear Theory
- **Free radical–arachidonic acid inflammation cycle**: Arachidonic Acid, Free Radicals, Inflammation, Inflammatory Cytokines, Phospholipase A2
- **Body water compartments**: Edematous Water, Extracellular Water, Intracellular Water, Total Body Water
- **BIA hydration/vitality parameters**: Basal Metabolic Rate, Bioelectrical Impedance Analysis, Intracellular Water, Phase Angle
- **Ubiquitin tagging and proteasomal degradation**: Proteasome, Proteolysis, Ubiquitin, Ubiquitin-Proteasome Pathway
- **Enzyme dysfunctions driving senescence**: Advanced Glycation End Products, Immunosenescence, Mitochondrial Free Radical Theory of Aging, Oxidative Stress, Peroxisome, Proteasome
- **Natural osmoprotectants/compatible solutes**: Carnitine, Ectoine, Glycine Betaine, N-Acetylglutaminylglutamine Amide, Proline, Proline Betaine, Taurine, Trehalose
- **AGE formation stages**: Advanced Glycation End Products, Amadori Product, Glycation, Glyoxal, Methylglyoxal, Schiff Base
- **Cellular protein clearance systems**: Autophagy, LC3-II, Proteasome, Ubiquitin, Ubiquitin-Proteasome Pathway
- **Telomere maintenance machinery**: Shelterin Complex, Telomerase, Telomeres, TRF2
- **Seven mammalian sirtuin isotypes**: SIRT1, SIRT2, SIRT3, SIRT4, SIRT5, SIRT6, SIRT7
- **Sirtuin NAD+-dependent deacetylation reaction**: NAD+, Niacinamide, 2'-O-Acetyl-ADP Ribose, Sirtuins
- **Primary epigenetic mechanisms**: Chromatin Remodeling, DNA Methylation, Histone Modification, Noncoding RNAs
- **Dietary/natural epigenetic modifiers**: Ascorbic Acid, Curcumin, Diallyl Sulfide, Epigallocatechin Gallate, Genistein, Resveratrol, Sulforaphane, Vitamin D
- **DNA damage response repair pathways**: Base Excision Repair, DNA Damage Response, Nucleotide Excision Repair, p53
- **Mammalian core clock feedback loop**: Casein Kinase, CLOCK/BMAL-1 Complex, Cryptochromes, PER Genes, REV-ERB alpha, ROR alpha
- **Nighttime skin repair/regeneration functions**: Cell Proliferation, DNA Repair, Skin Barrier, Stem Cells, Transepidermal Water Loss
- **HPA axis stress hormone cascade**: Adrenocorticotropic Hormone, Cortisol, Epinephrine, Hypothalamic-Pituitary-Adrenal Axis, Norepinephrine
- **Sleep stages**: Deep Sleep (Stage N3), Human Growth Hormone, REM Sleep, Sleep Stages
- **Epigenetic orthodontics mechanism**: Craniofacial Bone Remodeling, DNA Methylation, Functional (Formational) Appliances, Mechanotransduction

## Preguntas sugeridas para explorar el grafo

- ¿Qué relación tiene **Skin Aging** con las demás comunidades?
- ¿Qué relación tiene **UV Radiation** con las demás comunidades?
- ¿Qué relación tiene **Collagen** con las demás comunidades?
- ¿Qué relación tiene **Wrinkles** con las demás comunidades?
- ¿Qué relación tiene **Reactive Oxygen Species** con las demás comunidades?
- ¿Qué relación tiene **Cellular Senescence** con las demás comunidades?
- ¿Por qué **UV Radiation** se conecta con **Inflammasome**?
- ¿Por qué **Gene Expression Analysis** se conecta con **Skin Aging**?
- ¿Por qué **UV Radiation** se conecta con **Photo-Aging of Hair**?
- ¿Por qué **Hydroxyl Radical** se conecta con **Skin Aging**?

## Capítulos

| Archivo | Capítulo | Comunidad |
|---|---|---|
| sus-03-authors.md | Sustainability Book Authors | Sostenibilidad y biodiversidad |
| sus-04-Part_12.1.md | Sustainability and Eco-Responsibility: A Global Approach | Sostenibilidad y biodiversidad |
| v1-01-abouttheeditor.md | About the Editor-in-Chief | Society of Cosmetic Chemists |
| v1-02-preface.md | Preface | Tensioactivos y limpieza |
| v1-03-Part1.1.md | Marketing Concepts to Empower Technical People | Desarrollo de producto y marketing de fragancias |
| v1-04-Part_1.2.md | Creating the Right Fragrance for Your Personal Care Product | Fragancia: materias primas y evaporación |
| v1-05-Part_1.3.md | Fragrance Packaging Design | Desarrollo de producto y marketing de fragancias |
| v1-06-Part_1.4.md | Molecular Cell Biology and Gene Analysis for Cosmetics | Envejecimiento cutáneo: senescencia y epigenética |
| v1-07-Part_2.1.md | Regulatory Requirements, IP and Global Market Success | Regulación global y seguridad |
| v1-08-Part_2.2.md | Changing Regulatory Landscape in the U.S. and E.U. | Regulación global y seguridad |
| v1-09-Part_2.3.1.md | Global Market Access: Russia | Regulación global y seguridad |
| v1-10-Part_2.3.2.md | Saudi Arabia Cosmetics Market Access and Regulations | Regulación global y seguridad |
| v1-11-Part_2.3.3.md | Global Market Access: China | Regulación global y seguridad |
| v1-12-Part_2.3.4.md | Nanomaterials in Cosmetics: Regulatory and Safety | Regulación global y seguridad |
| v1-13-Part_2.4.md | Intellectual Property: Patents and Trade Secrets | Propiedad intelectual y mercados |
| v1-14-Part_3.1.md | The Skin: Structure, Biochemistry, and Function | Epidermis y función barrera |
| v1-15-Part_3.2.1.md | Classification Scale for Skin Complexions Around the World | Pigmentación, despigmentantes y acné |
| v1-16-Part_3.2.2.md | Dermatologic Disorders in Skin of Color | Pigmentación, despigmentantes y acné |
| v1-17-Part_3.2.3.md | Specialty Corrective Cosmeceuticals for Asian Ethnic Skin | Pigmentación, despigmentantes y acné |
| v1-18-Part_3.2.4.md | Compromised Skin in the Elderly | Dermis, colágeno y arrugas |
| v1-19-Part_3.3.0.md | The Hair: Editor's Overview | Fibra capilar: química y forma |
| v1-20-Part_3.3.1.md | Physical and Chemical Properties of Hair | Fibra capilar: química y forma |
| v1-21-Part_3.3.2.md | Hair Follicle Anatomy and Biology | Folículo piloso y ciclo del cabello |
| v1-22-Part_3.3.3.md | Hair Aging: Protection and Repair | Fibra capilar: química y forma |
| v1-23-Part_3.3.4.md | Mechanisms of Changes in Hair Shape | Fibra capilar: química y forma |
| v1-24-Part_3.3.5.md | Eyelashes: Anatomy and Lash Conditioners | Folículo piloso y ciclo del cabello |
| v1-25-Part_3.4.md | The Nails | Fibra capilar: química y forma |
| v1-26-Part_3.5.md | The Nose: Biology of Human Olfaction | Receptores olfativos y cribado |
| v1-27-Part_3.6.1.md | The Mouth and Oral Care | Cuidado oral |
| v1-28-Part_3.7.md | Lip Skin: Structure and Function | Epidermis y función barrera |
| v1-29-Part_3.8.md | Feminine Rejuvenation | Hormonas, celulitis y percepción sensorial |
| v2-03-Part_4.1.0.md | Editor's Introduction to the Ingredient Section | Biotechnology/Fermentation Ingredient Production |
| v2-04-Part_4.1.1.md | Surfactants | Tensioactivos y limpieza |
| v2-05-Part_4.1.2.md | Ingredients for Creating the Next Greatest Lipstick | Maquillaje, labial y colorantes |
| v2-06-Part_4.1.3.md | Hyaluronan: A Natural Moisturizer | Hidratación: ácido hialurónico, aminoácidos y péptidos |
| v2-07-Part_4.1.4.1.md | Ayurveda in Personal Care | Hormonas, celulitis y percepción sensorial |
| v2-08-Part_4.1.4.2.md | Probiotics in Topical Personal Healthcare | Epidermis y función barrera |
| v2-09-Part_4.1.4.3.md | Green and Sustainable Bioactives from Biofermentation | Epidermis y función barrera |
| v2-10-Part_4.1.5.md | Multi-Functional Botanicals for Topical Applications | Pigmentación, despigmentantes y acné |
| v2-11-Part_4.1.6.md | Ingredients to Strengthen Skin Barrier Integrity | Epidermis y función barrera |
| v2-12-Part_4.1.7.1.md | Antimicrobial Preservatives for Cosmetics | Regulación global y seguridad |
| v2-13-Part_4.1.7.2.md | Antioxidants: Extending Product Shelf Life | Radiación UV, estrés oxidativo y antioxidantes |
| v2-14-Part_4.2.1.md | Natural and Synthetic Polymers: Designing Rheological Properties | Emolientes, siliconas y reología |
| v2-15-Part_4.2.2.md | Rheology Modifiers and Consumer Perception | Emolientes, siliconas y reología |
| v2-16-Part_4.2.3.1.md | Silicones in Personal Care Products | Emolientes, siliconas y reología |
| v2-17-Part_4.2.3.2.md | Silicone Elastomer Applications | Emolientes, siliconas y reología |
| v2-18-Part_4.2.4.md | Skin Whitener Ingredients | Pigmentación, despigmentantes y acné |
| v2-19-Part_4.2.5.md | Marine Ingredients for Skin Care | Epidermis y función barrera |
| v2-20-Part_4.2.6.md | Topical Reduction of Cellulite | Hormonas, celulitis y percepción sensorial |
| v2-21-Part_4.3.1.md | Topical Retinoids | Dermis, colágeno y arrugas |
| v2-22-Part_4.3.2.md | Peptides for Anti-Aging Skin Care | Dermis, colágeno y arrugas |
| v2-23-Part_4.3.3.md | MicroRNAs in Skin Physiology | Envejecimiento cutáneo: senescencia y epigenética |
| v2-24-Part_4.3.4.md | Amino Acids | Hidratación: ácido hialurónico, aminoácidos y péptidos |
| v2-25-Part_4.3.5.md | AHAs and Beyond: Anti-Aging Ingredients | Dermis, colágeno y arrugas |
| v2-26-Part_4.3.6.md | Cytokines, Growth Factors, and Stem Cells | Dermis, colágeno y arrugas |
| v2-27-Part_4.3.7.md | Antioxidants in Cosmetics for Anti-Aging | Radiación UV, estrés oxidativo y antioxidantes |
| v2-28-Part_5.0.md | Fundamentals of Skin Anti-Aging Overview | Envejecimiento cutáneo: senescencia y epigenética |
| v2-29-Part_5.1.md | Theories of Aging: Skin Anti-Aging at the Tipping Point | Envejecimiento cutáneo: senescencia y epigenética |
| v2-30-Part_5.2.md | The Cellular Water Principle | Agua celular y nutrición |
| v2-31-Part_5.3.md | Anti-Senescence: Managing Cellular Functions | Radiación UV, estrés oxidativo y antioxidantes |
| v2-32-Part_5.4.md | Glycation, Proteasome Activation, and Telomere Maintenance | Glicación y ojeras |
| v2-33-Part_5.5.md | Sirtuins and Skin | Envejecimiento cutáneo: senescencia y epigenética |
| v2-34-Part_5.6.md | Epigenetics of Skin Aging | Envejecimiento cutáneo: senescencia y epigenética |
| v2-35-Part_5.7.md | Chronobiology of the Skin: Circadian Rhythm and Clock Genes | Envejecimiento cutáneo: senescencia y epigenética |
| v2-36-Part_5.8.md | Stress, Sleep and Epigenetic Orthodontics | Estrés, sueño y eje HPA |
