# Chapter 4: Centrifugal and Solution Blow Spinning Techniques in Tissue Engineering

*Authors: Muhammad Umar Aslam Khan, Saiful Izwan Abd. Razak, Rawaiz Khan, Sajjad Haider, Mohsin Ali Raza, Rashid Amin, Saqlain A. Shah, Anwarul Hasan*

## Core Idea
Electrospinning dominates nanofiber fabrication but is capped by low throughput, high-voltage safety concerns, and a requirement for conductive/spinnable polymer solutions — centrifugal spinning (CS) and solution blow spinning (SBS) are voltage-free, high-yield alternatives that use mechanical/centrifugal force or compressed gas instead of an electric field to draw the same submicron-to-nanoscale fibers from a much wider range of raw materials.

## Frameworks Introduced
- **Force-balance model of fiber formation (centrifugal spinning)**: fiber diameter is the outcome of a tug-of-war between centrifugal force (which stretches the jet), air friction (which resists it), surface tension (which pulls the jet back into beads), and rheological/viscous forces (which resist sudden structural change and keep the jet smooth).
  - When to use: as the diagnostic framework when troubleshooting bead defects or inconsistent fiber diameter in a CS setup.
  - How: centrifugal force `F_centri = mω²D/2` (m = fluid mass, ω = rotational speed, D = spinning-head diameter) must exceed the jet's surface tension to eject and stretch it; air friction `F_fri = πCρAω²D²/2` opposes stretching as the jet travels to the collector. Tune ω, D, and solution viscosity/concentration together rather than any single variable in isolation.
  - Berry number (Be) is the practical proxy for whether a given polymer solution/concentration will spin cleanly: too high above the critical Be* and polymer chains are too tightly entangled to draw into fiber; too far below and chain overlap is too sparse, both leading to beading or discontinuous fiber instead of smooth, bead-free nanofiber.
- **Voltage-free alternative selection rule**: when electrospinning's failure mode is throughput, safety, or non-conductive/non-spinnable polymer solutions, switch to a mechanical (CS) or pneumatic (SBS) draw mechanism instead of trying to fix electrospinning's electric-field dependency.
  - When to use: any time production volume, raw-material conductivity, or high-voltage safety are the binding constraint rather than fiber quality itself.
  - How: CS replaces the electric field with rotational/centrifugal force (borrowed from the glass-wool/cotton-candy mechanism); SBS replaces it with a high-velocity gas stream shearing the polymer solution at the nozzle tip — both need no conductive polymer and no high-voltage source.

## Key Concepts
- **Centrifugal spinning (CS)** — also called rotary spinning or rotary jet spinning; a rotating head (2,000–12,000 rpm depending on scale) ejects polymer solution or melt through nozzles, and centrifugal force stretches the ejected jets into fibers as they fly toward a surrounding collector.
- **Solution blow spinning (SBS)** — a concentric-nozzle technique where high-velocity compressed gas shears and elongates a polymer solution jet into fiber, analogous to melt blowing but done with a solution at near-ambient temperature.
- **Berry number (Be)** — a dimensionless group derived from a polymer solution's intrinsic viscosity and concentration; used (originally from electrospinning) to predict whether chain entanglement is in the right range to produce smooth, bead-free fiber rather than droplets or overly thick fiber.
- **Rotating head** — the CS component holding twin syringes/nozzles that spins the polymer fluid outward; head diameter and nozzle diameter are the two primary geometric levers on fiber diameter.
- **Formation bonnet** — in glass-fiber-industry CS, the housing beneath the spinning head that randomizes fiber deposition into a mat on a conveyor belt (the historical/industrial precedent CS nanofiber work is derived from).
- **Core-shell nanofiber** — a composite fiber architecture achievable by both CS and SBS (via coaxial/dual-fluid nozzle setups), useful for combining a structural core polymer with a bioactive/functional shell.
- **Segmented-pie bicomponent spinning** — a conventional (non-CS/SBS) technique where two incompatible polymers are co-spun then mechanically split into finer microfibers; included as one of several older nanofiber routes CS/SBS are positioned to replace.

## Mental Models
- Treat CS as "electrospinning's mechanical twin": same end product (nanofiber mat for TE scaffolds), but the driving force and therefore the tunable-parameter set is completely different (rotational speed/head geometry instead of voltage/field geometry) — don't try to reuse electrospinning process parameters when switching to CS.
- Fiber diameter shrinks monotonically as any of these three levers move in the "more stretching" direction: smaller nozzle diameter, higher rotational speed, greater nozzle-to-collector distance (up to a plateau) — but each lever has a practical floor/ceiling (too small a nozzle stops ejection entirely; too much distance past ~10 cm gives only marginal further reduction).
- SBS's central selling point is safety and material breadth, not necessarily superior fiber quality — it exists to be the technique you reach for when a polymer solution isn't conductive enough to electrospin, not to universally replace electrospinning.

## Anti-patterns
- **Assuming higher rotational speed always yields finer fiber**: past the speed needed to reach the motor's stable-rotation limit for a given head diameter, further increases destabilize rotation rather than improving fiber fineness.
- **Using too small a nozzle diameter chasing thinner fiber**: below a threshold the liquid jet cannot eject at all — nozzle diameter must stay large enough to sustain flow while still restricting mass throughput enough to draw a fine fiber.
- **Ignoring solvent evaporation timing**: nozzle-to-collector distance must be long enough for solvent to evaporate before the jet lands, but distances beyond ~10 cm give only nominal further diameter change — over-extending the flight path wastes chamber space without benefit.
- **Treating CS/SBS as solved commercial replacements for electrospinning across the board**: they solve throughput/voltage/conductivity limitations specifically, but the chapter is explicit that all nanofiber techniques (melt blowing, bicomponent, phase separation, template synthesis, self-assembly included) retain their own material-selection limitations.

## Reference Tables

**Table 1 — Functional comparison of Centrifugal Spinning vs. Solution Blow Spinning**

| Parameter | Centrifugal Spinning | Solution Blow Spinning |
|---|---|---|
| Nanofiber diameter range | 25 nm – 50 mm | 40 nm – several mm |
| Injection/production rate | up to 1 mL/min per nozzle | 20 mL/min |
| Influencing parameters | viscosity, rotational speed, orifice diameter, evaporation rate, distance | nozzle geometry, solution viscosity, solution feed rate, gas pressure |
| Commercialized | Yes | Yes |
| Aligned nanofiber production | Yes | Yes |
| Melt spinning capable | Yes | Yes |
| Concentrated polymer solutions | Yes | Yes |
| Voltage requirement | No | No |
| Composite (polymer + ceramic) fibers | Yes | Yes |
| Core-shell nanofiber fabrication | Yes | Yes |
| 3D nanofibrous production | Yes | Yes |

**Table 2 — CS process parameter effects (as reported)**

| Parameter change | Observed fiber-diameter effect |
|---|---|
| Nozzle diameter 1.0 mm → 0.4 mm | Fiber diameter 895 nm → 665 nm |
| Nozzle-to-collector distance 10 cm → 30 cm | Fiber diameter 665 nm → 647 nm (minor change beyond ~10 cm) |
| Rotational speed range used in literature | 3,000–12,000 rpm |
| Industrial glass-wool CS (precedent process) | Spinning head 900–1100 °C, rotating at 2,000–3,000 rpm |
| Ceramic nanofiber calcination (TiO2 from titanium tetrachloride precursor) | Calcined at 700 °C after centrifugal spinning |

## Worked Example
Ceramic nanofiber fabrication by centrifugal spinning (as reported for TiO2): chelate titanium tetrachloride with acetylacetone to form titanium polyacetylacetonate, a spinnable precursor. Centrifugally spin this precursor solution into nanofibers using the standard CS rotating-head setup. Calcine the spun precursor fibers at 700 °C, which converts them into crystalline TiO2 nanofibers. The same calcination-after-spinning pattern was reused with a zirconyl chloride precursor to produce ZrO2-based nanofibers — illustrating that CS's utility extends past polymers into ceramic precursor chemistry once a spinnable precursor solution is engineered.

## Key Takeaways
1. CS and SBS exist specifically to remove electrospinning's three biggest constraints: low throughput, high-voltage safety requirements, and dependency on conductive/spinnable polymer solutions.
2. CS fiber diameter is governed by a force balance (centrifugal vs. air friction vs. surface tension vs. rheological resistance) — use the Berry number to sanity-check whether a candidate polymer concentration will spin cleanly before committing to a run.
3. The three practical CS dials are rotational speed (3,000–12,000 rpm reported range), spinning-head diameter, and nozzle diameter — each has a floor/ceiling past which you get instability or ejection failure rather than further improvement.
4. Nozzle-to-collector distance matters mainly for solvent evaporation timing; ~10 cm is typically sufficient, with only marginal gains from going further.
5. SBS trades electrospinning's electric-field mechanism for a compressed-gas shear mechanism, achieving comparable or wider fiber-diameter range (40 nm–several mm) at higher throughput (~20 mL/min) without any conductivity requirement.
6. Both techniques support the same advanced fiber architectures as electrospinning — aligned fibers, core-shell fibers, composite polymer-ceramic fibers, and 3D nanofibrous structures — making them drop-in alternatives rather than lesser substitutes for most tissue-engineering scaffold needs.
7. CS extends beyond polymers to carbon nanofibers (via PAN/pitch precursor + stabilization/carbonization heat treatment) and ceramic nanofibers (via metal-salt precursor + calcination), following the same spin-then-heat-treat pattern each time.

## Connects To
- **Ch1 (Introduction)**: expands on the fiber-fabrication branch of Ch1's porogen/fiber/rapid-prototyping taxonomy, going deep on two specific fiber techniques only briefly named there.
- **Ch5 (Electrospun Nanofibers)**: the electrospinning technique this chapter positions CS/SBS as alternatives to; read together for a full nanofiber-scaffold picture.
- **cheatsheet.md**: CS/SBS fiber-diameter ranges and process-parameter effects are consolidated there alongside electrospinning's numbers for side-by-side comparison.
- **patterns.md**: centrifugal spinning and solution blow spinning are indexed there alongside electrospinning and melt blowing as nanofiber-generation techniques.
