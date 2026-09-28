# Chapter 4: DNA, RNA, and the Human Genome

## Core Idea
DNA's double-helical structure (Watson-Crick base pairing) is not a fixed rod but a dynamically flexible, hierarchically packaged molecule — from base pairs, to nucleosomes, to chromatin fibers, to chromosome territories — and this packaging, together with sparse but precisely organized gene structure, is what makes a 2-meter-long, 3-billion-base-pair genome fit inside a nucleus and function.

## Frameworks Introduced

- **Watson-Crick Base Pairing / DNA Double Helix (1953)**: A always pairs with T (2 H-bonds), G always pairs with C (3 H-bonds); the two antiparallel strands run 5'→3' and 3'→5', held together by a sugar-phosphate backbone with major and minor grooves that provide sequence-recognition surfaces for proteins.
  - When to use: Baseline model for any DNA structure, replication, transcription, or protein-DNA recognition question.
  - How: Purines (A, G) pair with pyrimidines (C, T/U); antiparallel strand orientation; synthesis always proceeds 5'→3'.

- **A-, B-, and Z-DNA conformations**: The double helix is polymorphic, not a single fixed structure.
  - When to use: Explaining DNA behavior under dehydration, RNA-DNA hybrids, or high-salt/alternating purine-pyrimidine sequences.
  - How: B-DNA (right-handed, ~10 bp/turn, 3.4 Å rise/bp, 19-20 Å diameter) is the standard physiological form; A-DNA (right-handed, 11 bp/turn, 2.56 Å rise/bp) forms under dehydration or in RNA-DNA hybrids (2'-OH sterically blocks B-form); Z-DNA (left-handed, zigzag backbone, 12 bp/turn) forms in alternating purine-pyrimidine tracts under high salt or in vivo in short regions.

- **Nucleosome / Chromatin Packaging Hierarchy**: DNA compaction proceeds through discrete, named orders of structure.
  - When to use: Explaining how ~2 m of DNA fits in a nucleus, or how packaging affects gene accessibility.
  - How: 1st order = naked double helix (2 nm); 2nd order = nucleosome core (~146 bp wrapped 1.65 times left-handed around a histone octamer, ~11 nm); 3rd order = 30 nm solenoid/zigzag fiber (6 nucleosomes linked by H1); higher order = ~1 Mb chromatin loop domains organized into chromosome territories.

- **Chromosome Territory (CT) Models**: Competing models for how chromosomes occupy 3D nuclear space during interphase.
  - When to use: Explaining spatial gene regulation, transcription factories, or nuclear organization.
  - How: CT-Interchromatin Compartment (CT-IC) model treats CTs and the interchromatin compartment (IC) as distinct; the Interchromatin Network (ICN) model treats chromatin fibers as intermingling in cis and trans; the Fraser-Bickmore model emphasizes giant loops sharing transcription factories; chromatin polymer models apply physics/entropy-based reasoning. Gene-rich chromosomes sit toward the nuclear interior, gene-poor ones toward the periphery.

- **End Replication Problem / Telomere Maintenance**: DNA polymerase's unidirectional (5'→3') synthesis cannot fully replicate the lagging strand's extreme 3' end.
  - When to use: Explaining cellular aging, senescence, and cancer immortalization.
  - How: Each division loses a small piece of telomeric TTAGGG repeat sequence; telomerase (active in stem/immune cells) or the recombination-based Alternative Lengthening of Telomeres (ALT) pathway can restore length; critically short telomeres trigger senescence or apoptosis (Hayflick limit); most cancers reactivate telomerase or ALT.

## Key Concepts
- **Nucleoside vs. nucleotide**: A nucleoside is sugar + base; a nucleotide adds one, two, or three phosphates at the 5' position (mono-, di-, tri-phosphate).
- **Purines vs. pyrimidines**: Purines (A, G) are double-ring bases found in both DNA and RNA; pyrimidines (C, T-DNA only, U-RNA only) are single-ring.
- **Phosphodiester linkage**: Bond formed when the growing chain's 3'-OH attacks the incoming nucleoside triphosphate's α-phosphate, releasing pyrophosphate (PPi); PPi hydrolysis (ΔG ≈ -7 kcal/mol) drives the overall reaction (ΔG ≈ -6.5 kcal/mol) forward and prevents reversal (pyrophosphorolysis).
- **DNA supercoiling**: Over- or under-winding of the helix; expressed as twist + writhe; negative supercoiling (most common in nature) facilitates replication/transcription access; topoisomerases relax or introduce supercoils and resolve catenation/knotting.
- **Plectoneme vs. toroid**: Two shapes of supercoiled DNA — plectonemes (two-start right-handed helix, common in bacterial plasmids) and toroids (one-start left-handed coil from negative supercoiling).
- **Histone octamer / nucleosome**: Two each of H2A, H2B, H3, H4 form an octamer (~63 Å diameter) around which ~146 bp of DNA wraps; linker histone H1/H5 locks DNA at nucleosome entry/exit points.
- **Mitochondrial genome**: Circular, 16,569 bp in humans, encodes only 13 proteins (most of the ~1,500 mitochondrial proteins are nuclear-encoded); supports the endosymbiotic theory via sequence similarity to alphaproteobacteria.
- **Gene structure elements (eukaryotic)**: Promoter (core + proximal), enhancers/silencers (can be many kb away), 5'/3' UTRs, exons/introns, 5' cap, poly-A tail — contrasted with prokaryotic polycistronic operons, ribosome binding sites (RBS), translational coupling, operators, and riboswitches.
- **Open reading frame (ORF)**: The gene region actually encoding protein/RNA information, read 5'→3' on the sense/coding strand.
- **G-quadruplex / T-loop / D-loop**: Telomere-specific structures — G4 (four guanines stacked in a planar unit, stabilized by metal-ion chelation), T-loop (single-stranded telomere end tucked into duplex DNA), D-loop (the resulting triple-stranded structure at the T-loop junction).

## Mental Models
- Think of DNA structure as a spectrum of conformations (A/B/Z), not a single rigid shape — local sequence, hydration, and protein binding all shift it.
- Use the packaging-hierarchy ladder (helix → nucleosome → 30 nm fiber → loop domain → territory) whenever reasoning about "how does X get access to this DNA" — compaction level is a proxy for accessibility.
- Treat telomere length as a molecular clock: shortening is protective against uncontrolled division in normal cells, but its evasion (telomerase/ALT reactivation) is a near-universal enabling step in cancer.
- Genome statistics only make sense in context: humans have >3 billion bp but only ~1.5% is protein-coding — most of "the genome" is regulatory sequence, repeats (LINEs/SINEs), introns, and sequence of unknown function, not genes.

## Anti-patterns / Common Misconceptions
- **"DNA is a static double helix"**: Wrong — it breathes (local transient strand opening), denatures/reanneals, tolerates intercalation and base-flipping, and switches between A/B/Z forms depending on conditions.
- **"More genes were expected before sequencing"**: Pre-genome estimates ran 50,000-140,000 genes; the real count is far lower (~19,000-20,000 protein-coding, ~46,831+ total loci including ~2,300 microRNA genes) — genome complexity comes from regulation and non-coding elements, not raw gene count.
- **"Introns are prokaryotic too"**: Introns are essentially absent in prokaryotes; polycistronic operons and translational coupling are the prokaryotic norm instead.
- **"Positive supercoiling is the default state"**: Negative supercoiling predominates in nature; positive supercoiling is transiently generated ahead of replication/transcription forks and must be relaxed by topoisomerases or it stalls the machinery.

## Key Equations & Reference Tables

**Thermodynamics of DNA synthesis**
- Pyrophosphate hydrolysis: ΔG ≈ -7 kcal/mol
- Overall polymerization reaction: ΔG ≈ -6.5 kcal/mol

| DNA form | Handedness | bp/turn | Rise/bp | Diameter | Occurrence |
|---|---|---|---|---|---|
| B-DNA | Right | 10 | 3.4 Å (0.34 nm) | ~19-20 Å | Predominant physiological form |
| A-DNA | Right | 11 | 2.56 Å | ~19 Å | Dehydrated DNA; RNA-DNA hybrids; dsRNA |
| Z-DNA | Left | 12 | ~19 Å (zigzag) | ~19 Å | Alternating purine-pyrimidine, high salt, some in vivo regions |

| Quantity | Value |
|---|---|
| Human genome size | >3 billion bp |
| Human diploid cell DNA length (uncoiled) | ~1.8 m; ~0.09 mm (90 μm) as chromatin |
| Human chromosomes | 23 pairs (46 total): 22 autosome pairs + 1 sex pair (XX/XY) |
| Mitochondrial genome | 16,569 bp; encodes 13 proteins |
| Nucleosome DNA wrap | ~146 bp, 1.65 left-handed turns around histone octamer |
| Protein-coding fraction of genome | ~1.5% |
| Human gene count | ~19,000-20,000 protein-coding; ≥46,831 total loci + ~2,300 microRNA genes |
| Telomere repeat | TTAGGG (human), thousands of repeats |

## Worked Example
**Reasoning through the "end replication problem":** DNA polymerase synthesizes only 5'→3' and needs an RNA primer to start. On the lagging strand, replication proceeds discontinuously as Okazaki fragments (~100-200 nt), each starting with its own RNA primer. When primers are removed and replaced with DNA, every gap can be filled by extending from the adjacent fragment's 3'-OH — except the very last primer at the chromosome's extreme 3' end, where there is no upstream fragment to extend from. That gap cannot be filled, so a small stretch of DNA is lost each division. Because human telomeres consist of thousands of noncoding TTAGGG repeats, this loss consumes "buffer" sequence rather than genes — but only up to a point. Once telomeres shorten past a critical threshold, the cell can no longer distinguish its own chromosome ends from DNA damage, and it enters senescence or apoptosis (the Hayflick limit). Stem cells, lymphocytes, and most cancer cells bypass this by expressing telomerase, which uses an internal RNA template to re-extend the 3' overhang; cancers lacking telomerase often instead activate ALT, a recombination-based end-extension pathway. This single structural quirk of DNA polymerase directionality thus underlies both normal cellular aging and a common route to cellular immortalization in cancer.

## Key Takeaways
1. DNA structure is conformationally flexible (A/B/Z forms, breathing, supercoiling) — "the double helix" is a family of related structures, not one shape.
2. Genome compaction is hierarchical and named at every level: helix → nucleosome (146 bp/octamer) → 30 nm fiber → ~1 Mb loop domains → chromosome territories.
3. Human genome coding capacity is sparse: only ~1.5% of 3+ billion bp is protein-coding; the rest is regulatory DNA, ncRNA genes, LINEs/SINEs, introns, and unknown-function sequence.
4. Eukaryotic and prokaryotic gene structure diverge mainly in regulatory complexity and coupling of transcription/translation: eukaryotes separate the two processes and add extensive introns/UTRs/enhancers; prokaryotes co-transcribe/translate polycistronic operons with operators and riboswitches.
5. The end replication problem — an inescapable consequence of 5'→3'-only DNA polymerase activity — necessitates telomeres and telomerase, and its dysregulation (via telomerase or ALT reactivation) is central to cancer biology.
6. Topoisomerases are essential housekeeping enzymes: without them, supercoiling, catenation, and knotting from replication/transcription would physically jam the genome.

## Connects To
- **Ch 5 (Investigating DNA)**: The structural features described here (double helix, base pairing, genome organization) are the substrate that sequencing, PCR, cloning, and bioinformatics tools in Chapter 5 are built to read and manipulate.
- **Ch 6 (Enzyme Principles)**: DNA/RNA polymerases, topoisomerases, and ligases introduced structurally here are concrete examples of the enzyme kinetics, specificity, and catalytic principles formalized in Chapter 6.
