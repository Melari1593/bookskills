# Chapter 6: Momentum Conservation for Control Volume

## Core Idea
Newton's second law, applied to a fluid system via the Reynolds Transport Theorem, becomes the **integral (linear) momentum equation** for a control volume: the sum of body forces, pressure forces, shear forces, and external (support) forces equals the rate of change of momentum stored in the control volume plus the net flux of momentum crossing its boundary — and the same RTT machinery, applied to moment of a vector, yields the **angular momentum equation** used for rotating machinery.

## Frameworks Introduced
- **Newton's Second Law for a system**: F = d(mU)/dt for one body; for n bodies, Sum(F_i) = Sum[d(m_i U_i)/dt]. Extended to a continuous fluid system: Sum(F) = D/Dt [Integral over system of U * rho dV].
  - When to use: Starting point for deriving any control-volume force balance.
  - How: Apply RTT to convert the system (Lagrangian) derivative D/Dt into control-volume (Eulerian) terms.

- **Force decomposition**: F_total = F_body + F_surface, with F_surface split into a component normal to the surface (S_n = -P*n̂ + S_ν, where S_ν ≈ 0 for most cases so only pressure remains) and a component along the surface (shear stress, tau).
  - When to use: Any time you need to identify what forces act on a chosen control volume.
  - How: Body force is gravity acting through the mass center (Integral of g*rho dV); surface force integrates pressure and shear over the control surface.

- **Integral Momentum Equation (general, RTT form)**: 
  Integral(g*rho dV) - Integral(P dA) + Integral(tau · dA) = d/dt[Integral(rho*U dV)]_cv + Integral(rho*U*U_rn dA)_cv
  - When to use: General unsteady, non-uniform flow through an arbitrary control volume.
  - How: U is the fluid velocity in the reference frame; U_rn is the fluid velocity relative to the (possibly moving) control surface. The last integral is the net momentum flux (out minus in).

- **Integral Momentum Equation with External Forces**: Sum(F_ext) + Integral(g*rho dV) - Integral(P dA) + Integral(tau·dA) = d/dt[Integral(rho*U dV)] + Integral(rho*U*U_rn dA)
  - When to use: Whenever the control volume boundary cuts through a solid (pipe wall, nozzle, support strut) — F_ext is the reaction force from that solid structure.
  - How: This is a vector equation; resolve into Cartesian components (x, y, z) using direction cosines (theta_x = angle between outward normal n̂ and unit vector î, etc.) before solving.

- **Momentum equation in an accelerating (non-inertial) reference frame**: Adds a fictitious "add force" F_add = Integral(a_acc * rho dV), where a_acc = omega x (r x omega) + 2U x omega + r x (domega/dt) - a_0 (centrifugal, Coriolis, angular-acceleration, and translational-acceleration terms).
  - When to use: Control volume attached to an accelerating/rotating body (rockets, carts, rotating machinery frames).
  - How: Compute a_acc from the frame's rotation (omega) and translation (a_0), integrate rho*a_acc over the control volume, and add it to the force balance.

- **Simplified momentum equation for uniform, frictionless, constant-pressure flow**: F = Integral_out(rho*U*U_rn dA) - Integral_in(rho*U*U_rn dA), reducing (when velocity is known/uniform) to F = m_dot * U_out_avg - m_dot * U_in_avg.
  - When to use: Jets exposed to atmosphere, free-surface flows where friction is negligible and pressure is essentially uniform (atmospheric) on the control surface.
  - How: Only need inlet/outlet mass flow rate and average velocities — no need to integrate pressure.

- **Average velocity from a velocity profile**: U_avg^2 = (1/A) * Integral_A[U(r)]^2 dA.
  - When to use: Converting a known (non-uniform) velocity profile into a single bulk velocity for use in the simplified momentum equation.
  - How: Integrate the square of the local velocity over the cross-section and divide by area (this is a momentum-weighted average, not a simple arithmetic mean — see momentum correction factor below).

- **Angular Momentum (Moment-of-Momentum) Equation**: M = r x F = D/Dt[Integral_sys(rho * (r x U) dV)], transformed via RTT to M = d/dt[Integral_cv(rho*(r x U) dV)] + Integral_cv[rho*(r x U)*U_rn dA]. For steady, uniform flow: M = m_dot*(r_2 x U_2 - r_1 x U_1).
  - When to use: Turbomachinery (pumps, turbines, impellers) where torque/shaft work is the quantity of interest, not linear force.
  - How: Apply the same RTT logic as linear momentum but to the moment r x U instead of U; for a centrifugal pump with radial inflow, M = m_dot * r_2 * U_t2 (tangential exit velocity only, since inlet is radial and contributes no moment).

## Key Concepts
- **Control volume (CV) vs system**: The system is a fixed collection of matter (Lagrangian); the control volume is a fixed or moving region in space (Eulerian) — RTT bridges the two.
- **U_rn (relative normal velocity)**: The fluid velocity relative to the control surface, measured in the same reference frame as U; it is what drives momentum flux through a (possibly moving) boundary.
- **External force (F_ext)**: Force transmitted through non-fluid elements (pipe walls, ducts, support structures) that intersect the control volume boundary — this is typically the unknown "reaction force" solved for in pipe/nozzle problems.
- **Body force**: Force acting on every fluid element (in this book, essentially gravity only), integrated over the CV volume and acting through the center of mass.
- **Surface force**: Pressure (normal) plus shear stress (tangential) integrated over the control surface.
- **Add force / fictitious force (F_add)**: The extra force term required when the control volume itself is accelerating or rotating (non-inertial frame), containing centrifugal, Coriolis, and angular-acceleration contributions.
- **Momentum correction factor (C)**: Ratio relating the momentum computed from average velocity to the actual momentum from the true velocity profile; equals 1 only when density (and effectively velocity profile shape) doesn't distort the average — otherwise C != 1.
- **Steady state vs uniform flow**: Steady state means d/dt term vanishes (CV storage doesn't change with time); uniform flow means velocity is spatially constant across the relevant cross-section — the two simplifications are independent and often combined.
- **Effective/relative exit velocity (U_e)**: In rocket problems, U_e = U_gas - U_rocket, the exhaust velocity relative to the accelerating body — the quantity that actually drives thrust.

## Mental Models
- Think of the momentum equation as "Newton's second law dressed up for open systems": forces in equal (rate of momentum stored) plus (net momentum carried across the boundary by flowing mass) — the flux term is the genuinely new piece compared to solid-body mechanics.
- Use the "cut the control volume through the solid" trick when you want to find a reaction/support force: choosing a CV boundary that slices through a pipe wall, bolt, or bracket turns that structural reaction into the unknown F_ext in an otherwise straightforward flux balance.
- Use the accelerating-frame approach (attach the reference frame to the moving body, e.g., a rocket or rolling tank) rather than tracking an accelerating control volume from a fixed frame — it converts a hard unsteady problem into a quasi-steady one at the cost of adding fictitious force terms.
- Think of angular momentum analysis for turbomachinery as "linear momentum equation, but with everything crossed with r" — the same RTT derivation, the same flux logic, just tracking r x U instead of U, which naturally produces torque and shaft power.

## Anti-patterns
- **Assuming average velocity can be used directly in momentum flux without correction**: The momentum flux depends on U^2 integrated over area, not on (average U)^2; using a simple arithmetic mean velocity in place of the true profile silently introduces error unless a momentum correction factor is applied.
- **Ignoring the relative velocity U_rn when the control surface is moving**: Momentum flux must use velocity relative to the (possibly moving/deforming) control surface, not the absolute fluid velocity in a fixed frame — critical for rockets, carts, and any deforming CV problem.
- **Forgetting the "add force" in accelerating/rotating control volumes**: Applying the inertial-frame momentum equation unchanged to a rocket, cart, or rotating machine frame omits the centrifugal/Coriolis/translational-acceleration terms and gives wrong forces.
- **Treating viscous normal stress as significant**: The book explicitly drops S_ν (viscous contribution to normal surface stress) as negligible in most engineering situations, retaining only pressure — including it needlessly overcomplicates the analysis for the typical inviscid-normal-stress assumption used throughout the chapter.
- **Neglecting that mass flow rate stays constant even when velocity direction changes**: In jet-deflection problems (Example 6.2), students sometimes assume speed or mass flow changes when only direction changes; for frictionless, incompressible deflection, |U| and m_dot are conserved even though the momentum vector direction and hence the force vector change substantially.
- **Missing that gravity direction (not magnitude) is what matters in the impinging-jet/block problem**: In Example 6.12, the required jet velocity to move a block is independent of gravity's magnitude for the horizontal balance — gravity's role there is only to keep the liquid falling in the correct direction, a subtlety easy to miss.

## Key Equations
1. **General RTT-based momentum equation**: Sum(F) = D/Dt Integral_sys(rho*U dV) = d/dt Integral_cv(rho*U dV) + Integral_cv(rho*U*U_rn dA). Governs unsteady flow through any control volume; left side is total force, right side splits into storage-rate and flux terms.
2. **Integral momentum with external forces (vector, per-axis)**: Sum(F_ext) + Integral(g·î rho dV) - Integral(P cos(theta_x) dA) + Integral(tau_x dA) = d/dt Integral(rho*U_x dV) + Integral(rho*U_x*U_rn dA). Used component-wise (x, y, z) to solve for unknown support/reaction forces.
3. **Simplified steady, frictionless, uniform-pressure form**: F = m_dot*(U_out - U_in). Applies to jets/free-surface flows exposed to atmosphere with negligible friction; the workhorse equation for jet-force and deflection problems.
4. **Average velocity definition**: U_avg^2 = (1/A) * Integral_A [U(r)]^2 dA. Converts an arbitrary velocity profile (e.g., parabolic laminar profile) into the effective velocity to use in momentum flux calculations.
5. **Rocket equation (velocity vs. time, F_R = 0)**: U(t) = U_e * ln[M_0 / (M_0 - t*M_dot)] - g*t. M_0 is initial total mass (rocket + fuel), M_dot is constant propellant mass flow rate, U_e is effective exhaust velocity relative to the rocket; derived by integrating the differential momentum balance in the rocket's own accelerating frame.
6. **Angular momentum / torque and shaft work for turbomachinery**: M = m_dot * r_2 * U_t2, and shaft power W_dot = m_dot * U_m2 * U_t2 (U_m2 = impeller tip speed = r_2*omega, U_t2 = tangential component of exit liquid velocity). Basis for centrifugal pump/turbine power estimates when inflow is radial (no inlet moment contribution).

## Worked Example
**Nozzle force problem (Example 6.3, reconstructed)**: Liquid (rho = 1000 kg/m^3) flows steadily through a symmetric nozzle. Inlet: area A1 = 0.0005 m^2, velocity U1 = 5 m/s, pressure P1 = 3 bar. Outlet: area A2 = 0.0001 cm^2 (note: as given, tiny), pressure P2 = 1 bar. Nozzle internal volume = 0.0015 m^3.

Step 1 — find exit velocity from continuity (constant density, steady): A1*U1 = A2*U2, so U2 = (A1/A2)*U1 = 25 m/s (using the given area ratio).

Step 2 — choose a control volume enclosing the nozzle and liquid inside it; apply the momentum equation in the axial (z) direction. Since the CV crosses the solid nozzle wall, the unknown nozzle-support reaction force F_nozzle appears as the external-force term. The body force (weight of liquid in the nozzle) is F_b = -g*rho*V_nozzle. The net pressure force on the nozzle from the fluid is P1*A1 - P2*A2 (evaluated at the two open faces). The momentum flux term is rho*(U2^2*A2 - U1^2*A1).

Step 3 — combine: F_nozzle = -g*rho*V_nozzle + P2*A2 - P1*A1 + rho*(U2^2*A2 - U1^2*A1). Plugging in numbers gives the force the nozzle attachment (e.g., a pipe flange or bolted joint) must supply to hold the nozzle in place, combining a weight term, a net-pressure term, and a momentum-change (thrust-like) term. This illustrates the standard method: cut the CV through the solid, isolate F_ext, then evaluate body, pressure, and flux terms separately.

## Key Takeaways
1. The linear momentum equation for a control volume is Newton's second law plus a momentum-flux correction term supplied by the Reynolds Transport Theorem — memorize the RTT structure once and it applies to mass (Ch. 5), momentum (Ch. 6), and (by extension) energy.
2. To find a reaction/support force, deliberately choose a control volume boundary that cuts through the solid structure — the unknown then appears cleanly as F_ext in the force balance.
3. For jets and free-surface flows exposed to atmosphere with negligible friction, the momentum equation collapses to F = m_dot*(U_out - U_in) — no need to evaluate pressure integrals.
4. Average velocity for momentum purposes is a root-mean-square-type average (U_avg^2 = (1/A)Integral U^2 dA), not a simple arithmetic mean; using the wrong average introduces silent error unless a correction factor is applied.
5. Accelerating or rotating control volumes require an explicit "add force" (centrifugal + Coriolis + angular-acceleration + translational terms) — this is the key extra ingredient for rocket and rotating-machinery problems.
6. The angular momentum equation is derived by the same RTT logic applied to r x U instead of U, making it the natural tool for torque and shaft-power analysis in pumps, turbines, and impellers.
7. Mass flow rate is conserved through direction changes (jet deflection) even though the force vector changes substantially — do not confuse "constant speed/mass flow" with "constant momentum vector."

## Connects To
- **Ch 5 (Mass Conservation for Control Volume)**: This chapter directly reuses the Reynolds Transport Theorem established there, now applied to a vector quantity (momentum) instead of a scalar (mass); several worked examples (e.g., the wheeled tank) reuse the Ch. 5 mass-conservation result as a prerequisite step.
- **Turbomachinery / Dimensional Analysis chapters**: The angular momentum equation introduced here is the foundation for pump and turbine performance analysis covered in later chapters; the "add mass/momentum" effect mentioned for the accelerating tank is deferred to the Dimensional Analysis and Ideal Flow chapters.
- **Reynolds Transport Theorem (external concept)**: The general mathematical tool (from continuum mechanics) converting system-based (Lagrangian) conservation laws into control-volume (Eulerian) form; central to this entire chapter's derivations.
- **Rigid-body dynamics / non-inertial reference frames (external concept)**: The centrifugal, Coriolis, and Euler acceleration terms used for the accelerating control volume are the same ones from classical mechanics of rotating frames.
