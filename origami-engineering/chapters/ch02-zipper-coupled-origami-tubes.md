# Chapter 2: Origami Tubes Assembled into Stiff, Yet Reconfigurable Structures and Metamaterials

Source: Filipov, Tachi & Paulino, PNAS 2015 (vol. 112, no. 40, pp. 12321–12326).

## Core Idea
Coupling two rigid-foldable Miura-ori tubes in a specific "zipper" orientation (rotated and zig-zag-joined, not simply translated) produces an assemblage that keeps exactly one soft (rigid-folding) deformation mode while becoming two orders of magnitude stiffer than any other tube-coupling scheme for every other mode — giving a structure that deploys easily but resists bending/twisting/loading without any separate locking step.

## Frameworks Introduced
- **Zipper coupling**: one Miura-ori tube is translated *and rotated* in the cross-sectional plane until its faces zig-zag-align with a second, identical tube's faces, then the adjacent facets are joined.
  - When to use: whenever you need a deployable structure/metamaterial that must be flexible along one motion (its packing/unpacking path) but stiff against all incidental loads (bending, twisting, point loads) in its deployed state.
  - How: take a single Miura-ori sheet (params a=c=1, α as design variable), mirror it into a tube, then rotate a duplicate tube in the Y–Z cross-section plane until opposing faces line up in a zipper pattern; bond/adhere the aligned facets.
- **Eigenvalue bandgap analysis (β = λ₈ − λ₇)**: use a bar-and-hinge FE-style model to compute the vibration/deformation eigenmodes of an origami assemblage; the 7th mode (post rigid-body modes) is defined as the rigid-folding mode, and the gap to the 8th mode quantifies "how much stiffer is everything else than the intended motion."
  - When to use: comparing candidate coupling/assembly strategies (zipper vs. aligned vs. internal) for which one best isolates a single soft mode.
  - How: build stiffness (K) and mass (M) matrices capturing fold-line bending, panel bending, and panel stretch/shear; solve Kvᵢ = λᵢMvᵢ; drop the first 6 rigid-body modes; compare λ₇ (intended motion) against λ₈ (next cheapest alternative deformation) across percent-extension.

## Key Concepts
- **Miura-ori cell** — four equivalent parallelogram panels defined by height a, width c, vertex angle α; tiled N times to form a sheet.
- **Percentage of extension** — configuration parameter from 0% (folded flat onto the Y–Z plane) to 100% (flat on the X–Y plane); the natural "state variable" for a rigid-foldable mechanism.
- **Zipper / Aligned / Internal coupling** — three ways to combine two compatible Miura tubes: zipper = rotate + interlock; aligned = pure translation, stacked; internal = one tube nested inside another, sized to go flat and lock at a target extension.
- **Bar-and-hinge model** — a simplified structural model (vs. full shell FE) capturing 3 physical behaviors: fold-line bending, flat-panel bending, and panel stretching/shearing; fast enough to explore many assemblage variants, validated against full shell FE.
- **Squeezing deformation** — a failure/alternative mode (mode 8 in single/aligned/internal tubes) where one end of the tube folds while the other unfolds — requires only fold/panel *bending*, no stretch, so it stays cheap (low λ₈) and competes with the intended rigid-folding mode.
- **Bistable state** — a configuration (here, 96.4% extension in the cellular metamaterial) where the cross-section is exactly square and can snap into either of two different rhombus shapes depending on fold direction.

## Mental Models
- Think of "stiffness anisotropy" as the actual design lever: a good deployable structure isn't uniformly stiff or uniformly soft — it's *precisely* soft in one direction (the deployment path) and stiff in every other, and the useful metric is the *gap* between those two, not either value alone.
- A tube-coupling geometry is really an engagement strategy for the *thin sheet's* tension/compression/shear capacity: zipper coupling works because any non-folding deformation now forces the panels to stretch or shear (expensive), while aligned/internal coupling still lets the tubes squeeze past each other cheaply (bending only).
- Treat a cross-section shape as a free parameter, not a constraint: any polygon with translational symmetry (not just quadrilateral) can be extruded into a rigid-foldable tube, and zipper coupling generalizes to hexagonal or arbitrary-sided cross-sections and to repeating the coupling in more than one direction (self-interlocking arrays).

## Anti-patterns
- **Assuming any tube-coupling scheme gives a large bandgap**: aligned and internally coupled tubes are *also* rigid-foldable and flat-foldable but do **not** get the bandgap benefit — they remain prone to squeezing deformations under end loads (Fig. S8), so coupling geometry, not just "tubes joined together," is what matters.
- **Loading a non-zipper deployable cantilever off-axis and expecting I-beam-like behavior**: aligned/internally coupled tubes are markedly anisotropic (stiff only in one loading direction in the Y–Z plane); only zipper tubes show a roughly circular (direction-independent) stiffness profile.
- **Ignoring mode switching**: a given eigenvalue's mode *shape* can change identity as extension changes (e.g., modes 7/8 of a plain Miura-ori sheet swap around 70% extension) — don't assume "mode 7" always means "the deployment mode" without checking for switching; zipper and single tubes are notable for *not* switching.

## Reference Tables

| System | λ₇ (rigid fold) | λ₈ (next mode) | Bandgap behavior at 70% ext. |
|---|---|---|---|
| Single Miura-ori sheet | 2.86 | 11.5 | Moderate; mode 7/8 can switch near 70% |
| Single tube | 1.37 | 1.43 | Tiny gap — squeezing mode nearly as cheap as folding |
| Zipper-coupled tubes | 2.78 | 1194 | ~2 orders of magnitude — hallmark result |

| Coupling type | Flat-foldable to 100%? | Anisotropy under cantilever load | Squeezing-prone? |
|---|---|---|---|
| Zipper | Yes | Low (near-circular stiffness profile) | No |
| Aligned | Yes | High (one strong axis only) | Yes |
| Internal | No (locks when internal tube goes flat, e.g. at 80%) | High, but very stiff once locked (esp. Z-direction) | Yes |

**Governing relation:** `K v_i = λ_i M v_i` (generalized eigenproblem); stiffness `K = F/δ = 1/δ` for unit applied load/force in cantilever and compression tests.

## Worked Example
**Cantilever comparison (Fig. 4):** all three coupled-tube systems are fixed at one end (all nodal displacements zero) and given a unit distributed load at the free end. Because the deformed shape is I-beam-like (material distributed away from centroid increases second moment of area), stiffness is measured as K = 1/δ_max in each Cartesian direction across extension 0–100%. Result: zipper tubes are stiffer overall and *increasingly* stiff as extension approaches 100%; aligned and internal tubes instead show squeezing-dominated deformation under the same end load. Rotating the load direction in the Y–Z plane at 40%, 70%, 95% extension (radial plots, Fig. 4 E–G) makes the anisotropy visible directly: zipper's stiffness plot is close to a circle (roughly load-direction-independent); aligned/internal plots are elongated ellipses (stiff on one axis only). This is the practical proof that zipper coupling, not just "any tube coupling," is what buys direction-independent stiffness.

## Key Takeaways
1. The specific *geometric orientation* of coupling (rotate + zig-zag vs. simple translation) determines whether you get a 2-orders-of-magnitude stiffness bandgap or not — "coupling two tubes" alone is not sufficient.
2. Use eigenvalue bandgap (β = λ₈ − λ₇) as a quantitative, scale-independent metric to compare candidate deployable-structure designs before physical prototyping.
3. Bar-and-hinge models (fast) are adequate for global behavior and design screening; reserve full shell FE for local stress concentrations and validation.
4. Cross-sections need not be quadrilateral — any translationally-symmetric polygon extrudes into a valid rigid-foldable tube, so zipper coupling generalizes to richer geometries (hexagons, curved canopies, self-interlocking arrays).
5. Partial coupling (zipper only in a tube's middle section, ends left free) lets you tune *how much* squeezing/bending freedom remains — coupling doesn't have to be all-or-nothing along a tube's length.
6. At 3D-printed (non-paper-foldable) scale, the same zipper geometry still yields the characteristic anisotropic mechanical response even though the piece cannot physically fold — useful for metamaterial applications where the fold motion itself is never used.

## Connects To
- **Ch 1 (Vacuumatics)**: an alternative stiffening strategy — Ch 1 stiffens hinges with a physical/pneumatic mechanism (vacuum + particles) that must be actively modulated; this chapter stiffens the *whole assemblage* purely through coupling geometry, with no added material state to control. Compare when you need actively-switchable stiffness (Ch 1) vs. passively fixed anisotropic stiffness (this chapter).
- **Ch 3 (Origamic architecture)**: both derive complex 3D form from a flat sheet via prescribed fold lines, but this chapter's Miura-ori tubes stay rigid-foldable (kinematic) while Ch 3's architectural models are static paper sculptures (no rigid-folding requirement).
- **Schenk & Guest 2013 "Geometry of Miura-folded metamaterials"** (ref 7) — source of the internally-coupled tube concept generalized here.
- **Cellular assemblages (Fig. 5–7 in source)** — zipper coupling combined with aligned/internal coupling in 2D/3D arrays; relevant when designing a metamaterial block rather than a single deployable member.
