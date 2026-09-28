# Chapter 5: Electrospun Nanofiber Scaffolds — Fabrication, Characterization and Biomedical Applications

*Authors: Murtada A. Oshi, Abdul Muhaymin, Ammara Safdar, Meshal Gul, Kainat Tufail, Fazli Khuda, Sultan Ullah, Fakhar-ud-Din, Fazli Subhan, Muhammad Naeem*

## Core Idea
Electrospinning turns a charged polymer solution jet (drawn from a Taylor cone under a 10–50 kV field) into continuous nanofibers whose diameter and morphology are jointly set by solution properties (viscosity, conductivity, solvent volatility) and process settings (voltage, flow rate, tip-to-collector distance) — and the choice of which of four electrospinning variants (blending, coaxial, emulsion, melt) to use is really a choice about how you want a drug or bioactive payload positioned inside the fiber.

## Frameworks Introduced
- **Four electrospun-nanofiber (ESNF) fabrication variants, keyed to payload placement**: blending / coaxial / emulsion / melt electrospinning.
  - When to use: blending when a single common solvent works for both drug and polymer and burst release is acceptable; coaxial when you need a core-shell architecture to protect a payload or sequence release of two drugs; emulsion when drug and polymer need different (incompatible) solvents; melt when the polymer tends to clog a needle in solution form or a solvent-free process is required.
  - How: blending = dissolve drug directly in the polymer solution before spinning; coaxial = feed core-forming and shell-forming polymer solutions through concentric capillaries so a stable Taylor cone yields a core/shell fiber; emulsion = disperse an aqueous drug phase as droplets within the polymer's oil phase, spin the emulsion directly (no shared solvent needed); melt = melt the polymer first, spin without solvent (yields thicker fibers).
  - This is a distinct decision layer from the four *drug-loading mechanisms* below — fabrication variant sets the fiber's physical architecture; loading mechanism sets how the drug integrates into it.
- **Solution-parameter vs. processing-parameter split for troubleshooting fiber defects**: bead formation and diameter inconsistency trace back to either the solution (solvent choice, viscosity, conductivity) or the process settings (voltage, flow rate, tip-collector distance) — diagnose which bucket before adjusting.
  - When to use: whenever ESNFs come out beaded, inconsistent, or the wrong diameter.
  - How: check solvent volatility first (too volatile → needle clogs; too low → beaded fibers from incomplete evaporation), then viscosity (too low → beads from lost intermolecular attraction; too high → oversized fiber diameter; workable range ~1–200 poise), then conductivity (below threshold → Taylor cone can't form); only after ruling out solution issues, tune voltage/flow rate/distance.
- **Four drug-loading mechanisms into ESNFs**: blending, core/sheath, encapsulation, attachment (surface modification).
  - When to use: blending for simplicity when burst release is tolerable; core/sheath when you need to suppress initial burst release and/or load more than one drug; encapsulation when drug and polymer need separate solvents (like emulsion electrospinning but framed as a loading strategy); attachment when the payload is a fragile biomolecule (genes, growth factors) that would degrade if blended into the spinning solution itself.

## Key Concepts
- **Taylor cone** — the conical droplet shape a polymer solution forms at a needle tip once electrostatic force overcomes surface tension; the origin point of the drawn fiber jet.
- **Coaxial electrospinning** — dual-capillary spinneret producing a core-shell fiber; shell composition controls release kinetics, core can hold a protected payload.
- **Burst release** — the common failure mode of simple blended ESNFs, where most of the loaded drug releases immediately rather than sustained over time; motivates core/sheath and attachment loading strategies.
- **Berry-number-independent viscosity window** — optimal electrospinning viscosity is reported at 1–200 poise; outside this range fibers either bead (too low) or thicken excessively (too high).
- **BET (Brunauer-Emmett-Teller) analysis** — the standard technique for quantifying ESNF specific surface area, used to correlate fiber diameter with adsorption capacity.
- **PCL (polycaprolactone)** — a biodegradable polyester workhorse material for ESNFs; glass-transition temperature −60 °C, melting point 60 °C.
- **Pore formation via rapid solvent evaporation** — porous (not just solid) ESNF surfaces can form when a highly volatile solvent (e.g., dichloromethane) evaporates rapidly from the fiber surface during flight, independent of any drug-loading step.

## Mental Models
- Treat solvent choice as a Goldilocks constraint, not a free variable: too volatile clogs the needle before fiber forms; too non-volatile produces beaded fiber because the jet doesn't dry in time — the workable middle band is small and material-specific.
- Fiber diameter and tip-to-collector distance mostly move together (larger distance → smaller diameter, more evaporation/stretching time) but this relationship is reported as *not universal* — some studies found no distance effect, so treat distance as a secondary lever to validate empirically rather than an assumed law.
- Choose loading mechanism by asking what the drug is most vulnerable to: burst-release-prone drugs want core/sheath; solvent-incompatible drug/polymer pairs want emulsion/encapsulation; fragile biomolecules (DNA, growth factors) want attachment (added after fiber formation, not exposed to spinning-solvent chemistry).

## Anti-patterns
- **Blending a fragile biomolecule (gene, growth factor) directly into the spinning solution**: exposure to solvent and electric field during spinning risks degrading it — use the attachment (post-fabrication surface) method instead.
- **Assuming a single "electrospinning" recipe transfers across polymers**: critical voltage, optimal viscosity range, and solvent choice are all polymer-specific; a parameter set validated for PAN won't necessarily transfer to PCL or PLGA.
- **Ignoring the compatibility problem in encapsulation-method loading**: eliminating the need for a shared solvent (encapsulation's main benefit) doesn't eliminate the separate problem of drug-polymer compatibility, which still needs its own validation.
- **Chasing thinner fiber via distance alone**: since some studies report no diameter effect from tip-to-collector distance, treat it as one lever among several (voltage, flow rate, solution viscosity) rather than the primary one.

## Reference Tables

**Table 1 — Solution and processing parameters affecting ESNF morphology**

| Parameter | Effect if too low | Effect if too high |
|---|---|---|
| Solvent volatility | Beaded fiber (slow drying) | Needle clogs (dries at tip) |
| Solution viscosity | Beads (lost intermolecular attraction) | Larger fiber diameter |
| Solution conductivity | Taylor cone can't form | Excess surface charge accumulation |
| Applied voltage | Below critical value: no fiber ejection | Larger-diameter fiber |
| Flow rate | — | Beyond critical value: beaded fiber |
| Tip-to-collector distance | Larger fiber diameter (shorter flight/less evaporation, most studies) | Smaller fiber diameter (some studies report no effect) |

**Table 2 — Reported optimal/typical process values**

| Parameter | Reported value/range |
|---|---|
| Applied voltage | ~10–50 kV |
| Solution viscosity (workable window) | ~1–200 poise |
| PCL glass-transition temperature | −60 °C |
| PCL melting point | 60 °C |
| Fiber diameter measurable by TEM | < 300 nm |
| BET surface-area increase example | specific surface area rose as fiber diameter increased 150 nm → 1.3 µm |

**Table 3 — ESNF biomaterial classes and representative polymers**

| Class | Examples | Notes |
|---|---|---|
| Natural polysaccharides | Cellulose, alginate derivatives, chitosan | Most common natural-polymer family for ESNFs |
| Natural proteins | Collagen, elastin, silk | Second most-used natural-polymer family |
| Bio-based synthetic polyester | PHB (polyhydroxybutyrate) | Biocompatible, biodegradable; usually blended with other polymers |
| Synthetic (FDA-approved for biomedical use) | PEO, PVA, PCL and co-polymers, PVP, PLA | Predominant materials for ESNF manufacture |

## Worked Example
Ibuprofen-loaded ESNFs via blending electrospinning (Yu et al., as reported): prepare a spinning solution of 40 wt% PVP K30 and 7.5 wt% ibuprofen in ethanol. Electrospin under standard Taylor-cone conditions to yield a uniform nanofiber mat. Characterize with XRD and DSC — both confirm the drug is dispersed in an amorphous (not crystalline) state within the fiber, which typically improves dissolution behavior versus crystalline drug. FTIR confirms strong hydrogen bonding between ibuprofen and the PVP backbone, indicating good drug-polymer compatibility — the mechanistic reason the blend forms a stable, uniform composite fiber rather than phase-separating. This blending-electrospinning + spectroscopic-confirmation pattern (spin → XRD/DSC for physical state → FTIR for interaction chemistry) is reused throughout the chapter's drug-delivery case studies.

## Key Takeaways
1. ESNF morphology is a joint function of solution parameters (solvent, viscosity 1–200 poise, conductivity) and processing parameters (voltage 10–50 kV, flow rate, tip-collector distance) — diagnose defects by checking solution parameters first.
2. Four fabrication variants (blending, coaxial, emulsion, melt) address different constraints: common-solvent simplicity, core-shell protection, solvent-incompatible payloads, and solvent-free processing respectively.
3. Four drug-loading mechanisms (blending, core/sheath, encapsulation, attachment) trade off burst-release control, solvent-compatibility flexibility, and payload fragility protection — pick based on what the drug is most vulnerable to.
4. SEM is the primary morphology tool; TEM resolves fiber diameters below 300 nm; BET quantifies surface area (which scales with fiber diameter); FTIR/XRD/DSC characterize chemical state and drug-polymer interaction.
5. ESNFs' biomedical application breadth (drug delivery, tissue engineering, wound healing, cancer therapy, dentistry, filtration/dialysis, biosensing) all stem from the same core properties: high surface-to-volume ratio, tunable porosity, and ease of functionalization.
6. Core/sheath and coaxial architectures are the go-to answer whenever burst release, multi-drug loading, or payload protection matter more than fabrication simplicity.

## Connects To
- **Ch1 (Introduction)**: electrospinning was flagged there as a conventional technique with a persistent pore-uniformity weakness; this chapter shows the parameter space used to manage that weakness.
- **Ch4 (Centrifugal and Solution Blow Spinning)**: the voltage-free alternatives to electrospinning positioned against the throughput/safety/conductivity limitations detailed here.
- **cheatsheet.md**: the solution-viscosity window, voltage range, and PCL thermal-transition numbers are consolidated there.
- **patterns.md**: electrospinning (all four variants) is indexed alongside centrifugal spinning, solution blow spinning, and melt blowing as nanofiber-generation techniques.
