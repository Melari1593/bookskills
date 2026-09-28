# Chapter 8: Differential Analysis

## Core Idea
Integral (control-volume) analysis only gives average, "black-box" answers; to know what the velocity, pressure, and stress are doing at every point in a flow, the conservation laws (mass, momentum) must be written as partial differential equations acting on an infinitesimal fluid element — this is how the continuity equation and the Navier-Stokes equations are derived.

## Frameworks Introduced

- **Differential Continuity Equation (mass conservation, infinitesimal form)**: `d(rho)/dt + div(rho*U) = 0`, equivalently `d(rho)/dt + U·grad(rho) + rho*div(U) = 0`.
  - When to use: any problem where density and/or velocity vary continuously with position and time and a pointwise (not averaged) description is needed.
  - How: start from Reynolds Transport Theorem (RTT) applied to an infinitesimal control volume, convert the surface-flux term to a volume integral with the divergence theorem, and shrink the volume to a point.

- **General Transport (RTT) at a Point**: for any intensive property `phi`, the infinitesimal-volume statement of RTT is `D(Phi)/Dt ≅ [ d(phi*rho)/dt + div(rho*phi*U) ] dV`.
  - When to use: as the master template for deriving *any* differential conservation law (mass with `phi=1`, momentum with `phi=U`, energy with `phi=e`, etc.) — the book explicitly generalizes the derivation this way before specializing to mass and momentum.
  - How: (1) write the system integral of `phi*rho`, (2) apply RTT to move to a control volume, (3) apply the divergence theorem to the surface flux term, (4) combine into one volume integral, (5) let the volume shrink to a point.

- **Substantial (Material) Derivative**: `D()/Dt = d()/dt + (U·grad)()`, splitting acceleration into **local acceleration** `dU/dt` (vanishes at steady state) and **convective acceleration** `(U·grad)U` (can be nonzero even at steady state, e.g., fluid accelerating through a nozzle).
  - When to use: whenever you need the rate of change following a fluid particle rather than at a fixed point.
  - How: expand the total derivative of a field `f(x,y,z,t)` using the chain rule with `dx/dt=Ux`, `dy/dt=Uy`, `dz/dt=Uz`.

- **Newtonian Stress-Rate-of-Strain Relation ("linear/solid continuum model")**: assumes (1) no preferred orientation (isotropic fluid), (2) zero strain rate when shear stress is zero, (3) a linear relation between shear stress and rate of strain. Leads to shear terms `tau_xy = mu*(dUy/dx + dUx/dy)` and normal terms `tau_xx = -Pm + 2*mu*dUx/dx - (2/3)*mu*div(U)`.
  - When to use: for any "ordinary" (Newtonian) viscous fluid where stress must be expressed in terms of the velocity field to close the momentum equation.
  - How: relate shear stress to angular deformation rate of a fluid element; rotate coordinates 45° to relate normal stresses to linear (dilatational) strain rates; combine into the general stress tensor formula `tau_ij = -[P + (2/3*mu - lambda)*div(U)]*delta_ij + mu*(dUi/dxj + dUj/dxi)`.

- **Navier-Stokes Equations** (the chapter's centerpiece): general compressible form
  `rho * DU/Dt = -grad(P) + (mu/3 + lambda) * grad(div(U)) + mu * laplacian(U) + f_B`
  reducing, for incompressible flow (`div(U)=0`), to
  `rho * DU/Dt = -grad(P) + mu * laplacian(U) + f_B`.
  - When to use: this is the governing vector PDE for any Newtonian viscous fluid; the incompressible form is the workhorse used throughout the rest of the book (boundary layers, exact solutions, viscous flow chapters).
  - How: substitute the stress-strain relation into the general momentum-conservation equation `rho*DU/Dt = div(tau) + rho*f_B`, then simplify term by term.

- **Symmetry of the Stress Tensor / Torque Balance**: angular-momentum balance on an infinitesimal cube shows `tau_ij = tau_ji` (for `i≠j`) unless an external body torque `G_T` (e.g., from a non-uniform magnetic body force) exists, in which case `G_T + tau_ij = tau_ji`.
  - When to use: to justify treating the 9-component stress tensor as having only 6 independent components in ordinary (non-polar) fluid mechanics.
  - How: sum moments from shear stresses on opposite faces of a shrinking cube; as the cube size goes to zero, the moment of inertia term vanishes faster than the stress terms, forcing symmetry.

- **Boundary Conditions Framework**: conditions are grouped into velocity (no-slip / slip), pressure, and shear-stress (including surface tension) categories.
  - **No-slip**: `t̂ · (U_fluid − U_boundary) = 0` — fluid velocity matches solid velocity at the interface (valid at large scale; breaks down at very small scale/high fluctuation, where a **slip condition** `t̂·(U_fluid − U_boundary) = f(scale, ...)` is used instead).
  - **Kinematic (free-surface) condition**: `Df/Dt = 0` on the moving surface `f(r,t)=0`, i.e., `df/dt + Ux*df/dx + Uy*df/dy = 0` in 2-D — no fluid crosses the free surface.
  - **Curved-interface stress jump (surface tension)**: `n̂·tau^(n) = sigma*(1/R1 + 1/R2)` for the normal component and `t̂·tau^(t) = -t̂·grad(sigma)` for the tangential component (Marangoni-type driving force from a surface-tension gradient).
  - When to use: needed to close the Navier-Stokes PDEs, which otherwise have infinitely many solutions; choice of condition set depends on scale and whether an interface is present.

## Key Concepts
- **Differential analysis**: examining conservation laws at an infinitesimal (point-wise) scale rather than over a finite control volume, yielding PDEs instead of algebraic/integral balances.
- **Substantial derivative**: `D/Dt`, the derivative following a moving fluid particle; splits into local (`d/dt`) plus convective (`U·grad`) parts.
- **Stress tensor `tau_ij`**: a 3×3 array representing the force per unit area on each of the three coordinate surfaces, in each of the three directions; symmetric in ordinary fluids.
- **Mechanical pressure `P_m`**: `P_m = -(tau_xx + tau_yy + tau_zz)/3`, the negative average of the three normal stresses — a true scalar (coordinate-invariant).
- **Thermodynamic pressure `P`**: `P = P_m + lambda*div(U)`; equals mechanical pressure exactly for incompressible flow or when the bulk viscosity effect is negligible.
- **Bulk (second) viscosity `lambda`**: the "expansion viscosity" coefficient relating dilatation (`div(U)`) to the difference between thermodynamic and mechanical pressure; vanishes for dilute monatomic gases, usually negligible except in shock waves/microfluidics.
- **Isotropic/Newtonian fluid assumption**: stress depends linearly on strain rate with no preferred direction — the "solid continuum model" applied to fluids.
- **No-slip vs. slip condition**: whether the fluid velocity at a solid boundary exactly equals the boundary's velocity (no-slip, valid at macroscopic scale) or differs from it (slip, relevant at small scales/high shear-rate fluctuations).
- **Kinematic boundary condition**: mathematical statement that a free/moving surface is a material surface (no flux across it), `Df/Dt=0`.
- **Interfacial instability**: instability arising at the interface between two fluids (e.g., gas over liquid) especially when one phase's domain becomes effectively infinite, driven by unmatched boundary-condition requirements.

## Mental Models
- Think of the Navier-Stokes equations as **Newton's second law applied to an infinitesimal fluid particle**: `rho*(acceleration) = (net surface force per volume) + (body force per volume)`, with the surface-force term expanded via the stress tensor.
- Use the **general RTT-at-a-point template** (`phi=1` → mass, `phi=U` → momentum) whenever deriving a new differential conservation law — it is one master pattern, not a new derivation each time.
- Treat the **stress tensor's diagonal terms as "pressure-like" and off-diagonal terms as "shear-like"**: rotate the coordinate system 45° to see how normal stress differences relate to angular (shear) strain rates — this is the geometric trick that unlocks the full stress-strain relation.
- View the **thermodynamic vs. mechanical pressure gap as a "relaxation" effect**: whenever a fluid element's volume is changing (`div(U) ≠ 0`), the actual (thermodynamic) pressure tends to lag/lead the average normal stress by an amount controlled by the bulk viscosity `lambda` — for nearly incompressible flow this gap is irrelevant.
- Use **scale as the deciding factor for no-slip vs. slip**: at ordinary engineering length scales, no-slip always holds; only at very small scales (or very sharp velocity fluctuations) does slip need to be modeled.

## Anti-patterns
- **Assuming the stress tensor is automatically symmetric**: it is symmetric only when there is no external body torque (`G_T = 0`); problems with non-uniform magnetic or other torque-producing body forces break this and must retain `G_T + tau_ij = tau_ji`.
- **Treating mechanical and thermodynamic pressure as always identical**: they coincide only when `div(U) ≈ 0` (incompressible or negligible bulk-viscosity effect); conflating them in compressible/shock-wave problems introduces error.
- **Ignoring the convective acceleration term at "steady state"**: steady state kills the local acceleration `dU/dt`, not the convective term `(U·grad)U` — a nozzle flow can be steady yet strongly accelerating.
- **Applying no-slip indiscriminately at very small scales**: at micro/nano scales or under strong velocity fluctuations, forcing no-slip is physically wrong; a slip condition must be used instead.
- **Forgetting that a density jump forces a shear-stress jump unless surface tension compensates**: a discontinuity in shear stress without a compensating force implies infinite acceleration on an infinitesimally thin layer, which is physically impossible — surface tension is what makes such jumps consistent.
- **Losing boundary conditions when idealizing a domain as infinite**: replacing a large-but-finite fluid layer with an "infinite" one (e.g., gas above liquid) can eliminate the conditions needed for a unique 1-D solution and is a known source of interfacial instability, not just a simplification.

## Key Equations

1. **Differential continuity equation (general)**: `d(rho)/dt + div(rho*U) = 0`. Applies to any compressible, unsteady flow; `rho` and `U` are functions of position and time.

2. **Continuity, incompressible / steady simplifications**: steady-state → `div(rho*U) = 0`; incompressible → `div(U) = 0`. Used whenever density can be treated as constant along the flow.

3. **Substantial derivative / acceleration**: `DU/Dt = dU/dt + (U·grad)U`, with `dU/dt` = local acceleration and `(U·grad)U` = convective acceleration. Governs the LHS ("mass × acceleration") of the momentum equation for every fluid particle.

4. **General momentum (Cauchy) equation**: `rho*DU/Dt = div(tau) + rho*f_B`, where `tau` is the stress tensor and `f_B` is body force per unit mass. Valid for any continuum (solid or fluid) before a constitutive law is chosen.

5. **Newtonian constitutive relation**: `tau_ij = -[P + (2/3*mu - lambda)*div(U)]*delta_ij + mu*(dUi/dxj + dUj/dxi)`. Relates stress to the velocity field for an isotropic, linearly-viscous (Newtonian) fluid; `delta_ij` is the Kronecker delta.

6. **Navier-Stokes equations (compressible, vector form)**: `rho*DU/Dt = -grad(P) + (mu/3 + lambda)*grad(div(U)) + mu*laplacian(U) + f_B`. The general governing PDE for Newtonian viscous flow, including bulk-viscosity effects.

7. **Navier-Stokes equations (incompressible form)**: `rho*DU/Dt = -grad(P) + mu*laplacian(U) + f_B`, or component-wise, e.g. in x: `rho*(dUx/dt + Ux*dUx/dx + Uy*dUx/dy + Uz*dUx/dz) = -dP/dx + mu*(d²Ux/dx² + d²Ux/dy² + d²Ux/dz²) + rho*gx`. This is the form used in nearly all subsequent problem-solving in the book.

8. **Mechanical vs. thermodynamic pressure**: `P_m = -(tau_xx+tau_yy+tau_zz)/3` and `P = P_m + lambda*div(U)`. Distinguishes the coordinate-invariant average normal stress from the thermodynamic pressure used in the equation of state; they coincide when `div(U) → 0`.

## Reference Tables
No comparison/property table is present in the scraped source for this chapter (it is derivation- and example-driven rather than tabular).

## Worked Example
**Example 8.1 — unsteady 1-D mass conservation with temperature-dependent density** (reconstructed compactly):

A liquid layer of initial height `H0` at uniform temperature `T0` has its top surface suddenly exposed to a new temperature `T1`. The temperature profile relaxes from uniform toward a linear profile over height, following `(T-T0)/(T1-T0) = alpha*(H0-y)/H0 * (1 - e^(-beta*t))`, and density is linearly tied to temperature via `(T-T0)/(T1-T0) = alpha*(rho-rho0)/(rho1-rho0)`. The velocity is assumed to depend only on `y`, with `Uy(y=0)=0` (bottom is stationary).

1. Start from the unsteady, 1-D continuity equation: `d(rho)/dt + d(rho*Uy)/dy = 0`.
2. Substitute the known `rho(y,t)` expression (derived by combining the two relations above) so the only unknown left is `Uy(y,t)`.
3. The result is a first-order ODE in `y` (with `t` as a parameter): differentiate the time-part of `rho` to get `d(rho)/dt`, plug into continuity, and integrate the remaining equation with respect to `y`.
4. Apply the boundary condition `Uy(y=0)=0` to fix the integration "constant" (actually an arbitrary function of `t`).
5. The final velocity field, `Uy(y,t) = beta*[(2H0-y)/(2(H0-y))] * [e^(-beta*t)/(1-e^(-beta*t))] * (1-y)`, shows that even though no external velocity is imposed, thermally-driven density changes alone induce a nonzero, time- and space-dependent velocity field — a direct illustration of how the continuity equation alone (given a known density field) can determine the flow.

The chapter also works three related variants: coating-flow with density varying in the flow direction (Example 8.2), a 2-D incompressible check where `Uy` is found from a given `Ux` and, separately, from an exponential density field (Example 8.3), a test for whether a candidate velocity field can physically exist and whether it is steady/incompressible via the divergence of `U` (Example 8.4), and a compressible 1-D problem solved by separation of variables where a complex-valued (impossible) branch of the solution is discarded on physical grounds (Example 8.5).

## Key Takeaways
1. The differential continuity equation `d(rho)/dt + div(rho*U) = 0` and its incompressible reduction `div(U)=0` are obtained from the same RTT-based derivation used for any conserved quantity — mass is just the `phi=1` case.
2. Acceleration of a fluid particle always splits into local (`dU/dt`) and convective (`(U·grad)U`) parts; "steady state" only removes the local part.
3. The Navier-Stokes equations follow from substituting a linear (Newtonian) stress-strain relation into the general Cauchy momentum equation `rho*DU/Dt = div(tau) + rho*f_B`.
4. The stress tensor is symmetric only in the absence of body torque; otherwise `G_T + tau_ij = tau_ji`.
5. Mechanical pressure (average normal stress) and thermodynamic pressure differ by a bulk-viscosity term `lambda*div(U)`, which is negligible for incompressible flow but can matter in shocks/microscale flows.
6. Solving the Navier-Stokes equations requires boundary conditions on velocity (no-slip/slip), pressure, and shear stress (including surface tension at interfaces); an interface with density and shear-stress jumps requires a surface-tension-driven jump condition to remain physical.
7. A candidate velocity field must satisfy continuity before it can be considered physically admissible; checking `div(U)` also reveals whether a flow is (in)compressible and whether it can persist indefinitely.

## Connects To
- **Ch 4 (Integral/Control Volume analysis)**: differential analysis is presented explicitly as the higher-resolution successor to integral analysis — RTT is reused, just applied at the point level.
- **Ch 9 (Ideal Flow / Euler equations)**: obtained by dropping the viscous terms (`mu=0`) from the Navier-Stokes equations derived here.
- **Boundary Layer Theory (Prandtl)**: the historical bridge the chapter cites between the mathematically simpler ideal-flow (Euler) equations and the experimentally-driven full Navier-Stokes equations.
- **Real Fluids / Turbulence chapters**: the chapter explicitly defers discussion of "non-regular" (non-unique, unstable) Navier-Stokes solutions to these later chapters.
- **Multi-Phase Flow chapter**: interfacial instability, introduced briefly here via the two-layer (gas/liquid) shear-flow example, is developed fully there.
- **Dimensional Analysis chapter**: the non-dimensionalization of the two-layer flow constants (`C1, C2, C3`) done at the end of this chapter is flagged as gaining fuller physical meaning once dimensional analysis is covered.
- **Surface tension / interface concepts**: the curved-surface stress-jump boundary condition connects directly to surface-tension theory used elsewhere in the book (e.g., capillary and free-surface problems).
