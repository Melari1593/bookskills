# Chapter 12: Compressible Flow 2-Dimensional

## Core Idea
When a supersonic flow meets a solid boundary that turns *into* the flow, the flow adjusts through an **oblique shock** (abrupt compression); when the boundary turns *away* from the flow, it adjusts through a **Prandtl–Meyer expansion fan** (smooth, isentropic acceleration) — together these two building blocks (plus their combination, "shock-expansion theory") let you compute pressure, lift, and drag on any two-dimensional supersonic body, and they explain why, unlike d'Alembert's inviscid-incompressible result, a supersonic body always experiences **wave drag**.

## Frameworks Introduced

- **Oblique shock relations (Rankine-Hugoniot generalized with a wall/wave angle theta)**: A shock inclined at angle theta to the upstream flow only "sees" the velocity component normal to itself, M1n = M1 sin(theta); that normal component obeys ordinary normal-shock relations, while the tangential velocity component is unchanged across the shock. The deflection angle delta (how much the flow turns) is related to M1 and theta by the theta-delta-M relation:
  cot(delta) = tan(theta) * [ (k+1) M1^2 / (2 (M1^2 sin^2(theta) - 1)) - 1 ]
  - When to use: Any supersonic flow turned *into* itself by a wedge, ramp, cone-like body, or compression corner.
  - How: Given M1 and the physical deflection delta (or a measured wave angle theta), solve the theta-delta-M relation (or the equivalent cubic in x = sin^2(theta)) for theta; then treat M1n = M1 sin(theta) as the upstream Mach number of an ordinary normal shock to get pressure/density/temperature/Mach-number jumps; recover the downstream Mach number as M2 = M2n / sin(theta - delta).

- **The governing cubic / weak vs. strong shock solution**: For given M1 and delta, theta satisfies a cubic x^3 + a1 x^2 + a2 x + a3 = 0 in x = sin^2(theta), with a1, a2, a3 functions of M1, delta, k. Depending on the discriminant D = Q^3 + R^2, either no physical solution exists (D>0, detached shock), or two physically realizable roots exist (D<0): the **weak solution** (smaller theta, flow usually stays supersonic downstream) and the **strong solution** (larger theta, flow always subsonic downstream, larger entropy increase). A third mathematical root exists but is thermodynamically unrealizable (entropy-decreasing) and never occurs in steady state.
  - When to use: Whenever you must decide which of the two physically possible shock angles actually occurs for a given wedge/deflection.
  - How: For an attached shock on a finite wedge in unconfined flow, the **weak solution is almost always the one observed** (a real wedge/cone photo or measurement is essentially always the weak shock, confirmed because measured theta < ~60-65 degrees); the strong solution requires an additional downstream boundary condition (e.g., high back pressure) to be enforced.

- **Maximum deflection angle / detachment condition**: For a fixed M1, there is a maximum deflection angle delta_max beyond which D>0 and no attached oblique shock solution exists at all — the wedge angle has become too large for the flow to turn while staying attached.
  - When to use: Predicting whether a wedge/cone at a given Mach number will produce an attached oblique shock or a detached bow shock standing off the body.
  - How: Set D = Q^3+R^2 = 0 for the given M1 to find delta_max and the corresponding theta_max; if the actual body deflection angle exceeds delta_max, the flow instead forms a detached (curved, standing-off) normal-ish shock ahead of the body — the "sees the obstacle as a blunt body" regime.

- **Prandtl–Meyer expansion (isentropic simple wave)**: When a supersonic flow turns *away* from itself (convex corner), it accelerates smoothly and isentropically through an infinite fan of Mach waves, with each Mach line inclined at the local Mach angle mu = sin^-1(1/M). The turning (Prandtl-Meyer) angle nu(M) is a function of Mach number alone (for fixed k):
  nu(M) = sqrt((k+1)/(k-1)) * tan^-1( sqrt((k-1)/(k+1)) * sqrt(M^2-1) ) - tan^-1( sqrt(M^2-1) )
  with the constant chosen so nu = 0 at M = 1.
  - When to use: Flow rounding a convex corner, over the shoulder/trailing edge of an airfoil, or a supersonic jet expanding to match a lower ambient pressure.
  - How: Compute nu(M1) from the incoming Mach number, add the physical turning angle (delta, positive when turning away from the flow) to get nu(M2) = nu(M1) + delta, then invert nu(M) (via tables, Potto-GDC, or numerically) to find M2; all other properties (P/P0, T/T0, rho/rho0, mu) follow from the isentropic relations at M2.

- **Maximum turning angle**: The Prandtl-Meyer function has an absolute maximum nu_infinity = (pi/2) * [sqrt((k+1)/(k-1)) - 1], reached as M starts at 1 and accelerates toward infinity.
  - When to use: Checking whether a prescribed expansion (e.g., to vacuum) is physically achievable via this model.
  - How: If the required turning angle would exceed nu_infinity (i.e., demands M -> infinity or beyond), the isentropic simple-wave model breaks down; beyond that limit the flow cannot continue as an attached expansion and effectively behaves as if a maximum angle has been reached, degenerating into a vortex-like/separated region.

- **Shock-expansion theory (combining oblique shocks and Prandtl-Meyer fans)**: A finite-thickness or angle-of-attack 2-D body (diamond airfoil, flat plate at incidence) is analyzed by breaking its surface into flat panels; each convex corner is a Prandtl-Meyer expansion, each concave/leading corner is an oblique shock, and the flow field between panels is uniform. Lift and drag are obtained by integrating (i.e., summing, since each panel has uniform pressure) the local static pressure over the projected areas.
  - When to use: Computing lift/drag coefficients of thin supersonic airfoils (diamond/wedge sections, flat plates at angle of attack).
  - How: Work forward panel by panel from the known freestream state, applying the oblique-shock relations at compression corners and the Prandtl-Meyer relation at expansion corners; match static pressure (not stagnation pressure) across any slip line/wake, since stagnation pressure differs between streams that crossed shocks of different strength.

## Key Concepts
- **Wave angle (theta) vs. deflection angle (delta)**: theta is the angle of the shock front itself relative to the upstream flow; delta is the angle by which the flow direction actually changes — they are related but distinct, and the oblique-shock relations connect M1, theta, and delta.
- **Weak vs. strong oblique shock**: two mathematically valid downstream states for the same M1 and delta; the weak shock (smaller theta, often supersonic exit) is what is normally realized on an unconfined wedge, while the strong shock (larger theta, always subsonic exit, larger entropy rise) requires special downstream conditions.
- **Detached shock**: When the required deflection exceeds delta_max for the given M1, no attached oblique shock exists; a curved, standing-off shock forms ahead of the body instead, transitioning from normal (at the centerline) to oblique further out.
- **Mach angle (mu)**: mu = sin^-1(1/M), the angle at which an infinitesimal disturbance (Mach wave) propagates in a supersonic stream; the geometric basis of the Prandtl-Meyer derivation.
- **Prandtl-Meyer function nu(M)**: A one-to-one (monotonic) function of Mach number giving the cumulative isentropic turning angle needed to accelerate a flow from M=1 up to M; used as a lookup/inversion tool for expansion-fan problems.
- **Slip line / slip condition**: The interface downstream of a lifting or asymmetric body across which pressure and flow direction must match on both sides, but where Mach number, density, and stagnation pressure may differ because the two streams passed through shocks/expansions of different strength.
- **Zero-inclination stability question**: A key theoretical issue addressed in the chapter — whether an oblique shock or a Mach wave (or neither) can exist right at zero deflection angle; the chapter's conclusion is that neither a persistent Mach wave nor an oblique shock is physically stable exactly at delta=0, because of boundary-layer smoothing and non-physical "perfect wall" assumptions, so the region near zero inclination is treated as a no-change zone.
- **Wave drag**: Drag arising purely from the pressure difference the shock/expansion pattern creates on the front vs. rear of a supersonic body, present even in a strictly inviscid gas (unlike the classical d'Alembert result for incompressible potential flow).

## Mental Models
- Think of an oblique shock as "a normal shock that only feels part of the velocity": decompose the upstream velocity into components normal and tangential to the shock, apply ordinary 1-D normal-shock jump relations to the normal component only, and simply carry the tangential component through unchanged.
- Use the weak-solution-by-default heuristic: for a real, unconfined wedge or cone, always start by assuming the weak shock is what is physically realized — reach for the strong solution only when a downstream boundary condition (duct back-pressure, blunt-body stagnation region) explicitly forces it.
- Think of Prandtl-Meyer expansion as "the mirror image of an oblique shock, made infinitely gradual and isentropic": both are wall-turning phenomena parameterized by a Mach-number function, but compression concentrates into a single discontinuous jump while expansion spreads into a smooth fan of Mach lines because compression waves would otherwise coalesce (creating entropy) while expansion waves diverge and never coalesce.
- Use shock-expansion theory as "state bookkeeping panel by panel": march along the body surface, and at each corner apply exactly one of two operators — oblique-shock-jump (compression) or Prandtl-Meyer-turn (expansion) — to update the local uniform flow state, then compute forces from the resulting piecewise-constant pressure distribution.

## Anti-patterns
- **Assuming the strong shock solution applies to a simple wedge/cone in free flow**: The strong solution requires additional constraints; a bare wedge or cone in an otherwise unconfined supersonic stream produces the weak shock (this is why measured shock angles in schlieren/shadowgraph photos of cones and wedges are consistently the smaller, weak-shock angle, not the larger one).
- **Assuming a Mach wave or oblique shock persists exactly at zero deflection angle**: The chapter shows this is not physically realizable in a real (viscous, imperfect-wall) flow; treat the zone near delta=0 as unchanged flow unless another boundary condition explicitly forces a shock.
- **Using stagnation pressure instead of static pressure to match conditions across a slip line**: Across a slip line downstream of asymmetric shocks/expansions, static pressure and flow direction must match, but stagnation pressure generally differs between the two streams (each has lost a different amount to its own shock/expansion history) — matching total pressure instead of static pressure gives the wrong downstream state.
- **Ignoring the maximum deflection angle and forcing an oblique-shock calculation past delta_max**: Beyond delta_max for the given M1, D becomes positive and there is no real oblique-shock solution; physically the shock detaches and stands off the body — continuing to solve the oblique-shock cubic in this regime yields meaningless (complex/unphysical) results.
- **Assuming the Prandtl-Meyer turning point can be a mathematically sharp corner with no boundary-layer accommodation**: The rigorous solution requires infinite (or very large) radial velocity right at the corner, which is unphysical; in practice the author recommends applying the expansion-fan model only outside roughly 2-4 boundary-layer thicknesses from the actual corner, treating the transition as smoothed rather than perfectly sharp.
- **Forgetting that oblique-shock/expansion-fan calculations assume a perfect (calorically ideal) gas with constant k**: The maximum-deflection-angle table and closed-form relations in this chapter are computed for a perfect gas; real high-temperature or unusual equation-of-state gases (per Henderson and Menikoff's extension) require different maximum-deflection calculations.

## Key Equations
1. **theta-delta-M1 relation (oblique shock)**: cot(delta) = tan(theta) [ (k+1)M1^2 / (2(M1^2 sin^2(theta)-1)) - 1 ]. The central relation linking upstream Mach number, wave angle, and flow-turning angle for any oblique shock.
2. **Pressure ratio across an oblique shock**: P2/P1 = [2k M1^2 sin^2(theta) - (k-1)] / (k+1). Identical in form to the normal-shock pressure ratio but using only the normal Mach number component M1 sin(theta).
3. **Density ratio across an oblique shock**: rho2/rho1 = (k+1) M1^2 sin^2(theta) / [ (k-1) M1^2 sin^2(theta) + 2 ]. Governs the normal-velocity-component jump (U1n/U2n).
4. **Downstream Mach number relation**: M2^2 sin^2(theta - delta) = [ (k-1) M1^2 sin^2(theta) + 2 ] / [ 2k M1^2 sin^2(theta) - (k-1) ]. Gives the normal Mach number squared downstream; divide appropriately by sin(theta - delta) to recover the full M2.
5. **Stagnation pressure ratio across an oblique shock**: P02/P01 = [ (k+1) M1^2 sin^2(theta) / ((k-1) M1^2 sin^2(theta)+2) ]^(k/(k-1)) * [ (k+1) / (2k M1^2 sin^2(theta) - (k-1)) ]^(1/(k-1)). Quantifies the entropy loss (irreversibility) through the shock — always less than 1.
6. **Prandtl-Meyer function**: nu(M) = sqrt((k+1)/(k-1)) tan^-1( sqrt((k-1)/(k+1)) sqrt(M^2-1) ) - tan^-1( sqrt(M^2-1) ), normalized so nu(1)=0. The core lookup function for expansion-fan problems: nu2 = nu1 + delta gives the new Mach number after a turn of delta degrees.
7. **Maximum (total) turning angle**: nu_infinity = (pi/2)[ sqrt((k+1)/(k-1)) - 1 ]. The absolute ceiling on how much a supersonic stream can turn via Prandtl-Meyer expansion starting from M=1.
8. **Mach angle**: mu = sin^-1(1/M) = tan^-1( 1/sqrt(M^2-1) ). Defines the direction of Mach (characteristic) lines, used throughout both oblique-shock geometry and Prandtl-Meyer fan construction.

## Reference Tables
Maximum deflection angle and corresponding wave angle vs. upstream Mach number (perfect gas, k=1.4) — selected rows from the chapter's table:

| M1 | M2 (at max) | delta_max (deg) | theta_max (deg) |
|----|------|------------|-------------|
| 1.1 | 0.9713 | 1.52 | 76.28 |
| 1.5 | 0.9217 | 12.11 | 66.57 |
| 2.0 | 0.9248 | 22.97 | 64.65 |
| 3.0 | 0.9544 | 34.07 | 65.23 |
| 4.0 | 0.9721 | 38.77 | 66.05 |
| 6.0 | 0.9871 | 42.44 | 66.90 |
| 10.0 | 0.9956 | 44.43 | 67.44 |

Note the non-monotonic theta_max (it dips to a minimum near M1 ~ 2.2 before rising again), while delta_max increases monotonically and saturates as M1 -> infinity (approaching just above 45 degrees for k=1.4).

## Worked Example
**Wedge at Mach 4 (based on Example 12.3)**: Air (k=1.4) at M1 = 4 approaches a wedge.

Step 1 — Maximum wedge angle: set D=0 for M1=4. Potto-GDC / the maximum-deflection table gives delta_max = 38.77 degrees at theta_max = 66.04 degrees, with the downstream (normal) Mach number M2 = 0.972 at that limiting condition. Any wedge half-angle larger than ~38.77 degrees at M1=4 cannot support an attached oblique shock — a detached bow shock forms instead.

Step 2 — Weak/strong solution for delta = 20 degrees: solving the governing cubic (or reading off the Potto-GDC oblique-shock table) for M1=4, delta=20 degrees gives two physical roots:
- Weak solution: theta_weak = 32.24 deg (0.5666 rad), downstream M2 (weak) = 2.5686.
- Strong solution: theta_strong = 83.85 deg (1.4635 rad), downstream M2 (strong) = 0.4852.

Step 3 — physical interpretation: for a real wedge of half-angle 20 degrees in unconfined M1=4 flow, the weak shock (theta ~ 32 deg, exit Mach ~2.57, supersonic) is what actually forms; the strong solution (nearly-normal shock, subsonic exit) would only occur if something downstream (e.g., a duct back-pressure) forced it.

This mirrors the chapter's cone example (Example 12.4): measuring a physical cone half-angle of 14.43 degrees and shock angle of 30.1 degrees on a schlieren photo, the back-calculated (wedge-equivalent) upstream Mach number is M1 ~ 3.23 — and because the measured wave angle (30.1 deg) is far below the ~60-65 degree strong-shock range, the shock is confidently identified as weak.

## Key Takeaways
1. An oblique shock is just a normal shock applied to the velocity component normal to the (inclined) shock front — the tangential component passes through unchanged, which is why the theta-delta-M relation and all the jump ratios reduce to normal-shock formulas evaluated at M1 sin(theta).
2. For a given M1 and delta there are generically two valid shock angles (weak and strong); on a real, unconfined wedge or cone, always default to the weak solution unless a specific downstream boundary condition justifies the strong one.
3. Beyond a Mach-number-dependent maximum deflection angle delta_max, no attached oblique shock solution exists at all — the flow instead forms a detached shock standing off the body.
4. Prandtl-Meyer expansion is the isentropic, smooth counterpart to the oblique shock: it turns supersonic flow away from itself through a continuous fan of Mach waves, governed by the single function nu(M), and — unlike compression — has no lower-angle instability and no "weak/strong" ambiguity, only an absolute maximum total turning angle nu_infinity.
5. Shock-expansion theory analyzes any thin 2-D supersonic body (diamond airfoils, flat plates at angle of attack) by chaining oblique-shock jumps at compression corners with Prandtl-Meyer turns at expansion corners, then integrating the resulting piecewise-uniform pressure field for lift and drag.
6. Even a perfectly inviscid supersonic flow produces nonzero drag (wave drag) on a body with thickness or lift — directly contradicting the classical (incompressible, subsonic) d'Alembert's Paradox of zero drag on a body in ideal flow.
7. Across a slip line separating streams that took different shock/expansion paths (e.g., upper vs. lower surface of a lifting plate), match static pressure and flow direction — not stagnation pressure, which will generally differ between the two streams.

## Connects To
- **Ch 11 (Normal Shock, implied)**: The oblique shock's normal-component analysis reduces exactly to the normal-shock relations from the 1-D compressible flow chapters — theta = 90 degrees recovers the normal shock as a special case.
- **Ch 5/6 (Isentropic Flow relations, implied)**: The Prandtl-Meyer expansion is fundamentally an application of the isentropic flow relations (P/P0, T/T0, rho/rho0 vs. Mach number) combined with the geometric turning-angle function nu(M).
- **Aerodynamics / airfoil design**: Shock-expansion theory here is the standard hand-calculation method (predating full CFD) for estimating lift, drag, and pressure distribution on thin supersonic airfoils and simple inlet/diffuser geometries.
- **d'Alembert's Paradox (classical inviscid hydrodynamics)**: This chapter explicitly contrasts the zero-drag result of incompressible potential flow theory with the always-present wave drag of supersonic flow, showing compressibility (not viscosity) as the source of drag here.
