# Cheatsheet — Fluid Mechanics (Bar-Meir)

## Which flow model applies? (decision rule)
1. Is Mach number M < ~0.3? → treat as incompressible (Ch5–Ch10 tools apply).
2. M ≥ 0.3, area changes, no friction/heat of note? → **Isentropic** relations (Ch11).
3. Supersonic flow meets a solid turning INTO the flow? → **Oblique shock** (Ch12); turning AWAY? → **Prandtl-Meyer expansion** (Ch12). Deflection angle beyond δ_max at that M1? → shock **detaches**.
4. Constant-area duct, friction present, negligible heat transfer (short/insulated)? → **Fanno flow** (choking at M=1).
5. Constant-area duct, friction present, long/poorly insulated (heat leaks to hold T≈const)? → **Isothermal flow** (choking at M=1/√k) — NOT Fanno.
6. Constant-area duct, heat addition/removal, negligible friction? → **Rayleigh flow** (choking at M=1; max T0 at M=1/√k).
7. Two phases present? → identify flow regime from a map matched to orientation FIRST, then pick homogeneous (well-mixed) or Lockhart-Martinelli (separated) model.

## Hydrostatics: one equation, different g_eff
| Situation | g_eff | Free/const-P surface shape |
|---|---|---|
| Plain gravity | g (down) | horizontal plane |
| Linear acceleration a | vector sum of g and −a | tilted plane, tanβ=a/g |
| Rigid rotation ω | −g k̂ + ω²r r̂ | paraboloid, z−z0=ω²r²/(2g) |

Always: grad P = ρ·g_eff; integrate along g_eff direction; other directions give P=const on perpendicular surfaces.

## Stability sign checks
- Floating body: stable iff **GM = BM − BG > 0** (subtract Σ I_xxb/V_b for any internal free liquid surface).
- Atmosphere: stable iff **Cx < ((k−1)/k)·(g/R)** (lapse rate below adiabatic).
- Heavy-over-light interface: stable iff wavelength **L < L_c = √(4π²σ/(g(ρ_H−ρ_L)))**.

## Dimensionless numbers — force ratio key
| Number | Ratio | Formula |
|---|---|---|
| Re | inertial/viscous | ρUℓ/μ |
| Fr | inertial/gravity | U²/(gℓ) |
| M | flow speed/sound speed | U/c |
| We | inertial/surface-tension | ρU²ℓ/σ |
| Eu | pressure/inertial | ΔP/(½ρU²) |
| Ca | viscous/surface-tension | μU/σ = We/Re |
| Oh | combines We,Re | √We/Re |

Rule of thumb: if you can name the two competing forces in a problem, you can usually write down which named number governs it — most "exotic" numbers (Ca, Oh, Ga, La) are just algebraic combinations of Re, Fr, We.

## Compressible-flow chokepoints (memorize the differences)
| Model | Choking Mach | What's held fixed |
|---|---|---|
| Isentropic (nozzle) | M=1 at throat only | s, T0, P0 |
| Fanno (friction, adiabatic) | M=1 | area, ṁ, T0 |
| Isothermal (friction+heat) | M=1/√k | area, ṁ, T (static) |
| Rayleigh (heat, frictionless) | M=1 (max entropy); max T0 at M=1/√k | area, ṁ, momentum |
| Normal shock | always supersonic→subsonic | ṁ, momentum, T0 (NOT P0, NOT s) |

## Oblique shock quick check
- Two math roots for given (M1, δ): **weak** (smaller θ, usually supersonic exit) is what a real unconfined wedge/cone shows; **strong** (larger θ, always subsonic exit) needs a forcing downstream BC.
- If required δ > δ_max(M1): no attached solution — shock **detaches**.
- Match **static** pressure (not stagnation) across a slip line.

## Common sign/setup traps
- Momentum average (U²-based) ≠ energy average (also U²-based but different correction factor C_F) ≠ arithmetic mean — pick the one matching what you're computing.
- U_rn is relative to the (possibly moving) control-surface, not ground-frame velocity — always subtract boundary velocity.
- Isentropic tables are invalid *across* a shock — switch to explicit shock relations at the shock plane.
- Moment of inertia is axis-dependent (use parallel axis theorem to shift); center of mass is not.
- Widening a choked orifice does NOT increase mass flow rate past the throat.

## Reynolds Transport Theorem — the one equation behind Ch5–Ch8
D/Dt ∫_sys(φρ)dV = d/dt ∫_cv(φρ)dV + ∫_S φρU_rn dA
φ=1 → mass (Ch5) · φ=U → linear momentum (Ch6) · φ=r×U → angular momentum (Ch6) · φ=e_total → energy (Ch7)
