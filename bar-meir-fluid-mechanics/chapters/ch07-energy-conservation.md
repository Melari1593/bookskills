# Chapter 7: Energy Conservation

## Core Idea
The first law of thermodynamics, applied to a control volume via the Reynolds Transport Theorem, gives a general energy-conservation equation for fluid flow; under steady, uniform, frictionless, no-shaft-work conditions it collapses to the simple Bernoulli equation, and adding back losses and shaft work gives the practical "extended Bernoulli" equation used for pumps, turbines, and piping systems.

## Frameworks Introduced
- **First law of thermodynamics for a control volume (general energy equation)**: Starting from the system rate equation `Q_dot - W_dot = D/Dt[E_u + m*U^2/2 + m*g*z]`, applying RTT to move from a system to a control volume yields the general form:
  `Q_dot - W_dot_shear - W_dot_shaft = d/dt ∫_V (E_u + U^2/2 + g*z)*rho*dV + ∫_S (h + U^2/2 + g*z)*U_rn*rho*dA + ∫_S P*U_bn*dA`
  where enthalpy `h = E_u + P/rho` absorbs the flow-work term `P/rho`.
  - When to use: any control-volume energy balance — the master equation from which every other energy relation in the chapter is a special case.
  - How: identify heat transfer (Fourier's law for conduction, `dq_dot = k_T*(dT/dn)*dA`), separate work into shear work, shaft work, and flow work (pressure force x velocity), then apply RTT to convert the system's material derivative into a control-volume time-derivative term plus a surface-flux term.
- **Steady-state energy equation**: Drop the time-derivative (accumulation) term when `d/dt = 0`:
  `Q_dot - W_dot_shear - W_dot_shaft = ∫_S (h + U^2/2 + g*z)*U_rn*rho*dA + ∫_S P*U_bn*dA`
  - When to use: flow that has reached steady conditions (uniform in time), even if not spatially uniform.
  - How: further assume uniform properties at each port to reduce the surface integrals to single inlet/outlet terms; divide by mass flow rate `m_dot` to get the per-unit-mass form `q_dot - w_shear - w_shaft = (h + U^2/2 + g*z)|_out - (h + U^2/2 + g*z)|_in`.
- **Frictionless (reversible) steady flow relation**: Using the second law (`T*ds = dE_u + P*dv`) alongside the energy equation to eliminate heat transfer gives, for constant density and no shaft work:
  `0 = (P2 - P1)/rho + (U2^2 - U1^2)/2 + g*(z2 - z1)`
  - When to use: idealized "no losses" flow, used as a reference/limit case (the basis of Bernoulli's equation, developed originally by Euler).
  - How: subtract the reversible-heat energy balance from the general steady energy balance so that heat transfer cancels, leaving only mechanical-energy terms (pressure, kinetic, potential).
- **Simple Bernoulli equation**: `(P/rho + U^2/2 + g*z)|_out = (P/rho + U^2/2 + g*z)|_in`, i.e. `h_total = P/rho + U^2/2 + g*z` is constant along the flow.
  - When to use: negligible energy loss (no friction) and no shaft work — the limiting case of the extended energy equation.
  - How: set the "energy loss" term and `w_shaft` to zero in the general per-unit-mass steady equation.
- **Extended energy equation with losses (engineering Bernoulli)**: `w_dot_shaft = (P/rho + U^2/2 + g*z)|_out - (P/rho + U^2/2 + g*z)|_in + energy loss`, where "energy loss" lumps internal-energy generation and heat transfer effects (friction/dissipation), and is treated as a strong function of `U^2/2` (minor losses and duct/friction losses).
  - When to use: real pipe/duct systems with pumps, turbines, and friction — the day-to-day engineering tool built directly on this chapter's derivation.
  - How: keep the enthalpy split into `P/rho` (pressure/flow work) plus internal energy change and heat transfer, group the latter into a single "loss" term, then solve for the unknown (exit velocity, required pump head, etc.).
- **Energy equation in accelerated (non-inertial) coordinates**: Add pseudo-potential terms for linear acceleration (`a_x*x + a_y*y + (a_z+g)*z`) and, for rotating frames, a centrifugal potential `-omega^2*r^2/2` (the Coriolis term drops out because it does no work along the streamline direction):
  `Q_dot - W_dot = d/dt ∫_cv [E_u + U^2/2 + a_x*x + a_y*y + (a_z+g)*z - omega^2*r^2/2]*rho*dV + ∫_cv (h + U^2/2 + ... )*U_rn*rho*dA + ∫_cv P*U_bn*dA`
  - When to use: fluid systems analyzed in a linearly accelerating or rotating reference frame (e.g., tanks in vehicles, rotating machinery casings).
  - How: treat each constant-acceleration component like an added "gravity" direction, forming an effective potential; for rotation, only the centrifugal term contributes a potential — the Coriolis term is discarded because it is always perpendicular to the relevant flux direction.
- **Correction factor for kinetic energy (`C_F`)**: `C_F = (∫_V rho*U dV)^2 / ∫_V rho*U^2 dV`; for constant density this reduces to `C_F = U_ave^2*V / ∫_V U^2 dV`. For fully developed laminar (parabolic) pipe flow, `C_F = 3/4`; for typical turbulent circular-pipe flow, `C_F ≈ 1.1`.
  - When to use: whenever kinetic energy is computed from an average velocity but the real velocity profile is non-uniform (laminar vs. turbulent pipe flow, etc.).
  - How: compute or look up the profile-dependent factor and multiply the `U_ave^2/2` kinetic-energy term by it to correct for the difference between "energy-averaged" and "momentum-averaged" velocity.

## Key Concepts
- **Enthalpy (h)**: `h = E_u + P/rho`; combines internal energy with the flow-work term `P/rho`, simplifying the energy equation's surface-flux term.
- **Flow work**: The work done by pressure forces at the control-volume boundary as fluid crosses it, `∫_S P*n_hat·U dA`, split into a flux part (`P/rho * rho*U_rn`) and a boundary-motion part (`P*U_bn`).
- **Shear work**: Work done by tangential (viscous/shear) stresses at the control surface, `W_dot_shear = -∫_S tau·U dA`; often zero at solid walls (no-slip → zero velocity) and at free/exit surfaces where shear is perpendicular to flow.
- **Shaft work**: Work transferred through a mechanical shaft (pumps add work, turbines extract it) — kept as a distinct explicit term in the energy balance.
- **Energy loss**: The lumped effect of irreversible internal-energy generation and associated heat transfer (friction, dissipation); modeled as a strong function of velocity squared and split in practice into minor losses and duct/friction losses.
- **Torricelli's equation**: `U ≅ sqrt(2*g*h)`, the limiting exit velocity from a large tank through a small opening (`A_e/A << 1`), derived from the tank energy balance.
- **Reynolds Transport Theorem (RTT)**: The mathematical tool used to convert a system-based (material derivative) energy statement into a control-volume statement (time-derivative + surface flux) — used repeatedly in this chapter.
- **Tank-emptying parameter (`T_e`)**: `T_e = (A / (f(G)*A_e))^2`, a lumped parameter characterizing how a container's height decreases over time, arising from including transverse (non-uniform) kinetic-energy corrections in the tank-emptying analysis.

## Mental Models
- Think of the energy equation as one master accounting statement: heat in, minus work out (shear + shaft), equals the rate of change of stored energy inside the control volume plus the net energy carried across its boundary by mass flow and by pressure doing work on moving boundaries. Every simplified form in this chapter (steady, uniform, frictionless, accelerated frame) is obtained by zeroing out specific terms of this one equation.
- Use Bernoulli's equation as the "no losses, no work" reference case, not as a universal law — it is a special case of the general energy equation, valid only when both `W_dot_shaft = 0` and the energy-loss term is negligible.
- When flow is not uniform across a cross-section (e.g., a velocity profile in a pipe, or the two "halves" of flow into a tank exit), the average of the whole field is not the same as separately averaging pieces of it — this is why kinetic-energy correction factors (`C_F`) and the tank's `f(G)` compensation function are needed; naive use of a single average velocity underestimates real kinetic energy.
- In an accelerated or rotating reference frame, treat the acceleration field the same way gravity is treated in the ordinary energy equation: as an added conservative potential term, because it "creates" a constant-direction (or radially varying, for rotation) body force just like gravity does.

## Anti-patterns
- **Assuming linear tank-draining rate (height ∝ time)**: Earlier, simpler treatments assume flow rate out of a tank is a linear function of height; the energy-based analysis in this chapter shows the actual relationship is nonlinear (`dh/dt ∝ sqrt(h)`), matching Torricelli's equation only in the small-exit-area limit.
- **Ignoring the "upper surface work" / boundary-motion pressure term**: For a non-deformable but internally moving control volume boundary (e.g., a free surface dropping in a tank), the term `∫ P*U_bn dA` does not vanish even when pressure is uniform, because the boundary itself moves — students often drop this term along with the flux term by mistake.
- **Applying the simple frictionless Bernoulli equation where losses or shaft work are present**: Bernoulli's equation only holds when both the loss term and shaft work vanish; using it uncritically in real piping systems (with pumps, valves, fittings) ignores real dissipation that the extended energy equation with a loss term is designed to capture.
- **Treating momentum-averaged velocity as equal to energy-averaged velocity**: Kinetic energy scales with `U^2`, not `U`, so the "averaged momentum" velocity and "averaged kinetic" velocity differ — non-uniform velocity profiles require an explicit correction factor (`C_F`), otherwise kinetic energy is systematically mis-estimated (this is why the same non-uniform-velocity correction differs between the momentum and energy chapters: opposite-direction components cancel in momentum but add in energy).
- **Using the integral method for problems dominated by dissipation or exact free-interface behavior**: The chapter explicitly warns that the integral (control-volume) energy approach cannot handle situations like an oscillating manometer, where the detailed velocity field and free-interface dynamics are the essence of the problem — a cruder tool applied there gives no useful answer.
- **Forgetting Coriolis contributes no potential term**: When adding rotational effects, it's tempting to include a Coriolis potential; the chapter shows this term's contribution vanishes because it is always perpendicular to the direction that matters (the velocity/flux direction), so only the centrifugal term survives in the energy potential.

## Key Equations
- **General control-volume energy equation**: `Q_dot - W_dot_shear - W_dot_shaft = d/dt ∫_V (E_u + U^2/2 + g*z)*rho*dV + ∫_S (h + U^2/2 + g*z)*U_rn*rho*dA + ∫_S P*U_bn*dA` — the master balance; `h = E_u + P/rho` is enthalpy, `U_rn` is velocity relative to the (possibly moving) boundary, `U_bn` is the boundary's own normal velocity.
- **Steady, uniform, fixed-boundary, per-unit-mass form**: `q_dot - w_shear - w_shaft = (h + U^2/2 + g*z)|_out - (h + U^2/2 + g*z)|_in` — the standard "textbook" steady flow energy equation per unit mass, used for pumps/turbines/nozzles with heat transfer.
- **Frictionless steady flow (Bernoulli-Euler relation), constant density**: `0 = (P2-P1)/rho + (U2^2-U1^2)/2 + g*(z2-z1)` — valid with no shaft work and no losses; rearranges to the classic `P/rho + U^2/2 + g*z = const`.
- **Extended (loss-inclusive) equation**: `w_dot_shaft = (P/rho + U^2/2 + g*z)|_out - (P/rho + U^2/2 + g*z)|_in + energy loss` — the practical engineering form for real systems with friction and machines.
- **Torricelli's equation**: `U ≅ sqrt(2*g*h)` — exit velocity from a large open tank through a small hole, valid when `A_e/A << 1`; with a discharge/loss coefficient `C`, `dh/dt ≅ C*sqrt(2*g*h)`.
- **Fourier's law of conduction**: `dq_dot = k_T*(dT/dn)*dA`, integrated to `Q_dot = ∫_A k_T*(dT/dn) dA` — the model used for the heat-transfer term `Q_dot` in the energy balance (radiation and complex convection are excluded as advanced material).

## Reference Tables
No formal comparison/property table is reproduced in the source chapter text; Figure 7.4 lists a few typical exit-loss coefficients qualitatively (sharp-edged inlet K≈1, rounded/other configurations K≈0.5 and K≈0.04) but is presented as a figure, not a data table, in the source.

## Worked Example
**Tank draining through a long pipe (combining Examples 7.1 and 7.2).**

Setup: A large cylindrical tank (diameter D, radius R) holds liquid at height h, above which is a gas at roughly constant pressure. A long pipe (radius r) carries the liquid from the tank to the atmosphere at pressure P_atm. The pipe has a friction/resistance coefficient K_p (assumed to scale with velocity squared); the tank has its own effective loss coefficient K_t. Goal: relate the tank height h(t) to the pipe exit velocity, accounting for both pipe friction and tank-side energy loss.

Approach:
1. **Mass conservation** links the tank's surface-drop velocity to the pipe velocity: `U_1 * A_pipe = (dh/dt) * A_tank`, so `U_1 = (R/r)^2 * dh/dt`.
2. **Energy balance on the tank control volume** (boundary/shaft work assumed zero, air-side energy change neglected) gives, after substituting the RTT-transformed unsteady and flux terms:
   `d/dt[(kinetic+potential terms)*h*A] - (1/2)*(dh/dt)^2*(A3/A1)^2*U1*A1 + (K_t/(2*rho))*(dh/dt)^2 = (P3-P1)/rho`
3. **Energy balance on the pipe control volume**, following the same steady-friction-pipe derivation as the single-pipe example (Example 7.1: `U + (2*rho*L*pi*r^2/K)*dU/dt = 2*(P_in - P_out)/K`), gives an analogous first-order ODE relating `U_p` (pipe velocity) to the pressure drop `P_1 - P_2` across the pipe, with resistance `K_p`.
4. Eliminating `U_p` via the mass-conservation relation (step 1) converts the pipe equation into one written purely in terms of `h`: `dh/dt + (4*rho*L*pi*r^2/K)*d^2h/dt^2 = (R/r)^2 * 2*(P1-P2)/K_p`.
5. **Adding the tank and pipe equations** eliminates the internal interface pressure `P_1` and yields a single second-order governing ODE for `h(t)`, combining gravitational head, tank-side kinetic-energy correction, and pipe friction — solvable numerically given initial conditions `h(0) = h_0` and `dh/dt(0) = 0`.

Key takeaway from the example: even a "simple" draining-tank-through-a-pipe problem requires two coupled control volumes (tank + pipe) and the tank's non-uniform velocity field must be corrected for (via the `f(G)` factor from earlier in the chapter) — the naive single-Bernoulli-equation shortcut misses both the friction loss and the transverse kinetic-energy contribution.

A simpler companion result (single long pipe suddenly exposed to a pressure difference, Example 7.1) shows the exit velocity approaches steady state exponentially:
`U(t) = [2*(P_in - P_out)/K] * (1 - e^(-t*K / (2*pi*r^2*rho*L)))`,
with steady-state limit `U_steady = 2*(P_in - P_out)/K`.

## Key Takeaways
1. Every energy relation used in fluid mechanics (Bernoulli, extended Bernoulli with losses, steady-flow energy equation) is a special case of one general control-volume first-law statement — know which terms you are allowed to drop and why.
2. Bernoulli's equation requires two simultaneous conditions: no shaft work and negligible energy loss; treat it as an idealization, not a default.
3. Enthalpy (`h = E_u + P/rho`) exists specifically to bundle the pressure/flow-work term with internal energy, simplifying the surface-flux term of the energy equation.
4. Non-uniform velocity profiles bias kinetic-energy estimates; always consider whether a correction factor (`C_F`, or a geometry-specific factor like `f(G)`) is needed before trusting an average-velocity kinetic-energy calculation.
5. The integral (control-volume) energy method is powerful but has real limits — it cannot resolve problems where the detailed velocity field or free-interface shape is the crux of the problem (e.g., oscillating manometers).
6. Accelerated or rotating reference frames are handled by adding effective potential-energy terms to the energy equation, exactly as gravity is already handled; only the centrifugal (not Coriolis) term contributes such a potential.
7. Real engineering flow problems (tanks, pipes, pumps) almost always require an explicit "energy loss" term, typically modeled as proportional to velocity squared, layered on top of the frictionless Bernoulli relation.

## Connects To
- **Ch 2**: The chapter opens directly from Chapter 2's system-based energy rate equation, `Q_dot - W_dot = D/Dt(E_U + m*U^2/2 + m*g*z)`, before transforming it via RTT to a control-volume form.
- **Ch 6 (momentum conservation)**: Parallel structure — the boundary/shear/flow-work decomposition mirrors the surface-stress decomposition in the momentum chapter; the chapter explicitly contrasts why velocity-profile correction differs between momentum (components can cancel) and energy (components always add, since energy scales with `U^2`).
- **Ideal Flow chapter**: The frictionless/Bernoulli relation derived here is the entry point to the book's dedicated treatment of ideal (inviscid) flow.
- **Differential equations chapter**: The chapter notes that unsteady and other forms of Bernoulli's equation are developed more fully there, using the differential (rather than integral) form of the governing equations.
- **Reynolds Transport Theorem**: The core external concept used throughout to move between system and control-volume formulations of the energy equation.
- **Second law of thermodynamics**: Used to derive the frictionless-flow relation by combining `T*ds = dE_u + P*dv` with the general energy equation and subtracting to cancel heat transfer.
