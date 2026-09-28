# Chapter 6: 3D Printed Biomaterials and their Scaffolds for Biomedical Engineering

*Authors: Rabail Zehra Raza, Arun Kumar Jaiswal, Muhammad Faheem, Sandeep Tiwari, Raees Khan, Siomar de Castro Soares, Asmat Ullah Khan, Vasco Azevedo, Syed Babar Jamal*

## Core Idea
3D printing/additive manufacturing (AM) replaces conventional formative (molding) and subtractive (machining) scaffold fabrication with direct, computer-aided layer-by-layer deposition — which is what makes patient-specific geometry, embedded drug payloads, and even living-cell bioprinting achievable in ways conventional techniques structurally cannot support.

## Frameworks Introduced
- **Three-level scaffold architecture (macro / micro / nano)**: the design hierarchy any 3D-printed scaffold must satisfy simultaneously.
  - When to use: as the design checklist before printing — a scaffold can fail even with perfect print resolution if only one architectural level was considered.
  - How: macroarchitecture = overall patient/organ-specific shape (from CAD/imaging data); microarchitecture = pore size, porosity, shape, spatial distribution, interconnectivity (governs cell-matrix interaction and nutrient transfer); nanoarchitecture = surface-level biomolecule attachment for cell adhesion/proliferation/differentiation.
- **Seven ISO/ASTM 52900 AM process categories**: powder-based (binder jetting, powder bed fusion), material deposition (material extrusion, directed energy deposition), material jetting, liquid reservoir (stereolithography), and sheet lamination — plus bioprinting as a cross-cutting cell-delivery method layered on top of these.
  - When to use: pick the category by what state your feedstock is in and what resolution/mechanical-property trade-off you need, not by habit.
  - How: powder bed fusion/binder jetting for ceramics/metals needing later sintering or infiltration; material extrusion (FDM, direct ink writing) for thermoplastic or hydrogel/paste scaffolds including cell-laden pastes; stereolithography for highest-resolution photopolymer resin parts; sheet lamination for cut-and-laminated sheet stacks; bioprinting (extrusion, jetting, or laser-assisted) whenever living cells must be positioned during fabrication rather than seeded afterward.
- **Bioink vs. biomaterial ink distinction**: bioinks carry living cells and must stay viable through printing (mild, cell-compatible conditions); biomaterial inks (ceramics, thermoplastics, metals, composites) are structural/scaffold materials processed under conditions cells could not survive (heat, solvent, UV).
  - When to use: decide this before selecting a print process — a bioink constrains you to gentle extrusion/jetting/laser-assisted methods; a biomaterial ink opens up higher-temperature or photopolymerization routes.
  - How: bioinks are typically natural hydrogels (alginate, gelatin/GelMA, collagen, fibrin, decellularized ECM) chosen for cross-linking chemistry and cytocompatibility; biomaterial inks are chosen for post-print mechanical/osteoconductive properties (ceramics, PCL/PLA/PVA thermoplastics, metal alloys) with cells (if any) seeded after printing.

## Key Concepts
- **Additive manufacturing (AM)** — layer-by-layer, CAD-driven material deposition; the umbrella term for all 3D printing categories in this chapter.
- **Bioprinting** — not itself a distinct AM process, but the use of any AM technique (extrusion, jetting, laser-assisted/nozzle-less) to deposit living cells suspended in bioink with spatial control.
- **Stereolithography (SLA)** — liquid-reservoir photopolymerization; the print bed is repeatedly lowered into and lifted from a UV/visible-light-curable resin bath, curing one layer per cycle; the highest-resolution AM technique cited in the chapter.
- **Fused deposition modeling (FDM)** — the most common material-extrusion technique; thermoplastic filament is softened and deposited layer by layer; dominant for low-cost scaffold and drug-tablet printing.
- **Selective laser melting/sintering (SLM/SLS)** — powder bed fusion using a laser (CO2 for polymers/ceramics, or high-power laser for metals) to fuse successive powder layers; used for metal implant lattices and porous architectures addressing stress-shielding.
- **GelMA (gelatin methacrylate)** — a UV-cross-linkable modified gelatin bioink that solves natural gelatin's slow, unreliable thermoreversible gelation, giving better shape fidelity for bioprinted constructs.
- **Alginate bioink** — the most common bioprinting hydrogel; a brown-algae-derived polysaccharide that cross-links with divalent cations (e.g., calcium) and can be functionalized (e.g., RGD peptide) to promote cell binding.
- **Decellularized ECM bioink** — tissue stripped of cells but retaining native biochemical signals; mechanically soft on its own, so typically blended with synthetic/natural reinforcement materials before printing.
- **Top-down vs. bottom-up nanofabrication** — top-down deconstructs bulk material into nanostructures (costly, low reproducibility); bottom-up self-assembles building blocks into nanostructures (better atomic-level control); nanofabrication sits adjacent to, but is not itself, a standard AM category.

## Mental Models
- Treat print-process selection as answering two questions in sequence: (1) does this need living cells during fabrication (bioink, gentle process) or can cells be seeded after (biomaterial ink, any process)? (2) what feedstock state do I have — powder, liquid resin, filament, or sheet — since that alone eliminates most of the seven ISO categories.
- Porosity is a double lever in 3D-printed implants specifically: it controls both mechanical load-bearing capacity (via stress-shielding behavior in metal implants) and biological integration (vessel/tissue ingrowth) — the same trade-off seen in porogen-based techniques (Ch1/Ch2) but now tunable with CAD precision rather than emergent from process chemistry.
- Bioprinted 3D/organoid models consistently outperform 2D cultures for drug-response fidelity (e.g., the mTOR-inhibitor signaling example) — when the downstream use case is drug screening or disease modeling, defaulting to a 2D culture is the anti-pattern, not the safe choice.

## Anti-patterns
- **Treating ceramics as printable without a binder/reinforcement strategy**: ceramics' inherent fragility means they're always mixed with a polymeric binder (powder printing) or combined with a polymer melt (extrusion) — printing pure ceramic ignores this constraint.
- **Relying on gelatin's native thermoreversible gelation for shape-fidelity-critical bioprinting**: unmodified gelatin's gelation rate is too slow and unreliable; use GelMA (UV cross-linkable) instead when shape fidelity matters.
- **Assuming stem-cell self-assembly gives structural control over organoid geometry**: self-assembly limits control over final structure, composition, and size — controlled spatial deposition via bioprinting is required when precise organoid architecture is the goal.
- **Ignoring interlayer continuity in AM parts**: printed layers can tear or crack between successive layers more easily than traditionally manufactured parts — treat this as an inherent AM weakness to design/process around, not an occasional defect.
- **Using AM for large-batch simple parts where conventional manufacturing is cheaper**: AM's advantage is complex, patient-specific, or otherwise-impossible geometry — for high-volume simple tablets/parts, conventional (molding) methods remain more efficient.

## Reference Tables

**Table 1 — 3D printing / AM process categories and biomedical use**

| Category | Mechanism | Typical materials | Biomedical use |
|---|---|---|---|
| Binder jetting | Liquid binder droplets bond powder-bed particles layer by layer | Any powder (often ceramics) | Bone scaffolds (post-processed via sintering/infiltration — as-printed parts are mechanically weak) |
| Powder bed fusion (SLS/SLM) | Laser melts/sinters powder layers | Thermoplastics, ceramics, metals | Metal implant lattices, porous orthopedic structures |
| Material extrusion (FDM, direct ink writing) | Thermoplastic or paste/hydrogel extruded through nozzle | PCL, PLA, PVA, hydrogels, cell-laden pastes | Scaffolds, tablets, drug-releasing implants |
| Material jetting | Inkjet-style deposition of photopolymer resin, UV-cured per layer | Photocurable resins | High-resolution structural parts |
| Stereolithography (SLA) | Print bed lowered into/out of photopolymer resin bath, light-cured | UV/visible-curable resins | Microneedles, organ/organoid models, dental prostheses |
| Sheet lamination | Sheets cut (knife/laser) per CAD cross-section, then bonded | Plastic, paper, metal sheets | Structural/anatomical models |
| Directed energy deposition | Laser/electron-beam/plasma melts fed powder or wire | Metal powder/wire | Metal implant repair/build-up |
| Melt electrospinning writing (MEW) | Fiber-based deposition combining electrospinning with AM control | Melt polymers | Fiber scaffolds for TE |

**Table 2 — Bioink vs. biomaterial ink materials**

| Type | Examples | Key property |
|---|---|---|
| Natural hydrogel bioinks | Alginate, gelatin/GelMA, collagen, fibrin, agarose, gellan gum | Cytocompatible; alginate cross-links with divalent cations; GelMA UV cross-links for shape fidelity |
| Decellularized ECM bioink | Processed native tissue (e.g., decellularized dentin) | Retains biochemical signals but mechanically soft; needs reinforcement |
| Synthetic hydrogel inks | Pluronic | Sacrificial ink for hollow structures / support material for overhangs |
| Elastomer inks | PDMS, silicone (via FRE/microgel embedding) | Mimics tissue viscoelasticity; used for branched hollow vessel/airway mimics |
| Thermoplastic/resin biomaterial inks | PCL, PLA, PVA, PORO-LAY (PVA-polyurethane blend) | Mechanical reinforcement, direct implantation, extrusion-printed |
| Ceramic biomaterial inks | Hydroxyapatite (HAp), tricalcium phosphate (TCP), bioglass, biphasic calcium phosphate (BCP), tetracalcium phosphate (TTCP) | Osteoconductive; mixed with polymer binder to offset fragility |
| Metal biomaterial inks | Stainless steel, Co-Cr-Mo, titanium alloys | Orthopedic/dental/craniofacial implants; SLM enables porous lattices |

## Worked Example
Vascularized bioink formulation and print for a bone-like construct (as reported): start with alginate as the base hydrogel and incorporate hydroxyapatite (HAp) to promote a calcified cartilage matrix — this addition measurably decreased chondrocyte glucosaminoglycan secretion while increasing Col II and calcified-cartilage markers (alizarin red, Col-X, alkaline phosphatase), evidence the ink is actively directing differentiation, not just providing scaffolding. Add sodium citrate to achieve a more homogeneous HAp distribution, which also improves extrudability by preventing needle clogging during printing. In a related GelMA-based approach, combine GelMA with vascular endothelial growth factor and print with material extrusion to create spatially organized vascular channels within the bone-like construct — demonstrating that bioink formulation (base polymer + mineral additive + growth factor) and print parameters (nozzle clog prevention) must be co-optimized, not treated as independent steps.

## Key Takeaways
1. Scaffold design must satisfy macro (patient-specific shape), micro (pore architecture), and nano (surface biomolecule) levels simultaneously — a print that nails macro-geometry can still fail biologically at the micro/nano level.
2. Seven ISO/ASTM 52900 AM categories cover all 3D printing; select by feedstock state (powder/liquid resin/filament/sheet) and by whether cells must be present during printing (bioink) or added after (biomaterial ink).
3. Alginate and GelMA are the two workhorse bioinks — alginate for ionic (divalent-cation) cross-linking and RGD functionalization, GelMA for UV cross-linking and better shape fidelity than native gelatin.
4. Ceramics and metals always need a processing strategy to offset fragility (binder for powder printing, polymer blend for extrusion) or achieve porosity control (SLM for metal lattices addressing stress-shielding).
5. 3D-printed drug delivery spans tablets (FDM, patient-specific dosing/release kinetics), transdermal microneedles (SLA), and drug-releasing implants (antibiotic-infused PLA outperforming surface-coated alternatives).
6. Interlayer weakness (tearing/cracking between printed layers) and porosity variation under identical build parameters remain open technical challenges across the whole AM category, not failures specific to one technique.
7. Bioprinted 3D/organoid models better replicate in vivo drug-response signaling than 2D cultures, making them the preferred platform for drug screening and disease modeling despite added fabrication complexity.

## Connects To
- **Ch1 (Introduction)**: expands the "rapid prototyping/solid free-form fabrication" branch of Ch1's fabrication taxonomy into a full technique inventory.
- **Ch2 (Biocomposites)**: extends the FDM/SFF discussion there (honeycomb PCL scaffold example) with the full seven-category AM framework and bioink/biomaterial-ink distinction.
- **Ch7 (Multiphoton Lithography)**: a higher-resolution photopolymerization technique complementary to this chapter's stereolithography coverage.
- **cheatsheet.md**: the seven AM process categories and bioink/biomaterial-ink material lists are consolidated there for quick technique selection.
- **patterns.md**: FDM, SLA, SLS/SLM, binder jetting, material jetting, sheet lamination, and bioprinting are indexed individually as fabrication techniques.
