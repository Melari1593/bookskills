# Patterns — Origami Engineering

## Vacuum-Modulated Hinge Stiffening
**When to use**: A rigid-foldable structure must be flat-packed/transported, then field-deployed to a target 3D shape, then hold that shape under load — without adding a separate lock/brace mechanism that would prevent re-folding.
**How**: Offset double-layer panels to avoid self-collision across the full fold-angle range. Pack loose particles (in a breathable sleeve) into the gap on only the valley-fold side of each hinge. Seal panels + particles + fabric in one airtight membrane. Apply a light vacuum during folding/deployment (particles stay mobile → hinge is plastic); strengthen the vacuum once the target shape is reached (particle friction locks → hinge is rigid). Release vacuum to re-fold/reuse.
**Trade-offs**: Gains reversible, actively-tunable stiffness and eliminates the need for locking rods; costs an added pneumatic subsystem (membrane, vacuum source, seal maintenance) and introduces an unavoidable small one-directional bending moment at every hinge (must be accounted for, though it is repurposed as a benefit near the flat state).

## Singularity Bias at the Flat State
**When to use**: Any rigid-origami mechanism must be actuated starting from its fully-unfolded (flat) configuration, where the governing kinematic equations are singular and a naive linearization can select an invalid fold direction.
**How**: Introduce a small, deliberately asymmetric perturbation consistent with the intended mountain/valley and convex/concave assignment before beginning actuation — e.g., a one-sided vacuum-induced moment (Ch 1), or equivalently any asymmetric pre-load/pre-bias engineered into the hinge design.
**Trade-offs**: A tiny, well-placed bias removes the need for external jigs or careful manual guidance at start-up; get the bias direction wrong (or omit it) and the structure can fold into an unintended, invalid branch.

## Boundary-Vertex Form-Finding
**When to use**: Controlling the 3D shape of a large multi-DOF rigid-origami mesh where DOF ≈ V₀ + 3 (boundary-vertex count dominated), so the interior is heavily overconstrained relative to a handful of boundary degrees of freedom.
**How**: Pin most (not all) boundary vertices, leaving a controlled excess of constraints (~V₀/6). Formulate ground/user constraints alongside the edge-length (rigidity) constraints as one stacked system `[C]{Δx}=0`; solve for the minimum-norm update via Moore–Penrose pseudo-inverse from an arbitrary user-driven estimate `Δx₀`. Move the pinned vertices along planar paths to sweep the whole 3D form.
**Trade-offs**: Because the system is overconstrained, arbitrary boundary configurations are not reachable — only paths consistent with the mesh's rigidity are valid; requires iterative numeric solving (e.g., via a tool like Freeform Origami) rather than closed-form placement.

## Zipper Coupling for Isotropic Stiffness
**When to use**: Need a rigid-foldable tube/panel assembly that deploys along exactly one soft motion but resists bending/twisting/point loads from any direction once in a working configuration.
**How**: Take two identical rigid-foldable tubes (e.g., Miura-ori derived). Rotate one tube (not just translate) in its cross-sectional plane until opposing faces zig-zag-align with the other tube's faces. Bond/adhere the aligned adjacent facets. Verify via eigenvalue bandgap analysis (β = λ₈ − λ₇) that the rigid-folding mode remains cheap while all others become expensive.
**Trade-offs**: Delivers ~2-orders-of-magnitude stiffness bandgap and near-isotropic off-axis stiffness versus simple aligned/internal coupling; requires more careful fabrication/bonding geometry (rotation + facet matching) than a simple translated stack.

## Partial-Length Coupling for Tunable End Compliance
**When to use**: A long deployable tube needs a rigid, stiff mid-span but must still fold/unfold freely at its two ends (e.g., an actuator or a connector to an outer rigid frame).
**How**: Apply zipper coupling only to the middle portion of two paired tubes; leave the end sections uncoupled so they can still squeeze/bend during actuation while the coupled middle resists global bending/squeezing.
**Trade-offs**: Buys local flexibility exactly where it's needed (ends) without sacrificing the global stiffness benefit in the coupled span; the transition zone between coupled and uncoupled sections needs careful detailing to avoid stress concentration.

## Zero-Line-First Layout (Origamic Architecture)
**When to use**: Designing any single-sheet 90° origamic-architecture model of a building, facade, or design-phase massing study.
**How**: Choose and draw the zero line (master fold) first, positioned to best capture the represented object's proportions. Derive every subsequent volume as a volumetric-face/sustaining-face pair, each offset from the zero line by measured valley/mountain-fold distances. Add vertical/horizontal cuts perpendicular to the zero line to release each face. Only after all volumes and folds are placed, laser-cut on ≥130 g/m² paper.
**Trade-offs**: Produces a single-sheet, fully self-mounting, flat-storable model with strong geometric consistency; limited to what one sheet's necessarily-open sides can represent — deeper/more complex buildings require the layered multi-sheet variant instead.

## Multi-Reference-Image Proportion Correction
**When to use**: Tracing a building's volumes into CAD from photographs, where a single photo's perspective would distort proportions.
**How**: Gather at least two reference photographs from different viewing angles. Trace preliminary volume outlines from the least-distorted image, then cross-check and correct dimensions against the second image before finalizing offsets from the zero line.
**Trade-offs**: Meaningfully improves dimensional accuracy of the finished model versus single-image tracing; adds an extra comparison/correction pass to the workflow and requires photographs (or views) that actually show the needed angles.
