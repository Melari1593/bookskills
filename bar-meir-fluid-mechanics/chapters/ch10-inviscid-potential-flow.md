# Chapter 10: Inviscid Flow or Potential Flow

## Core Idea
When viscosity is neglected (Euler equations) and the flow is additionally irrotational, the velocity field collapses to the gradient of a single scalar (the velocity potential) or, in 2D, can be paired with a stream function — both satisfying the linear Laplace equation, so complex flows (uniform flow past a cylinder, lifting airfoils) can be built by simple superposition of a handful of elementary solutions, with lift ultimately traced to circulation via the Kutta-Joukowski theorem.

## Frameworks Introduced
- **Euler Equations**: rho*(dU/dt) = -grad(P) - grad(rho*g*l), the Navier-Stokes equations with all viscous (shear) terms dropped, written per-axis in Cartesian coordinates.
  - When to use: Any flow where viscous stresses are negligible compared to pressure and inertia forces (high Reynolds number, away from solid boundaries and wakes).
  - How: Start from the full momentum equation, discard the viscous term, and manipulate the convective term using the vector identity U*dU/di = (1/2)*d(U^2)/di, which exposes the vorticity (curl U) explicitly.

- **Bernoulli's Equation on a Streamline**: dU/dt + U^2/2 + g*l + Integral(dP/rho) = f(t), valid along a single streamline for any inviscid flow (rotational or not), where f(t) can differ from one streamline to the next.
  - When to use: Rotational (viscous-history but currently inviscid-modeled) flow where you only need to relate two points that lie on the same streamline.
  - How: Integrate the Euler equation along the direction of U (dl), using U x curl(U) is perpendicular to U so its dot product with U vanishes.

- **Bernoulli's Equation for Irrotational (Potential) Flow**: d(phi)/dt + (grad phi)^2/2 + g*l + Integral(dP/rho) = f(t), where f(t) is now the SAME function everywhere in the field, not just along one streamline.
  - When to use: Whenever the flow is irrotational — lets you relate ANY two points in the flow field, not just points on a common streamline.
  - How: Substitute U = grad(phi) into the streamline Bernoulli derivation; because curl(grad phi) = 0 identically, the vorticity term drops out everywhere, and the gradient of the whole bracket is zero, so the bracket itself is a function of time only.

- **Velocity Potential (phi)**: U = grad(phi). Exists if and only if the flow is irrotational (curl U = 0), since curl(grad phi) = 0 identically by Clairaut/Schwarz's theorem on mixed partials.
  - When to use: 2D or 3D irrotational flow; reduces three unknown velocity components to one unknown scalar.
  - How: Differentiate phi in each coordinate direction to get the velocity components (Ux = d(phi)/dx, etc.); phi automatically satisfies irrotationality, and continuity (div U = 0) then forces phi to satisfy Laplace's equation.

- **Stream Function (psi), 2D**: Defined by Ux = d(psi)/dy and Uy = -d(psi)/dx; automatically satisfies the 2D continuity equation for any psi.
  - When to use: 2D (or axisymmetric) incompressible flow, rotational or not, when you want continuity satisfied automatically and a direct handle on flow rate and streamline shape.
  - How: Pick psi such that its cross-derivatives reproduce continuity identically; the difference psi_2 - psi_1 between two streamlines equals the volumetric flow rate crossing any line joining them; psi is constant along a streamline.

- **Superposition Principle for Potential Flows**: Because both phi and psi satisfy the linear Laplace equation, any linear combination of elementary solutions (uniform flow, source, sink, vortex, doublet, sector flow, etc.) is itself a valid potential flow.
  - When to use: Building the flow around a specific shape (e.g., a cylinder, a wing, a sharp corner) from known elementary building blocks.
  - How: Add the stream functions (or potentials) of the elementary flows; the boundary condition psi = constant on a candidate body surface identifies which combination represents flow around that shape (e.g., uniform flow + doublet = flow around a cylinder; add a vortex to introduce lift).

- **Complex Potential Method**: F(z) = phi(x,y) + i*psi(x,y), z = x + i*y; if F is analytic (Cauchy-Riemann equations hold), the complex velocity W(z) = dF/dz = Ux - i*Uy is independent of the direction of differentiation.
  - When to use: 2D potential-flow problems where an analytic-function representation is convenient (uniform flow at an angle, flow in a sector/corner, flow around sharp edges) — cannot be generalized to 3D.
  - How: Choose F(z) so that Cauchy-Riemann equations (d(phi)/dx = d(psi)/dy, d(phi)/dy = -d(psi)/dx) are satisfied automatically; both phi and psi then satisfy Laplace's equation for free, and W*conjugate(W) = Ux^2 + Uy^2 gives the speed squared needed for Bernoulli.

- **Circulation and the Kutta-Joukowski Theorem**: Circulation Gamma = closed-loop-integral of U dot ds. Lift per unit span L = -rho_infinity * U_infinity * Gamma.
  - When to use: Computing lift on a cylinder or airfoil once the circulation generated by the body/wake is known (or assumed via the Kutta condition at a sharp trailing edge, mentioned but not derived in this chapter).
  - How: Superpose a free vortex of strength Gamma onto a symmetric doublet-in-uniform-flow (cylinder) solution; the resulting asymmetric surface pressure integrates to a net transverse force equal to rho*U0*Gamma (the Magnus effect).

## Key Concepts
- **Irrotational flow**: A flow field with zero vorticity (curl U = 0) everywhere; mathematically identical to "potential flow" — the two terms are used interchangeably in this chapter.
- **Vorticity (Omega)**: Omega = curl(U) = grad x U; the quantity whose vanishing defines irrotational/potential flow and whose presence limits Bernoulli's equation to single streamlines.
- **Stagnation point**: A point where the local velocity is zero; on a body immersed in potential flow, located where the stream function value matches the body's constant-psi contour.
- **Doublet (dipole)**: The limiting case of a source and sink of equal strength brought together while their product (strength x separation) stays finite; combined with uniform flow it produces the classic potential-flow solution for a circular cylinder.
- **D'Alembert's Paradox**: A symmetric potential-flow solution (e.g., plain uniform flow past a cylinder, no circulation) predicts exactly zero net drag force, contradicting real (viscous) experience.
- **Magnus effect**: The transverse force (lift) produced when translation is combined with circulation/rotation (e.g., a spinning ball or cylinder), explained here through asymmetric surface pressure from superposed circulation.
- **Complex velocity W(z)**: W(z) = dF/dz = Ux - i*Uy; a single complex-valued function that packages both velocity components and is convenient for polar-coordinate manipulations (W = (Ur - i*U_theta)*e^{-i*theta}).
- **Axisymmetric flow**: A true stream function exists in 3D only for flows whose properties are independent of one coordinate direction (e.g., flow around a body of revolution); a fully general 3D stream function does not exist in closed analytic form (a vector stream function using two scalar functions, psi and chi, was proposed by Yih but has limited practical use).

## Mental Models
- Use the irrotational-flow Bernoulli equation when you need to compare pressure/velocity between two arbitrary points anywhere in the field; use the streamline Bernoulli equation when the flow may be rotational but you only need to relate points along one traced streamline — conflating the two is the single most common error in this topic.
- Think of the stream function as a running "flow-rate odometer": its value at any point tells you (relative to a reference streamline) how much volumetric flow has passed to one side, so the difference between two streamlines is literally the flow rate between them.
- Treat potential-flow superposition the way you would electrostatics or heat-conduction superposition: because Laplace's equation is linear, elementary "charges" (sources, sinks, vortices, doublets) can be placed and added freely, and the boundary shape simply falls out of where the combined stream function happens to equal a constant.
- Use the complex-potential/complex-velocity formalism as a shortcut around solving PDEs directly in 2D: pick an analytic function F(z), and the real and imaginary parts automatically hand you a valid (phi, psi) pair with continuity and irrotationality baked in.

## Anti-patterns
- **Applying the irrotational Bernoulli equation between two points that are not connected by a demonstrated irrotational path**: if any vorticity exists anywhere between the points, only the streamline form of Bernoulli's equation (same streamline only) is valid — treating the field-wide form as universally applicable silently introduces error in rotational (e.g., boundary-layer or wake) regions.
- **Trusting D'Alembert's paradox (zero drag) as physically complete**: symmetric potential flow gives zero drag only because viscosity has been discarded; real bodies always experience drag from boundary layers and separation, so potential flow should be understood as a limiting idealization, not a drag prediction tool.
- **Dismissing the Magnus effect as an "optical illusion"**: the chapter notes some historically dismissed the spinning-ball/cylinder lift effect, but it is a real, physically grounded phenomenon — viscosity is the mechanism that actually generates the circulation, which inviscid potential-flow theory then represents mathematically via a superposed vortex.
- **Assuming a stream function exists for general 3D flow**: a true scalar stream function is only guaranteed in 2D or axisymmetric 3D flow; for general 3D flow, no fully analytic stream-function representation is known (the Yih vector-potential approach exists but is of limited practical utility).
- **Forgetting the circulation limit on a lifting cylinder**: the doublet + free-vortex model only keeps stagnation points on the cylinder surface while |Gamma| <= 4*pi*U0*a; exceeding this bound moves the stagnation points off the body entirely, changing the flow topology.

## Key Equations
1. **Euler equation (vector form)**: rho*(dU/dt) = -grad(P) - grad(rho*g*l). The inviscid momentum equation underlying everything else in the chapter.
2. **Bernoulli on a streamline**: dU/dt + U^2/2 + g*l + Integral(dP/rho) = f(t). General (possibly rotational) inviscid result, valid only along one streamline.
3. **Bernoulli for irrotational flow**: d(phi)/dt + (grad phi)^2/2 + g*l + Integral(dP/rho) = f(t), with U = grad(phi). Valid between any two points in the field.
4. **Stream function / velocity relations (2D)**: Ux = d(psi)/dy, Uy = -d(psi)/dx, giving d^2(psi)/dx^2 + d^2(psi)/dy^2 = 0 (Laplace's equation) when the flow is also irrotational; flow rate between streamlines is Q_dot = psi_2 - psi_1.
5. **Complex potential and velocity**: F(z) = phi + i*psi, W(z) = dF/dz = Ux - i*Uy, with Cauchy-Riemann conditions d(phi)/dx = d(psi)/dy and d(phi)/dy = -d(psi)/dx guaranteeing both phi and psi satisfy Laplace's equation.
6. **Kutta-Joukowski lift theorem**: L = -rho_infinity * U_infinity * Gamma, with Gamma = closed-loop-integral of U dot ds; for the doublet+vortex cylinder this reduces to L = U0 * rho * Gamma per unit length.

## Reference Tables
**Table 10.1 — Basic 2D Solutions to Laplace's Equation** (stream function psi, potential function phi, complex potential F(z)):

| Name | Stream Function psi | Potential Function phi | Complex Potential F(z) |
|---|---|---|---|
| Uniform flow in x | U0*y | U0*x | U0*z |
| Uniform flow in y | U0*x | -U0*y | U0*z |
| Uniform flow at angle | U0y*y - U0x*x | U0x*x + U0y*y | (U0x - i*U0y)*z |
| Source (strength Q) | (Q/2*pi)*theta | (Q/2*pi)*ln(r) | (Q/2*pi)*ln(z) |
| Sink (strength Q) | -(Q/2*pi)*theta | -(Q/2*pi)*ln(r) | -(Q/2*pi)*ln(z) |
| Vortex (strength Gamma) | -(Gamma/2*pi)*ln(r) | (Gamma/2*pi)*theta | -i*(Gamma/2*pi)*ln(z) |
| Sector flow, angle pi/n | U*r^n*sin(n*theta) | U*r^n*cos(n*theta) | U*z^n |
| 90-degree sector (n=2) | U*r^2*sin(2*theta) | U*r^2*cos(2*theta) | U*z^2 |

Note: the source text's rows for "Doublet" and "Dipole" appear scrambled/duplicated in the original scrape (both list vortex-like log expressions); the reliable elementary building block used later in the chapter is the doublet formed from a source-sink pair in the limit of zero separation, combined with uniform flow to form the classic cylinder solution (psi = U0*r*sin(theta)*(1 - (a/r)^2)).

## Worked Example
**Cylinder with circulation (lift-generating superposition), based on the chapter's Section 10.3.1.1.**

Start from the potential-flow solution for a cylinder of radius a in a uniform stream U0 (a doublet superposed on uniform flow), which by itself is symmetric and produces zero lift and zero drag. Add a free vortex of strength Gamma centered on the cylinder axis. The combined stream function is:

psi = U0*r*sin(theta)*(1 - (r/a)^2) + (Gamma/(2*pi))*ln(a/r)

This still satisfies psi = 0 on r = a, so the body remains a perfect circle. The resulting surface (r=a) tangential velocity becomes U_theta = 2*U0*sin(theta) + Gamma/(2*pi*a) — no longer symmetric top-to-bottom once Gamma != 0.

Stagnation points (where U_theta = 0 on the surface) satisfy sin(theta) = -Gamma/(4*pi*U0*a). For example, with Gamma = -2*sqrt(2 - sqrt(3))*pi*U0*a, this gives sin(theta) = sqrt(2 - sqrt(3))/2, so theta = 15 degrees and 165 degrees — the two stagnation points have moved off the front/back of the cylinder and sit near the top. This only works while |Gamma| <= 4*pi*U0*a; beyond that bound, no real solution exists on the surface and the stagnation points detach from the body.

Using Bernoulli's equation, the surface pressure P(theta) = P0 - (1/2)*rho*(U_theta)^2 is now a parabolic (but asymmetric) function of sin(theta). Integrating the vertical component of pressure around the full circle, all odd-power sine terms integrate to zero over 0 to 2*pi except the cross term, leaving:

L = -(rho*U0*Gamma/(pi*a)) * Integral_0^{2pi}(sin^2(theta) d(theta)) * a = U0*rho*Gamma

So a cylinder with no circulation produces exactly zero net force (D'Alembert's paradox, confirmed by symmetry), but adding circulation Gamma produces a net lift proportional to U0*Gamma — this is the Magnus effect, and it generalizes (via the Kutta-Joukowski theorem, L = -rho*U_infinity*Gamma) to arbitrarily shaped bodies including airfoils, where the physical vortex-shedding at a sharp trailing edge is what sets the effective circulation in the real (viscous) flow.

## Key Takeaways
1. Two distinct Bernoulli equations exist in inviscid flow: one restricted to a single streamline (valid even if the flow is rotational) and one valid field-wide (only if the flow is irrotational/potential) — always check which condition your problem actually satisfies before applying either.
2. Every potential flow is irrotational and every irrotational flow is potential (they are the same condition, curl U = 0), which is what allows a single scalar potential phi to replace the full vector velocity field.
3. The stream function psi automatically satisfies 2D continuity by construction, and the difference between its values on two streamlines directly gives the volumetric flow rate between them — a compact, physically meaningful bookkeeping device.
4. Because Laplace's equation is linear, complicated potential flows (cylinders, corners, lifting bodies) are built by superposing elementary solutions (uniform flow, source/sink, vortex, doublet) — memorize the elementary building blocks, not the compound answers.
5. The complex-potential method (F(z) = phi + i*psi with Cauchy-Riemann conditions) turns 2D potential-flow problems into analytic-function problems, avoiding direct PDE solving, but it does not generalize to three dimensions.
6. Lift in potential-flow theory comes entirely from circulation (Kutta-Joukowski theorem, L = -rho*U_infinity*Gamma); a purely symmetric potential-flow body (no circulation) always has zero net force (D'Alembert's paradox), so any real lift or drag prediction ultimately needs a physical (viscous) mechanism to justify a nonzero Gamma.
7. A true stream function exists only in 2D or axisymmetric 3D flow — do not expect a simple scalar stream function to exist for fully general three-dimensional flow fields.

## Connects To
- **Ch 9 (viscous/Navier-Stokes flow)**: Potential flow is the inviscid limit of the full Navier-Stokes equations obtained by dropping the viscous stress terms; it is valid away from boundary layers and wakes where the viscous terms this chapter discards actually dominate — the source of D'Alembert's paradox and the real mechanism behind circulation and drag.
- **Ch 5/6 (mass and momentum conservation)**: The continuity equation reappears here as the requirement that the stream function's mixed partials cancel, and the Euler equation is simply the momentum equation with viscous stress removed.
- **External concept — Aerodynamics/airfoil theory**: The Kutta-Joukowski theorem and the mention of a sharp trailing edge (Kutta condition) connect directly to how real wings generate and sustain circulation via vortex shedding, a topic developed further in dedicated aerodynamics texts.
- **External concept — Complex analysis**: The complex-potential method relies directly on Cauchy-Riemann equations and analytic function theory from complex variables; understanding conformal mapping extends this chapter's 2D methods to more complex geometries.
