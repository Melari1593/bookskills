# Chapter 12: DNA Damage, Repair, and Mutations

## Core Idea
Cells face thousands of DNA lesions per day from oxidative, alkylating, UV, and radiation sources, but fewer than 1 in 1,000 lesions become an actual mutation because a portfolio of distinct, damage-type-specific repair pathways (mismatch repair, base excision repair, nucleotide excision repair, and double-strand-break repair via NHEJ or homologous recombination) — layered under a checkpoint system that arrests the cell cycle to buy repair time — intercepts most damage before it is fixed into the genome.

## Frameworks Introduced
- **Damage-Type-to-Pathway Mapping Model**: the organizing principle that repair pathway choice is dictated by the physical nature of the lesion, not by chance.
  - How: single mismatched/misincorporated bases from replication errors → Mismatch Repair (MMR); oxidized/alkylated/small single bases → Base Excision Repair (BER); bulky helix-distorting adducts and UV crosslinks → Nucleotide Excision Repair (NER); double-strand breaks → Non-Homologous End-Joining (NHEJ, cell-cycle-independent) or Homologous Recombination (HR, S/G2-restricted); damage the fork cannot wait for → Translesion Synthesis (TLS) bypass.
  - When to use: the first diagnostic question for any DNA-damage scenario — "what kind of lesion is this?" — determines which named pathway is relevant.
- **Mismatch Repair (MMR) Strand-Discrimination Model**: explains how repair machinery knows which of two strands is the "wrong" (newly synthesized, error-containing) one.
  - How: in E. coli, transient hemimethylation after replication marks the new strand as unmethylated at GATC sites; MutS recognizes the mismatch, MutL activates MutH, which nicks specifically at the unmethylated (new) strand's GATC site, and helicase/exonucleases (UvrD, RecJ/ExoI) excise the error-containing segment for Pol III to resynthesize. In eukaryotes and most other bacteria (no GATC methylation signal), strand discontinuities (nicks) mark the new strand instead, with MutSα/MutLα homologs directing EXO1-mediated excision and Pol δ resynthesis. MMR increases replication accuracy 20-400-fold, and its failure underlies ~90% of hereditary nonpolyposis colon cancers.
  - When to use: reference model whenever the question involves distinguishing template from newly-synthesized DNA strand for repair targeting.
- **Base Excision Repair (BER) Short-Patch vs. Long-Patch Pathway**: the named two-branch model for removing damaged single bases.
  - How: a lesion-specific DNA glycosylase (e.g., OGG1 for 8-oxo-dG) excises the damaged base, creating an AP (abasic) site → AP-endonuclease 1 (APE1) incises the backbone → short-patch: Pol β replaces the single missing nucleotide and Ligase III (with XRCC1 scaffold) seals the nick; long-patch: Pol δ/ε (with PCNA) replace several nucleotides, FEN1 removes the displaced flap, and Ligase I seals the nick.
  - When to use: reference model for oxidative or alkylation damage repair (single-base lesions), and to distinguish it from NER (which removes short oligonucleotide tracts around bulky lesions, not single bases).
- **Nucleotide Excision Repair (NER): Global Genome vs. Transcription-Coupled**: two entry routes into the same excision machinery for bulky, helix-distorting damage.
  - How: Global Genome NER (GG-NER) — XPC protein (or the DDB1-DDB2/XPE heterodimer for UV lesions) surveys the entire genome and detects bulky damage independent of transcriptional activity. Transcription-Coupled NER (TC-NER) — activated specifically when RNA polymerase II stalls at a lesion on the transcribed strand, prioritizing actively expressed genes. Both converge on assembly of a ~30-protein "repairasome" that excises a 24-32 nucleotide fragment containing the lesion, followed by resynthesis using the intact strand as template and ligation. Loss of NER function causes xeroderma pigmentosum (extreme photosensitivity, ~1,000-fold increased skin cancer risk).
- **Homologous Recombination (HR) Three-Mechanism Model**: how double-strand breaks are repaired with high fidelity using a homologous template.
  - How: the MRN complex (Mre11-Rad50-Nbs1) plus CtIP resects 5' strands to generate 3' single-stranded overhangs (extended by Exo1/DNA2/Sgs1) → RPA coats the ssDNA → BRCA1/BRCA2 mediate Rad51 replacement of RPA, forming a presynaptic nucleoprotein filament that invades homologous duplex DNA (preferentially the sister chromatid) → repair proceeds via one of three mechanistically distinct routes: Synthesis-Dependent Strand Annealing (SDSA), Double Holliday Junction resolution (via BLM helicase, with or without crossover), or Single-Strand Annealing (SSA, for repeats). HR is largely restricted to S/G2/M (requires a replicated sister chromatid), while NHEJ (Ku70/Ku80, DNA-PKcs, Ligase IV/XRCC4) operates throughout the cell cycle but is lower fidelity.

## Key Concepts
- **Transition vs. transversion mutation**: transition = purine↔purine or pyrimidine↔pyrimidine substitution; transversion = purine↔pyrimidine substitution; both arise when a polymerase inserts a random nucleotide opposite an unrepaired lesion.
- **Silent / missense / nonsense mutation**: silent = codon change encodes the same amino acid (degeneracy); missense = codon change encodes a different amino acid (effect depends on chemical similarity and protein location); nonsense = codon change creates a premature stop codon, truncating the protein.
- **Frameshift mutation**: an insertion/deletion not a multiple of 3 nucleotides, shifting the reading frame for every downstream codon — nearly always more damaging than a point mutation because it corrupts the entire downstream sequence and often introduces a premature stop.
- **8-oxo-7,8-dihydroguanine (8-oxoG)**: the most abundant oxidative DNA lesion (guanine has the lowest ionization potential of the four bases); mispairs with adenine during replication, causing G→T transversions if unrepaired; used clinically as an oxidative-stress biomarker.
- **AP (abasic) site**: a location lacking a purine or pyrimidine base, arising spontaneously (~10,000 apurinic + ~500 apyrimidinic sites/cell/day) or as a BER intermediate; if unrepaired, stalls replication or is bypassed via translesion synthesis.
- **Pyrimidine dimer (CPD / 6-4 photoproduct)**: UV-induced covalent crosslink between adjacent pyrimidines (commonly thymines); cyclobutane pyrimidine dimers (two covalent bonds) and 6-4 photoproducts (one bond) are the primary cause of UV-induced skin cancers if not repaired by photolyase or NER.
- **DNA damage checkpoints (ATM/ATR → CHK1/CHK2 → p53)**: the signaling cascade that senses damage and halts cell-cycle progression at G1/S, intra-S, or G2/M via CDK inhibition (e.g., p21^CIP1 blocking cyclin E-CDK2), giving repair machinery time to act before replication or mitosis.
- **Translesion synthesis (TLS)**: specialized, lower-fidelity DNA polymerases (recruited via PCNA monoubiquitination) that tolerate distorted template geometry to replicate past an unrepaired lesion, avoiding fork collapse at the cost of an elevated mutation rate.
- **CCR5-Δ32**: a naturally occurring deletion mutation in the CCR5 HIV co-receptor gene that confers strong (homozygous) or partial (heterozygous) resistance to HIV infection; a real-world example of a beneficial mutation under strong selective pressure.

## Mental Models
- Use the "damage type determines pathway" heuristic as the entry point for every repair question: ask what kind of lesion this is (single mismatched base? oxidized base? bulky adduct? double-strand break?) before asking which pathway applies.
- Think of MMR, BER, and NER as forming a size/complexity gradient: MMR corrects single mismatched bases using strand-discrimination cues; BER corrects single damaged bases using lesion-specific glycosylases; NER corrects short oligonucleotide tracts around bulky, helix-distorting lesions using a large multi-protein "repairasome" — each pathway is scaled to the size and nature of the problem it solves.
- Treat NHEJ vs. HR as a fidelity/availability trade-off, not a strict hierarchy: NHEJ is always available (any cell-cycle phase) but error-prone; HR is high-fidelity but requires a sister chromatid, restricting it to S/G2/M — cell-cycle phase alone often predicts which pathway a cell will use for a given DSB.
- Think of the checkpoint cascade (ATM/ATR → CHK1/CHK2 → p53/CDK inhibition) as a single converging signal: however damage is first detected, essentially all routes funnel into inhibiting CDK activity to arrest the cycle, making CDK inhibition the common "kill switch" across G1, S, and G2 checkpoints.

## Anti-patterns / Common Misconceptions
- **"DNA damage and mutation are the same thing"**: false — the vast majority of lesions (>999 of every 1,000) are repaired before they become permanent, heritable mutations; damage is the transient chemical lesion, mutation is the fixed sequence change.
- **"All insertions/deletions are as tolerable as point mutations"**: false — in-frame indels (multiples of 3) may be tolerated, but frameshift indels corrupt every downstream codon and are nearly always far more damaging than a single point mutation.
- **"Carcinogens and mutagens are unrelated concepts"**: most carcinogens are mutagenic (true per the chapter's practice content) — cancer arises from accumulated somatic mutations in genes controlling the cell cycle, DNA repair, and growth/survival.
- **"BER and NER are interchangeable ways to fix DNA damage"**: they are not — BER uses a lesion-specific glycosylase to recognize and directly excise a single damaged base, while NER uses a multi-protein complex to recognize helix distortion (not a specific base) and excise a whole oligonucleotide tract; using NER logic to explain 8-oxoG repair (a BER substrate) is a common error.
- **"Mismatch repair fixes DNA damage caused by mutagens"**: MMR's primary lesion source is replication errors (misincorporated/mismatched bases), not exogenous chemical or radiation damage — that is the domain of BER/NER.
- **"Homologous recombination can happen at any point in the cell cycle, like NHEJ"**: HR is largely restricted to S/G2/M because it requires a replicated sister chromatid as a template; NHEJ, not HR, is the cell-cycle-independent pathway.

## Key Equations & Reference Tables

**Scale of daily DNA damage:** 1,000-1,000,000 molecular lesions per cell per day (≈0.000165% of the ~6 billion base human genome); <1 in 1,000 lesions become a fixed mutation.

**Replication error rate:** 1 in 10⁶ to 1 in 10⁹ bases (despite proofreading), yielding an estimated 3-3,000 errors per human genome replication before MMR correction.

**Table 12.1-style — Point mutation types:**

| Type | Codon-level effect | Example (CAA = Gln) |
|---|---|---|
| Silent | Same amino acid | CAA → CAG (Gln) |
| Missense | Different amino acid | CAA → CCA (Pro) |
| Nonsense | Premature stop codon | CAA → UAA (stop) |

**DNA repair pathway comparison:**

| Pathway | Lesion type | Key recognition factor | Key excision/resolution factor |
|---|---|---|---|
| MMR | Replication mismatches | MutS/MutSα | MutH (E. coli) / EXO1 (eukaryotes) |
| BER | Oxidized/alkylated single bases | Lesion-specific glycosylase (e.g., OGG1) | APE1 → Pol β (short) or Pol δ/ε + FEN1 (long) |
| NER (GG) | Bulky adducts, genome-wide | XPC / DDB1-DDB2 | ~30-protein repairasome, 24-32 nt excision |
| NER (TC) | Bulky adducts, transcribed strand | Stalled RNA Pol II | Same repairasome, transcription-prioritized |
| NHEJ | Double-strand breaks | Ku70/Ku80 | DNA-PKcs, Ligase IV/XRCC4 |
| HR | Double-strand breaks | MRN complex + CtIP | Rad51 (BRCA1/2-mediated), BLM helicase |

**Occurrence rates cited:** ~100,000 8-oxoG lesions/cell/day; ~10,000 apurinic + ~500 apyrimidinic sites/cell/day; 50-100 UV photoreactions/second in a sunlight-exposed skin cell; 8-oxo-dG repaired with an ~11-minute half-life in irradiated mouse liver.

**Clinical/epidemiological figures:** MMR defects implicated in ~90% of hereditary nonpolyposis colon cancers; NER defects (xeroderma pigmentosum) confer ~1,000-fold increased internal tumor risk; CCR5-Δ32 allele frequency up to ~14% in some northern European populations, global HIV prevalence ~0.8% (2015), ~7.1% in Sub-Saharan Africa.

## Worked Example
**Diagnosing and tracing repair of a UV-induced thymine dimer, from damage to restored duplex (synthesizing Sections 12.2 and 12.6):**

1. UV light (non-ionizing radiation) is directly absorbed by adjacent thymine bases on one DNA strand, forming a covalent crosslink — either a cyclobutane pyrimidine dimer (two covalent bonds) or a 6-4 photoproduct (one covalent bond). This is a bulky, helix-distorting lesion, not a single damaged base — ruling out BER as the repair route.
2. If the lesion lies in an actively transcribed gene, RNA polymerase II stalls upon reaching it on the template strand, triggering Transcription-Coupled NER (TC-NER); if in bulk/silent genomic DNA, the XPC protein (or DDB1-DDB2 for UV lesions specifically) surveys and detects the distortion via Global Genome NER (GG-NER).
3. Detection nucleates assembly of the NER "repairasome" — a dynamically regulated, ~30-protein, ~18-polypeptide preincision complex whose composition changes as repair proceeds, providing the selectivity that no single subunit could achieve alone.
4. The repairasome excises a 24-32 nucleotide fragment of the damaged strand containing the dimer, leaving a single-stranded gap bordered by the intact complementary strand.
5. DNA polymerase resynthesizes the excised region using the undamaged complementary strand as template, restoring the correct sequence.
6. DNA ligase seals the final nick, restoring an intact, undamaged duplex.
7. Contrast case: if this repair pathway is nonfunctional (mutations in NER genes, e.g., XPC or other XP-family genes), the dimer persists; during replication a polymerase must either stall (risking a double-strand break) or use translesion synthesis to bypass it, frequently mis-inserting a base opposite the damaged thymine and fixing a mutation — the molecular basis of xeroderma pigmentosum's extreme skin cancer susceptibility.

## Key Takeaways
1. DNA damage is common (up to a million lesions/cell/day) but mutation is rare (<0.1% of lesions) precisely because dedicated, damage-type-specific repair pathways intercept most lesions before replication fixes them into the genome.
2. Repair pathway choice is diagnostic: single mismatched bases → MMR; single damaged bases → BER; bulky/helix-distorting adducts → NER; double-strand breaks → NHEJ (any cell-cycle phase, lower fidelity) or HR (S/G2/M only, high fidelity).
3. Frameshift mutations (non-multiple-of-3 indels) are categorically more damaging than point mutations because they corrupt every downstream codon, not just one.
4. Strand discrimination is the central engineering problem MMR must solve — E. coli uses transient GATC hemimethylation, while eukaryotes and most other bacteria use strand discontinuities (nicks) instead.
5. The DNA damage checkpoint cascade (ATM/ATR → CHK1/CHK2 → p53) converges on CDK inhibition regardless of which cell-cycle phase or damage type triggered it, arresting the cycle to allow repair before replication or mitosis proceeds.
6. Translesion synthesis is a deliberate fidelity-for-survival trade-off: when a lesion can't be repaired before the replication fork arrives, error-prone bypass polymerases (recruited via PCNA monoubiquitination) prevent fork collapse at the cost of an elevated local mutation rate.
7. Defects in these pathways have direct, well-characterized clinical consequences (hereditary nonpolyposis colon cancer from MMR defects, xeroderma pigmentosum from NER defects, BRCA1/2-associated breast/ovarian cancer from HR defects), making pathway identity clinically, not just mechanistically, important.

## Connects To
- **Ch 9**: DNA repair machinery directly interfaces with the replisome — stalled or collapsed replication forks (Ch. 9) are a major trigger for HR-mediated double-strand-break repair, and replication errors are the primary substrate for MMR.
- **Ch 10**: Transcription-coupled NER uses stalled RNA Polymerase II (introduced in Ch. 10's elongation section) as its damage-detection signal, directly linking transcription machinery to genome maintenance.
- **Ch 11**: Nonsense and frameshift mutations described here are interpreted through Ch. 11's codon-reading and stop-codon-recognition framework — the downstream translational consequence of a repair failure.
- **Ch 13**: DNA methylation, introduced here as a strand-discrimination signal in bacterial MMR, reappears in Ch. 13 as a major epigenetic gene-regulation mechanism — the same chemical modification serves entirely different biological purposes in the two contexts.
- **Ch 8**: Cyclin-CDK cell-cycle control (used here to arrest the cycle after damage detection) is the same regulatory system covered in Ch. 8/9's discussion of cell-cycle-gated processes, reinforcing CDK inhibition as a general-purpose "pause" mechanism.
