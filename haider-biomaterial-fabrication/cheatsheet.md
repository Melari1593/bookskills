# Cheatsheet: Numbers & Decision Rules

## Pore Size by Target Function

| Pore size | Function | Source |
|---|---|---|
| ~20 µm | Hepatocyte/fibroblast growth | Ch1 |
| 20–150 µm | Soft-tissue healing | Ch1 |
| 0.5–10 µm | Nutrient/physical-stimuli transport | Ch8 |
| 50–300 µm | Cell penetration, neovascularization | Ch8 |
| 200–400 µm | Bone tissue engineering | Ch1 |
| 3–250 µm (hierarchical) | Combined neo-tissue formation + uniform cell distribution | Ch8 |

## Porosity by Technique

| Technique | Porosity | Notes |
|---|---|---|
| Solvent casting/particulate leaching (baseline) | 50–90% (up to 500 µm pores) | Ch1, Ch8 |
| Solvent casting/particulate leaching (Mikos baseline) | 20–50% (30–300 µm pores) | Ch2 |
| Melt molding/particulate leaching | 80–84% | Ch2 |
| Gas foaming | up to 85% (closed-pore risk) | Ch1 |
| Gas foaming-salt leaching (PCL/elastin) | 91% (540 µm avg pore) | Ch8 |
| High-compression molding-salt leaching | 81.5–82.7% | Compressive modulus ~4.64 MPa, comparable to cancellous bone (2–10 MPa) |
| SLUP (bioglass/chitosan) | 90% | No solvent/heat |
| SCPL, PLA with chloroform | 93.3% | Highest among tested solvents |
| Compression Molding/Particulate Leaching (NaCl) | 50–90%, 10–1000 µm pores | Ch10 |
| Compression Molding/Particulate Leaching (gelatin) | 36–70%, 106–710 µm pores | Ch10 |
| Injection Molding/Particulate Leaching (tubular PLGA) | up to 94% | Ch10 |
| Extrusion/Particulate Leaching (double porogen) | >60%, >97% connectivity | NaCl + PEG | Ch10 |
| Microcellular foam injection molding (TPU/PLA) | 49–79% (115–252 µm pores) | Ch10 |
| Fused deposition modeling (honeycomb PCL) | 61% | Ch2 |
| FDM lattice geometries | Highly tunable | CAD-precise |

## Temperature & Thermal Parameters

| Parameter | Value | Context |
|---|---|---|
| Freeze-drying eutectic point (aqueous) | −40 to −80 °C | Ch3 |
| PCL organic-solvent freeze-drying | −80 °C | Ch3 |
| Camphene freeze-casting sinter (zirconia) | 1450 °C | Ch3 |
| Ceramic nanofiber calcination (TiO2) | 700 °C | Ch4 |
| Glass-wool CS spinning head | 900–1100 °C | Ch4 |
| PCL glass-transition temperature | −60 °C | Ch5 |
| PCL melting point | 60 °C | Ch5, Ch9 |
| High-compression molding | 180–220 °C, up to 640 MPa | Ch8 |
| Gas foaming melt (PCL/elastin) | 70 °C, 65 bar CO2 | Ch8 |
| Gas foaming (scCO2, Bak et al.) | 50 °C, 8 MPa | Ch8 |
| MPL cytocompatible wavelength floor | ≥365 nm (254 nm damages DNA) | Ch7 |
| MPL cell-safe pulse energy | <1.5 nJ (ablation >1.5 nJ; death >4 nJ) | Ch7 |

## Solution Viscosity & Spinning Parameters

| Parameter | Value | Technique |
|---|---|---|
| Electrospinning optimal viscosity | 1–200 poise | Ch5 |
| Electrospinning voltage | 10–50 kV | Ch5 |
| Centrifugal spinning rotational speed | 3,000–12,000 rpm | Ch4 |
| Centrifugal spinning fiber diameter | 25 nm – 50 mm | Ch4 |
| Solution blow spinning fiber diameter | 40 nm – several mm | Ch4 |
| CS production rate | up to 1 mL/min/nozzle | Ch4 |
| SBS production rate | ~20 mL/min | Ch4 |
| Directional freezing pore-spacing tuning | 10–100 µm/s freeze rate → 12–50 µm spacing | Ch3 |

## Solvent Choice Effects (PLA, SCPL)

| Solvent | Effect |
|---|---|
| Chloroform (CF) | Highest porosity (93.3%) |
| Dichloromethane (DCM) | Best thermal stability |
| Hexafluoroisopropanol (HFIP) | Density variation |

## Technique Selection by Constraint

| Constraint | Reach for |
|---|---|
| Solvent-free required | Gas foaming, gas foaming-salt leaching, SLUP, wire-network molding, camphene freeze-casting |
| Nanofiber mesh, no voltage/conductivity requirement | Centrifugal spinning, solution blow spinning |
| Nanofiber mesh, drug-loading flexibility | Electrospinning (blending/coaxial/emulsion/melt) |
| Patient-specific geometry | 3D printing (any of 7 AM categories) |
| Living cells positioned during fabrication | Bioprinting, MPL (cell-safe energy window) |
| True 3D nanoscale ECM-mimicking resolution | Multiphoton lithography |
| Aligned/anisotropic porous channels | Directional freeze-drying |
| Simple, cheap, tunable porosity | Particulate/salt leaching |
| Load-bearing mechanical strength | High-compression molding-salt leaching, injection molding |
| Tubular/continuous-profile geometry (vascular, nerve) | Extrusion + particulate leaching |
| Complex organ microarchitecture (liver, kidney) | Supramolecular self-assembly (bottom-up) |
| Ceramic/metal porous scaffold | Camphene freeze-casting, powder bed fusion (SLS/SLM) |
| Fine, uniform porosity, no porogen at all | Microcellular foam injection molding |
| Avoid burst drug release | Core/sheath or coaxial electrospinning |

## Biomaterial Class Quick-Pick

| Need | Class | Trade-off |
|---|---|---|
| Hardness/osteoinductivity | Ceramic | Brittle, slow degradation |
| Bioactivity/cell adhesion | Natural polymer | Rapid degradation, low mechanical strength |
| Tunable degradation | Synthetic polymer | Lower biocompatibility/mechanical strength |
| Load-bearing | Metal | Poor cell adhesion, ion leaching/corrosion risk |
| High biocompatibility + mechanical | Composite | Processing complexity |
| Tunable + biocompatible + controlled degradation | Hydrogel | Lengthy/complex procedure |

## Polymer Mechanical Properties (selected, salt-leaching context)

| Polymer | E (GPa) | Tensile Strength σ (MPa) | Elongation ε (%) |
|---|---|---|---|
| PGA | >6.9 | >68.9 | 15–20 |
| PLLA | 2.4–4.2 | 55.2–82.7 | 5–10 |
| PLGA | 1.4–2.08 | 41.4–55.2 | 3–10 |
| PCL | 0.21–0.34 | 20.7–34.5 | 300–700 |
| Silk fibroin | 9.860 | 513 | 23.4 |
| PVA | 37–45 (67–110 hydrolyzed) | 225–445 | — |

## Photoinitiators for Cell-Present MPL

| PI | Type | Wavelength | Water solubility |
|---|---|---|---|
| Irgacure 2959 | I | ~365 nm | ~1 wt% |
| LAP | I | 300–400 nm | ~8.5 wt% |
| Rose bengal | II | Visible | — (needs co-initiator) |
| Camphorquinone | II | Visible | — (needs co-initiator) |

## Salt/Porogen Loading Rule of Thumb

- ≥70% w/w salt loading → high pore interconnectivity (particulate leaching)
- ≥70% porosity → recommended for bone/cartilage regeneration (physiological ECM distribution approximation)
- Double-porogen (e.g., NaCl + PEG) → escapes single-porogen porosity-vs-strength trade-off
