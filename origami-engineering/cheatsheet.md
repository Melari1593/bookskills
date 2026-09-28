# Cheatsheet — Origami Engineering

## Decision: How do I get "flexible to deploy, stiff once deployed"?

| Situation | Use | Why |
|---|---|---|
| Need actively switchable stiffness (soft during install, hard afterward, re-foldable later) | **Vacuum-modulated hinges** (Ch 1) | Stiffness is a controllable pneumatic state, not fixed by geometry alone |
| Need passively fixed anisotropic stiffness, no moving parts/pneumatics wanted | **Zipper coupling** (Ch 2) | Geometry alone creates a permanent large stiffness bandgap |
| Need both a locked flat-state AND high Z-direction stiffness once locked | **Internal coupling** (Ch 2), possibly combined with zipper | Internal tube reaching flat = hard mechanical stop; combine with zipper for isotropy elsewhere |
| Need a static, non-load-bearing 3D representation from one sheet | **Origamic architecture, zero-line method** (Ch 3) | Not a mechanism — a fabrication/representation technique, no kinematic requirement |

## Decision: Which tube-coupling orientation?

| Coupling | Bandgap | Anisotropy | Flat-foldable to 100%? | Pick when… |
|---|---|---|---|---|
| Zipper | Very large (~10²×) | Low (near-isotropic) | Yes | You need uniform stiffness in all off-axis directions |
| Aligned | None (squeezing persists) | High (one strong axis) | Yes | Simplicity matters more than stiffness; loads are known and axis-aligned |
| Internal | None (until locked) | High, but very stiff once locked | No — locks early (e.g. 80%) | You want a hard mechanical stop at a specific extension |

## Thresholds & Defaults

| Parameter | Value / Rule of thumb | Source |
|---|---|---|
| Fold-angle safety margin δ | 180° − 11° = 169° max usable angle (thickness-driven) | Ch 1 |
| Boundary pinning for stable multi-DOF mesh | ≥ V₀/3 + 1 vertices; "every other" boundary vertex in practice | Ch 1 |
| Resulting excess constraints (over-pin) | ≈ V₀/6 | Ch 1 |
| Zipper vs. single-tube bandgap ratio | λ₈ jumps from ~1.4 (single tube) to ~1200 (zipper) — ~2 orders of magnitude | Ch 2 |
| Rigid-body modes to discard in eigenanalysis | First 6 (3 translation + 3 rotation) | Ch 2 |
| Rigid-folding mode index (typical) | 7th eigenmode (λ₇) | Ch 2 |
| Paper weight for origamic architecture | > 130 g/m² | Ch 3 |
| Minimum reference photos before tracing in CAD | ≥ 2, from different angles | Ch 3 |
| Standard origamic-architecture opening angle | 90° | Ch 3 |
| Sheet count for added depth/realism | 1 (simple) → 2–3 (complex/layered) | Ch 3 |

## Tells & Smells

- **If a "deployable" origami design squeezes at one end when loaded at the other** → it's aligned or internally coupled, not zipper-coupled; expect low off-axis stiffness.
- **If a rigid-origami actuation attempt from the flat state folds the wrong way** → you skipped the singularity bias; add an asymmetric pre-load/moment consistent with the intended crease assignment.
- **If two eigenvalues seem to "swap identity" as extension changes** → mode switching (seen in plain Miura-ori sheets near 70% extension); don't assume mode-7 always means "the deployment mode" — check the deformed shape, not just the index.
- **If a CAD-traced facade looks subtly "off" in proportion** → likely traced from one photo; cross-check against a second reference angle before finalizing zero-line offsets.
- **If an origamic-architecture model won't stand up when opened** → a volumetric face is missing its perpendicular sustaining-face partner.
- **If a physical vacuum-stiffened prototype won't fully rigidize** → check that particles are compressed to maximum mutual contact; insufficient vacuum leaves the hinge in its plastic (not locked) regime.

## Quick Decision Rules

- **When designing any rigid-origami mesh**: always resolve the flat-state singularity explicitly (asymmetric bias) — never assume linearization alone picks the right branch.
- **When picking a fold pattern for a freeform double-curved target**: require both convex and concave vertices; all-convex patterns (Yoshimura/PCCP) cannot do it.
- **When a design needs directional (not isotropic) stiffness on purpose**: aligned/internal coupling may actually be the right (simpler) choice — isotropy from zipper coupling is a benefit only when you need it.
- **When laying out an origamic-architecture sheet**: draw the zero line before anything else; every other measurement is relative to it, so an early zero-line mistake propagates through the whole model.
- **When scaling representational complexity beyond one sheet's limits (Ch 3)**: add layered sheets using the same zero-line method per sheet, rather than inventing a different technique.
