# Fabrication Technique Patterns

Flat, scannable index of the book's named fabrication techniques. Use this to jump straight to "which technique do I need" without re-reading a full chapter.

## Freeze-Drying (Lyophilization)
**When to use**: need a porous scaffold with solvent-toxicity avoidance and tunable morphology via freezing control; directional variant for aligned/anisotropic channels (nerve, vascular guidance).
**How**: freeze below eutectic point (−40 to −80 °C aqueous) → sublimate solvent under vacuum (primary drying) → desorb residual solvent at higher temp/lower pressure (secondary drying). Conventional freezing = isotropic pores; directional freezing = aligned pores, spacing tunable via freeze rate (10–100 µm/s).
**Trade-offs**: energy-intensive, slow (hours to days); irregular pores if freezing uncontrolled. (Ch3)

## Spray-Freezing into Liquid (SFL)
**When to use**: need free-flowing microparticles (not a monolithic scaffold), especially to boost dissolution of poorly water-soluble drugs.
**How**: atomize feed solution into cryogenic liquid at high pressure (~5000 psi via HPLC pump) → freeze-dry resulting microdroplets.
**Trade-offs**: produces particles, not scaffolds; requires specialized atomization equipment. (Ch3)

## Camphene-Based Freeze-Casting
**When to use**: porous ceramic or metal scaffolds (not polymer).
**How**: mix camphene + ceramic/metal powder + dispersant → freeze/mold → sublime camphene at room temp → sinter green body at high temp (>1000 °C, e.g. 1450 °C for zirconia).
**Trade-offs**: requires sintering step; graded porosity achievable via layered slurry pours. (Ch3)

## Centrifugal Spinning (CS)
**When to use**: high-throughput nanofiber production without voltage/conductivity constraints; when electrospinning's low yield or safety concerns are the blocker.
**How**: rotating head (3,000–12,000 rpm) ejects polymer solution/melt through nozzles; centrifugal force stretches jets into fiber. Diameter tuned by rotational speed, head diameter, nozzle diameter.
**Trade-offs**: 25 nm–50 mm diameter range; up to 1 mL/min per nozzle; needs stable high-speed rotation hardware. (Ch4)

## Solution Blow Spinning (SBS)
**When to use**: same throughput/safety motivation as CS, wider raw-material selection, no conductivity requirement.
**How**: high-velocity compressed gas shears a polymer solution jet at the nozzle tip, drawing it into fiber at near-ambient temperature.
**Trade-offs**: 40 nm–several mm diameter; ~20 mL/min throughput; higher equipment requirement than melt blowing. (Ch4)

## Electrospinning (ES) — Blending / Coaxial / Emulsion / Melt
**When to use**: nanofibrous ECM-mimicking scaffold with drug-loading flexibility; choose variant by payload placement need (blending=simple, coaxial=core-shell, emulsion=solvent-incompatible payload, melt=solvent-free).
**How**: 10–50 kV field draws Taylor-cone jet from polymer solution/melt onto grounded collector; solution viscosity 1–200 poise optimal.
**Trade-offs**: low production rate/throughput; humidity-sensitive; struggles with pore-size uniformity. (Ch1, Ch5)

## Melt Blowing
**When to use**: nonwoven fibers >1 µm diameter at industrial scale.
**How**: melt polymer → extrude through multiple nozzles → attenuate with high-velocity heated airflow → collect as nonwoven web.
**Trade-offs**: coarser fibers than electrospinning/CS/SBS; limited material range. (Ch4)

## Bicomponent (Segmented-Pie) Fiber Spinning
**When to use**: microfibers finer than conventional melt spinning, or fibers with dual-polymer functionality.
**How**: two incompatible polymers co-spun at the spinneret orifice, then mechanically split (segmented-pie technique) into microfibers.
**Trade-offs**: requires rheological balance between the two polymers. (Ch4)

## Wet Spinning (Chitosan / Fiber Mesh)
**When to use**: fiber mesh scaffolds needing tunable mechanical strength from a natural polymer (chitosan) or blend (CHT/PCL).
**How**: dissolve polymer in solvent (e.g., acetic acid) → extrude into a coagulation bath (e.g., NaOH/Na2SO4) → wash/dehydrate in staged methanol → dry.
**Trade-offs**: process parameters (bath composition, drying) directly determine mechanical strength — unoptimized fiber meshes are weak. (Ch9)

## 3D Printing / Additive Manufacturing (7 ISO/ASTM 52900 categories)
**When to use**: patient-specific geometry, complex internal architecture, or embedded drug/cell payloads impossible with conventional molding.
**How**: binder jetting and powder bed fusion (powder feedstock); material extrusion (FDM, direct ink writing); material jetting; stereolithography (liquid resin); sheet lamination; directed energy deposition (metal).
**Trade-offs**: interlayer weakness (tearing/cracking between layers); porosity variation under identical build parameters remains a technical challenge. (Ch1, Ch2, Ch6)

## Bioprinting (Extrusion / Jetting / Laser-Assisted)
**When to use**: living cells must be positioned with spatial precision during fabrication rather than seeded afterward.
**How**: cell-laden bioink (alginate, GelMA, decellularized ECM) deposited via extrusion, inkjet/drop-on-demand, or nozzle-less laser-assisted transfer; cross-link post-deposition.
**Trade-offs**: bioink must stay cytocompatible (mild processing only); microvascularization remains an open challenge. (Ch6)

## Stereolithography (SLA)
**When to use**: high-resolution photopolymer resin parts — microneedles, dental prostheses, organ/organoid models.
**How**: print bed repeatedly lowered into and lifted from a UV/visible-curable resin bath, one cured layer per cycle.
**Trade-offs**: limited to photopolymerizable resins; resolution vs. build volume trade-off. (Ch1, Ch6)

## Multiphoton Lithography (MPL)
**When to use**: true 3D, nanoscale-resolved hydrogel/ECM-mimicking structures, including fabrication in the presence of living cells.
**How**: femtosecond pulsed laser delivers two low-energy photons simultaneously to a photoinitiator at the focal point; quadratic power dependence confines polymerization to a sub-micron voxel.
**Trade-offs**: cell-present work requires energy below ~1.5 nJ pulse energy (subcellular ablation) and well below 4 nJ (cell death); limited build thickness/volume. (Ch7)

## Particulate Leaching (Salt Leaching)
**When to use**: simple, cheap, tunable-porosity scaffold; baseline porogen technique.
**How**: disperse water-soluble porogen (NaCl typical) in polymer → cast/mold → evaporate solvent → leach porogen in water. ≥70% w/w salt loading for high interconnectivity.
**Trade-offs**: thin parts only (~3 mm); solvent residue toxicity risk; slow (days–weeks evaporation). (Ch1, Ch2, Ch8)

## Melt Mixing + Particulate Leaching
**When to use**: batch/industrial-scale salt leaching without solvent evaporation wait time.
**How**: polymer + salt processed in a batch mixer → compression molded (180 bar, 190–220 °C) → salt leached.
**Trade-offs**: still requires heat; leaching step unchanged. (Ch8)

## High-Compression Molding-Salt Leaching
**When to use**: strong, regular-architecture scaffolds (e.g., load-bearing bone).
**How**: mix polymer + salt → high-pressure mold (up to 640 MPa) → cool → leach salt.
**Trade-offs**: specialized high-pressure equipment required; porosity 81.5–82.7% achievable with cancellous-bone-comparable compressive modulus. (Ch8)

## Gas Foaming
**When to use**: solvent-free porosity generation.
**How**: saturate polymer with CO2 under pressure (e.g., 5.5 MPa ambient temp, or 65 bar/70 °C melt) → rapidly depressurize, causing gas to escape and form pores.
**Trade-offs**: risk of closed (non-interconnected) pore structure. (Ch1, Ch2, Ch8)

## Gas Foaming-Salt Leaching
**When to use**: fully solvent-free process combining foam porosity with leached macropores.
**How**: melt-mix polymer + salt → foam with dense/supercritical CO2 → leach salt.
**Trade-offs**: requires gas-foaming reactor equipment; porosity up to 91% achievable. (Ch8)

## Salt Leaching Electrospinning
**When to use**: nanofibrous ECM-mimicking mat with artificially enlarged pores (e.g., skin tissue engineering).
**How**: co-disperse salt particles with electrospun fiber deposition → leach salt post-fabrication.
**Trade-offs**: combines equipment/process complexity of both techniques. (Ch8)

## Salt Leaching Using Powder (SLUP)
**When to use**: avoiding both solvent and heat-treatment steps entirely (e.g., bioglass composites).
**How**: mix sieved powder + polymer + salt by mechanical stirring only → mold/dry → leach salt.
**Trade-offs**: limited to formulations compatible with pure mechanical mixing. (Ch8)

## Solvent Casting
**When to use**: simple, cheap thin-membrane scaffold fabrication.
**How**: dissolve polymer in organic solvent → cast into/onto mold → evaporate solvent.
**Trade-offs**: limited to thin (~3 mm) tubular/plate shapes; solvent toxicity; slow evaporation. (Ch1, Ch2, Ch10)

## Compression Molding
**When to use**: robust simple-geometry scaffolds at relatively low temperature (bioactive-factor-compatible).
**How**: heat polymer/porogen mix above Tg while applying pressure to release trapped air and compact particles.
**Trade-offs**: geometry limited compared to injection molding. (Ch10)

## Injection Molding
**When to use**: complex, dimensionally accurate, repeatable external geometries (orthopedic parts).
**How**: granulate polymer + porogen → inject molten mixture into mold cavity → solidify → leach porogen.
**Trade-offs**: requires injection-molding equipment; up to 94% porosity achievable with leaching. (Ch10)

## Extrusion (+ Particulate Leaching)
**When to use**: tubular/continuous-profile scaffolds (vascular, nerve, intestinal).
**How**: melt-compound polymer + porogen(s) → crush to granules → extrude through convergent die → leach porogen(s).
**Trade-offs**: low mechanical strength, thermal degradation risk from high processing temperature. (Ch10)

## Wire-Network Molding
**When to use**: precisely controlled, solvent-free interconnected pore channel architecture, including dual-scale porosity.
**How**: embed removable wire lattice in mold → pour/inject molten polymer (with or without porogen) → cool → remove wires (and leach any porogen).
**Trade-offs**: not limited to thermoplastics; setup complexity for wire lattice. (Ch10)

## Gas-Assisted (Foam) Injection Molding
**When to use**: pore generation without a separate leaching step.
**How**: blowing agent (chemical, e.g. azodicarbonamide; or physical, e.g. CO2/N2/water vapor) generates gas that forms pores during/after injection.
**Trade-offs**: chemical agents risk cytotoxic residue; physical agents give less controlled pore distribution. (Ch10)

## Microcellular Foam Injection Molding
**When to use**: fine, uniform porosity without any porogen or leaching step at all.
**How**: dissolve supercritical fluid into polymer as single-phase solution → pressure drop at injection nucleates numerous microscale gas cells.
**Trade-offs**: specialized SCF equipment required. (Ch10)

## Phase Separation (Compression/Injection Molding variant)
**When to use**: interconnected pores with cylindrical (cell-spreading-favorable) rather than angular geometry.
**How**: cryomill two immiscible polymers into homogeneous blend → heat to trigger segregation/coarsening → selectively leach one polymer phase.
**Trade-offs**: process parameter-sensitive (cryomilling duration, composition, molding temperature). (Ch2, Ch10)

## Thermally-Induced Phase Separation (TIPS)
**When to use**: bioactive-molecule integration during fabrication, thermoplastics only.
**How**: polymer solution phase-separated via temperature-triggered gelation, then solvent removed.
**Trade-offs**: works only for thermoplastics. (Ch1)

## Fiber Bonding
**When to use**: bonded nonwoven fiber membrane from two polymers.
**How**: align PGA fibers → coat with dissolvable PLLA solution → heat above both polymers' melting points → dissolve away PLLA.
**Trade-offs**: narrow polymer-pair applicability. (Ch2)

## Self-Assembly (Peptide Amphiphiles, Surfactant-Like Peptides, Multi-Domain Peptides)
**When to use**: replicating complex organ microarchitecture (liver, kidney) that conventional scaffolds can't reproduce; injectable hydrogels; drug-carrier-free therapeutics (drug amphiphiles).
**How**: design building blocks (peptides, lipids, dendrimers) whose non-covalent interactions (electrostatic, hydrophobic, aromatic stacking, hydrogen bonding) drive spontaneous folding into target nanostructure (micelle, vesicle, nanofiber, nanotube).
**Trade-offs**: less engineering control over final macro-geometry than top-down scaffolding; still an emerging field for complex 3D constructs. (Ch9)

## Supramolecular Self-Assembly of Carbon-Based Nanostructures (CNTs, Graphene)
**When to use**: drug delivery via aromatic stacking, radioisotope transport, or medical imaging carriers.
**How**: surfactant-assisted self-assembly of graphene sheets into CNT microspheres, or graphene oxide nanocarrier synthesis.
**Trade-offs**: requires careful surface functionalization for biocompatibility/targeting. (Ch9)
