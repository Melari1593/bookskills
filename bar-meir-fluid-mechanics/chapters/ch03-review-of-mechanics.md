# Chapter 3: Review of Mechanics

## Core Idea
Before building the momentum and energy balances used throughout the book, the reader needs the rigid-body tools of statics/dynamics — center of mass, moment/product of inertia, and Newton's second law — because fluid mechanics repeatedly treats a fluid as a continuum built from infinitesimal "small bodies" to which these same laws apply.

## Frameworks Introduced
- **Center of mass / centroid**: the point through which a straight-line force can act on a body without inducing rotation; it is independent of the coordinate system used to compute it.
  - When to use: whenever a distributed mass or area must be replaced by an equivalent point for force/moment balances (e.g., locating the resultant of a distributed load).
  - How: integrate position weighted by density over the body, `x̄_i = (1/m)∫_V x_i ρ dV`; for a thin, uniform-thickness body this collapses to an area integral, `x̄_i = (1/A)∫_A x_i dA`.

- **Moment of inertia (mass and area)**: a measure of how mass/area is distributed relative to a chosen axis; unlike center of mass, it depends on which axis is chosen.
  - When to use: rotational dynamics (angular momentum, rotational kinetic energy) and, for the area form, bending/pressure-distribution problems (previewed here for use in the Fluid Statics chapter's forces on submerged surfaces).
  - How: integrate `r²` (squared distance from the axis) weighted by mass or area, `I_rr = ∫_m ρ r² dm` or `I_xx = ∫_A r² dA`; use the **radius of gyration** `r_k = √(I_m/m)` as a compact "equivalent point-mass distance."

- **Parallel Axis Theorem**: relates the moment of inertia about a centroidal axis to the moment of inertia about any parallel axis.
  - When to use: computing inertia of a composite shape, or moving an axis off the centroid, without re-integrating from scratch.
  - How: `I_x'x' = I_xx + r²A` (area form) or the mass-equivalent, where `r` is the perpendicular offset between the two parallel axes and the cross term vanishes because it integrates an odd function about the centroid.

- **Product of Inertia and Transfer-of-Axis Theorem**: quantifies the coupling between two perpendicular axes (`I_xy = ∫_A xy dA`), used together with moment of inertia when working in a rotated or non-principal frame.
  - When to use: whenever an area's principal axes are not the axes of convenience (e.g., unsymmetrical cross-sections), or before diagonalizing the inertia tensor.
  - How: transfer between parallel axes with `I_x'y' = I_xy + Δx·Δy·A`; note `I_xy = I_yx`, and any axis of symmetry makes the product of inertia through it exactly zero.

- **Principal Axes of Inertia**: the inertia tensor `[I_xx, -I_xy, -I_xz; -I_yx, I_yy, -I_yz; -I_zx, -I_zy, I_zz]` can, for a suitable rotation, be diagonalized (zero off-diagonal/product-of-inertia terms).
  - When to use: simplifying rotational dynamics calculations by working in the frame where products of inertia vanish.
  - How: apply the standard linear-algebra eigenvalue/eigenvector diagonalization to the inertia tensor (the chapter references this result without full derivation).

- **Newton's Second Law, continuum form**: extends the discrete-body law `ΣF = D(mU)/Dt` to a continuous medium by imagining the body divided into many small connected sub-bodies.
  - When to use: this is the direct precursor to the control-volume momentum equation used later for fluids — apply it whenever a fluid region must be analyzed as a collection of mass elements.
  - How: as the sub-bodies shrink, internal (inter-element) forces cancel in pairs, leaving `ΣF = ∫_V D(ρU)/Dt dV = D/Dt ∫_V ρU dV = D²/Dt² ∫_V ρr dV`; forces are split into **body forces** (act at a distance — gravity, magnetic field) and **surface forces** (act on the boundary — pressure, stress).

## Key Concepts
- **Center of mass**: the mass-weighted average position of a body; coordinate-system independent.
- **Line/area/volume density**: mass per unit length, area, or volume, used depending on whether the body is modeled as 1D, 2D (thin), or fully 3D.
- **Moment of inertia**: `∫ r² dm` (or `dA`) about a stated axis; always positive, always axis-dependent.
- **Radius of gyration**: the single equivalent distance from the axis at which all the mass could be concentrated to reproduce the same moment of inertia.
- **Product of inertia**: `∫ xy dA`; can be positive, negative, or zero (zero for any axis of symmetry).
- **Principal axes**: the orientation of axes for which the product-of-inertia terms of the inertia tensor vanish.
- **Body forces vs. surface forces**: forces acting throughout the volume from a distance (gravity) versus forces acting only on the boundary (pressure, shear stress).
- **Centrifugal, angular, and Coriolis acceleration**: the three "extra" acceleration terms that appear when describing motion using a rotating reference frame.

## Mental Models
- Think of the center of mass as the single support point that lets a body hang without rotating — this is why it is the natural point to apply a resultant force.
- Use the thin-body (area) approximation only as a shortcut for the full volume integral, valid when thickness is small compared to the other dimensions — not as a universally safe default.
- Build up the moment of inertia of a complex shape the way an engineer assembles a truss: compute simple pieces about their own centroids, then use the parallel axis theorem to shift each to a common axis and sum.
- Treat the continuum form of Newton's second law as "the same law, just applied to infinitely many infinitesimally small connected bodies" — internal forces between neighboring fluid elements cancel, which is exactly why only external (body + surface) forces survive in the control-volume statement used in later chapters.

## Anti-patterns
- **Assuming moment of inertia is coordinate-independent like center of mass**: it is not — it depends on the specific axis of rotation, so a value computed about one axis cannot be reused for a different (even parallel) axis without applying the parallel axis theorem.
- **Applying the thin-body/2D area approximation without checking thickness**: Example 3.4 shows the relative error between the "zero-thickness" and true 3D moment of inertia is controlled by `(t/a)²` and grows quickly even for modest thickness ratios — the width `b` of the shape has no effect on this error, which is easy to overlook.
- **Confusing "symmetric shape" with "symmetric matrix result"**: a symmetric area has zero *product* of inertia, not zero moment of inertia — the two quantities behave differently under symmetry.
- **Treating product of inertia as always positive**: unlike moment of inertia, it is signed; sign errors propagate directly into any subsequent principal-axis or transfer-of-axis calculation.
- **Forgetting the internal-force cancellation argument**: when moving from the discrete `ΣF = D(mU)/Dt` to the continuum form, students often keep or double-count inter-element forces; only body and surface forces on the *external* boundary should remain.

## Key Equations
- `x̄_i = (1/m)∫_V x_i ρ(x_i) dV` — center of mass along direction `i`; reduces to `x̄_i = (1/A)∫_A x_i dA` for a thin, uniform-thickness, uniform-density body.
- `I_rr = ∫_m ρ r² dm` (equivalently `I_xx=∫_A r² dA` for areas) — moment of inertia about a stated axis; `r_k = √(I_m/m)` is the radius of gyration.
- `I_x'x' = I_xx + r²A` — parallel axis theorem; shifts a centroidal moment of inertia to any parallel axis a perpendicular distance `r` away.
- `I_x'y' = I_xy + Δx·Δy·A`, with `I_xy = I_yx` — transfer-of-axis theorem for the product of inertia; vanishes identically about any axis of symmetry.
- `ΣF = D(mU)/Dt → ΣF = D/Dt ∫_V ρU dV = D²/Dt² ∫_V ρr dV` — Newton's second law generalized from a discrete body to a continuum (the direct ancestor of the control-volume momentum equation).
- `a = d²R/dt²|_R + (R × dω/dt) + ω×(R×ω) + 2(dR/dt|_R × ω)` — acceleration of a point in a rotating frame, decomposing into the "seen" acceleration plus angular, centrifugal, and Coriolis contributions.

## Reference Tables
**Table 3.1 — Moment of Inertia for common plane shapes about their own centroidal axis** (as tabulated in the chapter; `a`, `b` are shape dimensions, `r` is radius, `α` is a shape parameter/half-angle):

| Shape | Centroid location | Area `A` | `I_xx` |
|---|---|---|---|
| Rectangle | `a/2 , b/2` | `a·b` | `a·b³/12` |
| Triangle | `a/3` | `a·b/3` | `a·b³/36` |
| Circle | `b/2` | `π·b²/4` | `π·b⁴/64` |
| Ellipse | `a/2 , b/2` | `π·a·b/4` | `a·b³/64` |
| Parabola (`y=α x²`) | `3αb/(15α−5)` | `(6α−2)/3 · (b/α)^{3/2}` | `√b·(20b³−14b²)/(35√α)` |
| Quadrant of circle | `4r/(3π)` | `π r²/4` | `r⁴(π/16 − 4/9π)` |
| Ellipsoidal quadrant | `4b/(3π)` | `π·a·b/4` | `a·b³(π/16 − 4/9π)` |
| Half ellipse | `4b/(3π)` | `π·a·b/4` | `a·b³(π/16 − 4/9π)` |
| Circular sector (about centerline) | `0` | `2α·r²` | `(r⁴/4)(α − ½sin2α)` |
| Circular sector (about edge) | `(2/3)·r sinα/α` | `2α·r²` | `(r⁴/4)(α + ½sin2α)` |

## Worked Example
**Reconstructed from Example 3.1 (fire-hose/window problem).** A water jet nozzle sits a horizontal distance `a` from a building; the target window is a height `b` above the nozzle. Gravity is `g`. Find the launch angle `θ` (and required speed `U`) so the jet's velocity is exactly horizontal (vertical component = 0) at the moment it reaches the window.

Set up three equations for the two velocity components and time `t`:
1. Horizontal position: `a = U cosθ · t`
2. Vertical position (window taken as origin, height `b` above launch): `0 = −(g t²)/2 + U sinθ · t − b`
3. Vertical velocity is zero at the window: `0 = −g t + U sinθ`

From (3), the time to reach zero vertical velocity is `t = U sinθ / g`. Substituting `t` from (1) into (3) gives a relation between `U` and `θ`:
`U cosθ · (a/(U cosθ)) = a` is trivial, so instead eliminate `t` between (1) and (3) directly: `U sinθ/g = a/(U cosθ)`, which rearranges to
`U = √(a g) / cosθ`

Substituting this `U` into equation (2) (after eliminating `t`) yields the final closed-form result:
`tanθ = b/a + 1/2`

So the required aim angle depends only on the geometry ratio `b/a`, and the required launch speed follows from `U = √(ag)/cosθ` once `θ` is known. The example demonstrates the general method: write position/velocity kinematics as a small nonlinear system, use one physical condition (here, "velocity is horizontal at the target") to close the system, and eliminate variables algebraically rather than solving simultaneously.

## Key Takeaways
1. Center of mass/centroid calculations reduce to a density-weighted integral over volume (or area, for thin bodies) and are always independent of the coordinate system chosen.
2. Moment of inertia is fundamentally axis-dependent — always state or track the reference axis, and use the radius of gyration as a compact way to compare distributions.
3. The parallel axis theorem (`I_x'x' = I_xx + r²A`) is the practical tool for building up composite-shape inertias from tabulated centroidal values instead of re-integrating.
4. The product of inertia transforms similarly (`I_x'y' = I_xy + ΔxΔyA`) but is signed and vanishes identically for any axis of symmetry — a useful shortcut and a common sign-error trap.
5. Newton's second law scales seamlessly from a single rigid body (`ΣF = D(mU)/Dt`) to a continuum (`ΣF = D/Dt ∫_V ρU dV`) by imagining the body as infinitely many connected small bodies whose internal forces cancel — this is the conceptual bridge to control-volume analysis used throughout the rest of the book.
6. In a rotating frame, acceleration picks up centrifugal, angular, and Coriolis terms beyond the locally observed acceleration — essential for later treatment of rotating machinery and rotating fluid systems.
7. Thin-body (2D) simplifications for area properties are only safe when thickness is small relative to the other dimensions; the associated error grows with `(t/a)²` regardless of the shape's width.

## Connects To
- **Fluid Statics chapter**: directly reuses center of mass/area and moment of inertia (especially the parallel axis theorem and Table 3.1 shapes) to locate the center of pressure and compute resultant forces on submerged plane surfaces.
- **Momentum Conservation chapter**: the continuum form of Newton's second law derived here, `ΣF = D/Dt ∫_V ρU dV`, is the direct ancestor of the control-volume linear-momentum equation applied to flowing fluids.
- **Review of Thermodynamics chapter**: a parallel "review" chapter that supplies the other prerequisite toolkit (state relations, energy) needed alongside mechanics before the book's fluid-specific chapters begin.
- **Rotating reference frames / rotating machinery**: the centrifugal, angular, and Coriolis acceleration terms introduced here reappear whenever later analysis considers rotating fluid systems (e.g., pumps, turbomachinery, or rotating coordinate frames for atmospheric/oceanic flows).
