# Patterns — Fluid Mechanics (Bar-Meir)

## RTT Master Template (derive ANY conservation law)
**When to use**: deriving a control-volume form of mass, momentum, energy, or angular-momentum conservation.
**How**: (1) write the system integral of the intensive property φ times ρ; (2) apply the Reynolds Transport Theorem D/Dt∫_sys(φρ)dV = d/dt∫_cv(φρ)dV + ∫_S φρU_rn dA; (3) specialize φ: mass→φ=1, momentum→φ=U, angular momentum→φ=r×U, energy→φ=e_total.
**Trade-offs**: one pattern covers Ch5–Ch8 entirely; skipping straight to memorized final equations (e.g., ρAU=const) hides when the simplifying assumptions (steady, uniform, non-deformable) actually apply.

## Cut-the-Control-Volume-Through-the-Solid (find a reaction force)
**When to use**: any problem asking for the force/reaction on a nozzle, pipe bend, bracket, or support.
**How**: choose the CV boundary so it slices through the solid structure; the unknown reaction becomes a clean F_ext term in the momentum balance; evaluate body force, pressure force, and momentum flux separately, then solve for F_ext.
**Trade-offs**: requires correctly identifying every open face's pressure and velocity — a boundary chosen through fluid instead of solid buries the reaction force inside an unmeasurable internal stress.

## Displaced-Parcel Stability Test
**When to use**: any stability question — atmospheric convection, floating-body tilt, heavy-over-light interfaces (Rayleigh-Taylor).
**How**: perturb the system slightly (displace a slab, tilt a hull, deform an interface), compute whether the restoring force/density points back toward equilibrium, and read the sign as the stability criterion (GM>0, Cx < adiabatic lapse rate, L < L_c).
**Trade-offs**: gives a binary stable/unstable answer, not the growth rate or dynamics of the instability once triggered.

## g_eff Generalization (Fluid Statics)
**When to use**: any static/rigid-body-accelerating fluid problem (tilted tanks, rotating containers, geological columns).
**How**: compute g_eff = g_gravity − a_container (vector sum); constant-pressure surfaces are always perpendicular to g_eff; integrate grad P = ρ g_eff along that direction.
**Trade-offs**: only valid when the fluid moves rigidly with its container (no internal relative motion / sloshing).

## Star (*) Reference-State Normalization (Compressible Flow)
**When to use**: any Ch11 isentropic/shock/Fanno/Rayleigh two-point problem.
**How**: convert both known and unknown states to ratios against the M=1 critical (star) state first (T/T*, P/P*, A/A*, all functions of k alone), then combine — this is how printed compressible-flow tables and Potto-GDC work.
**Trade-offs**: star quantities are model-specific — a Fanno T* is not the same reference as an isentropic T*; never mix star ratios across models.

## Panel-by-Panel Shock-Expansion Marching
**When to use**: lift/drag on a thin 2-D supersonic body (diamond airfoil, flat plate at incidence, wedge).
**How**: break the surface into flat panels; at each compression corner apply oblique-shock jump relations, at each expansion corner apply the Prandtl-Meyer turn ν2=ν1+δ; assume uniform flow between panels; integrate piecewise-constant pressure for force. Match static pressure (not stagnation pressure) across any slip line.
**Trade-offs**: breaks down near δ_max (detachment) and treats corners as mathematically sharp, ignoring real boundary-layer smoothing.

## Superposition of Elementary Potential Flows
**When to use**: constructing 2D inviscid flow around a specific shape (cylinder, corner, lifting body).
**How**: because Laplace's equation is linear, add stream functions/potentials of uniform flow, source, sink, vortex, doublet; the body surface is wherever the combined ψ = constant.
**Trade-offs**: only valid outside boundary layers/wakes (viscosity is what actually generates the circulation Γ that potential theory then represents as an added vortex).

## Building Blocks Method (Dimensional Analysis)
**When to use**: default method for Buckingham π reduction with a moderate parameter count.
**How**: choose a repeating set of parameters spanning all basic dimensions (no two sharing a dimension), express each basic dimension in terms of that set, then normalize each remaining parameter against it to form one π group per leftover parameter.
**Trade-offs**: only gives the *minimum count* of groups — always cross-check against the governing equations (Nusselt's technique) when boundary/initial-condition-driven groups might be missed.

## Nusselt Non-Dimensionalization (governing-equation-driven)
**When to use**: real engineering scaling work, not classroom Buckingham exercises.
**How**: write the actual governing PDE plus boundary/initial conditions, normalize every variable by a characteristic scale, and read off the dimensionless groups that appear as coefficients.
**Trade-offs**: more laborious, requires knowing/deriving the governing equation first — but is the only method guaranteed to surface BC-driven groups (e.g., Nusselt number).

## Homogeneous-vs-Separated Model Choice (Multiphase Flow)
**When to use**: computing two-phase pressure drop.
**How**: identify the flow regime first (via a regime map matched to orientation); if well-mixed/dispersed (bubbly, mist), use the homogeneous model (averaged ρ, μ into single-phase correlations); if clearly separated (stratified, annular), use Lockhart-Martinelli two-phase multipliers instead.
**Trade-offs**: both are curve-fits, not first-principles models — no averaged-viscosity friction correlation is experimentally validated for two-phase flow; regime maps (Taitel-Dukler) are non-universal (fail under microgravity).

## Direct Integration over Center-of-Pressure Formulas (Curved Surfaces)
**When to use**: force/moment on curved or irregular (polynomial-boundary) submerged surfaces.
**How**: integrate dF and dM directly around the actual geometry rather than computing a centroid, moment of inertia, and center-of-pressure offset.
**Trade-offs**: the indirect (centroid + I_xx) method is standard and fast for simple flat shapes, but direct integration is often less error-prone and less laborious for curved/irregular boundaries.
