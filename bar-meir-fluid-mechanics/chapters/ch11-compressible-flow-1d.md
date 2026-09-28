# Chapter 11: Compressible Flow One Dimensional

## Core Idea
When a gas moves at a speed comparable to its own speed of sound, area changes, friction, and heat addition stop behaving like their incompressible counterparts and can instead force the flow into sudden discontinuities (shocks) or a hard ceiling on flow rate (choking) — and a handful of dimensionless models (isentropic, normal shock, Fanno, Rayleigh) let you predict exactly when and how.

## Frameworks Introduced

- **Speed of Sound, c = sqrt(dP/drho)|s**: the propagation speed of an infinitesimal pressure pulse, derived from a mass+energy (or momentum) balance on a control volume riding with the pulse.
  - When to use: any time you need to know whether a flow is "fast" relative to the medium.
  - How: for an ideal gas, c = sqrt(k R T) (depends only on temperature); for liquids/solids, c = sqrt(B_T/rho) using the bulk/elastic modulus — liquids run ~3-5x faster than gases, solids faster still.

- **Mach Number, M = U/c**: the ratio of local flow velocity to local speed of sound; the single parameter that governs whether compressibility effects matter.
  - When to use: as the primary independent variable for every model in this chapter.
  - How: M < 1 subsonic (area/pressure behave "normally"), M = 1 sonic/choked (critical, denoted with superscript *), M > 1 supersonic (area/pressure behave in reverse of intuition).

- **Isentropic Stagnation Relations**: link static properties to the theoretical fully-decelerated (stagnation, subscript 0) state for adiabatic, frictionless flow.
  - When to use: nozzles, diffusers, any flow where you know reservoir conditions and want local conditions (or vice versa).
  - How: T0/T = 1 + (k-1)/2 M^2; P0/P = (T0/T)^(k/(k-1)); rho0/rho = (T0/T)^(1/(k-1)).

- **Area-Mach Number Relation (converging-diverging nozzle behavior)**: dA/A = (M^2-1)/[M(1+(k-1)/2 M^2)] dM.
  - When to use: designing or analyzing a nozzle/diffuser to reach or exceed sonic velocity.
  - How: subsonic flow needs a converging area to accelerate (like incompressible flow); supersonic flow needs a diverging area to accelerate (opposite of incompressible intuition); M=1 can occur only at a minimum area ("throat"), though dA=0 does not guarantee M=1.

- **Choked Flow / Critical (*) Conditions**: the state where M=1; once the throat is choked, no downstream (back-pressure) change can increase the mass flow rate further.
  - When to use: nozzle mass-flow-rate limits, Fanno/Rayleigh maximum-length or maximum-heat problems.
  - How: identify the * properties (T*, P*, rho*, A*) from the k-only star relationships; once flow reaches M=1 at a throat, downstream conditions become irrelevant to upstream conditions.

- **Mass Flow Rate Ratio / Fliegner's Formula**: A/A* = (1/M)[(1+(k-1)/2 M^2)/((k+1)/2)]^(-(k+1)/(2(k-1))); maximum (choked) flow rate at M=1 gives (m_dot sqrt(T0))/(A* P0) = 0.0404 sqrt(k/R) (≈0.040418 for air).
  - When to use: computing maximum possible mass flow through a given throat area and stagnation state.
  - How: derived by requiring d(m_dot/A)/dM = 0, which occurs exactly at M=1 — independent of downstream geometry.

- **Impulse Function, F = PA(1+kM^2)**: a Mach-number-only function (with F* at M=1) used to compute net thrust/force on a duct or nozzle without tracking momentum flux directly.
  - When to use: net-force problems on nozzles, diffusers, or duct sections (e.g., rocket/converging-nozzle thrust).
  - How: F_net = P0 A* (1+k) [(k+1)/2]^(k/(k-1)) (F2/F* - F1/F*).

- **Normal Shock Relations**: a near-discontinuous jump from supersonic to subsonic flow satisfying mass, momentum, and energy conservation but NOT isentropic (entropy increases — the process is irreversible).
  - When to use: whenever M>1 flow must adjust to a higher downstream pressure (converging-diverging nozzle back-pressure mismatch, supersonic inlets, blast waves).
  - How: P_y/P_x = (2k M_x^2-(k-1))/(k+1); rho_y/rho_x = U_x/U_y = (k+1)M_x^2/((k-1)M_x^2+2); M_y^2 = ((k-1)M_x^2+2)/(2k M_x^2-(k-1)); as M_x→∞, M_y^2 → (k-1)/(2k) (finite floor, e.g. ~0.378 for k=1.4).

- **Prandtl's Relation / Star Mach Number**: M*_x · M*_y = 1 (using M* = U/c*, referenced to the constant critical sound speed c* rather than the discontinuous local c) — the cleanest statement of the shock jump condition.
  - When to use: converting across a shock without needing local temperature on each side separately.
  - How: c* = sqrt(kR·2T0/(k+1)); since U_x U_y = c*^2, a supersonic M*_x>1 upstream always maps to subsonic M*_y<1 downstream.

- **Fanno Flow**: adiabatic flow in a constant-area duct with friction (no heat transfer) — friction alone drives the Mach number toward 1 regardless of whether the flow starts subsonic or supersonic.
  - When to use: flow through pipes/ducts too short or well-insulated for significant heat transfer, but long/rough enough that friction matters (most pipe-flow compressible problems).
  - How: governing variable is the dimensionless friction length 4fL/D; solved via the Fanno line (T-s or P-v locus of all states with the same mass flux and stagnation enthalpy) and the working equation 4fL_max/D = (1-M^2)/(kM^2) + (k+1)/(2k) ln[((k+1)/2)M^2 / (1+(k-1)/2 M^2)].

- **Isothermal Flow**: flow in a constant-area duct with both friction and enough heat transfer to hold temperature constant (long, poorly-insulated pipelines) — a bounding/limiting case distinct from Fanno flow.
  - When to use: long pipelines (e.g., natural gas transmission) where wall heat exchange keeps T essentially constant, and the Fanno adiabatic assumption is invalid.
  - How: choking occurs at M = 1/sqrt(k) (not M=1); working equation 4fL_max/D = (1-kM^2)/(kM^2) + ln(kM^2).

- **Rayleigh Flow**: frictionless flow in a constant-area duct with heat addition or removal (combustion, condensation) — heat addition alone drives M toward 1.
  - When to use: combustion chambers, flow with chemical reaction or significant heat exchange but negligible wall friction.
  - How: governing variable is heat added; pressure ratio P2/P1 = (1+kM1^2)/(1+kM2^2); heating always pushes M toward 1 (accelerates subsonic, decelerates supersonic); cooling does the opposite; maximum stagnation temperature occurs at M=1/sqrt(k), not at M=1 — maximum entropy (choking) is at M=1.

## Key Concepts
- **Stagnation (Total) State**: the hypothetical state reached by isentropically decelerating the flow to zero velocity; denoted by subscript 0; T0 and P0 are constant along an adiabatic, frictionless flow.
- **Perfect Gas**: an ideal gas with constant specific heats Cp, Cv; assumed throughout this chapter for tractable closed-form relations.
- **Critical (Star) Condition**: the state at M=1, used as a fixed reference point (T*, P*, rho*, A*, c*) since ratios to it depend on k alone.
- **Choking**: the phenomenon where a downstream condition beyond some critical value no longer affects the upstream flow — the flow becomes "deaf" to further downstream changes.
- **Throat**: the minimum cross-sectional area of a converging-diverging nozzle; the only location where M=1 can occur (though M=1 there is not guaranteed).
- **Hydraulic Diameter, D_H**: 4×(cross-sectional area)/(wetted perimeter); generalizes pipe-flow relations to non-circular ducts.
- **Fanning Friction Factor, f**: f = tau_w / (½ ρU²), the dimensionless wall shear stress used in the Fanno/isothermal working equations (note: differs by a factor of 4 from the Darcy friction factor, hence "4fL/D").
- **4fL/D (dimensionless friction length)**: the single lumped parameter that determines Fanno/isothermal flow state changes along a duct, analogous to "how much friction has acted so far."
- **Shock (Rankine-Hugoniot) Jump**: the irreversible transition satisfying mass/momentum/energy but with an entropy increase; stagnation pressure always drops across a shock (P0y < P0x) even though stagnation temperature is unchanged.
- **Wave (Shock) Drag**: the drag force arising specifically from a moving (unsteady) shock transferring momentum to a moving body — does not exist for a stationary shock.
- **Impulse Function, F = PA(1+kM²)**: a device-independent, Mach-number-only bookkeeping tool for net forces on ducts/nozzles.
- **Fliegner's Number, Fn**: a dimensionless form of the maximum (choked) mass flow rate, Fn = kM(1+(k-1)/2 M²)^(-(k+1)/(2(k-1))), maximized at M=1.
- **T-s (Fanno/Rayleigh) Line**: the locus of all thermodynamic states reachable from a given inlet state under the Fanno (constant mass flux + stagnation enthalpy) or Rayleigh (constant mass flux + momentum) constraints; the point of maximum entropy on each line is M=1.
- **Double Choking**: in a converging-diverging nozzle feeding a Fanno duct, both the nozzle throat AND (independently) the duct exit can be choked simultaneously, fixing mass flow rate over a whole range of duct lengths.

## Mental Models
- Use the **Mach number as the master switch**: below M≈0.3 treat the flow as effectively incompressible; as M→1, treat area, pressure, and velocity relationships as fundamentally reversed from the incompressible intuition you've built elsewhere in the book.
- Think of **choking as a one-way valve**: once M=1 is reached at the controlling section (throat, or duct exit under enough friction/heat), information about further downstream reductions in pressure simply cannot propagate upstream (it would have to travel faster than the local flow, which is already sonic).
- Think of the **normal shock as "instantaneous Fanno+Rayleigh done in zero length"**: it satisfies the same mass/momentum/energy equations, jumps from supersonic to subsonic, and increases entropy — treat it as a discontinuous boundary condition, never solve "through" it with continuous isentropic relations.
- Use **Fanno vs. Rayleigh vs. Isothermal as three orthogonal "which effect dominates" bins**: friction-only-adiabatic (Fanno), heat-only-frictionless (Rayleigh), or friction-with-enough-heat-transfer-to-hold-T-constant (isothermal, the long-pipeline limit) — always ask which physical mechanism (friction or heat) is actually present before picking a model.
- Use **the "*'d" quantities as your universal ruler**: because ratios to the M=1 critical state depend only on k, always convert both known and unknown points to their star-ratios first, then combine — this is how the tables/Potto-GDC approach systematically solves two-point problems.

## Anti-patterns
- **Assuming dA=0 implies M=1**: the converse is false — a duct can have zero area change with dM=0 while still fully subsonic (or fully supersonic); only M=1 forces dA=0, not the reverse.
- **Applying isentropic relations across a shock**: a shock is irreversible (entropy strictly increases); using P0/P or T0/T isentropic tables "through" the shock location silently gives wrong answers — always switch to explicit shock relations at the shock plane.
- **Widening a choked nozzle/orifice to reduce force or increase flow ("naughty professor"/syringe problem)**: once flow is choked, increasing exit area downstream of the throat does not raise mass flow rate; for force reduction in a choked syringe, decreasing (not increasing) the plunger diameter is what actually reduces the required force, because force scales with the choked cross-sectional area.
- **Using the Fanno model for a long, poorly-insulated pipeline**: real long pipelines exchange enough heat with the environment that temperature stays roughly constant — this is the isothermal-flow regime (choking at M=1/√k), and Fanno's adiabatic assumption (choking at M=1) overstates the achievable Mach number.
- **Ignoring the entrance velocity / treating stagnation conditions as the pipe inlet static conditions**: forgetting that the reservoir's T0, P0 differ from the actual pipe-entrance static T, P (which depend on the entrance Mach number) is a common setup error in nozzle-feeding-a-duct problems.
- **Believing higher upstream Mach number always gives arbitrarily higher post-shock temperature/pressure ratios**: downstream Mach number M_y has a hard floor as M_x→∞ (M_y² → (k-1)/(2k)), and pressure/density/temperature ratios asymptote to finite multiples of M_x²/M_x — not unbounded in the way naive scaling might suggest.
- **Explaining wave/shock drag via a naive fixed control volume with unchanged area**: a commonly reproduced textbook explanation of shock drag ignores that the isentropic expansion downstream changes the control volume's width; the simple "just a momentum change with U1>U2" argument is actually backwards (U1<U2 relative to the body) and misses the volume's expansion.

## Key Equations
- `c = sqrt(k R T)` — ideal gas speed of sound; depends only on absolute temperature and gas properties (k, R).
- `M = U / c` — Mach number, the flow's local velocity ratio to local sound speed.
- `T0/T = 1 + (k-1)/2 * M^2` — isentropic stagnation temperature ratio; the backbone relation from which pressure/density ratios follow.
- `P0/P = (1 + (k-1)/2 * M^2)^(k/(k-1))` — isentropic stagnation pressure ratio.
- `dA/A = (M^2 - 1)/(M*(1+(k-1)/2*M^2)) * dM` — area-Mach relation; sign of (M²−1) controls whether area and Mach number move together or oppositely.
- `A/A* = (1/M) * [(1+(k-1)/2*M^2)/((k+1)/2)]^(-(k+1)/(2(k-1)))` — mass flow rate (area) ratio to the choked/throat area; used to size nozzles for a target Mach number.
- `P_y/P_x = (2k*M_x^2 - (k-1)) / (k+1)` — normal shock static pressure ratio (Rankine-Hugoniot).
- `M_y^2 = ((k-1)*M_x^2 + 2) / (2k*M_x^2 - (k-1))` — normal shock downstream Mach number from upstream Mach number.
- `M*_x * M*_y = 1` — Prandtl's relation across a normal shock, using the star (critical-speed-referenced) Mach numbers.
- `4fL_max/D = (1-M^2)/(k*M^2) + (k+1)/(2k) * ln[((k+1)/2*M^2)/(1+(k-1)/2*M^2)]` — Fanno flow: maximum dimensionless friction length to reach choking (M=1) from a given M.
- `4fL_max/D = (1-k*M^2)/(k*M^2) + ln(k*M^2)` — isothermal flow analogue of the Fanno choking-length relation; choking occurs at M=1/sqrt(k), not M=1.
- `P2/P1 = (1 + k*M1^2) / (1 + k*M2^2)` — Rayleigh flow static pressure ratio between any two points (heat addition/removal, constant area, no friction).
- `(m_dot * sqrt(T0)) / (A* * P0) = 0.0404 * sqrt(k/R)` — Fliegner's formula: the maximum (choked) mass flow rate per unit throat area for given stagnation conditions.

## Reference Tables

| Model | Held Constant | Driving Variable | Governing Equations Used | Choking Condition | Typical Use Case |
|---|---|---|---|---|---|
| **Isentropic** (variable area) | Entropy (s), stagnation T0 & P0 | Cross-sectional area A | Mass, energy, isentropic state relations | M=1 only possible at minimum-area throat | Converging-diverging nozzles, diffusers, venturi |
| **Normal Shock** | Mass flux, momentum, stagnation enthalpy (T0) — NOT entropy or P0 | None (discontinuous, zero-length) | Mass, momentum, energy (Rankine-Hugoniot) | Always transitions supersonic→subsonic | Nozzle back-pressure mismatch, supersonic inlets |
| **Fanno** (friction, adiabatic) | Area (constant), mass flux, stagnation enthalpy (T0) | Friction length 4fL/D | Mass, momentum (with wall shear), adiabatic energy | M=1 at maximum 4fL/D | Short/insulated pipe runs, nozzle-feeding ducts |
| **Isothermal** (friction + heat, const. T) | Area (constant), mass flux, static temperature T | Friction length 4fL/D | Mass, momentum (with wall shear), isothermal state | M=1/sqrt(k) | Long, poorly-insulated pipelines (e.g., natural gas transport) |
| **Rayleigh** (heat addition, frictionless) | Area (constant), mass flux, momentum | Heat added/removed Q | Mass, frictionless momentum, energy with Q | M=1 (max entropy); max T0 at M=1/sqrt(k) | Combustion chambers, flow with chemical reaction |

## Worked Example

**Isentropic nozzle sizing (Example 11.3 style).** Air leaves a reservoir at T0=294 K, P0=5 MPa, with mass flow rate 1 kg/s. At a downstream point the static pressure is measured as 3 MPa. Find M, velocity, and area there (k=1.4).
1. Compute P/P0 = 3/5 = 0.6.
2. Look up (or solve) the isentropic table at P/P0=0.6: M ≈ 0.886, T/T0 ≈ 0.864, rho/rho0 ≈ 0.694, A/A* ≈ 1.01.
3. Static temperature: T = 0.864 × 294 ≈ 254 K.
4. Density: rho = 0.694 × P0/(R T0) ≈ 41.1 kg/m³.
5. Velocity: U = M·sqrt(kRT) = 0.886 × sqrt(1.4×287×254) ≈ 283 m/s.
6. Area from mass conservation: A = m_dot/(rho U) ≈ 8.26×10⁻⁵ m² (~1 cm diameter tube).

**Normal shock (Example 11.12 style).** Air at M_x=3, P_x=0.5 bar (worked with 1.5 bar in source), T_x=273 K crosses a normal shock (k=1.4).
1. From isentropic table at M_x=3: P_x/P0x = 0.02722 → P0x = P_x/0.02722.
2. c_x = sqrt(1.4×287×273) ≈ 331 m/s → U_x = 3×331 ≈ 994 m/s.
3. From shock table at M_x=3: M_y=0.475, T_y/T_x=2.679, rho_y/rho_x=3.857, P_y/P_x=10.33, P0y/P0x=0.328.
4. U_y = U_x/(rho_y/rho_x) ≈ 994/3.857 ≈ 258 m/s.
5. P0y = 0.328 × P0x — the drop in stagnation pressure across the shock is the direct measure of the irreversible loss.

## Key Takeaways
1. Mach number, not velocity itself, is the parameter that determines whether area, pressure, and friction behave "normally" (subsonic, like incompressible flow) or in reverse (supersonic).
2. Choking is a one-way informational barrier: once M=1 is reached at a controlling section, no further downstream pressure reduction can increase mass flow rate.
3. A converging-diverging (de Laval) nozzle is required to accelerate a gas from subsonic through M=1 to supersonic; the throat is a necessary but not sufficient location for M=1.
4. A normal shock is irreversible — always jumps supersonic to subsonic, conserves mass/momentum/(stagnation) energy but not entropy, and always decreases stagnation pressure.
5. Fanno flow (friction, no heat transfer) and Rayleigh flow (heat, no friction) are two independent "pure" idealizations; isothermal flow is a third, hybrid limiting case relevant for long pipelines.
6. Both friction (Fanno) and heat addition (Rayleigh) independently drive the Mach number toward 1 — they are two different physical routes to the same choking endpoint.
7. Downstream Mach number after a shock has a hard floor (M_y² → (k-1)/(2k) as M_x→∞); shock relations do not scale unboundedly with upstream Mach number.
8. The "star" (critical, M=1) state is the universal reference point across all four models — ratios to it depend only on k, making it the natural pivot for solving two-point problems.
9. Compressible-flow intuition is frequently the opposite of incompressible intuition (e.g., decreasing an orifice diameter reduces choked-flow force; diverging area accelerates supersonic flow) — always re-derive from the governing equations rather than trusting incompressible reflexes.
10. Wave/shock drag exists only for moving (unsteady) shocks, not stationary ones — a subtlety that trips up even some published textbook explanations.

## Connects To
- **Ch 9**: This chapter's use of Mach number as the key parameter builds directly on the dimensional analysis / dimensionless-groups framework (Mach, Reynolds, etc.) introduced there.
- **Ch 12 (external/two-dimensional compressible flow, oblique shocks)**: normal shocks here are the limiting case (zero deflection angle) of the oblique shocks treated in the next chapter; wave drag concepts extend directly.
- **Bernoulli's Equation / Energy Equation**: the incompressible energy equation used throughout the book is generalized here into the stagnation-enthalpy form for compressible, adiabatic flow.
- **Second Law of Thermodynamics**: used explicitly to prove shocks must be supersonic→subsonic (entropy cannot decrease), and to identify the maximum-entropy point (M=1) on Fanno/Rayleigh lines.
- **Perfect Gas / Ideal Gas Law**: every closed-form relation in this chapter (isentropic ratios, shock relations, Fanno/Rayleigh equations) assumes the ideal/perfect gas equation of state P = ρRT with constant k.
