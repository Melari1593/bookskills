# Chapter 11: Translation

## Core Idea
Translation decodes mRNA codons into protein with remarkably high fidelity (~1 error per 10,000 amino acids) through the coordinated action of the genetic code's built-in redundancy (wobble pairing), highly specific aminoacyl-tRNA synthetases, and a ribosome that uses kinetic proofreading — not just thermodynamics — to discriminate correct from incorrect tRNAs at every step of initiation, elongation, and termination.

## Frameworks Introduced
- **The Genetic Code and Wobble Hypothesis**: explains how 61 sense codons are read by a smaller set of tRNAs while preserving high fidelity.
  - How: 64 codons encode 20 amino acids, producing redundancy concentrated at the third ("wobble") codon position; non-Watson-Crick wobble pairs (G-U, I-U, I-A, I-C) at the first anticodon position (aligned to the third codon position) allow one tRNA to read multiple synonymous codons; specific modified nucleosides at the wobble position (e.g., lysidine k2C34 on tRNA-Ile, restricting it to AUA only) fine-tune which codons a given tRNA can and cannot read, preventing dangerous cross-reading (e.g., of the methionine start codon AUG).
  - When to use: reference framework for explaining why synonymous codon changes are often silent, and why a cell needs far fewer than 61 distinct tRNA species.
- **Two-Step Aminoacylation Mechanism (aaRS Class I vs. Class II)**: the universal mechanism by which amino acids are "charged" onto their cognate tRNAs, with two structurally distinct enzyme families.
  - How: Step 1 (amino acid activation) — the amino acid's α-carboxylate attacks ATP's α-phosphate, forming an enzyme-bound aminoacyl-adenylate (aa-AMP) and releasing pyrophosphate. Step 2 (transfer) — the terminal adenosine's 2'-OH (Class I enzymes) or 3'-OH (Class II enzymes, except PheRS) attacks the adenylate's carbonyl carbon, producing aminoacyl-tRNA and AMP. Class I synthetases use a Rossmann-fold catalytic domain, approach the tRNA acceptor stem from the minor groove, and bind ATP extended; Class II synthetases use a seven-stranded β-sheet domain, approach from the major groove, and bind ATP bent. ~10 of the 23 known aaRSs additionally possess pre- and/or post-transfer editing activity to hydrolyze misactivated amino acids or misacylated tRNAs, raising overall fidelity.
  - When to use: reference model for how amino acid selection accuracy is established upstream of the ribosome itself.
- **Kinetic Proofreading in Codon-Anticodon Selection**: explains how the ribosome achieves fidelity beyond what thermodynamic base-pairing energy alone could provide.
  - How: decoding-center nucleotides A1492, A1493 (with G530) flip out to shield a correctly paired codon-anticodon mini-helix from solvent; near-cognate pairs are shielded incompletely, increasing their free-energy penalty and docking flexibility; this differential triggers a two-step kinetic process — initial selection (affecting GTP hydrolysis rate of the delivering GTPase) and a subsequent proofreading step (affecting tRNA rejection rate) — that multiplies the discrimination factor well beyond simple binding-affinity differences. Aminoglycoside antibiotics lock A1492/A1493 in the flipped-out conformation regardless of pairing correctness, causing mistranslation and bacterial cell death.
- **The Universal Elongation Cycle (Delivery → Decoding → Peptide Bond Formation → Translocation)**: the repeating cycle at the core of both prokaryotic and eukaryotic translation.
  - How: aminoacyl-tRNA is delivered to the A-site as a ternary complex with a translational GTPase and GTP (EF-Tu in bacteria, eEF1α in eukaryotes) → correct codon-anticodon pairing triggers GTP hydrolysis and GTPase release → the ribosome (a ribozyme) catalyzes peptide bond formation, transferring the P-site peptide to the A-site amino acid (always N-to-C direction) → a second GTPase (EF-G in bacteria, eEF2 in eukaryotes) drives translocation, shifting A-site→P-site, P-site→E-site, and E-site tRNA release, powered by GTP-hydrolysis-driven conformational "power stroke" folding and large-scale ribosomal subunit rotation (including L1-stalk movement).
  - When to use: reference cycle for any question about the mechanics of chain elongation and the GTPase "checkpoints" that enforce fidelity.

## Key Concepts
- **Codon / reading frame**: mRNA is read in non-overlapping 5'→3' triplets (codons); only one of three possible reading frames is correct, and frameshift mutations (Ch. 12) shift every downstream codon.
- **Shine-Dalgarno sequence**: a purine-rich bacterial mRNA element (typically 4-9 nt upstream of the start codon) complementary to the 16S rRNA anti-SD sequence, helping position the 30S subunit at the correct AUG (not universally required).
- **Kozak sequence**: the eukaryotic consensus context around the start codon, (gcc)gccRccAUGG, that determines "strength" (efficiency) of start-codon recognition during 5'-cap-dependent scanning.
- **Initiator tRNA (tRNA-fMet / tRNA-i)**: the specialized initiator tRNA carrying N-formylmethionine (bacteria) or methionine (eukaryotes), delivered to the P-site (not the A-site) during initiation.
- **A-site, P-site, E-site**: the three ribosomal tRNA-binding sites — aminoacyl (decoding), peptidyl (holds growing chain), and exit (deacylated tRNA release) — through which every tRNA transits in sequence.
- **Peptidyl transferase center (PTC)**: the catalytic core of the large ribosomal subunit, composed of rRNA (making the ribosome a ribozyme), responsible for peptide bond formation.
- **Release factors (RF1/RF2/RF3 in bacteria; eRF1/eRF3 in eukaryotes)**: proteins that recognize stop codons in the A-site and trigger hydrolysis of the peptidyl-tRNA bond via a universally conserved GGQ motif; bacteria use two codon-specific class I RFs (RF1: UAA/UAG; RF2: UAA/UGA) plus GTPase RF3, while eukaryotes use a single "omnipotent" eRF1 that reads all three stop codons.
- **Exit tunnel**: the ~100 Å channel through which the nascent peptide exits the large subunit; can bind macrolide antibiotics and cause context-dependent ribosome stalling (e.g., at polyproline stretches, relieved by elongation factor EF-P).
- **Ribosome filter hypothesis**: Mauro & Edelman's (2002) model proposing that heterogeneity in ribosomal protein/rRNA composition allows ribosomes to selectively translate specific mRNA subsets, contributing to translational regulation.
- **Post-transcriptional tRNA modification**: tRNAs carry the highest modification density of any RNA class (93 known modifications), concentrated in the anticodon loop (direct role in codon recognition/wobble) and the D-/T-loop core (structural stabilization of the canonical L-shaped tertiary fold).

## Mental Models
- Think of wobble pairing as the genetic code's "compression algorithm": it lets the cell get away with far fewer than 61 tRNA species while still reading every sense codon, at the cost of needing precise, modification-dependent restriction (like lysidine on tRNA-Ile) to prevent dangerous ambiguity.
- Use the two-step kinetic proofreading model as the general template for "how does a biological machine achieve fidelity beyond single-binding-event thermodynamics" — the same logic (an irreversible, energy-spending checkpoint after initial binding) reappears throughout molecular biology (e.g., DNA polymerase proofreading in Ch. 9).
- Treat aaRS Class I vs. Class II as a structural fork with predictable downstream consequences: minor-groove approach/2'-OH transfer/extended-ATP (Class I) vs. major-groove approach/3'-OH transfer/bent-ATP (Class II) — knowing the class often predicts other mechanistic details.
- Think of the elongation cycle's two GTPases (delivery GTPase and translocation GTPase) as two independent "go/no-go" checkpoints per cycle — one for tRNA selection accuracy, one for correct physical movement — rather than a single continuous process.

## Anti-patterns / Common Misconceptions
- **"The genetic code is ambiguous because multiple codons specify one amino acid"**: backwards — degeneracy (many codons → one amino acid) is not the same as ambiguity (one codon → many amino acids); the code has almost no true ambiguity, and degeneracy is a feature that minimizes the impact of mutations.
- **"Any tRNA with a complementary anticodon will be accepted by the ribosome"**: false — the ribosome actively discriminates against near-cognate tRNAs via incomplete solvent shielding and kinetic proofreading, not just base-pairing thermodynamics; this is why aminoglycosides (which disable this discrimination) are bactericidal.
- **"Ribosomal proteins do the catalytic work of peptide bond formation"**: incorrect — the peptidyl transferase center is built from rRNA; the ribosome is a ribozyme, a fact experimentally confirmed using an archaeal large subunit.
- **"Eukaryotic translation termination works just like bacterial termination with different protein names"**: eukaryotic eRF1 has no sequence or structural homology to bacterial RF1/RF2 (apart from the conserved GGQ motif) and is a single factor reading all three stop codons, versus bacteria's two codon-specific RFs — a qualitative, not just nominal, difference.
- **"Translation initiation is essentially the same across all mRNAs in eukaryotes"**: cap-dependent scanning is the default, but cap-independent initiation via internal ribosome entry sites (IRES) is a distinct alternative pathway used by certain transcripts and hijacked by some viruses (via eIF4G cleavage).

## Key Equations & Reference Tables

**Genetic code scale:** 4³ = 64 codons; 20 standard amino acids; 3 stop codons (UAA, UAG, UGA); translation error rate ≈ 10⁻⁴ (1 per 10,000 amino acids).

**Four main wobble base pairs (first anticodon position : third codon position):**

| Wobble pair | Pairing type |
|---|---|
| G-U | Non-Watson-Crick |
| I-U | Non-Watson-Crick (inosine) |
| I-A | Non-Watson-Crick (inosine) |
| I-C | Non-Watson-Crick (inosine) |

**Ribosome composition:**

| Component | Prokaryote (70S, ~2500 kDa) | Eukaryote (80S, human cytosolic) |
|---|---|---|
| Small subunit | 30S: 21 proteins + 16S rRNA | 40S: 33 proteins + 18S rRNA |
| Large subunit | 50S: 34 proteins + 23S + 5S rRNA | 60S: 47 proteins + 28S + 5.8S + 5S rRNA |

**Elongation factor comparison (Table 11.2-style):**

| Function | Prokaryote | Eukaryote |
|---|---|---|
| Aminoacyl-tRNA delivery (GTPase) | EF-Tu | eEF1α |
| GDP/GTP exchange for delivery factor | EF-Ts | (intrinsic/other) |
| Translocation (GTPase) | EF-G | eEF2 |
| Polyproline-stall relief | EF-P | eIF5A |

**Release factor specificity:**

| Factor | Stop codons read |
|---|---|
| RF1 (bacteria) | UAA, UAG |
| RF2 (bacteria) | UAA, UGA |
| eRF1 (eukaryotes/archaea) | UAA, UAG, UGA (all three — "omnipotent") |

**tRNA gene counts (examples cited):** S. cerevisiae ≈ 275 tRNA genes; C. elegans: 620 of 29,647 total genes; human: 497 nuclear cytoplasmic tRNA genes + 22 mitochondrial + 324 pseudogenes, clustered heavily on chromosome 6p (~140 genes).

**Exit tunnel / translation rate:** tunnel ≈ 100 Å long, accommodates 30-60 amino acids; bacterial elongation rate ≈ 4-22 amino acids/second; eukaryotic incorporation rate ≈ ~1 amino acid per 1/6 second.

## Worked Example
**Tracing a bacterial mRNA through initiation, one elongation cycle, and termination (synthesizing Sections 11.5-11.7):**

1. IF3 and IF2 bind the free 30S subunit, forming an unstable complex; IF1 binding (occupying the A-site, contacting protein S12) stabilizes the complex and enables recruitment of initiator tRNA-fMet by IF2.
2. mRNA binds the 30S subunit (independent of tRNA-fMet order); if the Shine-Dalgarno sequence is present, it base-pairs with the 16S rRNA's anti-SD sequence, helping position the start codon in the P-site decoding region. IF2-GTP helps unfold inhibitory mRNA secondary structure (antagonized by IF3).
3. tRNA-fMet's anticodon pairs with the P-site AUG codon, forming the 30S initiation complex (30S-IC); this correct pairing represents the last fidelity checkpoint enforced by IF3/IF1.
4. The 50S subunit docks; IF2's GTPase activity is triggered, GTP is hydrolyzed, IF3 and IF1 dissociate, and a rate-limiting isomerization completes formation of the 70S initiation complex; IF2-GDP then leaves, vacating the A-site for the first elongation factor.
5. Elongation begins: EF-Tu-GTP delivers the second codon's cognate aminoacyl-tRNA to the A-site as a ternary complex. Correct codon-anticodon pairing (shielded by flipped-out A1492/A1493/G530) triggers EF-Tu's GTP hydrolysis and dissociation.
6. The PTC (an rRNA-based ribozyme active site) catalyzes peptide bond formation, transferring the formyl-methionine from the P-site tRNA to the A-site aminoacyl-tRNA, forming an fMet-aa dipeptide still attached to the A-site tRNA.
7. EF-G-GTP binds the A-site; rapid GTP hydrolysis acts as a "power stroke," driving large-scale ribosomal subunit rotation and L1-stalk movement that translocates the dipeptidyl-tRNA from A-site to P-site, the deacylated tRNA from P-site to E-site (then release), and exposes the next codon in the now-vacant A-site.
8. Steps 5-7 repeat for each subsequent codon until a stop codon (e.g., UAA) enters the A-site, where it is recognized by RF1 or RF2 rather than a tRNA.
9. The RF's domain 2 recognizes the stop codon at the decoding site while its domain 3's conserved GGQ motif reaches ~80 Å into the PTC, triggering hydrolysis of the ester bond linking the peptide to the final P-site tRNA and releasing the completed polypeptide through the exit tunnel.
10. RF3-GTP accelerates RF1/RF2 dissociation from the post-termination complex; ribosome recycling factor (RRF) and EF-G then drive large-subunit dissociation from the small subunit and mRNA, freeing all components for another round of initiation.

## Key Takeaways
1. Genetic code degeneracy is concentrated at the codon's third (wobble) position and is read by non-Watson-Crick wobble pairing, allowing far fewer tRNA species than there are sense codons — but specific tRNA modifications (e.g., lysidine, agmatidine) are required to prevent dangerous cross-reading of similar codons like AUA and AUG.
2. Aminoacylation fidelity is established before the ribosome even sees the tRNA: aaRSs use a universal two-step mechanism and, in ~10 of 23 cases, dedicated pre- and post-transfer editing domains to correct amino acid misactivation and misacylation.
3. Ribosomal fidelity during elongation is a kinetic, not purely thermodynamic, phenomenon — differential shielding of cognate vs. near-cognate codon-anticodon pairs by decoding-center nucleotides drives a two-step (initial selection + proofreading) discrimination process; disabling this (aminoglycosides) is directly bactericidal.
4. The ribosome is fundamentally a ribozyme — the peptidyl transferase reaction is catalyzed by rRNA in the large subunit, not by ribosomal proteins.
5. Bacterial and eukaryotic translation share the same core elongation logic (GTPase-delivered aminoacyl-tRNA, ribozyme-catalyzed peptide bond formation, GTPase-driven translocation) but diverge substantially in initiation complexity (Shine-Dalgarno vs. cap-dependent scanning/Kozak context) and termination (codon-specific RF1/RF2 vs. omnipotent eRF1).
6. Translation is actively regulated beyond the core mechanics — via ribosome heterogeneity (the "ribosome filter hypothesis"), miRNA-mediated interference, mRNA secondary structure, and nascent-peptide/exit-tunnel interactions (e.g., polyproline-induced stalling relieved by EF-P/eIF5A).

## Connects To
- **Ch 10**: The mature, capped, spliced, polyadenylated mRNA produced by the processes in Ch. 10 is the direct substrate for the initiation mechanisms (cap-dependent scanning, Kozak sequence recognition) detailed here.
- **Ch 12**: Frameshift mutations and nonsense mutations (Ch. 12) are directly interpretable through this chapter's reading-frame and stop-codon-recognition frameworks — a single-nucleotide indel here means every downstream codon (and likely premature termination) changes.
- **Ch 9**: The kinetic-proofreading logic used for ribosomal fidelity closely parallels DNA polymerase proofreading (Ch. 9), illustrating a general "two-step discrimination" strategy reused across the central dogma.
- **Ch 8**: Regulation of translation via mRNA-binding factors and ribosome heterogeneity connects to Ch. 8's broader treatment of post-transcriptional and post-translational control of protein output.
