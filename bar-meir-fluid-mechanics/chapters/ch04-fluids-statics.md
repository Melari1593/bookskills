# Chapter 4: Fluids Statics

## Core Idea
When a fluid is at rest (or moves as a rigid body with the container, as in linear or angular acceleration), the pressure field obeys a single balance law — the pressure gradient equals the effective body force per unit volume, `grad P = rho * g_eff` — and every result in the chapter (barometers, manometers, forces on dams, ship stability, surface tension, Rayleigh-Taylor instability) is a specialization of that one equation to a particular density model or a particular effective gravity.

## Frameworks Introduced

- **The Fluid Static Equation (Hydrostatic Equation)**: `grad P = rho * g_eff`, where `g_eff = g_gravity - a` combines true gravity with any body acceleration.
  - When to use: any fluid in mechanical equilibrium with itself, whether truly at rest or rigidly accelerating (linear or rotating) with its container.
  - How: identify `g_eff`, choose the coordinate whose axis is anti-parallel to `g_eff`, then integrate the one nontrivial component; the other two components give `P = constant` on planes perpendicular to `g_eff`.

- **Piezometric Pressure Relationship**: `P(h) - P0 = rho * g * h`, with `h` measured against the direction of `g_eff`.
  - When to use: constant-density fluid, no acceleration — the workhorse formula for manometers, tanks, and barometers.
  - How: pick a reference point of known pressure `P0`, measure vertical liquid-height difference `h` to the point of interest, multiply by `rho * g`.

- **Barometric Formulas for Compressible Fluids**: ideal gas isothermal column `P/P0 = exp(-g(z - z0)/(R*T))`; real-gas version replaces `R*T` with `Z*R*T`.
  - When to use: gas columns of significant height (atmosphere, gas-filled shafts) where density cannot be treated as constant.
  - How: substitute the ideal/real gas equation of state into the hydrostatic equation, separate variables in `dP/P`, and integrate.

- **Compressible-Liquid Density-Depth Relation**: from the bulk modulus definition `B_T = rho * dP/drho`, integrating the coupled density/hydrostatic equations gives `rho/rho0 = 1/sqrt(2*g*rho0*z/B_T + 1)`.
  - When to use: very deep liquid columns (oceans, deep wells) where "incompressible liquid" is no longer a good assumption.
  - How: solve the density ODE from the bulk-modulus definition together with `dP/dz = -rho*g` (Example 4.6 shows the full derivation via an integral equation).

- **Linear-Lapse-Rate Atmosphere**: with `T = T0 - Cx*h`, `P/P0 = ((T0 - Cx*h)/T0)^(g/(R*Cx))`.
  - When to use: modeling real atmospheric pressure decay where temperature falls linearly with height.
  - How: substitute `T(h)` into the ideal-gas hydrostatic equation and integrate; reduces to the isothermal exponential formula as `Cx -> 0`.

- **Atmospheric (Convective) Stability Criterion**: a displaced slab is stable only if `Cx < ((k-1)/k) * (g/R)` (using isentropic/adiabatic expansion of the displaced parcel vs. the ambient lapse rate).
  - When to use: deciding whether a stratified atmosphere (or any stratified gas column) will support convection.
  - How: compare the density of an adiabatically-displaced slab to the ambient density at the new height; stable if the displaced slab is always denser than its new surroundings.

- **Effective Gravity in Accelerated Systems**: linear acceleration gives `g_eff = a*i_hat + g*k_hat`, `|g_eff| = sqrt(g^2 + a^2)`, `tan(beta) = a/g`; rigid rotation gives `g_eff = -g*k_hat + omega^2*r*r_hat`, producing a **parabolic** free surface `z - z0 = omega^2*r^2/(2*g)`.
  - When to use: tanks on accelerating vehicles, or fluid in a rotating container (centrifuges, rotating U-tubes).
  - How: vector-sum true gravity and the (negative of the) container's acceleration to get `g_eff`; free/constant-pressure surfaces are always perpendicular to `g_eff`.

- **Hydrostatic Force and Center of Pressure on a Flat Submerged Surface**: `F = P_atmos*A + rho*g*sin(beta)*x_c*A`; center of pressure `x_p = x_c + I_xx/(x_c*A)` (and similarly for `y_p`), valid when `P0`/atmospheric contribution is stripped out.
  - When to use: dams, gates, tank walls — any planar surface at an angle `beta` to the free surface.
  - How: total force is density times gravity times the centroid depth times area (plus atmospheric term); the center of pressure is offset from the centroid by `I_xx/(x_c*A)`, always deeper than the centroid.

- **Forces on Curved Surfaces (decomposition method)**: `F_x, F_y` = integrals of pressure over the surface's projected areas in each direction; `F_z` = weight of the (real or virtual) fluid column above the surface, `F_z = integral of h*g*rho dA_z`.
  - When to use: curved dams, gates, and submerged/floating shapes where a single planar formula doesn't apply.
  - How: project the curved surface onto planes normal to each axis; horizontal components use the flat-surface formula on the projection, the vertical component equals the weight of fluid (real or imaginary, for "cut-out" shapes) directly above the surface up to the free surface.

- **Metacentric Height Stability Criterion**: a floating body is stable if `GM = BM - BG > 0`, i.e., the metacenter `M` lies above the center of gravity `G`; with a shifting liquid load, corrections subtract `I_xxB/V_B` type terms (from the free surface of liquid carried inside the body).
  - When to use: ship and floating-body stability analysis, including the effect of sloshing liquid cargo.
  - How: compute `BM = I_xx/V_displaced` about the waterplane, subtract `BG` (distance from buoyancy center to CG), then subtract further corrections for any internal free liquid surfaces (`sum I_xxbi/V_bi`); `GM > 0` required for stability, and the roll frequency scales as `sqrt(V*rho_s*GM / I_body)`.

- **Rayleigh-Taylor Instability Criterion**: a heavy fluid layer over a light one is stable against a disturbance of wavelength `L` only if `4*pi^2*sigma/L^2 > g*(rho_H - rho_L)`; the neutral (critical) wavelength is `L_c = sqrt(4*pi^2*sigma/(g*(rho_H - rho_L)))`.
  - When to use: any heavy-over-light stratified interface (die casting cavities, dense fluid over gas) to decide whether surface tension can hold the interface flat.
  - How: compare the surface-tension-driven restoring pressure at a cosine-shaped depression to the destabilizing buoyancy pressure difference; disturbances longer than `L_c` grow, shorter ones are damped.

## Key Concepts
- **Pressure gradient (`grad P`)**: the vector whose components are the spatial derivatives of pressure; in a static fluid it exactly balances the effective body force per unit volume.
- **Effective gravity (`g_eff`)**: the vector sum of true gravitational acceleration and the negative of any rigid-body (linear or angular) acceleration of the fluid's container.
- **Piezometric pressure**: the `rho*g*h` term added to a reference pressure to get local pressure in a constant-density fluid at rest.
- **Bulk modulus (`B_T`)**: `rho * dP/drho`, the measure of a liquid's resistance to compression, used to model density variation with depth in very deep or high-pressure liquid columns.
- **Compressibility factor (`Z`)**: correction to the ideal gas law (`P = Z*rho*R*T`) used in real-gas hydrostatic formulas, entering the barometric exponent as `h/Z`.
- **Lapse rate (`Cx`)**: the (assumed constant) rate of temperature decrease with height, `dT/dh = -Cx`, used to model realistic atmospheric pressure profiles.
- **Manometer (U-tube, inclined, inverted, "magnified")**: devices that infer pressure differences from measured liquid-column height differences; inclined and magnified designs increase the visible height change per unit pressure difference by using near-matched densities or a shallow tube angle.
- **Center of pressure**: the point on a submerged surface through which the resultant hydrostatic force effectively acts, always below (deeper than) the geometric centroid due to the `I_xx/(x_c*A)` offset.
- **Buoyancy center (`B`)**: the centroid of the displaced fluid volume; the point of application of the buoyant force.
- **Metacenter (`M`)** and **metacentric height (`GM`)**: `M` is the point where the buoyant-force line of action crosses the body's centerline during small tilts; `GM` is the distance from the center of gravity `G` to `M`, the key scalar measure of floating-body (rotational) stability.
- **Surface tension (`sigma`)**: the mathematically complex, force-per-length effect at fluid interfaces responsible for holding a needle afloat, forming barometer menisci, and stabilizing (or destabilizing) heavy-over-light interfaces.
- **Rayleigh-Taylor instability**: the unstable growth of interfacial disturbances when a heavier fluid sits above a lighter one and surface tension cannot supply enough restoring force.
- **Neutral frequency of a floating body**: the natural roll frequency `(1/2*pi)*sqrt(V*rho_s*GM/I_body)`, directly analogous to a pendulum's frequency, with `GM` playing the role of the pendulum length inverse.

## Mental Models
- Treat **every static-fluid problem as "find g_eff, then apply the same integration"** — linear acceleration, rotation, and plain gravity are not separate topics but the same equation with a different effective gravity vector.
- For **curved surfaces**, decompose into "horizontal components behave like flat, vertical surfaces (use projected area and centroid pressure)" and "the vertical component is just the weight of fluid above/below it" — direct integration of the actual geometry is often *simpler* than computing centers of pressure and moments of inertia, especially for irregular or polynomial-shaped boundaries (Example 4.18 shows the traditional method is far more laborious than direct integration).
- For **multi-layer fluids**, think of the total force/moment as a sum over layers, each contributing its own `rho_i * x_ci * A_i` term, with the "atmospheric" pressure at the top of each layer absorbing everything above it — this converts an apparently continuous-density problem into a piecewise-constant sum.
- For **stability (atmospheric or floating-body)**, think of a **displaced parcel/slab test**: perturb something slightly, compute whether the restoring force is toward or away from the original state, and the sign of that comparison (density difference, or `GM` sign) *is* the stability criterion — this single idea underlies both the atmospheric lapse-rate stability condition and the metacentric-height criterion for ships.

## Anti-patterns
- **Applying the pressure-center formulas (`x_p = x_c + I_xx/(x_c*A)`) with atmospheric pressure still present**: these formulas are derived assuming atmospheric pressure is neglected or cancels; including it without adjustment gives wrong centers of pressure.
- **Treating `dA_x` (the x-projection of a differential curved-surface element) and `A_x` (the total projected area) as interchangeable in intermediate steps**: they use different trigonometric factors (`cos(theta)` locally vs. `sin(theta_0)` for the whole projected height) — conflating them is a common source of sign/factor errors on curved-surface problems.
- **Assuming liquids are strictly incompressible at all depths**: at oceanic depths (kilometers), bulk-modulus corrections to density are non-negligible; using constant density silently discards a real, computable correction (Example 4.6 quantifies this).
- **Neglecting the gas density in ordinary U-tube manometers when the pressure difference is small**: for small `Delta-P` this approximation swamps the signal, which is exactly why "magnified" (matched-density) and inclined manometers were invented.
- **Using the free-expansion adiabatic-index (`k`) stability criterion as an exact threshold**: the chapter explicitly notes it only bounds a *range* around the neutral lapse rate; real gases require the polytropic index `n` and additional care near the boundary.
- **Computing floating-body `GM` while ignoring free liquid surfaces inside the body (fuel, ballast, cargo)**: any internal liquid with a free surface reduces effective `GM` by `I_xxb/V_b` terms; omitting shifting-load tanks overstates stability.
- **Ignoring the direction/sign convention of `dA`**: the chapter stresses `dA` is conventionally outward-positive; sign errors here propagate directly into force and moment integrals on curved and cut-out shapes.

## Key Equations
- `grad P = rho * g_eff` — the master hydrostatic equation; reduces to every other formula in the chapter for a specific `g_eff` and density model.
- `dP/dz = -rho*g` and `P(h) - P0 = rho*g*h` — constant-density fluid under plain gravity; `h` is height measured opposite `g`.
- `P/P0 = exp(-g*(z-z0)/(R*T))` — ideal-gas isothermal hydrostatic column (replace `R*T` with `Z*R*T` for real gas with constant compressibility `Z`).
- `rho/rho0 = 1/sqrt(2*g*rho0*z/B_T + 1)` — density vs. depth for a liquid with constant bulk modulus `B_T`.
- `P/P0 = ((T0 - Cx*h)/T0)^(g/(R*Cx))` — atmospheric pressure with a linear temperature lapse rate `Cx`.
- `Cx < ((k-1)/k)*(g/R)` — condition for atmospheric (convective) stability against small vertical displacements.
- `z - z0 = omega^2*r^2/(2*g)` — shape of the free surface in a rigidly rotating fluid (paraboloid); combined with `P - P0 = rho*g*[(z0-z) + omega^2*r^2/(2*g)]` for the full pressure field.
- `F = P_atmos*A + rho*g*sin(beta)*x_c*A` with `x_p = x_c + I_xx/(x_c*A)` — resultant force and center of pressure on an inclined flat submerged surface.
- `F_z = integral of h*g*rho dA_z` (vertical force on a curved surface = weight of fluid, real or virtual, above it); horizontal components from projected flat-surface formulas.
- `L_c = sqrt(4*pi^2*sigma/(g*(rho_H - rho_L)))` — critical (neutral-stability) wavelength for the Rayleigh-Taylor instability at a heavy-over-light interface.

## Worked Example

**1. Mercury barometer (Example 4.4).** A sealed tube full of mercury is inverted into a mercury reservoir; the space above the mercury column contains only mercury vapor at pressure `P_vapor`. Using the piezometric relationship at the reference point `a` at the reservoir surface: `P_a = rho*g*h + P_vapor`. With mercury density `rho = 13545.85 kg/m^3`, `g = 9.82 m/s^2`, column height `h = 0.76 m`, and `P_vapor = 0.000179264 kPa`: `P_a = 13545.85 * 9.82 * 0.76 ≈ 101095.4 Pa ≈ 1.01 bar`. The vapor-pressure term contributes only about `10^-4` percent of the total — which is precisely why mercury (very low vapor pressure, high density, liquid over a wide range) is the classical barometric fluid.

**2. Force and moment on a curved (arc) dam (Example 4.17).** A dam shaped as a circular arc of radius `r = 2 m`, spanning angle `theta0 = 45 deg`, width `b = 4 m`, holding water of `rho = 1000 kg/m^3` at `g = 9.8 m/s^2`. Horizontal force: treat it like a flat vertical projection — pressure at the centroid of the projected area times that area, `F_x = rho*g*b*r*sin^2(theta0)/2 ≈ 19,600 N`. Vertical force: the weight of the (virtual) fluid volume between the arc and the free surface, `F_y ≈ 22,375 N`, located via the arc-minus-triangle centroid (`y_c ≈ 0.348 m` from point O). Moment from the horizontal force uses its center of pressure (`x_p = 5*r*cos(theta0)/9`), giving `M_h ≈ 15,399 N·m`; the vertical force's moment is `M_v = y_c*F_y ≈ 7,792 N·m`; total moment about O `≈ 23,192 N·m`. The chapter emphasizes that direct integration of `dF` and `dM` around the arc (using the perpendicular-distance geometry) reproduces the same numbers with far less bookkeeping than computing centroids and moments of inertia — a general lesson for curved-surface problems.

## Key Takeaways
1. Every hydrostatic result in this chapter — barometers, manometers, tank forces, ship stability, Rayleigh-Taylor — is one equation, `grad P = rho*g_eff`, applied with a different `g_eff` or density model; master the master equation, not the individual formulas.
2. Constant-pressure surfaces are always planes (or curved surfaces) perpendicular to `g_eff`; in rotating systems this makes them paraboloids, not flat planes.
3. Manometer design is an exercise in maximizing sensitivity: neglecting the light-fluid (gas) density gives simple gauges, while matching densities closely ("magnified" manometers) or inclining the tube trades geometry for sensitivity when pressure differences are small.
4. Treating liquids as strictly incompressible breaks down at extreme depths (oceans, deep wells) — the bulk modulus correction is quantifiable and sometimes significant.
5. For curved or irregular surfaces, direct integration of force and moment is frequently simpler than computing centroids and moments of inertia for an indirect (center-of-pressure) calculation — especially for polynomial or otherwise non-standard shapes.
6. Floating-body stability reduces to a single sign check on `GM = BM - BG` (with corrections for internal free liquid surfaces); the same displaced-parcel logic gives the atmospheric convective-stability criterion.
7. Surface tension is a stabilizing mechanism at interfaces (holding needles afloat, resisting Rayleigh-Taylor growth for short wavelengths) but is overwhelmed by buoyancy forces beyond a computable critical length scale `L_c`.
8. Multi-layer and cut-out-shape problems are solved by superposition — sum per-layer or per-region contributions, folding everything "above" a layer into an effective atmospheric pressure for that layer.

## Connects To
- **Ch 1 (Introduction/Properties)**: bulk modulus, ideal/real gas equations of state, and compressibility factor `Z` used here for pressure-density relations are defined in the Introduction chapter.
- **Ch 9 (Dimensionless Numbers)**: several ratios introduced here informally (e.g., `G*r_b/(R*T)`, the Rayleigh-Taylor length scale) are formalized later as dimensionless groups.
- **Fundamentals of Compressible Flow (companion text by the same author)**: referenced directly for the speed-of-sound derivation used in Example 4.7 and for the isentropic-expansion assumption used in the atmospheric stability analysis.
- **Rigid-body dynamics**: the entire accelerated-system treatment (linear and angular) is explicitly framed as a generalization of the rigid-body mechanics the reader is assumed to already know.
- **Later fluid-dynamics chapters**: the "fluid element in equilibrium" derivation technique (surface forces + body forces = 0) is the direct ancestor of the momentum-balance derivations used once the fluid is allowed to move.
