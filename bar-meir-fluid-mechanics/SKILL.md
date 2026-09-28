---
name: bar-meir-fluid-mechanics
description: "Knowledge base from \"Fluid Mechanics\" by Genick Bar-Meir (Potto Project, hosted on LibreTexts Engineering). Use when applying Bar-Meir's frameworks for fluid statics, control-volume mass/momentum/energy conservation, differential (Navier-Stokes) analysis, dimensional analysis and similitude, potential/inviscid flow, compressible (1D and 2D) flow, or multi-phase flow, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Fluid Mechanics (Bar-Meir)
**Author**: Dr. Genick Bar-Meir (Potto Project) | **Source**: eng.libretexts.org, GNU FDL 1.3 | **Chapters**: 13 | **Generated**: 2026-09-07

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `choking`, `metacentric height`, `Buckingham pi`, or another indexed topic; I find and read the relevant chapter
- **With a chapter** — ask for `ch11`; I load that specific chapter file
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**One master equation per domain, then specialize.** This book is built on four "master equations" that every other formula in it derives from:
1. **Hydrostatics**: `grad P = ρ·g_eff` (Ch4) — g_eff = true gravity + (−container acceleration); every barometer, manometer, tank-force, ship-stability, and Rayleigh-Taylor result is this equation with a different g_eff or density model.
2. **Reynolds Transport Theorem**: `D/Dt ∫_sys(φρ)dV = d/dt ∫_cv(φρ)dV + ∫_S φρU_rn dA` (Ch5–Ch8) — φ=1 gives mass conservation, φ=U gives linear momentum, φ=r×U gives angular momentum, φ=e_total gives energy. Master this once; four chapters fall out of it.
3. **Navier-Stokes equations**: `ρ DU/Dt = −grad P + μ∇²U + f_B` (Ch8, incompressible form) — the differential (pointwise) counterpart to the RTT-based integral laws; drop viscosity (μ=0) to get the Euler equation behind potential flow (Ch10).
4. **Mach number as master switch** (Ch9, Ch11): M=U/c decides whether area/pressure/friction behave "normally" (M<1) or in reverse (M>1); every compressible-flow chapter (11, 12) is organized around this one ratio.

**Newton's law of viscosity**: τ_xy = μ(dU/dy) defines a Newtonian fluid (Ch1). Gas viscosity rises with T (momentum-exchange mechanism); liquid viscosity falls with T (cohesion mechanism) — never assume both directions are the same.

**Choking is a one-way informational barrier** (Ch11, Ch13): once a flow reaches its model-specific critical Mach number (M=1 for isentropic/Fanno/Rayleigh/normal-shock, M=1/√k for isothermal), no further downstream change can increase mass flow rate. Widening a choked orifice does not help.

**Weak vs. strong shock default** (Ch12): for a real, unconfined wedge or cone, the **weak** oblique-shock solution is what is physically observed; the strong solution requires a specific downstream boundary condition to force it. Beyond the Mach-dependent maximum deflection angle δ_max, the shock **detaches**.

**Dimensional analysis has two tiers** (Ch9): Buckingham's π theorem (one-shot / building-blocks / matrix methods) gives only the *minimum count* of dimensionless groups from intuition — it can miss groups that arise from boundary/initial conditions. Nusselt's technique (non-dimensionalize the actual governing PDE + BCs) is the author's recommended real-world method because it cannot miss those groups.

**Stability is always a displaced-parcel sign test** (Ch4): perturb slightly, check whether the restoring force points home. This single idea produces the floating-body criterion (GM=BM−BG>0), the atmospheric convective-stability criterion, and the Rayleigh-Taylor critical wavelength.

**Two Bernoulli equations, not one** (Ch10): the streamline form holds even in rotational flow but only along one streamline; the field-wide form requires irrotational flow but then holds between ANY two points. Conflating them is the most common error in inviscid-flow work.

**Average velocity is context-dependent** (Ch6, Ch7): momentum flux needs a U²-weighted average with its own correction factor; kinetic energy needs a *different* U²-weighted correction factor (C_F); neither equals the simple arithmetic mean of a velocity profile.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-introduction-to-fluids.md) | Introduction to Fluids | Newton's law of viscosity, kinematic/dynamic viscosity, Sutherland's equation, capillary rise |
| [ch02](chapters/ch02-review-of-thermodynamics.md) | Review of Thermodynamics | First/second law, Gibbs equation, ideal gas law, isentropic relations |
| [ch03](chapters/ch03-review-of-mechanics.md) | Review of Mechanics | Center of mass, moment/product of inertia, parallel axis theorem, Newton's 2nd law (continuum form) |
| [ch04](chapters/ch04-fluids-statics.md) | Fluids Statics | Hydrostatic equation, g_eff, barometric formulas, metacentric height, Rayleigh-Taylor instability |
| [ch05](chapters/ch05-control-volume-mass-conservation.md) | Control Volume & Mass Conservation | Reynolds Transport Theorem, Lagrangian vs. Eulerian, deformable CV |
| [ch06](chapters/ch06-momentum-conservation.md) | Momentum Conservation | Integral momentum equation, angular momentum/turbomachinery, rocket equation |
| [ch07](chapters/ch07-energy-conservation.md) | Energy Conservation | Control-volume energy equation, Bernoulli (simple & extended), Torricelli's equation |
| [ch08](chapters/ch08-differential-analysis.md) | Differential Analysis | Differential continuity, substantial derivative, Navier-Stokes equations, boundary conditions |
| [ch09](chapters/ch09-dimensional-analysis.md) | Dimensional Analysis | Buckingham π theorem, building blocks method, Nusselt's technique, similitude |
| [ch10](chapters/ch10-inviscid-potential-flow.md) | Inviscid / Potential Flow | Euler equations, velocity potential, stream function, superposition, Kutta-Joukowski lift |
| [ch11](chapters/ch11-compressible-flow-1d.md) | Compressible Flow (1D) | Speed of sound, isentropic relations, normal shock, Fanno/isothermal/Rayleigh flow |
| [ch12](chapters/ch12-compressible-flow-2d.md) | Compressible Flow (2D) | Oblique shocks, weak/strong solution, Prandtl-Meyer expansion, shock-expansion theory |
| [ch13](chapters/ch13-multiphase-flow.md) | Multi-Phase Flow | Homogeneous/separated flow models, flow regime maps, fluidization |

## Topic Index

- **Angular momentum / turbomachinery** → ch06
- **Bernoulli's equation (simple, extended, streamline vs. field)** → ch07, ch10
- **Boundary conditions (no-slip, kinematic, surface-tension jump)** → ch08
- **Buckingham π theorem / dimensional analysis** → ch09
- **Buoyancy / metacentric height / ship stability** → ch04
- **Capillary rise / surface tension** → ch01, ch04
- **Choking (compressible & multiphase)** → ch11, ch13
- **Compressibility factor Z** → ch02, ch04
- **Continuum / Navier-Stokes equations** → ch08
- **Control volume, deformable vs. non-deformable** → ch05
- **Dimensionless numbers (Re, Fr, M, We, Eu, Ca, etc.)** → ch09
- **Fanno / Isothermal / Rayleigh flow** → ch11
- **Flow regimes (multiphase)** → ch13
- **Fluidization / terminal velocity** → ch13
- **Hydrostatic equation / g_eff** → ch04
- **Ideal gas law / equation of state** → ch02
- **Isentropic relations, stagnation state** → ch02, ch11
- **Kutta-Joukowski theorem / lift / circulation** → ch10
- **Lockhart-Martinelli model** → ch13
- **Mach number / speed of sound** → ch09, ch11
- **Moment of inertia / parallel axis theorem** → ch03
- **Navier-Stokes equations** → ch08
- **Newtonian fluid / viscosity** → ch01
- **Normal shock relations** → ch11
- **Oblique shock / Prandtl-Meyer expansion** → ch12
- **Potential flow / stream function / velocity potential** → ch10
- **Rayleigh-Taylor instability** → ch04
- **Reynolds Transport Theorem (RTT)** → ch05, ch06, ch07, ch08
- **Similitude / model scaling** → ch09
- **Wave (shock) drag** → ch11, ch12
- **Worked-example method: cut CV through solid** → ch06

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and problem-solving patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides

---

## Scope & Limits

This skill covers the book content only, reconstructed from the LibreTexts web edition (equations and tables re-derived from scraped HTML, since no clean PDF/EPUB export was available — treat exact numeric coefficients as reliable but always re-derive from first principles for anything safety-critical). Front Matter and Back Matter were unfilled LibreTexts templates with no book content and were omitted. For hands-on implementation (CFD, pipe-sizing software) or topics beyond this book, combine with project-specific tools or ask directly.
