# Chapter 8: Particulate Leaching (Salt Leaching) Technique for Fabrication of Biomaterials

*Authors: Nurhasni Hasan, Aliyah Putranto, Sumarheni, Andi Arjuna*

## Core Idea
Particulate/salt leaching builds porosity by dispersing a sacrificial, water-soluble particle (porogen — typically NaCl) throughout a polymer matrix and then dissolving it out with water — the porogen's particle size and loading fraction directly set the resulting pore size and porosity, making this the most directly *tunable* of the conventional porogen-based techniques, at the cost of solvent residue risk and thin/limited-geometry parts.

## Frameworks Introduced
- **Porogen-loading-to-porosity-and-interconnectivity relationship**: salt content in the mixture is the primary dial controlling both overall porosity and pore interconnectivity.
  - When to use: as the first parameter to set when targeting a specific porosity/interconnectivity combination, before touching polymer chemistry or leaching time.
  - How: porosity output ranges 50–90%+ depending on salt loading; interconnectivity becomes high once salt content reaches ≥70% w/w — below that threshold, pores risk being isolated rather than open/connected, which defeats the purpose for cell infiltration.
- **Six salt-leaching process variants, keyed to what limitation you're solving**: conventional, melt-mixing + leaching, high-compression-molding + leaching, gas-foaming + leaching, salt-leaching electrospinning, salt-leaching-using-powder (SLUP).
  - When to use: conventional for the simplest solvent-cast baseline; melt-mixing for batch-mixer-scale processing; high-compression molding when you need strong mechanical properties and regular architecture (e.g., load-bearing bone scaffolds); gas-foaming-leaching when organic solvent must be eliminated entirely; salt-leaching-electrospinning when you need a nanofibrous ECM-mimicking mat with artificially enlarged pores; SLUP when you need to avoid both solvent and heat-treatment steps (e.g., for bioglass composites).
  - How: each variant swaps out one step of the base sequence (disperse porogen in polymer → fix/mold → remove porogen) — melt-mixing/high-compression replace solvent casting with thermal processing under pressure; gas-foaming replaces solvent evaporation with CO2 depressurization; electrospinning replaces solvent casting with fiber deposition around dispersed salt; SLUP skips solvent/heat entirely by mechanically stirring a bioglass-polymer-salt slurry.
- **Pore-size-by-function tiering**: distinct pore-size targets serve distinct biological functions within the same scaffold.
  - When to use: whenever a scaffold needs both structural cell-ingrowth pores and finer nutrient-transport porosity — consider a hierarchical (multi-scale) pore design rather than a single pore size.
  - How: 50–300 μm pores for cell penetration and neovascularization; 0.5–10 μm pores for nutrient/physical-stimuli transport; hierarchical scaffolds (e.g., 3–250 μm range in one part) combine both scales for better neo-tissue formation and uniform cell distribution.

## Key Concepts
- **Porogen** — the sacrificial particulate phase (salt) dispersed in the polymer to template pores; removed by leaching (dissolution in water) rather than sublimation (freeze-drying) or gas evolution (gas foaming).
- **NaCl as the preferred porogen** — chosen for high aqueous solubility (easy, complete leaching) and physiological safety (Na+/Cl- are already present in plasma, so trace residue is non-toxic); NaHCO3, NaOAc, and CaCl2 are used in some variants.
- **Solvent-casting particulate leaching (SCPL)** — the conventional variant name combining organic-solvent polymer casting with salt dispersion before leaching.
- **Combination of melt mixing and particulate leaching** — batch/measurement-mixer processing of polymer+salt, followed by compression molding, then leaching; avoids the slow solvent-evaporation step of conventional casting.
- **Gas foaming-salt leaching** — a three-step, fully solvent-free variant: melt-mix polymer+salt → foam with dense/supercritical CO2 → leach out salt; eliminates organic-solvent toxicity risk entirely.
- **Salt leaching electrospinning** — combines fiber deposition (for ECM-mimicking nanofibrous architecture) with co-dispersed salt particles released from a rotating cylinder, later leached to open up larger pores than electrospinning alone can achieve.
- **SLUP (Salt Leaching Using Powder)** — mixes a sieved powder (e.g., Bioglass 45S6) directly with polymer and salt, avoiding both solvent and heat-treatment steps; used for bioglass/chitosan hybrid scaffolds.

## Mental Models
- Treat salt content as a two-output dial, not one: raising NaCl loading simultaneously raises porosity *and* interconnectivity — but past a certain point, higher porosity trades away mechanical strength, so the "70%+ salt for good interconnectivity" rule has to be balanced against the specific tissue's load-bearing requirement.
- Think of the six process variants as each solving exactly one weakness of the conventional method (solvent toxicity → gas foaming; weak mechanical properties → high-compression molding; lack of nanofibrous architecture → electrospinning combination; need to skip both solvent and heat → SLUP) — pick the variant by naming your binding constraint first.
- Scaffold thinness (~3 mm typical) is a structural ceiling of the technique, not a tunable parameter — for thick or complex 3D geometries (e.g., full bone or ear models), salt leaching alone is the wrong tool; it's best reserved for thin-walled or laminated/combined constructs.

## Anti-patterns
- **Loading salt below ~70% w/w when open interconnected porosity is required**: lower salt content produces isolated (non-interconnected) pores that trap cells or block nutrient diffusion instead of supporting ingrowth.
- **Ignoring solvent residue toxicity in conventional/SCPL variants**: some solvents used to dissolve certain polymers (e.g., hexafluoroacetone and hexafluoroisopropanol for PGA) are highly cytotoxic — the chapter explicitly flags that many published scaffold studies skip toxicology evaluation, which is a validation gap, not a solved problem.
- **Assuming higher porosity is strictly better**: porosity beyond ~70-90% substantially weakens mechanical properties, making the scaffold unsuitable for load-bearing bone applications even though it may look ideal for nutrient/ECM distribution.
- **Using salt leaching for scaffolds thicker than ~3 mm or with complex 3D geometry**: the technique's diffusion-limited leaching and solvent-evaporation steps cap practical thickness — pair with a complementary technique (compression molding, electrospinning, gas foaming) or choose a different fabrication route entirely for thick/complex parts.

## Reference Tables

**Table 1 — Mechanical properties of polymers used in salt leaching (selected)**

| Polymer | Density (g/cm³) | Young's Modulus E (GPa) | Tensile Strength σ (MPa) | Elongation ε (%) |
|---|---|---|---|---|
| Poly(glycolic acid), PGA | 1.53 | >6.9 | >68.9 | 15–20 |
| Poly(L-lactic acid), PLLA | 1.210–1.430 | 2.4–4.2 | 55.2–82.7 | 5–10 |
| Poly(L-lactic-co-glycolic acid), PLGA | 1.3 | 1.4–2.08 | 41.4–55.2 | 3–10 |
| Polycaprolactone, PCL | 1.14 | 0.21–0.34 | 20.7–34.5 | 300–700 |
| Chitosan | — | 0.15–0.3 | 30 | — |
| Silk fibroin | 1.40 | 9.860 | 513 | 23.4 |
| PVA | 1.2–1.3 | 37–45 (67–110 at 98–99% hydrolyzed) | 225–445 | — |
| Nylon (non-biodegradable) | 1.15 | 2.7 | 82.7 | 10.0–86.0 |

**Table 2 — Process variant parameters and outcomes**

| Variant | Key conditions | Resulting porosity / pore size |
|---|---|---|
| Conventional (PCLA-F example) | NaCl 200–250 μm, methylene chloride solvent, leach 24 h at 100 rpm | Irregular, well-interconnected pores |
| High-compression molding-salt leaching | 640 MPa, 10–15 min press, mixed 50 rpm at 180 °C | Porosity 81.5–82.7%; compressive modulus ~4.64 ± 0.2 MPa (comparable to human cancellous bone, 2–10 MPa) |
| Gas foaming-salt leaching (Annabi et al., PCL/elastin) | CO2 at 65 bar, 70 °C melt, depressurization 15 bar/min, 1 h | Porosity 91%; average pore size 540 μm |
| Gas foaming-salt leaching (Bak et al., scCO2) | 50 °C, 8 MPa, CO2 dissolved 6 h, rapid depressurization | Average pore size 427.89 μm; bimodal pore structure |
| SLUP (bioglass 45S6 + chitosan) | Mechanical stirring only, no solvent/heat | Porosity 90%, well-interconnected |

**Table 3 — Advantages and disadvantages of particulate leaching**

| Advantages | Disadvantages |
|---|---|
| Relatively easy technique | Thin membranes only (up to ~3 mm) |
| Produces porous 3D structure | Limited useful lifespan of the mold/process |
| Low cost | Limited/constrained pore size range |
| High porosity achievable (50–90%) | Solvent residue toxicity risk |
| Tunable 3D cell growth via pore size | Time-consuming (solvent evaporation: days to weeks) |
| Works with a wide range of polymers | Particle entrapment can prevent fully open-cell structure |
| Controllable porosity and crystallinity | Irregular pore shapes; inter-pore opening size hard to control |

**Table 4 — Pore-size targets by function**

| Pore size range | Function |
|---|---|
| 50–300 μm | Cell penetration and neovascularization |
| 0.5–10 μm | Nutrient/physical-stimuli transport |
| 3–250 μm (hierarchical example) | Combined neo-tissue formation + uniform cell distribution |
| ≥70% salt loading | Recommended threshold for high pore interconnectivity |
| ≥70% porosity | Recommended for bone/cartilage regeneration to approximate physiological ECM distribution |

## Worked Example
High-compression molding-salt leaching of a PLLA/PLGA/hydroxyapatite composite scaffold (Zhang et al., as reported): dissolve the polymer blend in a suitable organic solvent and mix with sieved NaCl of the target particle size. Mechanically mix in an internal mixer at 50 rpm and 180 °C. Mold the mixture under high pressure — 640 MPa for 10–15 minutes — in a custom high-pressure press with a heated, thermocouple-controlled mold core. Cool to room temperature while maintaining the interconnected pore structure, then leach the salt out with water until the scaffold reaches constant weight (confirming complete salt removal). Result: porosity of 81.5–82.7% with a compressive modulus around 4.64 ± 0.2 MPa — closely matching human cancellous bone's 2–10 MPa range, making the scaffold mechanically appropriate for bone tissue engineering despite the process's typical thin-part limitation.

## Key Takeaways
1. Salt loading is the master dial: raising NaCl content increases both porosity and pore interconnectivity, with ≥70% w/w salt as the practical threshold for good interconnectivity — but porosity gains trade against mechanical strength.
2. NaCl dominates as the porogen of choice specifically because of high water solubility (complete, easy leaching) and physiological compatibility of any trace residue.
3. Six documented process variants each target one weakness of the conventional method — solvent toxicity (gas foaming), weak mechanics (high-compression molding), lack of nanofiber architecture (electrospinning combination), or the need to skip both solvent and heat (SLUP).
4. Scaffold thickness is capped around 3 mm by the diffusion-limited leaching process — this technique is not suited to thick or geometrically complex parts without combining it with another method.
5. Pore-size targeting should be function-specific: 50–300 μm for cell penetration/vascularization, 0.5–10 μm for nutrient transport; hierarchical (multi-scale) pore scaffolds combine both.
6. Toxicology evaluation is frequently missing from published salt-leaching scaffold studies despite known solvent-residue risk (e.g., hexafluoroacetone/hexafluoroisopropanol for PGA) — treat toxicity screening as a required step, not an optional add-on.
7. Salt leaching's application breadth spans bone engineering, neural retinal precursor cell scaffolds, and skin substitutes, with reported porosity in essentially every case falling in the 50–91% band.

## Connects To
- **Ch1 (Introduction)**: expands the porogen-based branch of Ch1's fabrication taxonomy (there illustrated as "casting/particle-leaching," 50–90% porosity) into full process-variant detail.
- **Ch2 (Biocomposites)**: directly continues the solvent-casting/particulate-leaching and melt-molding/particulate-leaching techniques introduced there (Mikos et al. baseline, 20–50% porosity / 30–300 μm pores) with six concrete modern variants and mechanical-property data.
- **Ch10 (Solvent Casting and Melt Molding)**: shares the compression-molding and melt-processing steps used in several of this chapter's leaching variants.
- **cheatsheet.md**: polymer mechanical-property table, pore-size-by-function tiers, and porosity/pressure numbers by variant are consolidated there.
- **patterns.md**: particulate/salt leaching (all six variants) is indexed alongside solvent casting, melt molding, and gas foaming as porogen-based techniques.
