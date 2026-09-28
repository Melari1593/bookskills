# Chapter 3: Origamic Architecture — A Method of Execution

Source: Philippi Filho, Schmitt & Pupo, "Origamic Architecture: um método de execução," SIGRADI 2014. (Original in Portuguese; terms below preserve the authors' Portuguese vocabulary where it names a specific technique, with English gloss.)

## Core Idea
Origamic architecture (a Masahiro Chatani technique combining origami/fold + kirigami/cut + pop-up/mount) turns a single flat sheet of paper into a self-mounting, freestanding 3D model of a building by defining one reference fold ("linha zero") and deriving every other cut and fold from it — making the whole model a *2.5D* object: neither fully 3D nor fully flat, since faces are cut/folded but the sides stay open.

## Frameworks Introduced
- **Linha zero (zero line) method**: choose one principal fold line as the origin/reference for the entire model; every volume's position, depth and offset is measured as a distance *from* this line, not from the sheet edges.
  - When to use: at the very start of laying out any origamic-architecture model, before drawing any volume.
  - How: pick the fold that will open the model to 90° (the paper's structural spine); place it wherever best captures the object's proportions (not necessarily sheet-center); then define valley and mountain folds at measured distances from it, and vertical/horizontal cuts that release each face from the surrounding sheet.
- **Volumetric-face / sustaining-face pairing**: every representational (volumétrica) face that faces one plane (e.g., vertical) is paired with a sustaining (sustentação) face on the perpendicular plane (e.g., horizontal) that structurally carries it.
  - When to use: whenever adding a new architectural volume (a wall segment, a tower, a stair) to the model.
  - How: draw the volume's visible facade as the volumetric face; add a companion face at 90° to it that will fold flat and anchor to the base sheet, closing the model back to 0° cleanly.
- **90° origamic architecture** (one of four opening-angle families: 0°, 90°, 180°, 360°): the family used for architectural representation because it best exposes constructive detail while folding fully flat for storage/transport.
  - When to use: representing an existing building's facade, or visualizing an early-stage design volume, from one single sheet.
  - How: see the full step-by-step in Worked Example below.

## Key Concepts
- **Origami / Kirigami / Pop-up** — the three source techniques Chatani (1981, Tokyo Institute of Technology) compiled: fold, cut, and self-mounting assembly, respectively.
- **Linha zero (zero line)** — the master fold that defines the model's volumetric relationships; not necessarily centered on the sheet.
- **Plano horizontal / plano vertical** — the two planes created when the sheet folds to 90° at the zero line; the structural base of every model.
- **Dobra vale / dobra montanha (valley / mountain fold)** — the two secondary fold types, always defined relative to the zero line; their mutual distance sets each volume's height/depth.
- **Face volumétrica / face de sustentação (volumetric face / sustaining face)** — see framework above; a face facing one plane always pairs with a sustaining face on the other.
- **Cortes verticais e horizontais (vertical/horizontal cuts)** — cuts that delimit volumetric vs. sustaining faces; their orientation is *coupled* to the zero line's orientation (zero line horizontal → cuts vertical, and vice versa) because that's what lets a face detach from the flat sheet and stand proud in 3D.
- **Detalhes construtivos (constructive details)** — small removed paper areas (windows, ornament, structural articulation) that read as recognizable architectural detail once the model is folded.
- **2.5D** — the authors' term for the model's ontological status: because faces are cut/folded from one sheet, sides are never closed, so it is neither a true 3D solid nor a flat 2D drawing.
- **Opening-angle families** — 0° (single sheet, layered look, closes flat, no assembly of separate pieces), 90° (architecture standard — this chapter's focus), 180° (classic pop-up, needs glued/joined tabs), 360° (full solid volumetric form, typically symmetric, e.g. cubes).

## Mental Models
- Treat the zero line the way a structural engineer treats a spine or keel: everything else in the model is *dimensioned relative to it*, so choosing its position well (not just "the middle of the page") is the single highest-leverage decision in the whole layout.
- A "volume" in this technique is really a *hinge pair*: one face you want people to see (volumetric) always needs an invisible partner face (sustaining) at 90° to it, or the model won't stand up when opened — design in pairs, not single facades.
- Treat perspective distortion as a measurement problem, not an aesthetic one: compare at least two reference photos from different angles before tracing volumes in CAD, specifically to recover true proportions the single "best" photo would otherwise distort.
- Multi-sheet variants (2–3 layered sheets) aren't a different technique — they're the same zero-line logic applied independently per sheet, then registered together; use them when one flat sheet's necessarily-open sides start limiting how much depth/realism a single complex building needs.

## Anti-patterns
- **Digitizing an existing pre-made model's unfolded pattern without re-deriving zero-line relationships**: the authors found that redoing existing published models (Chatani, Siliakus, Bianchini, Aysta) in CAD only clarified the underlying logic once dimensions were re-verified between fold lines and the represented volume — copying the flat pattern visually is not the same as understanding its generative geometry.
- **Tracing a facade from a single, highly foreshortened photo**: produces proportion errors; the method explicitly calls for ≥2 reference images at different angles specifically to cross-check proportions before committing to the zero-line layout.
- **Treating fabrication (laser-cutting settings) as an afterthought**: paper weight (<130 g/m²) and un-tuned laser power/speed/kerf settings were found, in practice, to be discoverable *only* after test cuts — plan a materialization/testing pass into the schedule, don't assume the digital plan transfers 1:1 to the physical cut.
- **Skipping physical mockups/sketches between digital planning and final CAD**: the authors note the creative process required hand sketches and manual paper tests interleaved with CAD, not a single linear "model in CAD → cut" pipeline.

## Reference Tables

| Opening angle | Common name | Behavior when closed | Assembly |
|---|---|---|---|
| 0° | (layered look) | Folds flat; appears to have multiple paper layers | Single sheet only |
| 90° | Standard architecture model | Closes fully flat (90°→0°) | Single sheet only |
| 180° | Pop-up | Opens/views at 180° | May need glued tabs / added paper pieces |
| 360° | Full volumetric | Forms a complete 3D solid (often symmetric, e.g. cubes) | Chatani's dedicated method |

| Material/process parameter | Recommendation |
|---|---|
| Paper weight | > 130 g/m² for a stable, uniform model |
| Cutting method | Laser cutting — fast digital↔physical iteration, precise finish |
| Laser settings | Power/speed tuned per paper weight/type via test cuts (no universal preset given) |
| Layer count | 1 sheet (simple volumes) → 2–3 sheets (complex/layered volumes needing more depth realism) |

## Worked Example
**Step-by-step build of a facade model (illustrated with the Catedral Metropolitana de Florianópolis):**
1. **Choose viewpoint & gather references** — decide which facade/angle to represent (here: front facade); collect ≥2 reference photos from different angles so depth/proportion can be cross-checked.
2. **Block out volumes in 2D CAD (AutoCAD)** — import the least-distorted reference image; mark vertical/horizontal axis limits for each volume you can identify; trace one volume at a time to keep auxiliary construction lines legible.
3. **Cross-check proportions** — compare the two reference images against each other to correct for any remaining perspective distortion; refine each volume's outline with true proportions rather than single-image foreshortening.
4. **Mark constructive details** — add the cut-out details (windows, moldings, structural elements) most relevant to recognizing the building; color-code or hatch each volume/group differently to keep them distinguishable in later steps.
5. **Define the zero line** — choose and draw the master fold that will open/close the whole model at 90°.
6. **Offset each volume from the zero line** — set valley-fold distances one volume at a time (doing them together makes the offsets hard to track); the background reference image can now be deleted, working from derived lines only.
7. **Build the sustaining faces** — mirror the same offset logic onto the horizontal plane, behind each volumetric face, to create its structural sustaining face; where multiple volumes share one sustaining face, subdivide the distances accordingly.
8. **Finalize valley/mountain folds** — mark the fold-type (valley vs. mountain) for every line now that volumetric and sustaining faces are both defined.
9. **Add secondary structures as needed** — e.g., a staircase volume was appended to the cathedral's main body afterward, following the same zero-line-relative geometric logic as the primary volumes — the method composes rather than requiring one monolithic layout pass.
10. **Cut & fold (materialize)** — laser-cut the finished CAD pattern on ≥130 g/m² paper, then fold and self-mount the model.
The authors note the same pipeline generalizes beyond photographed buildings: it works equally from freehand sketches or design-phase drawings, making it usable as an early massing/visualization tool during design, not only for representing already-built architecture.

## Key Takeaways
1. Always establish the zero line before drawing any volume — it is the single reference every other measurement in the model depends on.
2. Design faces in volumetric/sustaining pairs; a facade with no sustaining partner face will not hold its shape when the model opens.
3. Use at least two reference photographs (or views) to counteract single-image perspective distortion before committing proportions to CAD.
4. Treat digital planning (CAD) and physical materialization (paper choice, laser settings) as separate passes needing their own tuning/testing — don't assume digital precision guarantees physical fidelity.
5. The technique scales in complexity via layering (1 → 2 → 3 sheets), not by abandoning the single-sheet zero-line method — added sheets are more instances of the same geometric logic, aligned together.
6. This is fundamentally a *representation and spatial-reasoning* tool as much as a fabrication technique — the authors report that laying out the zero-line relationships builds an understanding of a building's volumetry that a photo or a physical scale model conveys less directly.

## Connects To
- **Ch 1 (Vacuumatics)** and **Ch 2 (Zipper-coupled tubes)**: both engineering chapters describe *rigid, load-bearing, kinematically-foldable* structures; this chapter's models are explicitly non-rigid paper sculpture (faces are flat cut/fold shapes, not moving mechanisms) — useful as a contrasting "representation-only" origami application versus "structural" origami.
- **Descriptive geometry** — the shared mathematical backbone cited by the authors as underlying all origamic-architecture closure conditions (analogous to how Ch 1 relies on rigid-origami kinematics equations).
- **CAD-to-fabrication pipeline** — the same "digitize a flat pattern, physically test-cut, then finalize" loop appears conceptually in Ch 1's discussion of build/deploy staging, though applied there to structural rather than representational models.
