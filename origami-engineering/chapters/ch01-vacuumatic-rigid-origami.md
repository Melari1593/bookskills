# Chapter 1: Rigid Origami Structures with Vacuumatics

Source: Tachi, Masubuchi & Iwamoto, "Rigid Origami Structures with Vacuumatics: Geometric Considerations," IASS 2012.

## Core Idea
A multi-DOF rigid-foldable origami structure can be made temporarily stiff — without locking it into a single fixed shape — by embedding particle-filled Vacuumatics (negative-pressure double membranes) along its hinge lines, so the *same* structure is soft enough to fold on site and stiff enough to stand once evacuated.

## Frameworks Introduced
- **Vacuumatics-stiffened hinge**: a hinge made of two offset rigid panels with loose aggregate particles packed between them in a breathable sleeve, the whole assembly sealed in an airtight membrane.
  - When to use: any rigid-origami structure that must be field-deployed (transported flat/compact) and then hold shape under self-weight and load without a separate locking mechanism.
  - How: (1) size the panel offset from max fold angle and panel thickness so panels never collide during folding; (2) fill only the valley-fold side gap with particles; (3) enclose in one airtight membrane forming a single air chamber; (4) modulate vacuum strength to move the hinge between plastic (foldable) and rigid (locked) states.
- **Singularity-breaking via induced moment**: because particles sit only on the valley-fold side, evacuating the chamber produces a small one-directional bending moment at every hinge — this moment is not a structural bonus, it is a kinematic tool.
  - When to use: at the flat (fully unfolded) configuration, where rigid-origami's governing equations are singular and a generic small perturbation could fold the structure the *wrong* way (invalid mountain/valley or convex/concave assignment).
  - How: apply a light vacuum before actuating boundary points; the asymmetric particle placement biases the structure into the *correct* transformation branch automatically, removing the need for external jigging at start-up.

## Key Concepts
- **Vacuumatics** — a negative-pressure double membrane containing loose particles; friction between compressed particles stiffens the assembly (originates with J. Gilbert's 1971 "LIVING-ROOM" and Frei Otto's 1970s pneumatic-structure research).
- **Rigid origami** — a folding kinematics where all deformation is concentrated at crease lines and panels themselves stay flat (undeformed) throughout motion.
- **Waterbomb corrugation ("namako")** — a triangle-based fold pattern mixing convex and concave vertices (unlike Miura-ori/Yoshimura, which are all-convex), chosen here because mixed curvature is needed to sculpt freeform double-curved surfaces.
- **Convex / concave vertex** — a vertex is convex if the solid angle around it is >2π, concave if <2π; a vertex with 4 mountain folds (of the surrounding folds) is convex, 2 mountain folds is concave.
- **DOF (degrees of freedom)** — for a triangulated disk-like mesh, DOF = V₀ + 3 + S, where V₀ = boundary vertices and S = self-equilibrium/degenerate constraints; pinning enough boundary vertices drives DOF to 0 (a stable structure).
- **Singular flat state** — the fully unfolded configuration, where the origami's constraint Jacobian degenerates (∂L/∂z = 0 for every vertex), so the valid configuration space is a union of cells meeting at one point rather than a single smooth manifold.
- **2.5D / thick-panel offset** — technique (from Tachi 2010, ref [9]) of offsetting panel outlines so double-layer thick panels don't collide when folding to a target max angle.

## Mental Models
- Think of the flat, fully-unfolded origami state as a *branch point*, not a starting point: many valid and invalid folding paths emanate from it, and without a bias you can accidentally choose an invalid one (wrong mountain/valley, wrong convexity). A tiny asymmetric force at that exact point is cheap insurance against a global folding error.
- Treat "stiffness" and "shape control" as two *independently dialable* knobs on the same hardware: lower vacuum = plastic/moldable, higher vacuum = locked/stiff. You are not choosing between a soft structure and a rigid one at design time — you are choosing a *vacuum schedule* at construction/operation time.
- A rigid-origami vertex mesh under partial boundary pinning is statically indeterminate on purpose: pinning "nearly every other" boundary vertex (~V₀/3+1 minimum, more in practice) leaves ~V₀/6 excess constraints, trading a small amount of over-constraint for a much more predictable, jitter-free 3D shape.

## Anti-patterns
- **Locking a multi-DOF origami shell with add-on rods/braces** (e.g., 3 fixing rods per concave vertex, as in Resch & Christiansen's doubly-expandable shells): defeats the reusability/transformability that was the whole point of choosing rigid origami in the first place.
- **Ignoring the flat-state singularity**: naively linearizing the truss model at the fully-unfolded state and picking *any* nontrivial null-space direction can produce a kinematically "unfavorable" fold (Figure 6, left) that violates the intended crease assignment — always bias the choice with a physical or numerical nudge consistent with the design's mountain/valley pattern.
- **Choosing an all-convex pattern (Yoshimura/PCCP) for a freeform double-curved target shape**: all-convex patterns can't produce mixed positive/negative mean curvature; you need vertices of both types.

## Reference Tables

| Design parameter (example design) | Value |
|---|---|
| Max fold angle range | 0° → 169° (thickness/offset constrained) |
| Fold-angle constraint margin δ | 11° (i.e., \|ρ\| ≤ 180° − 11°) |
| Exterior panel thickness : longest-edge ratio | ≈ 0.009 |
| Interior panel thickness : longest-edge ratio | ≈ 0.006 |
| Grid pattern basis | 36° grid waterbomb corrugation |
| Workable fold-angle range (this pattern) | 0° to 161° |

**Governing equations (unstable truss model):**
- Constraint: `[∂L/∂x]{Δx} = {0}` — nontrivial null-space solutions are valid infinitesimal motions.
- DOF count: `DOF = 3V − E + S` in general; `DOF = V₀ + 3 + S` for a triangulated-disk mesh (Euler's formula applied).
- Constrained system (ground + fold-angle + user constraints stacked): `[C]{Δx} = [∂L/∂x; ∂G/∂x]{Δx} = {0}`, solved for minimum-norm update via Moore–Penrose pseudo-inverse: `{Δx} = {I − [C]⁺[C]}{Δx₀}`.
- Fold-angle inequality treated as an equality **only when violated** (penalty-function style), not enforced everywhere.

## Worked Example
**The 3-stage build/deploy sequence** the paper proposes for a full-scale shell:
1. **Prefabrication (flat, off-site):** lay the membranes, panels, particles and fabric flat, apply negative pressure so the small self-folding moment appears everywhere at once, then fold the whole sheet to a compact bundle for transport — the vacuum-induced moment is what makes this initial fold *deterministic* instead of ambiguous.
2. **On-site deployment:** unfold under a *light* vacuum (particles still mobile → hinges plastic/moldable) while operators or a mechanism move only the boundary vertices; because the interior is massively overconstrained relative to a handful of boundary DOF (DOF = V₀+3), moving the boundary is enough to sweep the entire 3D shape through a continuous family of valid forms (Figure 8 shows several distinct boundary-driven target shapes from one pattern).
3. **Final set:** once the desired 3D configuration is reached, *strengthen* the vacuum — particles lock via friction, hinges go rigid, structure becomes load-bearing. To re-use or re-route the structure, release vacuum (back to plastic) and re-fold to compact form; repeat.
The authors validated with an interactive tool (**Freeform Origami**) that a continuous, constraint-respecting path exists connecting: flat state → compact folded state → several target 3D states (Fig. 8), all while enforcing the fold-angle and ground-pinning constraints from Eq. 2–3.

## Key Takeaways
1. Vacuum strength is a *design variable*, not just a fabrication detail — use a low vacuum to keep hinges plastic during shaping, a high vacuum to lock the final structure.
2. The flat/fully-unfolded state of any rigid-origami mesh is kinematically singular; resolve it with a small deliberate asymmetric bias (here: one-sided particle packing) rather than assuming "any" perturbation direction works.
3. Choose a fold pattern with both convex and concave vertices whenever the target surface needs both positive and negative mean curvature (i.e., anything beyond a simple corrugation).
4. A partially-pinned multi-DOF origami mesh is intentionally over-constrained (~V₀/6 excess) — this is a feature that keeps the interactive form-finding well-behaved, not a bug to eliminate.
5. Reusable/transformable structures should get their stiffness from a reversible physical mechanism (vacuum/friction) rather than from mechanical locks that must be removed to re-fold.

## Connects To
- **Ch 2 (Zipper-coupled origami tubes)**: an alternative, purely-geometric route to combining "flexible to deploy" with "stiff once deployed" — compare vacuum-based stiffening (this chapter) against overconstraint-based stiffening via tube coupling (Ch 2) as two different levers for the same design goal.
- **Ch 3 (Origamic architecture)**: both chapters rely on the same descriptive-geometry backbone (a base/reference fold line, defined mountain/valley assignment, and closure conditions) even though Ch 3's models are non-rigid single-sheet paper art rather than load-bearing structures.
- **Freeform Origami software** (Tachi 2010) — the interactive form-finding tool used to validate constrained paths in this chapter; useful whenever you need to numerically explore the constrained configuration space of a rigid-origami pattern.
