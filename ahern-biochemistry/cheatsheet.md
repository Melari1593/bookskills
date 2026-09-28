# Cheatsheet

## Thermodynamics decision rules
- ΔG < 0 → toward products; ΔG = 0 → equilibrium; ΔG > 0 → toward reactants.
- Spontaneity depends on ΔG (=ΔH−TΔS), never ΔH alone — an endothermic reaction can be spontaneous if ΔS rises enough.
- Le Chatelier: add reactant → shifts to products; add product → shifts to reactants; remove heat from exothermic → shifts to products (reverse for endothermic).
- Enzymes never change Keq/ΔG — only activation energy/rate.

## Buffering
- Buffer strongest exactly at pH = pKa; effective range ≈ pKa ± 1.
- pH > 1 unit above pKa → group deprotonated; pH > 1 unit below pKa → group protonated.
- Buffer capacity is limited by buffer *concentration*, not just having the right pKa.

## Enzyme kinetics diagnostic table

| Inhibitor type | Km | Vmax | Overcome by excess [S]? |
|---|---|---|---|
| Competitive | ↑ | unchanged | Yes |
| Noncompetitive | unchanged | ↓ | No |
| Uncompetitive | ↓ | ↓ | No |

- Km = affinity (inverse; low Km = tight binder). Vmax = rate ceiling at saturation. Two enzymes can share one and differ wildly on the other.
- Sigmoidal (non-hyperbolic) kinetics → suspect an allosteric, usually multi-subunit, regulatory enzyme (MWC or KNF), not simple Michaelis-Menten.

## Structure/technique selection

| Need | Choose |
|---|---|
| Static atomic-resolution structure, any size, have a crystal | X-ray crystallography |
| Structure + dynamics, protein <~40 kDa | NMR |
| Huge complex, no crystal, least sample | Cryo-EM |
| Protein purity/MW | SDS-PAGE |
| Native charge/shape preserved | Native PAGE / FPLC |
| One long gold-standard read | Sanger sequencing |
| Whole-genome, high depth, low cost | NGS (Illumina/Ion Torrent/454/Nanopore) |
| Insert <15 kb / 15–45 kb / ≤350 kb / >1 Mb | Plasmid / Cosmid / BAC / YAC |

## DNA repair pathway by lesion (fast lookup)

| Lesion | Pathway |
|---|---|
| Replication mismatch (single base) | MMR |
| Oxidized/alkylated single base | BER |
| Bulky adduct / UV dimer (helix-distorting) | NER (GG- or TC-) |
| Double-strand break, any cell-cycle phase | NHEJ (lower fidelity) |
| Double-strand break, S/G2/M only | HR (high fidelity, needs sister chromatid) |
| Fork blocked by unrepaired lesion | TLS (error-prone bypass) |

## Thresholds & defaults worth memorizing
- Genetic code: 64 codons, 61 sense, 3 stop (UAA/UAG/UGA); reading frame set by AUG.
- Translation error rate ≈ 1 in 10,000 amino acids; DNA replication error rate ≈ 1 in 10⁶–10⁹ bases (pre-MMR).
- <1 in 1,000 DNA lesions becomes a fixed mutation (most are repaired first).
- Human genome: >3 billion bp, only ~1.5% protein-coding, ~19,000–20,000 protein-coding genes.
- Nucleosome: 146 bp DNA per histone octamer, 1.65 left-handed turns.
- NER excises a 24–32 nt fragment; Edman degradation reads ≤~30–60 residues; NMR structure work tops out ~40 kDa.
- Catalysis by approximation: ~10⁵–10⁷-fold rate boost from converting a bimolecular into an effective unimolecular reaction.

## Tells & smells (fast recognition heuristics)
- "Sigmoidal binding/rate curve" → allosteric regulation (MWC/KNF), not simple Km/Vmax.
- "Residue acting against its expected pKa" → suspect desolvation (active-site water exclusion shifting local pKa).
- "Tetrahedral/pentacoordinate negative intermediate stabilized" → look for an oxyanion hole or metal-ion electrostatic clamp nearby.
- "Same reaction, different tissue-specific kinetics" → isozymes, not one enzyme behaving differently.
- "Gene has the right TF motif but isn't expressed" → chromatin accessibility is very likely the blocker, not motif absence.
- "Repair pathway question" → identify the lesion type *first*; that alone usually names the pathway (see table above).
- "Antibiotic mechanism disables ribosomal proofreading" → aminoglycosides locking A1492/A1493 open, causing mistranslation.
