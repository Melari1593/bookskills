# Chapter 1: Introduction to Fluids

## Core Idea
Fluid mechanics has no sharp boundaries — between solid and fluid, laminar and turbulent, single- and multi-phase — so the engineer's first job is to correctly identify which simplified model (Newtonian, incompressible, single-phase, etc.) actually applies to a given problem; applying the wrong model (e.g., a turbulent-flow model to a still liquid) produces absurd results even when the mathematics is executed correctly.

## Frameworks Introduced
- **Newton's law of viscosity (definition of a Newtonian fluid)**: τ_xy = μ (dU/dy) — shear stress is directly proportional to the velocity gradient (rate of angular deformation), with μ (absolute/dynamic viscosity) as the constant of proportionality.
  - When to use: Any fluid whose shear-stress/strain-rate ratio is constant over the range of interest (air, water, most simple liquids and gases).
  - How: Measure or look up μ at the relevant temperature; multiply by the local velocity gradient dU/dy to get shear stress. If the ratio is not constant, the fluid is non-Newtonian and this law does not apply.
- **Continuum / gray-boundary view of matter**: The solid/fluid distinction is not sharp — glass, sand, quicksand, mushy-zone aluminum, and grain all "behave" as liquids under the right conditions.
  - When to use: Before choosing a solid-mechanics vs. fluid-mechanics approach for an unusual material.
  - How: Ask whether the material continues to deform without limit under an applied shear stress (fluid behavior) or reaches a fixed deformation (solid behavior) over the timescale of interest.
- **Kinematic viscosity**: ν = μ/ρ, units [m²/sec].
  - When to use: When experimental data or governing equations (e.g., diffusion of momentum) are naturally expressed per unit density, or when comparing gases/liquids where density effects matter alongside μ.
  - How: Divide dynamic viscosity by density at the same conditions.
- **Sutherland's equation (gas viscosity vs. temperature)**: μ = μ₀ · [(0.555 T₀ + S)/(0.555 T + S)] · (T/T₀)^(3/2).
  - When to use: Estimating gas viscosity across a temperature range (valid roughly −40°C to 1600°C per the text) when only a reference viscosity and Sutherland's constant S are known.
  - How: Look up μ₀, T₀, and S (material-specific) in a reference table, plug in the target temperature T.
- **Generalized (reduced) viscosity correlation (Hougen et al.)**: μ_r = μ/μ_c plotted vs. reduced temperature T_r = T/T_c, with lines of constant reduced pressure P_r = P/P_c.
  - When to use: Estimating viscosity of a fluid near/at conditions where direct data is unavailable, given critical properties (T_c, P_c, μ_c).
  - How: Compute T_r and P_r, read μ_r off the generalized chart, recover μ = μ_r · μ_c. Critical viscosity μ_c can itself be approximated as μ_c = √(M·T_c)·v_c^(2/3) or μ_c = √M · P_c^(2/3) · T_c^(−1/6) when not tabulated.
- **Wilke's correlation (viscosity of low-density gas mixtures)**: μ_mix = Σᵢ [xᵢμᵢ / Σⱼ xⱼφᵢⱼ], with φᵢⱼ = (1/√8)·√(1+Mᵢ/Mⱼ)·[1+√(μᵢ/μⱼ)·(Mⱼ/Mᵢ)^(1/4)]².
  - When to use: Estimating the viscosity of a homogeneous mixture of low-density gases from pure-component data.
  - How: Compute pairwise φᵢⱼ from molecular weights and pure viscosities, then combine with mole fractions xᵢ. Note φᵢᵢ = 1 by definition.
- **Reiner–Phillippoff model (non-Newtonian / mixture correlation)**: dU_x/dy = τ_xy / [μ_∞ + (μ₀−μ_∞)/(1+(τ_xy/τ_s)²)].
  - When to use: Two-liquid mixtures where viscosity is dominated by the high-viscosity component at low shear stress and by the low-viscosity component at high shear stress (shear-thinning-like behavior).
  - How: Requires experimentally fitted μ_∞ (high-shear viscosity), μ₀ (zero-shear viscosity), and τ_s (characteristic shear stress); valid only over a limited stress range (noted as accurate up to τ ≈ 0.001 kN/m² for molten sulfur).
- **Bulk modulus of a liquid mixture**: (B_T)_mix = 1 / (x₁/(B_T)₁ + x₂/(B_T)₂ + ... + xᵢ/(B_T)ᵢ), derived by assuming the total volume change is the sum of each phase's individual volume change under uniform pressure.
  - When to use: Estimating compressibility of a mixture or emulsion of several liquids/phases.
  - How: Weight the reciprocals of each component's bulk modulus by its volume fraction xᵢ, then invert the sum.
- **Capillary rise (Jurin-type relation)**: h = 2σcos(β) / (gΔρ·r); maximum (perfect wetting) case: h_max = 2σ/(gΔρ·r).
  - When to use: Estimating the height a liquid rises/depresses in a narrow tube due to surface tension, when the contact angle β is known or assumed.
  - How: Plug in surface tension σ, density difference Δρ between liquid and gas, and tube radius r. Recognize the model breaks down (predicts unphysical negative pressure) at very small radii.

## Key Concepts
- **Fluid mechanics**: The branch of continuum mechanics relating forces, motion, and static conditions in a continuous material that cannot sustain shear stress at rest.
- **Shear stress (τ_xy)**: Force per unit area acting tangentially (parallel) to a surface; in fluids it can only be transmitted through relative motion (deformation), not statically as in solids.
- **Absolute (dynamic) viscosity, μ**: The proportionality constant between shear stress and velocity gradient; units [N·sec/m²]; arises from cohesion and molecular momentum exchange.
- **Kinematic viscosity, ν**: μ/ρ; has units of [m²/sec] (acceleration-like/diffusivity units).
- **Newtonian fluid**: A fluid for which τ_xy/(dU/dy) is constant (e.g., air, water, glycerin).
- **D'Alembert's paradox**: The historical conflict between "ideal" (inviscid) fluid theory, which predicts zero drag/resistance, and observed reality; resolved by recognizing the necessity of grounding fluid theory in experiment.
- **Surface tension (σ)**: The force per unit length at a liquid interface responsible for capillary rise/depression and pressure differences across curved interfaces.
- **Bulk modulus (B_T)**: Measure of a fluid's resistance to uniform compression, v·(∂P/∂v) = B_T.
- **Reduced properties (T_r, P_r, μ_r)**: Properties normalized by their value at the critical point, used in generalized correlation charts.
- **No clear boundary between disciplines**: The recurring theme that laminar/turbulent, single/multi-phase, and solid/fluid distinctions are contextual approximations, not absolute categories.

## Mental Models
- Think of viscosity as "flux of momentum" diffusing in the direction perpendicular to flow — shear stress is literally x-momentum being transported in the y-direction, which is why the author prefers writing it as τ_xy rather than a bare force/area ratio.
- Use the two-plate (Couette) picture as the default mental model for shear: whenever you need to reason about a viscous force, imagine a thin fluid layer being dragged between two surfaces with a linear velocity profile.
- Think of gas viscosity and liquid viscosity as governed by opposite physical mechanisms: in gases, viscosity rises with temperature because molecular momentum exchange increases with agitation; in liquids, viscosity falls with temperature because cohesive intermolecular forces weaken as temperature rises. Never assume both behave the same way.
- Treat every "boundary" in fluid mechanics (laminar/turbulent, single/multi-phase, solid/fluid) as a spectrum with an arbitrary cutoff chosen for engineering convenience, not a law of nature — use dimensional analysis to decide which regime dominates in a given problem.
- Use generalized/reduced-property charts as a fallback estimation tool only when direct experimental data for a specific fluid is unavailable — they trade precision for universality.

## Anti-patterns
- **Applying a complex/turbulent model to a simple or still-flow problem**: The author explicitly cites engineers analyzing a "complete still liquid" with a complex turbulent flow model — the model choice must match the actual physical regime, not default to the most sophisticated available tool.
- **Trusting numerical/CFD output without checking whether the input assumptions match reality**: "these programs are as good as the input provided" — assuming turbulent flow for what is actually still flow will produce confidently wrong results.
- **Treating viscosity as meaningful inside the two-phase dome**: There is no well-defined viscosity for, e.g., "30% liquid" during a phase-change process — viscosity there depends on the flow structure itself and must be handled with multiphase-flow methods, not a single-phase property lookup.
- **Using the simple capillary-rise equation at very small tube radii**: h = 2σcos(β)/(gΔρ·r) predicts unbounded/negative-pressure heights as r → 0, which is unphysical (the liquid would vaporize first) — signals that the continuum/simplistic model has broken down and a different model is required.
- **Assuming a constant contact angle is known or measurable in practice**: The author flags that real contact angle data is rarely available, making the basic capillary equation useful mainly for showing trends, not precise predictions.
- **Ignoring pressure/temperature swings in hydraulic systems**: Assuming a hydraulic fluid's bulk modulus is constant when in practice temperature changes of 50°C from friction can change the bulk modulus by more than 60%, significantly altering system response time.

## Key Equations
- **τ_xy = μ (dU/dy)** — Newton's law of viscosity; defines Newtonian fluids; τ in [N/m²], μ in [N·sec/m²], dU/dy in [1/sec]. Applies whenever the fluid's stress-strain-rate ratio is constant.
- **ν = μ/ρ** — Kinematic viscosity; converts dynamic viscosity to units of [m²/sec]; used when density-normalized momentum diffusivity is more natural (e.g., some correlations/experimental data).
- **μ = μ₀ · [(0.555 T₀+S)/(0.555 T+S)] · (T/T₀)^(3/2)** — Sutherland's equation; estimates gas viscosity as a function of absolute temperature T given a reference state (μ₀, T₀) and Sutherland's constant S; valid roughly −40°C to 1600°C.
- **M = π μ ω R⁴ / (2δ)** — Torque on a rotating disc with a thin gap δ filled with fluid, angular velocity ω, disc radius R; derived by integrating τ = μ(ωr/δ) over the disc area (τ_local · r · dA).
- **(B_T)_mix = 1 / Σᵢ(xᵢ/(B_T)ᵢ)** — Bulk modulus of a mixture of liquids/phases as a volume-fraction-weighted harmonic mean of individual bulk moduli.
- **h = 2σcos(β) / (gΔρ r)** (and h_max = 2σ/(gΔρ r) at β=0) — Capillary rise/depression height as a function of surface tension σ, density difference Δρ, gravity g, and tube radius r; breaks down at very small r.
- **ΔP = 2σ/r** — Laplace pressure jump across a spherical liquid droplet surface (used in the droplet examples); ΔP is the pressure difference between the inside and outside of the droplet, σ is surface tension, r is droplet radius.

## Reference Tables
**Table 1.2 — Viscosity of selected gases (N·sec/m²)**

| Substance | Formula | T [°C] | Viscosity [N·sec/m²] |
|---|---|---|---|
| Isobutane | i-C₄H₁₀ | 23 | 0.0000076 |
| Methane | CH₄ | 20 | 0.0000109 |
| Oxygen | O₂ | 20 | 0.0000203 |
| Mercury vapor | Hg | 380 | 0.0000654 |

**Table 1.3 — Viscosity of selected liquids (N·sec/m²)**

| Substance | Formula | T [°C] | Viscosity [N·sec/m²] |
|---|---|---|---|
| Diethyl ether | (C₂H₅)₂O | 20 | 0.000245 |
| Benzene | C₆H₆ | 20 | 0.000647 |
| Bromine | Br₂ | 26 | 0.000946 |
| Ethanol | C₂H₅OH | 20 | 0.001194 |
| Mercury | Hg | 25 | 0.001547 |
| Sulfuric acid | H₂SO₄ | 25 | 0.01915 |
| Olive oil | — | 25 | 0.084 |
| Castor oil | — | 25 | 0.986 |
| Glucose | — | 25 | 5–20 |
| Corn oil | — | 20 | 0.072 |
| SAE 30 | — | — | 0.15–0.200 |
| SAE 50 | — | ~25 | 0.54 |
| SAE 70 | — | ~25 | 1.6 |
| Glycerol | — | 20 | 1.069 |
| Firm glass | — | — | ~1×10⁷ |

**Table 1.4 — Critical properties for the generalized viscosity chart (selected)**

| Component | M | T_c [K] | P_c [bar] | μ_c [N·sec/m²] |
|---|---|---|---|---|
| H₂ | 2.016 | 33.3 | 12.97 | 3.47 |
| He | 4.003 | 5.26 | 2.29 | 2.54 |
| Air (mixed) | 28.97 | 132 | 36.88 | 19.3 |
| CO₂ | 44.01 | 304.2 | 73.87 | 19.0 |
| O₂ | 32.00 | 154.4 | 50.36 | 18.0 |
| CH₄ | 16.04 | 190.7 | 46.41 | 15.9 |
| Water | 18.015 | 647.1 | 220.64 | ~11.0 |

## Worked Example
Reconstructed from Example 1.1 (drag between parallel plates): A thin plate of area A = 1 m² is dragged at speed U = 0.5 m/s through a 1 cm (h = 0.01 m) gap filled with glycerin (μ ≈ 1.069 N·sec/m²). Assuming Newtonian behavior and a linear velocity profile across the gap, the required force follows directly from τ_xy = μ(U/h) applied over the area:

F = A·μ·U/h = (1)(1.069)(0.5)/(0.01) ≈ 53.45 N

This is the simplest possible application of Newton's law of viscosity: no integration is needed because the geometry (flat plates, small gap) guarantees a linear velocity profile, so the velocity gradient dU/dy collapses to the constant U/h. The same pattern (shear stress × area = force, or shear stress × area × moment arm = torque) recurs throughout the chapter in progressively more complex geometries: concentric rotating cylinders (Example 1.2 and 1.6, where the moment arm is the cylinder radius and the gap is r_o − r_i), a block sliding on an oil film down an incline (Example 1.7, where the driving force is gravity and the resisting force is viscous shear), and a rotating disc with a thin gap (Example 1.8, where τ = μωr/δ must be integrated over the disc area because both the shear stress and the differential area depend on radius r, giving the r⁴ torque relation).

## Key Takeaways
1. Before analyzing any fluid problem, first determine which simplified regime actually applies (laminar/turbulent, single/multi-phase, Newtonian/non-Newtonian) — the boundaries are fuzzy by nature, and choosing the wrong regime produces nonsensical results even with correct mathematics.
2. Newton's law of viscosity, τ_xy = μ(dU/dy), is the foundational constitutive relation for this book; nearly every worked example in the chapter reduces to computing a shear stress and multiplying by area (force) or area×radius (torque).
3. Gas and liquid viscosity respond to temperature in opposite directions — gas viscosity increases with T (kinetic/momentum-exchange mechanism), liquid viscosity decreases with T (cohesion-dominated mechanism).
4. When direct viscosity data is unavailable, use Sutherland's equation for gases or the reduced-property (Hougen) chart for a cruder, more general estimate — but recognize both are approximations valid only in specific ranges.
5. Viscosity of mixtures is highly nonlinear in composition; Wilke's correlation handles low-density gas mixtures, but liquid mixtures generally require experimental characterization.
6. Compressibility (bulk modulus) effects matter mainly in hydraulic systems, deep-ocean, and geological contexts — and even modest temperature swings (50°C) can change a hydraulic fluid's bulk modulus by 60%+, materially affecting system dynamics.
7. Capillary/surface-tension models are only reliable in a middle range of length scales — they fail at very small radii (unphysical negative pressure) and become negligible at large radii (gravity dominates).

## Connects To
- **Ch 2 (Fluid statics/pressure, expected next chapter)**: The density and bulk-modulus discussion here (fluid compressibility, equation of state) sets up the pressure-density relationships used in hydrostatics.
- **Multiphase flow chapter**: The chapter explicitly defers the "meaningless viscosity inside the phase-change dome" problem to the dedicated multiphase flow chapter, and previews open-channel flow as a sub-class of multiphase flow.
- **Reynolds number / dimensional analysis (external concept)**: The chapter's discussion of laminar vs. turbulent flow and the historical mention of Reynolds's and Rayleigh's dimensional-analysis work foreshadow the dimensionless-number framework used throughout the rest of the book.
- **Boundary layer theory (external concept)**: Prandtl's boundary-layer concept is credited as the turning point that unified theoretical and experimental fluid mechanics — a framework developed in later chapters on differential/boundary-layer analysis.
