# Chapter 7: Fabrication of Photosensitive Polymers-based Biomaterials through Multiphoton Lithography

*Authors: Mohammad Sherjeel Javed Khan, Sehrish Manan, Ronan R. McCarthy, Muhammad Wajid Ullah*

## Core Idea
Multiphoton lithography (MPL) uses simultaneous absorption of two low-energy (typically infrared) photons — rather than one high-energy photon as in conventional photolithography — to confine photopolymerization to a sub-micron focal volume in 3D space, which is what makes it possible to fabricate ECM-mimicking hydrogel scaffolds with true 3D, nanoscale-resolved structure directly in the presence of living cells, not just on a 2D patterned surface.

## Frameworks Introduced
- **Single-photon vs. multiphoton excitation as a resolution/depth trade-off**: conventional (single-photon, UV) photopolymerization is limited to planar/layered patterns because it can't confine excitation to a true 3D focal point; multiphoton excitation's quadratic dependence on laser power confines the polymerization reaction to the focal volume only, enabling true sub-micron 3D structures and deeper penetration using less-scattered IR/near-IR light.
  - When to use: reach for MPL specifically when the target structure needs micro/nanoscale 3D resolution (e.g., replicating ECM's time-varying nanoscale architecture) that layer-by-layer photolithography or stereolithography cannot achieve; use single-photon/conventional photopolymerization when planar coatings, casts, or simpler layered 3D builds suffice.
  - How: a femtosecond pulsed laser (e.g., Ti:sapphire) delivers two photons within femtoseconds to a photoinitiator at the focal point; initiation rate scales quadratically (not linearly) with average laser power, which is the physical reason excitation stays confined near the focal plane instead of throughout the beam path.
- **Photoinitiator Type-I vs. Type-II selection framework**: choose photoinitiator chemistry based on whether self-cleavage (Type-I) or a co-initiator/hydrogen-donor reaction (Type-II) fits your wavelength and cytocompatibility constraints.
  - When to use: Type-I when you need UV-range (<400 nm) initiation and simplicity (self-cleaving, no co-initiator needed); Type-II when you need visible-light range (<600 nm, gentler on cells) and can supply a hydrogen-donor co-initiator (amine/thiol-containing molecule).
  - How: Type-I (e.g., Irgacure 2959, LAP) dissociates directly into free radicals on photon absorption; Type-II (e.g., rose bengal, camphorquinone) excites to a triplet state that then reacts with a co-initiator to generate radicals — pick water-soluble variants (e.g., LAP at ~8.5 wt% solubility vs. Irgacure 2959's ~1 wt%) when working in aqueous/cell-culture conditions.
- **Additive vs. subtractive photochemical biomaterial modulation**: two complementary strategies for spatiotemporally patterning biochemical cues into an already-formed scaffold.
  - When to use: additive (radical chain polymerization of acrylic-functionalized peptides like RGD or VEGF; thiol-ene patterning) when you need to introduce cell-signaling motifs into specific 3D regions; subtractive (photolabile linker cleavage, e.g., o-nitrobenzyl ester) when you need to selectively remove a cue to trigger a defined cellular response (e.g., releasing RGD to promote cartilage formation).
  - How: combine both (e.g., visible-light thiol-ene addition + UV-mediated o-nitrobenzyl cleavage) to achieve fully reversible biochemical patterning — load a ligand, observe cell response, then remove it dynamically.

## Key Concepts
- **Multiphoton excitation** — simultaneous absorption of two (or more) lower-energy photons by a molecule, first theorized by Maria Goeppert-Mayer (Nobel Prize in Physics, 1963); the physical basis of MPL's spatial confinement advantage over single-photon methods.
- **Photoinitiator (PI)** — the organic compound that converts absorbed light into reactive free radicals to start polymerization; classified as Type-I (self-cleaving) or Type-II (co-initiator-dependent).
- **Voxel resolution** — the smallest addressable 3D volume element MPL can polymerize; can approach ~1 μm³ (sub-femtoliter), enabling access to intracellular length scales.
- **Photocage** — a molecular "gatekeeper" group that physically blocks a reaction until cleaved by light, at which point it releases a reactive functional group to trigger conjugation (e.g., strain-promoted azide-alkyne cycloaddition, oxime ligation, Michael addition).
- **Photolabile linker** (e.g., o-nitrobenzyl ester, coumarin, disulfide) — a bond that cleaves under light exposure at physiologically relevant conditions, used for controlled depolymerization or triggered release of a biomolecule cue.
- **Automatic slowdown (autodeceleration)** — the phenomenon where propagation rate constant (kp) and termination rate constant (kt) both drop as the macromonomer converts and the network crosslinks, because diffusion of reactive species becomes increasingly restricted; polymerization halts once available functional groups are consumed.
- **Cytocompatible wavelength window** — light of ≥365 nm is generally safe for living cells and sufficient to drive polymerization, whereas ~254 nm rapidly damages cellular DNA and denatures protein — the practical wavelength floor for any cell-present MPL process.

## Mental Models
- Treat MPL as "photolithography with a built-in 3D address system": the quadratic (not linear) dependence of initiation rate on laser power is the entire reason MPL can pattern a true 3D point cloud instead of stacking 2D layers — this is the single fact that explains most of MPL's advantages and constraints.
- Photoinitiator choice is a three-way constraint satisfaction problem, not a single "best" choice: wavelength range (UV vs. visible), water solubility (needed for aqueous/cell environments), and cytocompatibility (must not damage cells or DNA at the exposure energy used) all have to be satisfied together.
- Energy dosing in cell-present MPL is a narrow safety window, not a simple "more power = better resolution" dial: pulse energies above ~1.5 nJ risk subcellular optical ablation, and above ~4 nJ risk cell death — resolution gains beyond the safe window come at the cost of viability, so treat energy as bounded above by biology, not just by optics.

## Anti-patterns
- **Using single-photon (conventional UV) photopolymerization when true 3D nanoscale ECM-mimicking structure is required**: single-photon methods are inherently limited to planar patterns stacked into layers — they cannot achieve MPL's true 3D spatial confinement, so attempting to replicate ECM's time-varying nanoscale architecture this way will fail on resolution grounds alone.
- **Selecting a photoinitiator by wavelength/reactivity alone, ignoring water solubility**: a highly reactive but poorly water-soluble PI (like the parent Irgacure 2959 compound at ~1 wt% solubility) will underperform in an aqueous cell-culture environment regardless of its polymerization efficiency in organic solvent.
- **Pushing laser pulse energy up to improve resolution during cell-encapsulating fabrication**: past ~1.5 nJ (subcellular ablation risk) and definitely past ~4 nJ (cell death), higher energy actively destroys the biology you're trying to scaffold — resolution and viability must be co-optimized, not resolution alone.
- **Treating all natural/synthetic hydrogel backbone polymers as interchangeable**: PEG is favored specifically for its nonstick, elasticity-mimicking properties; natural polymers (alginate, collagen, gelatin, hyaluronic acid, fibrin, chitosan) each bring different native bioactivity — backbone choice should match the target tissue's signaling needs, not just processability.

## Reference Tables

**Table 1 — Photoinitiator types for MPL in the presence of viable cells**

| Photoinitiator | Type | Active wavelength | Water solubility | Notes |
|---|---|---|---|---|
| Irgacure 2959 | Type-I | ~365 nm (UV) | ~1 wt% (~50 mM) | Most commonly used; low water solubility limits aqueous use |
| LAP (lithium phenyl-2,4,6-trimethylbenzoylphosphinate) | Type-I | 300–400 nm | ~8.5 wt% (~300 mM) | Much higher water solubility than Irgacure 2959; two-step, near-quantitative synthesis |
| Rose bengal | Type-II | Visible | — | Requires hydrogen-donor co-initiator (amine/thiol) |
| Camphorquinone | Type-II | Visible | — | Requires hydrogen-donor co-initiator; less well-characterized photodynamics than Type-I |

**Table 2 — Energy/damage thresholds for cell-present MPL (as reported)**

| Threshold | Effect |
|---|---|
| PEG-hydrogel synthesis energy > 2.3 nJ | Cavitation of highly water-swollen gels |
| Pulse energy > 1.5 nJ | Subcellular optical ablation risk |
| Pulse energy > 4 nJ | Cell death |
| Safe operating zone | < 1.5 nJ pulse energy avoids indeterminate subcellular scaffold damage while maintaining cell viability |
| Cytocompatible light wavelength | ≥ 365 nm (254 nm rapidly damages DNA/denatures protein) |

**Table 3 — Backbone polymer classes used in MPL-fabricated hydrogels**

| Class | Examples | Notes |
|---|---|---|
| Synthetic hydrophilic | PEG, PVA, PAA, polycaprolactone, PHEMA | PEG most widely used — nonstick, mimics natural tissue elasticity/transport |
| Natural hydrophilic | Alginate, collagen, gelatin, hyaluronic acid, fibrin, chitosan, bacterial cellulose | Bring native bioactivity/signaling; often need added polymerizable groups (meth)acrylate, (meth)acrylamide, thiolene) |

## Worked Example
Reversible biochemical patterning of a cell-laden hydrogel (as reported): first load the hydrogel scaffold, in the presence of viable cells, with a binder ligand via a visible-light-promoted thiol-ene addition reaction — this covalently attaches a cell-adhesion or signaling motif (e.g., an RGD-functionalized peptide) at specific 3D coordinates defined by the MPL focal point. Observe and record the resulting cell behavior (adhesion, spreading, migration) while the ligand is present. Then trigger UV-mediated cleavage of an o-nitrobenzyl (oNB) photolabile linker built into the same construct to release the ligand from the hydrogel, removing the cue without disturbing the surrounding scaffold. Monitor the change in cell behavior after cue removal. This additive-then-subtractive sequence — established separately for RGD release increasing human mesenchymal stem cell cartilage formation — demonstrates MPL's unique capability: dynamically toggling biochemical signals in a living 3D culture, not just building a static structure.

## Key Takeaways
1. MPL's core advantage over single-photon photopolymerization is spatial confinement — the quadratic power dependence of two-photon absorption keeps polymerization inside a sub-micron focal volume, enabling true 3D nanoscale structures rather than stacked 2D layers.
2. Photoinitiator selection is a three-constraint problem (wavelength range, water solubility, cytocompatibility); LAP's much higher water solubility than Irgacure 2959 makes it preferable for aqueous/cell-laden work despite Irgacure 2959 being more established.
3. Cell-present MPL fabrication has a hard energy ceiling: keep pulse energy below ~1.5 nJ to avoid subcellular optical ablation and well below 4 nJ to avoid outright cell death.
4. Two complementary chemistries let MPL do more than build static structures: additive photopolymerization (introduce cues like RGD/VEGF) and photolabile-linker cleavage (subtractively remove cues) — combined, they enable fully reversible, dynamic biochemical patterning in living 3D culture.
5. Backbone polymer choice (PEG for elasticity/nonstick behavior vs. natural polymers like alginate/collagen/gelatin for native bioactivity) should be driven by what signaling behavior the target tissue needs, not generic hydrogel processability.
6. MPL applications split into two material categories: pre-formed biocompatible scaffolds seeded with cells afterward, and hydrogels that directly encapsulate viable cells during fabrication — the energy/PI constraints above apply mainly to the latter.

## Connects To
- **Ch6 (3D Printed Biomaterials)**: MPL is a higher-resolution photopolymerization technique complementary to Ch6's stereolithography (SLA) coverage — SLA for macro/meso-scale resin parts, MPL for nanoscale 3D-resolved hydrogel/ECM-mimicking structures.
- **cheatsheet.md**: the photoinitiator wavelength/solubility table and cell-safety energy thresholds are consolidated there for quick reference during hydrogel formulation.
- **patterns.md**: multiphoton lithography is indexed alongside stereolithography and photolithography as photopolymerization-based fabrication techniques.
