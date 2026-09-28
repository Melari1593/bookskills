# Chapter 13: Multi-Phase Flow

## Core Idea
When two or more phases/materials flow together (gas-liquid, solid-liquid, solid-gas), the mixture organizes itself into distinct, geometrically-recognizable **flow regimes** (stratified, slug, annular, bubbly, mist, etc.) whose transitions depend on flow rates, orientation (horizontal/vertical/against-or-with gravity), and fluid properties — and because no single "averaged" property (viscosity, density) captures this behavior, engineers must either (a) identify the regime and apply a regime-specific model or (b) fall back on approximate homogeneous or separated-flow models.

## Frameworks Introduced
- **Homogeneous flow model**: Treat the two-phase mixture as a single pseudo-fluid with averaged density (rho_average), averaged viscosity (mu_m), and mixture velocity (U_m), then apply single-phase pressure-drop correlations (friction factor f = C*(rho_m*U_m*D/mu_m)^-n) to that pseudo-fluid.
  - When to use: When the phases are well-mixed (bubbly, mist, or finely dispersed flow) and no strong slip exists between phases (SLP ~ 1).
  - How: Compute rho_average = 1/(X/rho_G + (1-X)/rho_L) and one of the three suggested averaged viscosities (Dukler's volumetric-flow-weighted average, the harmonic/quality-weighted average, or the simple mass-fraction-weighted average); substitute into the standard friction-factor correlation as if it were a single-phase fluid.

- **Separated (Lockhart-Martinelli) flow model**: Assume each phase flows independently in its own part of the cross-section, and correlate the two-phase pressure loss to the single-phase pressure loss of each phase separately via the two-phase multipliers phi_G and Xi (the Martinelli parameter), rather than deriving it from first principles.
  - When to use: When phases are clearly separated (stratified, annular) and a homogeneous-mixture assumption is not physical, and when only a crude/engineering estimate of combined pressure loss is needed.
  - How: Compute (dP/dx)|_SG and (dP/dx)|_SL as if each phase alone flowed in the full pipe; form phi_G = sqrt[(dP/dx)|_TP / (dP/dx)|_SG] and Xi = sqrt[(dP/dx)|_SL / (dP/dx)|_SG]; use the empirical correlation between these multipliers (established by Lockhart and Martinelli) to back out the actual two-phase pressure loss.

- **Flow regime maps**: A 2-D (or dimensionless) map whose axes are superficial velocities (or dimensionless groups combining Froude, Reynolds, and Weber numbers) that partitions the plane into regions corresponding to each observed flow pattern (stratified, wavy, slug/plug, annular, bubbly, mist, etc.).
  - When to use: Before choosing any pressure-drop model — the regime dictates which model (homogeneous vs. separated vs. a dedicated correlation) is appropriate.
  - How: Compute the superficial velocities U_sG and U_sL (or the relevant dimensionless groups) for the actual flow conditions, locate the point on the map appropriate to the pipe orientation (horizontal, vertical-against-gravity, vertical-with-gravity, micro-gravity), and read off the regime. Taitel and Dukler's five-dimensionless-group map is cited as the most widely used general-purpose map, though it is not universal (e.g., it fails under microgravity).

- **Terminal/minimum fluidization velocity model (solid-liquid, heavier solids)**: Balance gravity-buoyancy force against drag force on a single spherical particle to find the liquid velocity at which the particle is suspended ("floating"), using a regime-dependent drag coefficient (Stokes' law for Re<1, an intermediate correlation for 1<Re<1000, Newton's law C_D=0.44 for larger Re).
  - When to use: Predicting the onset of fluidized-bed behavior (fixed -> mixed -> fully fluidized bed -> pneumatic conveying) in solid-liquid or solid-gas flow.
  - How: Solve (pi*D^3*g*(rho_S-rho_L))/6 = C_D_inf * (fluid dynamic term) for U_L, using the Reynolds number Re = U_L*D*rho_L/mu_L to pick the correct C_D_inf correlation; for multiple particles, correct with a void-fraction function f(alpha) since neighboring particles alter the effective drag.

## Key Concepts
- **Quality (X, "dryness fraction")**: The ratio of gas mass flow rate to total mass flow rate, X = m_dot_G / m_dot = G_G/G; (1-X) is the "wetness fraction."
- **Void fraction (alpha)**: The ratio of the gas-occupied cross-sectional area to the total cross-sectional area, alpha = A_G/A; varies along the tube because gas density changes.
- **Liquid holdup (L_H)**: The complementary liquid fraction, L_H = 1 - alpha = A_L/A.
- **Superficial velocity (U_sG, U_sL)**: The velocity a phase would have if it alone occupied the entire cross-section of the tube (U_sG = G_G/rho_G = Q_G, and similarly for liquid) — a bookkeeping velocity, not an actually observed one.
- **Slip (SLP)**: The ratio of actual gas velocity to actual liquid velocity, SLP = U_G/U_L; usually greater than unity, and not constant along the tube.
- **Flow regime**: A qualitatively distinct spatial configuration of the phases (e.g., stratified, slug, annular, bubbly, mist) that determines which pressure-drop and heat-transfer correlations apply.
- **Double choking**: The phenomenon (analogous to compressible-flow choking) in which liquid-liquid or gas-liquid flow reaches a maximum combined flow rate that cannot be exceeded regardless of driving pressure, because the lighter/compressible phase chokes.
- **Flooding / reversal flow**: In counter-current flow (e.g., liquid falling, gas rising), a critical interfacial shear stress beyond which the liquid film's net flow rate drops to zero or reverses direction — critical for nuclear/boiler safety (loss of coolant to the heated zone).
- **Hysteresis in flow regimes**: The regime transition path when flow rate is decreasing does not retrace the same sequence of regimes seen when flow rate was increasing.

## Mental Models
- Think of every "single-phase" flow (including plain air) as an approximation of an underlying multiphase flow that is valid only because the phases are so well mixed (or so dilute) that averaging introduces negligible error — the homogeneous assumption is a convenience, not a law of nature, and breaks down under strong body forces or large accelerations (stratification).
- Use flow-regime identification as the mandatory first step, not an afterthought: the correct pressure-drop or holdup calculation method depends entirely on which regime you're in, so "compute an average viscosity and proceed" is only valid inside the homogeneous-flow regime.
- Think of horizontal and vertical multiphase flow as needing genuinely different regime maps and different physical mechanisms for the *same-named* regime (e.g., "slug flow" is created by wave-reaching-the-crown in horizontal flow but by bubble coalescence in vertical flow) — do not transfer intuition about a regime name across orientations.
- Treat the Lockhart-Martinelli approach as a "pressure-loss ratio correlation," not a derivation: it works because it was fit to data relating two-phase loss to each phase's hypothetical single-phase loss, not because the phases are truly independent.

## Anti-patterns
- **Assuming a single "average viscosity" always exists and is meaningful**: In flows like oil-water pipelines or slug flow, the water simply lubricates around the oil (or the phases alternate as plugs), so an average viscosity is not just imprecise — it can be conceptually meaningless because the "average" depends on the (unknown, regime-dependent) internal geometry of the flow.
- **Ignoring flow orientation when applying a flow regime map**: A map built for horizontal flow (Mandhane-type) cannot be applied to vertical flow, and vertical-against-gravity differs from vertical-with-gravity because buoyancy acts in opposite directions relative to the driving pressure force for each phase.
- **Assuming the interface between two flowing liquids is a straight/flat line**: The chapter's flooding analysis shows this assumption is physically inconsistent — it cannot simultaneously satisfy equal velocity and equal shear stress at the interface, meaning the true interface must be wavy; treating it as flat gives contradictory boundary conditions.
- **Extrapolating "normal gravity, air/water" flow regime maps to other conditions**: Regime maps (e.g., Taitel-Dukler) are explicitly stated to be non-universal; they fail for microgravity, and different maps are needed for very different density ratios, tube diameters, or surface-tension regimes.
- **Neglecting choking in solid-gas (pneumatic) flow**: Because the speed of sound in a gas drops sharply as solid particle concentration increases, gas velocity in solid-gas conveying can be limited to roughly Mach 1/sqrt(k) to 1 — treating the carrier gas as effectively incompressible over long conduits is invalid and understates the achievable/limiting flow rate.
- **Using the friction factor correlation with the true two-phase wall shear stress relationship**: The book is explicit that no experimental data actually ties averaged two-phase velocity to wall shear stress; single-phase friction-factor correlations are reused only for lack of anything better, not because they are validated for two-phase flow.

## Key Equations
1. **Quality**: X = m_dot_G/m_dot = G_G/G. Defines the mass fraction of gas in the flow; the primary independent variable for most homogeneous-model correlations.
2. **Void fraction and its relation to quality (equal-velocity case, SLP=1)**: X = rho_G*alpha / [rho_L*(1-alpha) + rho_G*alpha]. Links the area-based void fraction to the mass-based quality when there is no slip between phases.
3. **Averaged (homogeneous) density**: rho_average = 1 / [X/rho_G + (1-X)/rho_L]. The core relation underlying the homogeneous flow model; equivalent to a harmonic mean weighted by quality.
4. **Homogeneous-model friction pressure loss**: -(dP/dx)|_f = (4*tau_w)/D, with tau_w = f*rho_m*U_m^2/2 and f = C*(rho_m*U_m*D/mu_m)^-n (C=16, n=1 laminar; C=0.079, n=0.25 turbulent). Applies single-phase friction-factor formalism to the averaged mixture properties.
5. **Lockhart-Martinelli two-phase multipliers**: phi_G = sqrt[(dP/dx)|_TP / (dP/dx)|_SG] and Xi = sqrt[(dP/dx)|_SL / (dP/dx)|_SG]. Correlates actual two-phase pressure loss to the hypothetical single-phase pressure loss of each phase flowing alone in the full pipe.
6. **Total pressure loss decomposition**: Delta P_ab = (friction term) + (acceleration term) + (gravity term), where the acceleration term is -(dP/dx)|_a = m_dot^2*[(1/A)*d(1/rho_m)/dx + (1/(rho_m*A^2))*dA/dx] and the gravity term is (dP/dx)|_g = g*rho_m*sin(theta). Mirrors the single-phase mechanical-energy balance but with mixture density rho_m in place of a single fluid's density.

## Reference Tables

| Regime | Orientation | Defining characteristic | Occurs when |
|---|---|---|---|
| Stratified (open-channel-like) | Horizontal | Heavy liquid on bottom, light phase on top, flat-ish interface | Very low flow rate of both phases |
| Stratified wavy | Horizontal | Interface develops waves as lighter-phase velocity increases | Increasing superficial velocity of light phase, heavy-phase rate still moderate/low |
| Annular | Horizontal | Heavier liquid pushed entirely to the pipe periphery; light phase forms a core | Lighter-phase flow rate high enough that waves cannot reach the crown, or as end-state of increasing gas rate |
| Slug / plug | Horizontal | Alternating "plugs" of heavy liquid (with light-phase bubbles) and near-full-tube "chunks" of light phase | Heavy-liquid flow rate large enough that waves reach the pipe crown |
| Bubble flow | Vertical, against gravity | Discrete gas bubbles dispersed in continuous liquid | Low-to-moderate light-phase flow rate; flow must start this way against gravity (cannot start stratified) |
| Slug / plug (vertical) | Vertical, against gravity | Bubbles collide and coalesce into large gas slugs separated by liquid | Increasing gas flow rate from bubbly flow |
| Elongated bubble / churn flow | Vertical, against gravity | "Super slugs" from further bubble coalescence; chaotic, turbulent | Further increase in light-phase flow rate beyond slug flow |
| Annular (vertical) | Vertical, against gravity | Continuous gas core with liquid film on the wall | High gas flow rate; end-state after churn flow |
| Mist flow | Vertical, micro-gravity or high gas rate | Liquid entirely broken into tiny drops carried by gas | Very high gas flow rate relative to liquid |
| Bubbly flow (micro-gravity) | Vertical, micro-gravity | Liquid fills the void, gas present as small bubbles | High liquid flow rate, low gas flow rate under weak-gravity/surface-tension-dominated conditions |
| Pulse flow | Vertical, micro-gravity | Liquid moves in frequent pulses | Medium gas and liquid flow rates under micro-gravity |
| Fixed / mixed / fully fluidized bed | Solid-liquid or solid-gas | Solids stationary, then partially, then fully suspended and moving | Fluid velocity increasing from below to above the terminal (minimum fluidization) velocity |
| Pneumatic conveying | Solid-gas | Sparse solid particles dispersed throughout the gas | Very high fluid velocity, well beyond fluidization onset |
| Horizontal counter-current stratified | Horizontal, counter-current | Liquid and gas flow in opposite directions in separate layers | Both flow rates small |
| Flooding / reversal | Vertical or horizontal counter-current | Liquid film flow rate driven to zero or reversed by gas shear | Interfacial shear stress exceeds the critical value tau_i_critical = (2*g*h*rho_L)/3 |

## Worked Example
**Identifying the fluidization/flow regime for a heavier solid particle in an upward liquid stream (reconstructed from Section 13.8.1):**

Consider a spherical solid particle of diameter D and density rho_S denser than the carrying liquid (rho_L), being lifted by an upward liquid flow.

Step 1 — Set up the force balance for the "floating" (terminal/minimum fluidization) condition: gravity-minus-buoyancy on the particle must equal the drag force from the liquid, i.e. (pi*D^3*g*(rho_S - rho_L))/6 = drag force expressed through C_D_infinity(Re)*U_L^2 terms.

Step 2 — Compute the particle Reynolds number, Re = U_L*D*rho_L/mu_L, to select the correct drag correlation: Stokes' law (C_D = 24/Re) for Re<1, the intermediate correlation C_D = (24/Re)*(1 + Re^(2/3)/6) for 1<Re<1000, or Newton's regime (C_D ≈ 0.44, roughly constant) for larger Re. The chapter notes most practical solid-liquid systems fall in the intermediate (second) range.

Step 3 — Solve the resulting equation for U_L, the minimum liquid velocity needed to keep the particle suspended ("floating"); below this velocity the particle sinks, above it the particle is carried along with the liquid.

Step 4 — Interpret the regime progression as fluid velocity increases past this minimum: fixed fluidized bed (particles barely mobile) -> mixed fluidized bed -> fully fluidized bed -> (for liquids) slug flow with nearly particle-free domes, or (for gases) "tunnel" formation and eventually churn/large-bubble flow -> pneumatic conveying (solids sparsely dispersed throughout the carrier fluid) at the highest velocities.

Step 5 — Note the added constraint for gas carriers: because the speed of sound in the gas drops sharply with increasing particle loading, the gas velocity may choke near Mach 1/sqrt(k) to 1 before pneumatic conveying is fully achieved over long conduits — a limitation that does not meaningfully apply to liquid carriers.

## Key Takeaways
1. Always identify the flow regime (via a regime map appropriate to the pipe orientation) before selecting a pressure-drop model — the same nominal flow rates can require completely different physics depending on regime.
2. The homogeneous flow model (averaged density/viscosity applied to single-phase correlations) is a convenience valid mainly for well-mixed/dispersed regimes (bubbly, mist); it is not derived from first principles and has no dedicated experimental validation for the friction factor.
3. The Lockhart-Martinelli separated-flow model is an empirical correlation between two-phase pressure loss and each phase's hypothetical single-phase pressure loss — useful for stratified/annular regimes where homogeneous mixing is not physical.
4. Vertical flow against gravity and vertical flow with gravity are fundamentally different flow-regime sequences because buoyancy acts oppositely on the light and heavy phases in each case; horizontal flow differs from both because of stratification instability.
5. Void fraction, quality, and slip are three distinct (and generally non-constant along the tube) descriptors of phase distribution — do not conflate mass-based quality with area-based void fraction except under the no-slip assumption.
6. Flooding/reversal in counter-current flow has an identifiable critical interfacial shear stress (tau_i_critical = 2*g*h*rho_L/3 in the simplified two-dimensional laminar model); exceeding it drives the liquid flow rate toward zero or reverses it — a key safety consideration in boiler/nuclear engineering.
7. Regime and pressure-loss maps in this field are empirical, incomplete, and orientation/condition-specific (e.g., Taitel-Dukler's map fails under microgravity) — multiphase flow is presented as an evolving field without a universal consensus model.

## Connects To
- **Ch 5 (Control Volume Mass Conservation)**: The mass-flow-rate and continuity bookkeeping (m_dot = m_dot_G + m_dot_L, mass velocities G) used to define quality and superficial velocity directly extends the single-phase mass-conservation framework to two coexisting phases.
- **Ch 6 (Momentum Conservation)**: The friction, acceleration, and gravity pressure-loss components (Section 13.7) are a two-phase-specific decomposition of the same mechanical-energy/momentum balance used for single-phase pipe flow.
- **Compressible flow / Fanno flow (external, "Fundamentals of Compressible Flow")**: The chapter explicitly defers explanation of choking in gas-solid pneumatic conveying and gas compressibility effects on interfacial pressure profiles to the author's companion compressible-flow text.
- **Open Channel Flow (later chapter)**: Stratified flow with negligible light-phase flow rate is identified as reducing to open-channel flow, which is treated as an extreme sub-case of liquid-gas multiphase flow and developed fully in its own chapter.
- **Dimensionless numbers (Froude, Reynolds, Weber)**: The micro-gravity vertical flow map and general flow-regime transitions are organized using combinations of these three dimensionless groups, tying this chapter to the broader dimensional-analysis framework used throughout the book.
