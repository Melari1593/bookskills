---
name: ahern-biochemistry
description: "Knowledge base from \"CH450/CH451: Biochemistry — Defining Life at the Molecular Level\" by Kevin Ahern & Indira Rajagopal (hosted online by Western Oregon University). Use when applying biochemistry frameworks for protein structure/purification, enzyme kinetics and catalysis, DNA/RNA structure and manipulation, replication, transcription, translation, DNA repair, or transcriptional/epigenetic control, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CH450/CH451: Biochemistry — Defining Life at the Molecular Level
**Authors**: Kevin Ahern & Indira Rajagopal | **Chapters**: 13 | **Source**: WOU Online Chemistry Textbooks | **Generated**: 2026-09-07

## How to Use This Skill

- **Without arguments** — load core frameworks below for reference
- **With a topic** — ask about `enzyme kinetics`, `DNA repair`, `translation`, or another indexed topic; I find and read the relevant chapter
- **With a chapter** — ask for `ch07`; I load that specific chapter file
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered below, I will read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Thermodynamics of reactions** — ΔG = ΔG° + RTlnQ. ΔG° reflects intrinsic reactant/product stability (from Keq); RTlnQ reflects concentration. ΔG<0 → products; =0 → equilibrium; >0 → reactants. Spontaneity depends on ΔG=ΔH−TΔS, never ΔH alone. Le Chatelier's Principle predicts shift direction under perturbation. Entropy = S=k ln W (accessible microstates), not "disorder" — this correctly explains the hydrophobic effect and protein folding as entropy-driven.

**Enzymes never change equilibrium** — they only lower activation energy, accelerating approach to a thermodynamically fixed Keq. Michaelis-Menten kinetics (v=Vmax[S]/(Km+[S])) is the default lens: Km = affinity (inverse), Vmax = rate ceiling. Inhibitor type is diagnosed from how Km/Vmax shift (competitive: ↑Km only; noncompetitive: ↓Vmax only; uncompetitive: both ↓). Allosteric, usually multi-subunit, regulatory enzymes show sigmoidal kinetics via MWC (concerted, all-or-none) or KNF (sequential, graded) cooperativity.

**Seven catalytic strategies** recur across all enzyme mechanisms: covalent, acid-base, electrostatic, desolvation, catalysis by approximation, strain distortion, and cofactor catalysis. The serine protease catalytic triad (Ser-His-Asp) is the canonical worked example combining four of these at once. Ribozymes (spliceosome core, ribosomal peptidyl transferase center) prove RNA alone can catalyze, supporting the RNA World hypothesis.

**Protein structure is strictly hierarchical**: primary sequence → secondary structure (α-helix, β-sheet, via Ramachandran-allowed Phi/Psi) → tertiary fold → quaternary assembly. Anfinsen's Dogma: native structure is fully encoded by sequence. The hydrophobic effect (entropy-driven water release), not H-bonding alone, is folding's dominant force. Intrinsically disordered proteins are a legitimate, common functional class.

**DNA is a flexible, hierarchically packaged molecule**, not a static rod: A/B/Z conformations; helix → nucleosome (146 bp/octamer) → 30 nm fiber → loop domains → chromosome territories. Only ~1.5% of the human genome is protein-coding. Replication is semiconservative (Meselson-Stahl) and unidirectional 5'→3' only — this single constraint explains leading/lagging strand asymmetry, Okazaki fragments, and the end-replication problem (solved by telomerase).

**Central dogma machinery uses recurring design patterns**: multi-subunit polymerases requiring accessory factors for specificity (sigma factors in bacteria, the >100-protein PIC in eukaryotes); kinetic proofreading (not just thermodynamics) for fidelity, in both DNA replication and ribosomal decoding; and staged, checkpoint-gated assembly (spliceosome E→A→B→B*→C; replisome licensing/firing).

**DNA repair pathway choice is diagnostic on lesion type**: single mismatch → MMR; single damaged base → BER; bulky/helix-distorting adduct → NER; double-strand break → NHEJ (any phase, low fidelity) or HR (S/G2/M only, high fidelity). Fewer than 1 in 1,000 daily lesions becomes a fixed mutation. DNA damage checkpoints (ATM/ATR→CHK1/CHK2→p53) converge on CDK inhibition regardless of trigger.

**Gene regulation compounds across layers**: bacterial operons (repressible vs. inducible, often integrating multiple signals via AND-gate logic like lac's CAP-cAMP + repressor); eukaryotic regulation requires BOTH an activated transcription factor AND accessible chromatin (histone code: writers/erasers/readers; ATP-dependent remodelers) — motif presence alone is not sufficient (~99.8% of predicted TF motifs are unoccupied in vivo). PTMs and alternative splicing/polyadenylation expand ~20,000 genes into a proteome of over a million distinct protein forms.

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-foundations-of-biochemistry.md) | The Foundations of Biochemistry | ΔG/Keq/Le Chatelier, Henderson-Hasselbalch, lock-and-key vs. induced fit, cell transport |
| [ch02](chapters/ch02-protein-structure.md) | Protein Structure | Hierarchical structure, Ramachandran plot, Anfinsen's Dogma, hydrophobic collapse |
| [ch03](chapters/ch03-investigating-proteins.md) | Investigating Proteins | Purification scheme, chromatography, SDS-PAGE, X-ray/NMR/cryo-EM trade-offs |
| [ch04](chapters/ch04-dna-rna-human-genome.md) | DNA, RNA, and the Human Genome | Watson-Crick pairing, A/B/Z-DNA, chromatin packaging, end-replication problem |
| [ch05](chapters/ch05-investigating-dna.md) | Investigating DNA | Sanger/NGS sequencing, PCR, restriction/ligase cloning, vectors |
| [ch06](chapters/ch06-enzyme-principles-biotechnology.md) | Enzyme Principles and Biotechnological Applications | Michaelis-Menten, Lineweaver-Burk, inhibition types, allosteric (MWC) |
| [ch07](chapters/ch07-catalytic-mechanisms-of-enzymes.md) | Catalytic Mechanisms of Enzymes | Seven catalytic strategies, serine protease triad, ribozymes |
| [ch08](chapters/ch08-protein-regulation-degradation.md) | Protein Regulation and Degradation | Isozymes, PTMs, MWC/KNF, zymogen activation, ubiquitin-proteasome |
| [ch09](chapters/ch09-dna-replication.md) | DNA Replication | Meselson-Stahl, replisome assembly, origin licensing, telomerase |
| [ch10](chapters/ch10-transcription-rna-processing.md) | Transcription and RNA Processing | Sigma factors, PIC assembly, termination models, splicing, capping/CPA |
| [ch11](chapters/ch11-translation.md) | Translation | Wobble hypothesis, aaRS classes, kinetic proofreading, elongation cycle |
| [ch12](chapters/ch12-dna-damage-repair-mutations.md) | DNA Damage, Repair, and Mutations | Mutation types, MMR/BER/NER/HR/NHEJ, damage checkpoints |
| [ch13](chapters/ch13-transcriptional-control-epigenetics.md) | Transcriptional Control and Epigenetics | Operon models, CAP-cAMP, chromatin/histone code, p53, epigenetic inheritance |

## Topic Index

- **Allosteric regulation (MWC/KNF)** → ch06, ch08
- **Antibodies / Western blot / ELISA** → ch03
- **Catalytic mechanisms (7 strategies)** → ch07
- **Chromatin / histone code / epigenetics** → ch04, ch13
- **Chromatography** → ch03
- **Cloning (vectors, restriction enzymes)** → ch05
- **DNA damage & repair (MMR/BER/NER/HR/NHEJ)** → ch12
- **DNA replication (replisome, telomeres)** → ch09
- **DNA structure (A/B/Z, packaging)** → ch04
- **Enzyme inhibition** → ch06
- **Enzyme kinetics (Michaelis-Menten)** → ch06
- **Epigenetic inheritance** → ch13
- **Free energy / thermodynamics** → ch01
- **Genetic code / wobble / codons** → ch01, ch11
- **Mutations (types)** → ch12
- **Operons (lac, trp)** → ch13
- **p53** → ch13
- **PCR / sequencing (Sanger, NGS)** → ch05
- **Protein degradation (ubiquitin-proteasome)** → ch08
- **Protein folding / structure** → ch02
- **Protein purification** → ch03
- **PTMs (post-translational modifications)** → ch08
- **Ribozymes** → ch07, ch10, ch11
- **Splicing / RNA processing** → ch10
- **Structural biology (X-ray/NMR/cryo-EM)** → ch03
- **Transcription (prokaryotic & eukaryotic)** → ch10
- **Translation (initiation/elongation/termination)** → ch11
- **Zymogen activation** → ch08

## Supporting Files

- [glossary.md](glossary.md) — ~90 key terms with definitions and chapter references
- [patterns.md](patterns.md) — 18 concrete techniques/decision frameworks (when to use, how, trade-offs)
- [cheatsheet.md](cheatsheet.md) — quick-reference tables, decision rules, and thresholds

---

## Scope & Limits

This skill covers the 13 chapters of Ahern & Rajagopal's online biochemistry textbook (protein structure/investigation, enzyme kinetics/catalysis, DNA/RNA structure/investigation, replication, transcription, translation, DNA repair, and transcriptional/epigenetic control). It does not cover metabolic pathways (glycolysis, TCA cycle, etc.) or lipid biochemistry in depth, as the source chapters converted here focus on the molecular-biology/protein-biochemistry track. For topics beyond this book, check related skills or ask directly.
