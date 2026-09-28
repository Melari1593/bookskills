# Chapter 5: Investigating DNA

## Core Idea
A small toolkit of core techniques — DNA isolation, sequencing (Sanger and next-generation), PCR, restriction/ligation-based cloning, and bioinformatic analysis — together let researchers read, copy, cut-and-paste, and computationally interpret DNA, and these tools compound: PCR feeds sequencing and cloning, cloning feeds recombinant expression, and bioinformatics organizes and mines the output of all of them.

## Frameworks Introduced

- **Sanger (chain-termination) sequencing**: Uses dideoxynucleotides (ddNTPs) that lack a 3'-OH to randomly terminate DNA synthesis, generating a nested set of fragments whose lengths reveal sequence.
  - When to use: Reference-quality sequencing of individual clones/genes; historically the method used for the first human genome (2001).
  - How: Four separate reactions (or one with four dyes), each with a low ratio of one ddNTP (~1:100) to its normal dNTP; DNA polymerase extends a primed template until random ddNTP incorporation halts the chain; fragments separated by size via (capillary) gel electrophoresis and read shortest-to-longest from the primer end. Automated/fluorescent capillary versions process up to 384 samples/batch but degrade in quality after ~400-500 bases.

- **Next-Generation Sequencing (NGS) / high-throughput sequencing**: Massively parallel sequencing-by-synthesis or -by-detection, replacing single-reaction Sanger runs with millions of simultaneous short reads.
  - When to use: Whole-genome or large-scale sequencing where speed, cost, and depth of coverage matter more than single-read length.
  - How: Illumina (100-150 bp reads; fluorescently labeled reversible terminators, one base/cycle, imaged each cycle); Roche 454 (up to 1 kb reads; bead-based pyrosequencing, light released per nucleotide incorporation, variable-length homopolymer signal); Ion Torrent (~200 bp reads; detects H+ release electrically via semiconductor chip, no optics); Oxford Nanopore MinION (portable, real-time, up to 30 Gb/sample). NGS beats Sanger on sample size, speed (massively parallel), cost (~$1,000/genome now vs. ~$2.7 billion in 2003), and accuracy (redundant overlapping coverage), while Sanger still wins on raw single-read length.

- **Polymerase Chain Reaction (PCR)**: Exponential in-vitro amplification of a targeted DNA region using a thermostable polymerase (e.g., Taq) and two flanking primers.
  - When to use: Whenever a specific DNA segment needs to be copied billions-fold for cloning, diagnostics, or forensics — before sequencing, cloning, or genotyping.
  - How: Repeated three-temperature cycles — denaturation (~95°C, separates strands), annealing (50-65°C, primers bind), elongation (~75-80°C, polymerase extends) — doubling target copy number each cycle until reagents are exhausted (typically plateaus at 30-40 cycles). Variants: quantitative/real-time PCR (qPCR, using SYBR Green or sequence-specific hybridization probes to monitor amplification numerically) and reverse-transcription PCR (RT-PCR, converts mRNA to cDNA first for gene-expression analysis).

- **Restriction-enzyme/ligase cloning**: Cutting DNA at specific recognition (often palindromic) sequences and rejoining fragments to build recombinant DNA molecules.
  - When to use: Inserting a gene of interest into a cloning/expression vector for propagation, study, or protein production.
  - How: Restriction endonucleases (e.g., EcoRI — sticky ends; SmaI/EcoRV — blunt ends) cut vector and insert at compatible sites (often within a multiple cloning site, MCS); DNA ligase joins compatible ends; the vector supplies an origin of replication, a selectable marker (e.g., antibiotic resistance), and — for expression — a promoter and ribosome binding site. Alternatives requiring no restriction/ligase step: TOPO cloning (topoisomerase-charged vector) and Gateway cloning (site-specific recombination).

## Key Concepts
- **Genomic DNA vs. cDNA**: Genomic DNA (gDNA) is the full chromosomal sequence including introns; complementary DNA (cDNA) is reverse-transcribed from mature mRNA (via reverse transcriptase) and therefore contains only exons — this lets eukaryotic genes be expressed in intron-blind prokaryotic hosts.
- **Palindromic recognition sequence**: A restriction site reads the same 5'→3' on both strands (e.g., GAATTC), which is why the enzyme can cut both strands symmetrically to leave sticky or blunt ends.
- **Cloning vector**: A self-replicating DNA carrier (plasmid, phage, cosmid, BAC, YAC) with defined insert-capacity, copy number, and required elements (ori, selectable marker, cloning site, and for expression: promoter + RBS).
- **Gel electrophoresis**: Separates nucleic acid fragments by size (and charge) as they migrate through a gel matrix toward the positive electrode under an electric field; smaller fragments migrate faster.
- **Selectable marker**: A gene (commonly antibiotic resistance, e.g., beta-lactamase/ampicillin resistance) that lets only successfully transformed cells survive/grow, distinguishing them from untransformed cells.
- **Gene synthesis / codon optimization**: De novo chemical synthesis of DNA (phosphoramidite chemistry, ~200 bp practical single-oligo limit) without a template; codon optimization exploits genetic code degeneracy (>10^150 synonymous combinations for a 300-aa protein) to boost heterologous expression 2-10× (occasionally >100×).
- **Bioinformatics**: The hybrid discipline combining molecular biology, computer science, mathematics, and statistics to store, annotate, and mine large-scale biological data (genomics, proteomics, comparative genomics, drug discovery, personalized medicine).
- **BLAST**: The standard tool for aligning a query DNA/protein sequence against sequence databases to find homologs — representative of the broader landscape of specialized bioinformatics tools (Table 5.1-5.5 in the source list dozens by task: motif-finding, phylogenetics, structure prediction, gene expression analysis).

## Mental Models
- Use PCR when you need many copies of a *known* short region fast; use cloning when you need the gene stably maintained, propagated, or expressed in a living host; use sequencing when you need to *read* an unknown or variant sequence.
- Think of a cloning vector as a modular delivery vehicle: swap the insert-capacity/copy-number/host combination (plasmid → cosmid → BAC → YAC) as the DNA fragment you need to carry grows from kilobases to megabases.
- NGS vs. Sanger is a throughput/read-length trade-off: NGS wins on cost, speed, and depth via massive parallelism with short reads; Sanger still wins when you need one long, gold-standard read from a single template.
- Treat bioinformatics tools as a pipeline, not a single tool: raw sequence → alignment/homology (BLAST) → structure/function prediction → pathway/expression analysis → clinical or evolutionary interpretation.

## Anti-patterns / Common Misconceptions
- **"PCR and real-time PCR (qPCR) are the same thing"**: Standard PCR only gives qualitative/endpoint results; qPCR adds fluorescent monitoring during amplification for quantitative measurement — they are frequently confused but are distinct techniques (as are RT-PCR and real-time PCR, despite similar names).
- **"Restriction/ligase cloning is the only way to build recombinant DNA"**: TOPO and Gateway cloning bypass restriction digestion and ligase entirely, using topoisomerase charging or site-specific recombination instead.
- **"More cycles of PCR means more product, without limit"**: Amplification is exponential only up to a point; it plateaus around 30-40 cycles due to reagent depletion, inhibitors, and self-annealing of accumulated product.
- **"NGS reads are inherently long"**: NGS platforms (Illumina ~100-150 bp, Ion Torrent ~200 bp) actually produce much shorter reads than classic Sanger (400-500 bp usable); NGS's power comes from parallel depth and computational reassembly, not per-read length (454/Nanopore are exceptions with longer reads).

## Key Equations & Reference Tables

**Vector insert capacity and copy number**

| Vector type | Insert capacity | Typical copy number | Common use |
|---|---|---|---|
| Plasmid | Up to ~15 kb | High (e.g., pUC19: 500-700/cell) or low | General cloning/expression |
| Bacteriophage (λ) | Up to ~53 kb (avg. genome ~48.5 kb) | — | Genomic libraries |
| Cosmid | 28-45 kb | — | Larger inserts, λ packaging |
| Bacterial Artificial Chromosome (BAC) | Up to 350 kb | 1/cell | Genome sequencing (e.g., HGP) |
| Yeast Artificial Chromosome (YAC) | >1 Mb | — | Very large fragment/genome mapping |
| Human Artificial Chromosome | No practical upper limit | — | Gene-transfer research |

**Sequencing platform comparison**

| Platform | Read length | Detection mechanism |
|---|---|---|
| Sanger (automated) | ~400-500 bp usable | Fluorescent ddNTP, capillary electrophoresis |
| Illumina | 100-150 bp | Fluorescent reversible terminators |
| Roche 454 | Up to 1 kb | Pyrosequencing (light emission) |
| Ion Torrent | ~200 bp | H+ release, semiconductor pH sensing |
| Oxford Nanopore MinION | Long, real-time | Portable, up to 30 Gb/sample |

**Cost of sequencing a human genome**: ~$2.7 billion (2003, HGP) → ~$300,000 (2006, Sanger) → ~$1,000 (current, NGS)

**PCR reaction cycle**: Denaturation (~95°C) → Annealing (50-65°C) → Elongation (~75-80°C), repeated ~30-40×, doubling target amplicon each cycle (exponential: copies ≈ initial × 2^n cycles, until plateau).

## Worked Example
**Cloning a PCR-amplified gene into an expression plasmid (Figure 5.21 workflow, reconstructed):** Suppose a researcher wants bacteria to express a eukaryotic protein. First, mRNA is isolated and reverse-transcribed into cDNA (so introns are already removed). PCR amplifies the coding sequence using primers tailed with an EcoRI site, producing many billion-fold copies of just that gene. Both the PCR product and the target plasmid vector are digested with EcoRI, generating matching sticky ends. DNA ligase joins the insert into the vector's multiple cloning site, positioned downstream of a promoter (e.g., T7 or lac) and ribosome binding site so the host's transcription/translation machinery will express it. The ligated mixture is transformed into E. coli, and only cells that took up a plasmid survive on antibiotic-selective media (the plasmid's beta-lactamase marker confers resistance). Successful clones are verified by restriction digestion (checking fragment sizes) and/or Sanger sequencing before scaling up the culture for protein production. This chain — PCR → restriction digest → ligation → transformation → selection → verification — is the generic path from "gene of interest" to "recombinant protein-producing organism," and every step draws on a technique introduced earlier in the chapter.

## Key Takeaways
1. Sanger sequencing (chain-termination via ddNTPs) was the workhorse method (1977-~2005, first human genome); NGS platforms (Illumina, 454, Ion Torrent, Nanopore) replaced it for large-scale work by trading read length for massive parallelism, speed, and cost.
2. PCR's power is exponential amplification from trace template using only two primers, a thermostable polymerase, and thermal cycling — but it plateaus (~30-40 cycles) and is highly sensitive to contamination and nonspecific primer annealing.
3. Cloning vectors form a size-capacity ladder (plasmid < cosmid < BAC < YAC < human artificial chromosome); pick the vector by how much DNA you need to carry and in what host.
4. Restriction enzymes cut palindromic recognition sequences to leave sticky or blunt ends; only compatible-end fragments ligate together, which is what makes directional, predictable cloning possible.
5. cDNA (from mRNA via reverse transcriptase) strips out introns, enabling eukaryotic genes to be expressed in prokaryotic hosts that cannot splice.
6. Bioinformatics is not one tool but an ecosystem (BLAST for homology, structure predictors, expression/motif databases, phylogenetics) layered on top of the wet-lab techniques to interpret sequence data at scale.
7. Cost and speed of sequencing dropped roughly six orders of magnitude (billions to ~$1,000 per genome) in about two decades, which is the single biggest enabler of modern genomics and personalized medicine.

## Connects To
- **Ch 4 (DNA, RNA, and the Human Genome)**: The structural features of DNA (base pairing, antiparallel strands, palindromic sequences) explained there are exactly what restriction enzymes, primers, and polymerases in this chapter exploit mechanically.
- **Ch 6 (Enzyme Principles)**: DNA polymerase, reverse transcriptase, restriction endonucleases, ligase, and topoisomerase are all concrete enzymes whose kinetics, specificity, and catalytic mechanisms are formalized in Chapter 6's enzyme framework.
