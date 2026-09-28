---
name: origami-engineering
description: "Knowledge base from three origami engineering papers: Tachi/Masubuchi/Iwamoto's vacuumatic rigid-origami stiffening, Filipov/Tachi/Paulino's zipper-coupled origami tubes, and Philippi Filho/Schmitt/Pupo's origamic-architecture execution method. Use when designing rigid-foldable/deployable structures, choosing a tube-coupling or hinge-stiffening strategy, analyzing origami stiffness with eigenvalue bandgaps, or building single-sheet origamic-architecture (Chatani-style) models."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Origami Engineering: Rigid Structures, Stiffening & Execution Methods
**Sources**: Tachi, Masubuchi & Iwamoto (IASS 2012) · Filipov, Tachi & Paulino (PNAS 2015) · Philippi Filho, Schmitt & Pupo (SIGRADI 2014) | **Chapters**: 3 | **Generated**: 2026-09-16

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `vacuumatics`, `zipper coupling`, `zero line`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch01`, `ch02`, or `ch03`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Two ways to get "soft to deploy, stiff once deployed" out of rigid origami:**
1. **Active/pneumatic (Ch 1, vacuumatics)** — build hinges from offset panels with loose particles packed on the valley-fold side, sealed in an airtight membrane. Low vacuum = particles mobile = hinge plastic/foldable. High vacuum = particle friction locks = hinge rigid. This is a *dial*, not a one-time choice: fold/deploy under light vacuum, lock under strong vacuum, release to re-fold and reuse. A side effect of one-sided particle packing — a small one-directional bending moment at each hinge — is deliberately exploited to break the kinematic singularity at the flat state (see below), not just tolerated.
2. **Passive/geometric (Ch 2, zipper coupling)** — instead of adding a controllable material, choose a *coupling orientation* between two identical rigid-foldable tubes that geometrically forces every non-deployment deformation to stretch/shear the thin sheet (expensive) while the one intended folding motion stays cheap. Rotate one tube into zig-zag alignment with the other (not simple translation) and bond the aligned facets. Measured result: the eigenvalue "bandgap" between the folding mode (λ₇) and the next mode (λ₈) grows ~2 orders of magnitude versus translated (aligned) or nested (internal) coupling, and off-axis stiffness becomes nearly direction-independent (isotropic) — unlike aligned/internal coupling, which stays anisotropic and prone to a "squeezing" failure mode.

**The flat-state singularity problem (Ch 1) applies to any rigid-origami mechanism, not just vacuumatics:** at the fully-unfolded configuration, the constraint Jacobian is singular — `∂L/∂z_i = 0` for every vertex — so the valid configuration space is a union of cells meeting at one point, not a smooth manifold. A naive perturbation there can send the structure down an *invalid* fold path (wrong mountain/valley or convex/concave assignment). Always resolve this with a small, deliberately asymmetric bias consistent with the intended crease pattern — Ch 1's vacuum-induced moment is one concrete way to do this; any comparable pre-load/pre-bias works in principle.

**Boundary-vertex form-finding (Ch 1):** for a multi-DOF triangulated rigid-origami mesh, DOF ≈ V₀ + 3 (V₀ = boundary vertex count), meaning the *interior* is almost entirely determined once you pin roughly a third of the boundary vertices (leaving ~V₀/6 excess/over-constraint on purpose, for stability). The practical upshot: you can drive the entire 3D shape of a large, complex mesh just by moving a handful of boundary control points along planar paths — this is how the interactive "Freeform Origami" form-finding tool works.

**Choosing a fold pattern for freeform (double-curved) surfaces (Ch 1):** you need *both* convex and concave vertices in the base pattern (e.g., waterbomb/namako corrugation). All-convex patterns like Yoshimura/PCCP shells can only produce single-signed mean curvature and cannot sculpt a freeform double-curved shell.

**Zero-line-first layout (Ch 3, origamic architecture):** unrelated to the structural/kinematic chapters above — this is a *representation* technique, not a load-bearing mechanism. Define one master "zero line" fold first; every subsequent volume is a **volumetric-face / sustaining-face pair** measured as valley/mountain-fold offsets *from* the zero line, with cuts always perpendicular to the zero line's own orientation. Skipping the zero-line-first discipline (e.g., tracing volumes before defining it, or from a single distorted photo) is the most common source of a model that won't close or stand correctly.

**When to reach for which:** actively-switchable stiffness with a controllable "off" state → vacuumatics (Ch 1). Fixed, always-on isotropic stiffness with no moving/pneumatic parts → zipper coupling (Ch 2). A single-sheet, non-load-bearing 3D representation of a building or design concept → zero-line origamic architecture (Ch 3). See [cheatsheet.md](cheatsheet.md) for the full decision tables.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-vacuumatic-rigid-origami.md) | Rigid Origami Structures with Vacuumatics | Vacuum-modulated hinge stiffening, singularity-breaking via induced moment, boundary-vertex form-finding |
| [ch02](chapters/ch02-zipper-coupled-origami-tubes.md) | Origami Tubes Assembled into Stiff, Yet Reconfigurable Structures | Zipper coupling, eigenvalue bandgap analysis, bar-and-hinge modeling |
| [ch03](chapters/ch03-origamic-architecture-execution-method.md) | Origamic Architecture — A Method of Execution | Zero-line method, volumetric/sustaining face pairing, 90° origamic architecture workflow |

## Topic Index

- **Anisotropy (stiffness)** → ch02
- **Bandgap (eigenvalue)** → ch02
- **Bar-and-hinge model** → ch02
- **Boundary constraints / form-finding** → ch01
- **Cantilever analysis** → ch02
- **Constructive details (detalhes construtivos)** → ch03
- **Convex / concave vertex** → ch01
- **CAD workflow (AutoCAD, tracing)** → ch03
- **Cellular metamaterials / assemblages** → ch02
- **Descriptive geometry** → ch01, ch03
- **DOF (degrees of freedom)** → ch01
- **Fold-angle constraint** → ch01
- **Freeform Origami (software)** → ch01
- **Kirigami** → ch03
- **Laser cutting / materialization** → ch03
- **Linha zero / zero line** → ch03
- **Miura-ori** → ch02
- **Origamic architecture** → ch03
- **Opening-angle families (0°/90°/180°/360°)** → ch03
- **Pop-up** → ch03
- **Rigid origami (kinematics)** → ch01, ch02
- **Singularity (flat state)** → ch01
- **Squeezing deformation** → ch02
- **Sustaining face / volumetric face** → ch03
- **Vacuumatics** → ch01
- **Waterbomb corrugation (namako)** → ch01
- **Zipper coupling** → ch02

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides

---

## Scope & Limits

This skill covers the three source papers only: geometric/kinematic theory of vacuumatic-stiffened rigid origami, structural/eigenvalue analysis of zipper-coupled origami tubes, and the practical CAD/laser-cutting workflow for single-sheet origamic architecture. It does not cover general origami mathematics beyond what these papers use, other stiffening or coupling schemes not discussed in them, or hands-on fabrication troubleshooting beyond what each paper reports. For implementation (CAD scripting, FE analysis code, laser-cutter operation) combine with project-specific tools.
