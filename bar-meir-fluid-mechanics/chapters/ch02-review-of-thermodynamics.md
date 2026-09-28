# Chapter 2: Review of Thermodynamics

## Core Idea
Fluid mechanics problems are ultimately energy-and-mass-conservation problems, so this chapter re-establishes the thermodynamic scaffolding — work, internal energy, the first and second laws, entropy, enthalpy, specific heats, and the ideal gas equation of state — that every later compressible-flow and energy-balance derivation in the book leans on.

## Frameworks Introduced
- **First Law of Thermodynamics (energy conservation for a non-accelerating system)**: `Q₁₂ − W₁₂ = E₂ − E₁`. Since (per the author) all systems can be treated as non-accelerating for this purpose, the law applies universally within the book's scope.
  - When to use: Any process where heat and work cross the system boundary and you need to track total system energy between two states.
  - How: Define system boundaries, sum all forms of energy in state 1 and state 2 (kinetic, potential, internal), and balance against net heat added and net work done by the system on its surroundings.
- **Adiabatic process relation**: For `Q₁₂ = 0`, the first law reduces to `W₁₂ = E₁ − E₂` — the work done depends only on the endpoint energies, not on the path or intermediate states.
  - When to use: Insulated systems, or processes fast enough that heat transfer is negligible.
  - How: Drop the Q term and equate work directly to the drop in total system energy.
- **Total/Specific Energy Equation**: `(mU₁²)/2 + mgz₁ + Eu1 + Q = (mU₂²)/2 + mgz₂ + Eu2 + W` (per-unit-mass form: `U₁²/2 + gz₁ + eu1 + q = U₂²/2 + gz₂ + eu2 + w`).
  - When to use: General energy balance between two states of a system including kinetic, potential (gravity, `mgz`), and internal energy.
  - How: Differentiate with respect to time to get the rate form `Q̇ − Ẇ = D(Eu)/Dt + mU(DU/Dt) + mg(Dz/Dt)` for continuous/steady analysis (the `D/Dt` denotes a system-property, not a fixed-point, derivative).
- **Second Law of Thermodynamics — Clausius Inequality**: `∮ δQ/T ≥ 0` over any cycle, becoming an equality `∮ δQ/T = 0` for a reversible cycle.
  - When to use: To test whether a cyclic process is physically realizable and to define entropy.
  - How: Because the reversible cyclic integral is path-independent, define entropy via `ds ≡ (δQ/T)_rev`, then integrate: `S₂ − S₁ = ∫₁² (δQ/T)_rev`.
- **Isentropic process definition**: A reversible + adiabatic process has `dS = 0` (entropy constant). Note the one-way logic: reversible+adiabatic ⟹ isentropic, but isentropic does NOT imply reversible (an irreversible process with just the right heat transfer can still have zero net entropy change).
  - When to use: Idealized compression/expansion processes (turbines, nozzles, compressors) as a baseline/limiting case.
  - How: Set `dS = 0` and use `TdS = dEu + Pdv` or `TdS = dh − v dP` to relate T, P, and V/v directly.
- **Gibbs Equation (Tds relations)**: `TdS = dEu + PdV` (from combining `δQ = TdS` and `δW = PdV` into the first law) and, via the enthalpy definition, `TdS = dH − VdP`. Per unit mass: `T ds = du + P dv = dh − dP/ρ`.
  - When to use: Relating entropy change to internal energy/enthalpy and P-V or P-ρ changes; valid for reversible AND irreversible processes even though derived assuming no ΔKE/ΔPE.
  - How: Pick the du-form or dh-form depending on whether volume or pressure data is available.
- **Ideal Gas Equation of State**: `P = ρRT` (equivalently `Pv = RT` or `PV = mRT`), with specific gas constant `R = R̄/M` derived from the universal gas constant `R̄ = 8.3145 kJ/(kmol·K)` via Avogadro's law.
  - When to use: Gases at conditions far from the critical point / not near phase change — the default assumption throughout the book unless stated otherwise.
  - How: Look up molecular weight M for the gas, compute R, then relate P, ρ (or v), and T directly.
- **Compressibility factor Z (real-gas correction)**: `Z = PV/(RT)`.
  - When to use: When a gas deviates from ideal-gas behavior (high pressure, low temperature, near saturation).
  - How: Z = 1 recovers the ideal gas law; Z ≠ 1 quantifies the deviation, to be looked up from charts/tables per gas and reduced state.

## Key Concepts
- **Work**: Mechanically, `work = ∫F·dl = ∫P dV`; sign convention is that work done BY the system ON its surroundings is positive; not all energy transfer is "work" (e.g., pure conductive heat transfer is not work, but electrical current is).
- **System**: A continuous (at least partially) fixed quantity of matter whose mass is treated as constant (non-relativistic assumption); its dimensions/shape can change while mass conservation and energy conservation are tracked as two separate laws.
- **Internal energy (E_U, or e_u per unit mass)**: A state property depending on other properties of the system (e.g., for pure/homogeneous simple gases, on two properties like T and P).
- **Enthalpy (H, or h per unit mass)**: Defined as `H = E_U + PV`; a derived state property combining internal energy and flow work, central to open-system/control-volume energy analysis used later in the book.
- **Entropy (S, or s per unit mass)**: Defined via `ds ≡ (δQ/T)_rev`; a state property whose path-independence follows directly from the Clausius equality.
- **Specific heat at constant volume, Cv**: `Cv ≡ (∂Eu/∂T)`, the rate of internal-energy change with temperature.
- **Specific heat at constant pressure, Cp**: `Cp ≡ (∂h/∂T)`, the rate of enthalpy change with temperature.
- **Specific heat ratio, k**: `k ≡ Cp/Cv`; near 1 for solids (Cp ≈ Cv), larger than 1 for gases, ranging up to about 1.667 for monatomic gases, and depends on molecular degrees of freedom.
- **Reversible vs. irreversible process**: A reversible process is one with no losses, satisfying the Clausius equality with equality; irreversibility is the general case satisfying only the inequality.

## Mental Models
- Think of the **first law as pure bookkeeping**: total energy (kinetic + potential + internal) in state 1, plus heat in, minus work out, equals total energy in state 2 — the path taken between states is irrelevant to the final tally (this is why the adiabatic-process result `W₁₂ = E₁ − E₂` is "interesting": it's path-independent).
- Use **entropy as a path-independence detector**: because `∮δQ/T = 0` for reversible cycles, the quantity `δQ/T` behaves like an exact differential (a state property), which is precisely why entropy can be defined at all.
- Treat **isentropic as an idealization, not a synonym for reversible**: reversible+adiabatic guarantees isentropic, but isentropic can also arise from a special-case irreversible process with compensating heat transfer — don't assume ds=0 implies a lossless process.
- Think of the **ideal gas law as the default working model** for gas behavior in this book, with the compressibility factor Z as the correction dial you turn only when conditions (high P, low T) push you away from ideal behavior.

## Anti-patterns
- **Confusing heat transfer with work in all cases**: The author explicitly separates energy transfer that does work (e.g., electrical current) from energy transfer that doesn't (pure conductive heat transfer) — treating all boundary energy transfer as "work" breaks the energy balance's sign conventions.
- **Assuming zero entropy change implies a reversible process**: This is explicitly flagged as an invalid reverse inference — an irreversible process can coincidentally have `ΔS = 0` if heat transfer happens to compensate exactly.
- **Using `Cp − Cv = R` for non-ideal gases or solids/liquids**: This relationship is derived specifically for the ideal/perfect gas model and is not generally valid otherwise.
- **Ignoring the Cp ≠ Cv distinction for liquids while assuming it's as safe as for solids**: The approximation "Cp ≈ Cv" is reasonable for solids (ratio ≈ 1) but is explicitly noted as "less strong" (less justified) for liquids, so applying it uncritically there introduces more error.
- **Treating internal energy as a function of only temperature for real (non-ideal) gases**: The chapter shows `dh = f(T)` only holds for perfect gases (because `d(Pv) = RdT` depends on the ideal gas relation); assuming this generally for real gases breaks the enthalpy/entropy derivations that follow.

## Key Equations
- `Q₁₂ − W₁₂ = E₂ − E₁` — First law for a closed system; Q and W are net heat added and net work done by the system between states 1 and 2.
- `TdS = dEu + PdV` (Gibbs/Tds equation, extensive form) and per unit mass `T ds = du + P dv = dh − dP/ρ` — links entropy change to internal energy/enthalpy and volume/pressure change; valid for reversible and irreversible processes alike.
- `H = Eu + PV` — Definition of enthalpy; `h` is enthalpy per unit mass.
- `Cp − Cv = R` — Mayer-type relation for ideal/perfect gases only, connecting the two specific heats via the specific gas constant R.
- `P = ρRT` — Ideal gas equation of state; ρ is density, R = R̄/M is the specific gas constant, T is absolute temperature.
- `T₂/T₁ = (P₂/P₁)^((k−1)/k) = (V₁/V₂)^(k−1)` — Ideal-gas isentropic relations (from setting Δs = 0 in the entropy-change equation), tying temperature, pressure, and volume ratios together via the specific heat ratio k.
- `s₂ − s₁ = Cp ln(T₂/T₁) − R ln(P₂/P₁)` — Entropy change for an ideal gas between two states, the working formula behind the isentropic relations above.

## Reference Tables
**Table 2.1 — Properties of Various Ideal Gases at 300 K** (Gas / Chemical Formula / Molecular Weight / R [kJ/(kg·K)] / Cp [kJ/(kg·K)] / Cv [kJ/(kg·K)] / k)

| Gas | Formula | M | R | Cp | Cv | k |
|---|---|---|---|---|---|---|
| Air | — | 28.970 | 0.28700 | 1.0035 | 0.7165 | 1.400 |
| Argon | Ar | 39.948 | 0.20813 | 0.5203 | 0.3122 | 1.400 |
| Butane | C₄H₁₀ | 58.124 | 0.14304 | 1.7164 | 1.5734 | 1.091 |
| Carbon Dioxide | CO₂ | 44.01 | 0.18892 | 0.8418 | 0.6529 | 1.289 |
| Carbon Monoxide | CO | 28.01 | 0.29683 | 1.0413 | 0.7445 | 1.400 |
| Ethane | C₂H₆ | 30.07 | 0.27650 | 1.7662 | 1.4897 | 1.186 |
| Ethylene | C₂H₄ | 28.054 | 0.29637 | 1.5482 | 1.2518 | 1.237 |
| Helium | He | 4.003 | 2.07703 | 5.1926 | 3.1156 | 1.667 |
| Hydrogen | H₂ | 2.016 | 4.12418 | 14.2091 | 10.0849 | 1.409 |
| Methane | CH₄ | 16.04 | 0.51835 | 2.2537 | 1.7354 | 1.299 |
| Neon | Ne | 20.183 | 0.41195 | 1.0299 | 0.6179 | 1.667 |
| Nitrogen | N₂ | 28.013 | 0.29680 | 1.0416 | 0.7448 | 1.400 |
| Octane | C₈H₁₈ | 114.230 | 0.07279 | 1.7113 | 1.6385 | 1.044 |
| Oxygen | O₂ | 31.999 | 0.25983 | 0.9216 | 0.6618 | 1.393 |
| Propane | C₃H₈ | 44.097 | 0.18855 | 1.6794 | 1.4909 | 1.327 |
| Steam | H₂O | 18.015 | 0.48152 | 1.8723 | 1.4108 | 1.327 |

## Worked Example
The chapter derives the ideal-gas specific-heat relationship step by step; reconstructed here as a worked derivation:

1. Start from the ideal gas equation of state `Pv = RT`. Differentiating: `d(Pv) = R dT`.
2. For a perfect gas, enthalpy per unit mass is `h = eu + Pv`, so `dh = deu + d(Pv) = deu + d(RT)`. Since both `eu` and `Pv = RT` depend only on T for an ideal gas, this shows `h` is a function of T alone: `dh = f(T)`.
3. Rearranging the enthalpy definition: `d(Pv) = dh − deu`.
4. Substitute step 1's result (`d(Pv) = R dT`) into step 3: `R dT = dh − deu`.
5. Divide through by `dT`: `R = dh/dT − deu/dT = Cp − Cv` (using the definitions `Cp ≡ ∂h/∂T` and `Cv ≡ ∂eu/∂T`).
6. Result: `Cp − Cv = R`, valid only for ideal/perfect gases.
7. Combine with the specific heat ratio `k = Cp/Cv` to solve the pair simultaneously: substituting `Cp = kCv` into `Cp − Cv = R` gives `Cv(k−1) = R`, so `Cv = R/(k−1)` and `Cp = kR/(k−1)`.

This pair of formulas lets you compute Cp and Cv for any ideal gas from just its specific gas constant R (itself computed from molecular weight via `R = R̄/M`) and its specific heat ratio k — exactly how Table 2.1's columns are internally consistent with each other.

## Key Takeaways
1. The first law is path-independent bookkeeping of total energy (kinetic + potential + internal) across system boundaries via heat and work — memorize `Q₁₂ − W₁₂ = E₂ − E₁` as the anchor equation for everything else in the book.
2. Entropy is defined through the reversible-cycle equality in the Clausius inequality; it exists as a state property precisely because that reversible integral is path-independent.
3. Isentropic (Δs = 0) is a narrower and looser condition than "reversible" — reversible+adiabatic guarantees it, but it does not guarantee reversibility in reverse.
4. The Gibbs/Tds relations (`Tds = deu + Pdv = dh − dP/ρ`) are the bridge between entropy, internal energy/enthalpy, and P-V(or P-ρ) behavior, and hold for both reversible and irreversible processes.
5. `Cp − Cv = R` and the derived forms `Cv = R/(k−1)`, `Cp = kR/(k−1)` are ideal-gas-only relationships — do not carry them over to liquids, solids, or real (non-ideal) gases without the Z-correction context.
6. The compressibility factor Z is the explicit escape hatch from the ideal gas law when a real gas deviates from ideal behavior (high pressure/low temperature regimes).

## Connects To
- **Ch 1 (presumed introductory chapter)**: Sets up definitions of density, pressure, and fluid properties that pair with this chapter's state variables (P, T, v/ρ) in the equation of state.
- **Later compressible flow chapters**: The isentropic relations (`T₂/T₁ = (P₂/P₁)^((k−1)/k) = (V₁/V₂)^(k−1)`) and specific heat ratio k derived here are the direct foundation for speed-of-sound, Mach number, and isentropic nozzle/duct flow analysis used throughout the book's compressible flow material.
- **Energy equation / Bernoulli-type analysis**: The Total/Specific Energy Equation and its rate form `Q̇ − Ẇ = D(Eu)/Dt + ...` generalize into the control-volume energy equations used for pipe flow, turbines, and compressors elsewhere in the book.
- **External concept — Van Wylen, "Fundamentals of Classical Thermodynamics"**: The author explicitly points to this text for deeper explanation of why k depends on molecular degrees of freedom.
