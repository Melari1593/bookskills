# Chapter 3: Investigating Proteins

## Core Idea
Studying a protein requires a toolkit matched to the question: purification techniques exploit differences in size, charge, and hydrophobicity to isolate a protein; identification/visualization techniques (electrophoresis, antibody-based methods) confirm identity and abundance; and structure-elucidation techniques (X-ray crystallography, NMR, cryo-EM) each trade off resolution, sample requirements, and ability to capture dynamics.

## Frameworks Introduced
- **Protein purification scheme (Total Protein, Total Activity, Specific Activity, Yield, Purification Level)**: A quantitative system for tracking purification progress across multiple steps.
  - When to use: Evaluating and comparing the effectiveness of successive purification steps for a protein with a measurable biological activity.
  - How: Total Protein = concentration × volume; Total Activity = activity/volume × volume; Specific Activity = Total Activity ÷ Total Protein; Yield (%) = (Total Activity at step ÷ Total Activity at step 1) × 100; Purification Level = Specific Activity at step ÷ Specific Activity at step 1.
- **Chromatographic separation principles (size, charge, hydrophobicity, affinity)**: The four physical/chemical properties chromatography exploits to separate proteins.
  - When to use: Choosing a chromatography method for a given purification goal.
  - How: Size exclusion (gel filtration) separates by molecular size/exclusion limit; ion exchange separates by net charge (anion exchange for negatively charged proteins, cation exchange for positively charged); hydrophobic interaction chromatography (HIC) separates by surface hydrophobicity under high-to-low salt gradient; affinity chromatography exploits a specific ligand-target ("lock and key") interaction (e.g., His-tag/Ni2+, lectin/glycoprotein, antibody/antigen).
  - Related: **HPLC vs. FPLC** — HPLC uses high pressure for fast, high-resolution reversed-phase separation but often denatures proteins; FPLC uses lower pressure, higher flow rate, and preserves native protein conformation, making it the standard for preparative protein purification.
- **SDS-PAGE / Native PAGE framework**: Gel electrophoresis separates proteins by different criteria depending on conditions.
  - When to use: Determining protein molecular weight (SDS-PAGE) vs. preserving native charge/shape/size information (Native PAGE).
  - How: SDS coats protein with uniform negative charge, masking intrinsic charge, so migration depends only on size (mass); reducing agents (DTT) break disulfide bonds to fully denature/dissociate subunits; Native PAGE (no SDS) separates by combined charge, size, and shape.
- **Structure-elucidation trade-off framework (X-ray crystallography vs. NMR vs. cryo-EM)**: A decision framework comparing the three major structural biology techniques.
  - When to use: Choosing a method to solve a protein's 3D structure given available sample, size, and whether dynamics information is needed.
  - How: X-ray crystallography — needs a crystal, works for any size, gives a static high-resolution (~2 Å) structure, requires slow/uncertain crystallization; NMR — solution-state, captures dynamics, but limited to proteins <~40 kDa due to tumbling-rate signal decay, requires isotope (15N/13C) labeling; cryo-EM — no crystal needed, works for very large complexes (e.g., ribosome), achieves near-atomic resolution (down to ~1.5 Å), captures a near-native frozen snapshot but not dynamics.

## Key Concepts
- **Salting out**: Precipitation of proteins by adding high concentrations of a salt (e.g., ammonium sulfate), which reduces protein solubility by competing for water and promoting hydrophobic protein-protein aggregation.
- **Size exclusion (gel filtration) chromatography**: Separates by molecular size using porous beads; larger molecules elute first because they cannot enter the bead "tunnels."
- **Isoelectric focusing (IEF)**: Separates amphoteric molecules (proteins) in a pH gradient; a protein migrates until it reaches the pH equal to its pI, where it has zero net charge and stops moving.
- **Two-dimensional gel electrophoresis (2-DE)**: Combines IEF (first dimension, separates by pI) with SDS-PAGE (second dimension, separates by molecular weight) for high-resolution proteome separation.
- **Western blot**: A 7-step method (sample prep, gel electrophoresis, blotting to membrane, antibody probing, detection, imaging, analysis) to detect a specific protein using primary and labeled secondary antibodies after transfer from a gel to a membrane (nitrocellulose, PVDF, or nylon).
- **Polyclonal vs. monoclonal antibodies**: Polyclonal antibodies (from animal antiserum) recognize multiple epitopes on an antigen; monoclonal antibodies (from hybridoma cell lines, fusing B cells with myeloma cells) recognize a single epitope with high specificity.
- **ELISA (enzyme-linked immunosorbent assay)**: Uses an enzyme-antibody conjugate to quantify an analyte (replaced the older, radioactivity-based radioimmunoassay/RIA).
- **Immunohistochemistry (IHC)**: Antibody-based technique to visualize protein localization directly within tissue sections, typically using an enzyme (HRP)-linked secondary antibody and a chromogenic substrate (e.g., DAB) for a colored precipitate.
- **Edman degradation**: A sequential N-terminal amino acid sequencing method (labeling and cleaving one residue at a time as a PTH-amino acid derivative); limited to ~30–60 residues and requires a free, unmodified N-terminus.
- **Mass spectrometry (MALDI-TOF, peptide mass fingerprinting)**: Identifies proteins by measuring the mass-to-charge ratio of ionized peptide fragments (commonly after trypsin digestion, which cleaves at Lys/Arg except before Pro) and matching against databases; "bottom-up" (digest first) is the dominant proteomics approach vs. "top-down" (intact protein) or "middle-down."
- **X-ray crystallography resolution**: The three-component system (crystal, X-ray source, detector) that reveals atomic structure; resolution ~2 Å is typical for proteins (5–10 Å reveals only chain topology; 1–1.5 Å resolves individual atoms).
- **Proteome / proteomics**: The complete, dynamic set of proteins expressed by a cell/organism at a given time — unlike the relatively static genome, the proteome varies by cell type, time, and condition, and does not correlate perfectly with mRNA levels.

## Mental Models
- Use the purification scheme's "specific activity should rise, total protein should fall" pattern as a built-in sanity check: if specific activity plateaus or drops at a step, suspect loss of protein, loss of activity/denaturation, or loss of a required cofactor — not just an ineffective separation method.
- Think of the choice between X-ray, NMR, and cryo-EM as a triangle of trade-offs between resolution, sample amount/purity required, size limits, and whether you need to see the protein move — no single technique dominates on all axes, and they are complementary (e.g., overlay NMR dynamics data onto a crystal structure).
- Treat antibody specificity as a spectrum, not binary: polyclonal antibodies trade specificity for potency/robustness (multi-epitope binding drowns out background); monoclonal antibodies trade robustness for well-defined, reproducible single-epitope specificity.
- Use "bottom-up beats top-down for complex mixtures" as the default mass spec strategy: digesting proteins into small, uniform peptides before MS analysis avoids the ionization-suppression and spectral-complexity problems that plague whole-protein (top-down) analysis of mixtures.

## Anti-patterns / Common Misconceptions
- **"HPLC is strictly better than FPLC because it's higher performance"**: Wrong for native protein purification — HPLC's high pressure and reversed-phase organic solvents frequently denature proteins, whereas FPLC's lower pressure, aqueous buffers preserve native/functional conformation, making FPLC the preferred method when biological activity must be retained.
- **"A bigger protein is harder to solve by any method"**: Not universally true — size is not a major obstacle for X-ray crystallography or cryo-EM (both have solved massive complexes like the ribosome), but it is a major obstacle for NMR specifically, because larger proteins tumble more slowly, broadening peaks and degrading spectral quality (proteins >~40 kDa become difficult).
- **"mRNA levels are a good proxy for protein levels"**: The chapter explicitly notes this assumption fails — translation efficiency and protein stability vary by gene and cell state, so proteomics (direct protein measurement) is needed to confirm what genomics/transcriptomics only predicts.
- **"SDS-PAGE separates proteins by their natural charge"**: Incorrect — SDS binding coats the protein in a uniform negative charge-to-mass ratio, deliberately masking intrinsic charge so that migration reflects size (mass) only; this is why Native PAGE (without SDS) is used instead when charge/shape information matters.

## Key Equations & Reference Tables

**Purification scheme calculations**:
```
Total Protein (mg) = [protein] (mg/mL) × total volume (mL)
Total Activity (units) = [activity] (units/mL) × total volume (mL)
Specific Activity (units/mg) = Total Activity ÷ Total Protein
Yield (%) = (Total Activity at step N ÷ Total Activity at step 1) × 100
Purification Level = (Specific Activity at step N ÷ Specific Activity at step 1)
```
One enzyme unit (U) = amount of enzyme that converts 1 μmol substrate/min under specified assay conditions.

**Worked purification numbers from the chapter's example** (starting material: 10 mL bacterial lysate supernatant):
| Parameter | Value |
|---|---|
| Protein concentration (assay) | 7.5 μg/μL |
| Total Protein | 75 mg |
| Activity (assay) | 2.5 units/μL |
| Total Activity | 25,000 units |
| Specific Activity | 333.3 units/mg |

**X-ray crystallography resolution ranges**:
| Resolution | Reveals |
|---|---|
| 5–10 Å | polypeptide chain topology |
| 3–4 Å | groups of atoms |
| 1–1.5 Å | individual atoms |
| ~2 Å | typical protein crystal structure resolution |

**Structure-elucidation sample requirements (approximate)**:
| Method | Typical sample need |
|---|---|
| X-ray crystallography | ~500 μL protein at 5–10 mg/mL |
| NMR | 300–600 μL, 0.1–3 mM protein, isotope-labeled (15N/13C) |
| Cryo-EM | ~50 μL at 1 mg/mL (least material of the three) |

**Edman degradation limits**: practically effective for ≤30 residues (theoretical max ~50–60); requires 1–100 picomoles of peptide; automated since 1967.

## Worked Example
**Designing a purification + identification workflow for a novel bacterial enzyme with a colorimetric activity assay:**

1. **Lysis**: Freeze/thaw the harvested bacterial pellet in reaction buffer; centrifuge to remove insoluble debris, retaining the supernatant (soluble protein fraction). This is purification "step 1" — baseline Total Protein and Total Activity are measured here (see worked numbers above: 75 mg protein, 25,000 units, specific activity 333.3 units/mg). By definition, yield = 100% and purification level = 1 at this step.
2. **Bulk fractionation**: Apply ammonium sulfate salting-out to precipitate proteins in fractions; collect the fraction enriched for the target's activity, then measure Total Protein/Activity again — expect Total Protein to drop (bulk contaminants removed) and Specific Activity to rise (target enriched), while Yield drops modestly (some target lost to imperfect fractionation).
3. **Chromatographic polishing**: Choose a chromatography method based on the target's known properties — e.g., ion exchange chromatography if its pI is known and differs from contaminants, or affinity chromatography if a His-tag or specific ligand is available (fastest route to high purity in one step).
4. **Quality check via electrophoresis**: Run SDS-PAGE (with DTT) at each step to visualize the shrinking number of bands and confirm the target band's relative intensity increases; Coomassie or silver staining detects total protein, while a Western blot with a specific antibody confirms the target's identity and approximate size.
5. **Definitive identification**: Excise the target band, digest with trypsin, and analyze by MALDI-TOF MS (peptide mass fingerprinting) to confirm identity against a sequence database — or use Edman degradation on the first 5–10 N-terminal residues if only a quick confirmatory tag is needed.
6. **Track overall success**: If, after 4 purification steps, the protein reaches ~95% purity, this implies it originally constituted only ~1.24% of the total starting protein — illustrating why purification level should increase roughly exponentially across a well-designed scheme.

## Key Takeaways
1. Protein purification is a multi-step process that must be quantitatively tracked (Total Protein, Total Activity, Specific Activity, Yield, Purification Level) to know whether each step is actually improving purity without losing too much target protein.
2. Chromatography methods separate proteins on orthogonal physical properties — size, charge, hydrophobicity, or specific affinity — and effective purification schemes typically combine 2–3 of these principles sequentially.
3. SDS-PAGE separates strictly by size (via SDS-imposed uniform charge), while Native PAGE and isoelectric focusing preserve/exploit native charge and shape information.
4. Antibody-based detection methods (Western blot, ELISA, IHC) all rely on the same primary/secondary antibody logic but differ in readout format — membrane band, plate-well signal, or in-tissue visualization, respectively.
5. Mass spectrometry (especially bottom-up/tryptic-digest MALDI-TOF) is the dominant modern method for protein identification because it handles complex mixtures far better than intact-protein (top-down) analysis.
6. No single structural biology technique (X-ray, NMR, cryo-EM) is universally superior — the right choice depends on protein size, available sample quantity, need for dynamics information, and crystallizability; the techniques are complementary, not competing.
7. The proteome is fundamentally more complex and dynamic than the genome — because mRNA levels do not reliably predict protein levels, direct proteomic measurement is necessary to understand real cellular protein content and post-translational modification state.

## Connects To
- **Ch 2**: All separation and identification techniques here directly exploit the structural properties (size, charge, hydrophobicity, folding state, epitopes) established in Chapter 2.
- **Ch 5**: Recombinant DNA/tagging techniques (His-tag, Strep-tag) mentioned here for affinity purification are covered in full detail in the DNA techniques chapter.
- **Ch 4**: Antibody diversity generation (VJ recombination) mentioned briefly here connects to the immunoglobulin gene structure covered alongside DNA/RNA topics.
- **Ch 6/7**: Purified, identified proteins characterized by these techniques are the starting material for the enzyme kinetics and catalytic mechanism studies in subsequent chapters.
