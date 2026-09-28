# Chapter 9: DNA Replication

## Core Idea
DNA replication is semiconservative (each daughter duplex has one parental and one new strand, proven by the Meselson-Stahl experiment) and is carried out by a highly conserved but increasingly complex multi-protein replisome machine across prokaryotes, eukaryotes, and mitochondria — with distinct solutions needed for circular vs. linear genomes and for the fundamental asymmetry of leading/lagging strand synthesis.

## Frameworks Introduced
- **Semiconservative Replication Model, proven by the Meselson-Stahl Experiment (Section 9.1)**: the foundational named experiment of molecular biology.
  - How: E. coli grown in heavy ¹⁵N medium (labeling parental DNA), then shifted to ¹⁴N medium. After one generation, DNA banded at an intermediate density (ruling out the conservative model, which predicts two separate bands). After two generations, DNA formed two bands — one intermediate, one light — ruling out the dispersive model and confirming semiconservative replication as the only model consistent with both generations of data.
  - When to use: this is the canonical example of using physical/density separation (ultracentrifugation) to distinguish between competing mechanistic models when direct observation isn't possible.
- **The Prokaryotic Replisome Assembly Pathway (Section 9.2)**: a step-ordered named model for how replication initiates and proceeds in bacteria (E. coli as the model organism).
  - How: DnaA (initiator) binds oriC, melts the AT-rich DNA to form a bubble → DnaC (helicase loader) loads DnaB (helicase) hexamers onto each ssDNA strand → SSB coats remaining ssDNA → each DnaB recruits DnaG (primase) to synthesize RNA primers → DNA polymerase III holoenzyme (Pol III HE) assembles to form the core replisome → bidirectional replication proceeds from oriC until forks meet at Ter sites bound by Tus protein (termination, forming a polar "replication fork trap").
  - When to use: as the reference pathway for "how does a circular, single-origin genome get copied accurately and bidirectionally."
- **Leading/Lagging Strand Asymmetry and Okazaki Fragment Synthesis**: since DNA polymerases synthesize only 5′→3′, and the two template strands are antiparallel, one new strand (leading) is made continuously in the direction of fork movement, while the other (lagging) must be made discontinuously as short, individually primed Okazaki fragments (bacteria: ~1000-2000 nt; eukaryotes: ~100-200 nt) that are later joined.
  - How: primase lays an RNA primer for each fragment → DNA polymerase extends it → DNA polymerase I (bacteria) or FEN1 (eukaryotes) removes the RNA primer and fills the gap with DNA → DNA ligase seals the remaining nick.
- **Rolling Circle Replication (Section 9.3)**: the mechanism used by many plasmids, some bacteriophages, and some eukaryotic viruses to unidirectionally copy circular genomes.
  - How: a nick is made at the double-stranded origin (dso); DNA polymerase III extends the 3′-OH of the nicked strand using the un-nicked strand as template, displacing the original nicked strand; once the displaced strand recircularizes, RNA primase initiates synthesis at its single-stranded origin (sso) to convert it to double-stranded DNA.
- **Eukaryotic Origin Licensing and Firing (Section 9.4)**: a two-step control model that prevents both under- and over-replication of large, multi-origin linear genomes.
  - How: during late M/G1, Cdc6 and Cdt1 load inactive MCM2-7 double hexamers onto DNA at origins (origin licensing, creating a pre-replication complex/pre-RC). At S-phase onset, cyclin-CDK-driven phosphorylation (e.g., Cyclin E-CDK2) triggers a subset (10-20% in mammalian cells) of licensed origins to actually initiate (origin firing), assembling the active replisome (Cdc45, GINS, Pol ε/δ). Unfired licensed origins serve as reserve/backup origins activated under replication stress.
- **The Cell Cycle / CDK-Cyclin Control Model**: ordered phases (G1 → S → G2 → M, with G0 as a resting/senescent exit state) gated by cyclin-dependent kinase (CDK/CDC) complexes that require binding of stage-specific cyclins for activity; e.g., Cyclin E-CDK2 phosphorylates pRb, releasing E2F transcription factors to drive the G1→S transition and DNA replication gene expression.
- **Mitochondrial Strand-Displacement Replication Model (Section 9.5)**: distinct from both nuclear and rolling-circle mechanisms.
  - How: replication initiates unidirectionally at OH; POLγ synthesizes the new H-strand while mtSSB coats and protects the displaced parental H-strand; when the fork passes the second origin OL (~2/3 around the genome), the exposed parental H-strand there forms a stem-loop that blocks mtSSB, allowing mitochondrial RNA polymerase (POLRMT) to prime L-strand synthesis, which POLγ then extends; H- and L-strand synthesis proceed until both are complete circles; DNA Ligase III seals the strands.
- **The End-Replication Problem and Telomerase Solution (Section 9.6)**: explains why linear chromosomes need a dedicated protective/extension mechanism that circular genomes do not.
  - How: because the terminal RNA primer at the extreme 3′ end of the lagging strand cannot be replaced by DNA polymerase (no upstream 3′-OH to extend from), 30-200 nucleotides are lost per replication round. Telomerase (TERT reverse transcriptase + TERC RNA template) uses its RNA component as a template to extend the 3′ single-stranded overhang de novo, compensating for this loss in germline/stem/cancer cells; most somatic cells lack sufficient telomerase activity and undergo progressive telomere shortening toward the Hayflick limit and replicative senescence.

## Key Concepts
- **Origin of replication (oriC)**: in E. coli, a single ~245 bp, AT-rich sequence where replication initiates; eukaryotes use hundreds (yeast) to tens of thousands (humans) of origins per genome, mostly without strict consensus sequences (except in S. cerevisiae).
- **Replisome**: the multi-protein complex (helicase, primase, polymerase(s), clamp, clamp loader, SSB/RPA, etc.) that assembles at the replication fork to carry out coordinated DNA synthesis.
- **DNA Polymerase III (Pol III HE)**: the primary bacterial replicative polymerase; a 10-subunit holoenzyme organized into the αεθ core (α = polymerase, ε = 3′→5′ proofreading exonuclease, θ = stabilizer), the β2 sliding clamp, and the clamp-loader complex; incorporates 600-1,000 nt/sec with >100,000 nt processivity per binding event and an error rate of ~1 per million.
- **DNA Polymerase I**: removes RNA primers via its 5′→3′ exonuclease activity (housed in the Klenow fragment) and fills the resulting gaps with DNA using its 5′→3′ polymerase activity; cannot seal the final nick (DNA ligase does that).
- **Eukaryotic replicative polymerase trio**: Pol α (primase-associated, lays RNA-DNA hybrid primers on both strands and at each Okazaki fragment), Pol ε (continuous leading-strand synthesis), Pol δ (discontinuous lagging-strand/Okazaki fragment synthesis) — all three are B-family polymerases and are essential for viability.
- **PCNA (Proliferating Cell Nuclear Antigen)**: the eukaryotic homotrimeric sliding clamp (functional analog of bacterial β2 clamp) that boosts polymerase processivity up to 1,000-fold.
- **Topoisomerases**: Type I (nick one strand, no ATP required, relax supercoiling by controlled rotation, e.g., E. coli Topo I removes only negative supercoils, Topo III aids decatenation) vs. Type II (break both strands, require ATP, pass one duplex through another, e.g., DNA gyrase relieves positive supercoiling ahead of the fork, Topoisomerase IV resolves precatenanes/aids termination).
- **Tus-Ter termination complex**: ten polar 23 bp Ter sites in E. coli, bound by monomeric Tus protein; forms a "locked" complex (via a flipped-out cytosine) that blocks replisome passage from one direction only, ensuring forks converge and stop in the terminus region.
- **Telomere / shelterin complex**: TTAGGG repeats (human) capped by a six-protein shelterin complex forming a protective T-loop that prevents chromosome ends from being misread as double-strand breaks by DNA damage machinery.
- **Hayflick limit**: the finite number of cell divisions (roughly ~100 mitoses in the passage described) before telomere erosion triggers replicative senescence in normal somatic cells.

## Mental Models
- Think of the replisome as an assembly line with strict directionality: helicase unwinds ahead, primase lays starter RNA, polymerase(s) extend 5′→3′ only, clamps hold polymerases on track, and ligase/exonuclease activities clean up seams — nearly every "why does X protein exist" question in this chapter resolves to one gap in that assembly line.
- Use the "backup generator" model for eukaryotic origin licensing: license far more origins than you will use (10-20% fire per S phase); this margin is the cell's insurance against local replication stress, not inefficiency.
- Treat topoisomerases as "pressure relief valves": anywhere unwinding DNA would otherwise build up destructive torsional strain (ahead of a fork, between converging forks, around circular genomes), expect a Type I or Type II topoisomerase to be the named answer.
- Treat telomerase/telomere shortening as a trade-off, not a flaw: limited replicative lifespan in somatic cells is a tumor-suppressive mechanism (unchecked telomerase activity is a hallmark of most cancers), while its controlled reactivation is being explored (e.g., adenoviral mTERT gene therapy in mice) as an anti-aging intervention with its own cancer-risk trade-offs.

## Anti-patterns / Common Misconceptions
- **"Meselson-Stahl's first-generation result alone proved semiconservative replication"**: it only ruled out the conservative model; a second generation was required to distinguish semiconservative from dispersive replication — always check that this two-generation logic is preserved when explaining the experiment.
- **"DNA polymerase can initiate synthesis de novo"**: false for essentially all replicative DNA polymerases — they require a primer (RNA, laid by primase/Pol α) with a free 3′-OH; this requirement is also the direct cause of the end-replication problem.
- **"Leading and lagging strand synthesis are always tightly, permanently coupled within one holoenzyme"**: recent structural/single-molecule studies (Section 9.2, discussed via Xu & Dixon 2018) show bacterial Pol III subunits can exchange at the fork and leading/lagging synthesis may decouple — the "two polymerases hard-wired together" textbook cartoon is a simplification.
- **"E. coli Topoisomerase I relieves the positive supercoiling generated by the replicative helicase"**: it cannot — E. coli Topo I only removes negative supercoils; positive supercoiling ahead of the fork is relieved by the Type II enzyme DNA gyrase.
- **"All eukaryotic replication origins are marked by a consensus DNA sequence like E. coli's oriC"**: only S. cerevisiae and closely related species have such consensus origin sequences; most eukaryotic origin locations are instead determined by chromatin context, DNA topology, and structural features.
- **"Telomerase reactivation is straightforwardly beneficial"**: constitutive telomerase expression is a defining feature of most cancers; only carefully limited, mosaic reactivation (as in the mouse gene-therapy studies) avoided elevated cancer incidence while still improving healthspan metrics.

## Key Equations & Reference Tables

**E. coli replication scale:** genome = 4.6 Mbp; full replication ≈ 42 minutes; rate ≈ 1000 nucleotides/second per fork (bidirectional, single origin oriC).

**Table 9.1-style summary — Key E. coli replication proteins:**

| Protein | Role |
|---|---|
| DnaA | Initiator; melts oriC, recruits helicase loader |
| DnaB | Replicative helicase (hexameric); unwinds duplex DNA |
| DnaC | Helicase loader; delivers DnaB onto ssDNA |
| SSB | Single-stranded DNA-binding protein; protects exposed ssDNA |
| DnaG (primase) | Synthesizes RNA primers on both strands |
| DNA Pol III HE | Main replicative polymerase (leading + Okazaki fragment synthesis) |
| DNA Pol I | Removes RNA primers (5′→3′ exo, Klenow domain) and fills gaps with DNA |
| DNA Ligase | Seals nicks between adjacent DNA fragments (5′-P to 3′-OH) |
| DNA Gyrase (Topo II) | Relieves positive supercoiling ahead of the fork (Type II, ATP-dependent) |
| Topoisomerase I | Relaxes negative supercoiling only (Type I, no ATP) |
| Topoisomerase IV | Decatenates daughter chromosomes; aids termination (Type II) |
| Tus | Binds Ter sites; polar block that halts converging replisomes |

**Table 9.2-style summary — Eukaryotic replicative DNA polymerases (B family):**

| Polymerase | Role | Strand |
|---|---|---|
| Pol α (+ primase) | Synthesizes short RNA-DNA hybrid primers | Both (initiation at origins and each Okazaki fragment) |
| Pol ε | Continuous synthesis | Leading strand |
| Pol δ | Discontinuous synthesis, generates Okazaki fragments | Lagging strand |

**Fidelity figures:** DNA Pol III error rate ≈ 1 per million bases; mitochondrial POLγ misincorporation frequency < 1 × 10⁻⁶.

**Telomere loss rate:** ~30-200 nucleotides lost per round of replication (end-replication problem); ~50-200 bp per division cited in the telomerase/senescence discussion; ~100 mitoses approximate the Hayflick limit.

**Mitochondrial genome:** human mtDNA ≈ 16.6 kb, circular, double-stranded; encodes 13 mRNAs, 22 tRNAs, 2 rRNAs; two origins (OH in the noncoding control region, OL within a tRNA cluster ~11,000 bp downstream).

## Worked Example
**Reconstructing bidirectional replication initiation and fork progression in E. coli, end-to-end (Sections 9.2, synthesizing Figures 9.3-9.9):**

1. DnaA protein (ATP-bound) binds conserved DnaA-boxes within oriC (~245 bp, AT-rich). Multiple DnaA subunits oligomerize into a helical filament, wrapping and torsionally straining the duplex DNA, which melts the adjacent AT-rich DNA-unwinding element into a single-stranded "bubble."
2. The helicase loader DnaC (ATP-bound) binds hexameric DnaB helicase in its open "lockwasher" conformation and delivers one DnaB-DnaC complex onto each of the two exposed ssDNA strands, aided by DnaA domain I contacting DnaB's N-terminal domain.
3. DnaC dissociates; DnaB closes into an active hexameric ring around each ssDNA strand and begins translocating, unwinding the duplex ahead of it using ATP hydrolysis, forming a Y-shaped replication fork moving in each direction (bidirectional).
4. Newly exposed ssDNA is rapidly coated by single-stranded binding protein (SSB), preventing reannealing and protecting the DNA.
5. Each DnaB helicase recruits primase (DnaG) via its C-terminal domain, completing primosome assembly; DnaG synthesizes short RNA primers on both the leading and lagging template strands.
6. The DNA Polymerase III holoenzyme assembles at each primer: the β2 sliding clamp is loaded by the clamp-loader complex onto the primer-template junction, and the αεθ polymerase core binds the clamp via clamp-binding motifs, tethering Pol III for high-speed (~1000 nt/s), high-processivity (>150 kb) synthesis.
7. On the leading strand, Pol III extends continuously in the same direction as fork movement. On the lagging strand, Pol III synthesizes short Okazaki fragments discontinuously, repeatedly releasing and repositioning (aided by a large conformational "switch" of the polymerase tail) at newly primed sites roughly every ~1000 bp.
8. Ahead of each fork, unwinding generates positive supercoiling; DNA gyrase (a Type II topoisomerase) introduces negative supercoils to relieve this strain, allowing continued fork progression.
9. DNA Polymerase I removes each RNA primer via its 5′→3′ exonuclease (Klenow-adjacent) activity and fills the resulting gap using its 5′→3′ polymerase activity; DNA ligase then seals the remaining nick between adjacent Okazaki fragments.
10. The two bidirectional forks travel around the circular chromosome until they converge in the terminus region, where polar Tus-Ter "lock" complexes (arranged as two oppositely oriented groups of five Ter sites) allow the first-arriving fork through but block the second, forcing both forks to stop in the terminus region for proper segregation. Topoisomerase IV then resolves any resulting precatenanes so the daughter chromosomes can be separated.

## Key Takeaways
1. DNA replication is semiconservative — proven definitively only by carrying the Meselson-Stahl density-labeling experiment through two full generations, not one.
2. All known DNA polymerases require a primer with a free 3′-OH and synthesize exclusively 5′→3′; this single constraint explains leading/lagging strand asymmetry, Okazaki fragments, and the end-replication problem.
3. Prokaryotic replication uses a single origin (oriC) and bidirectional forks that converge at polar Tus-Ter termination complexes; eukaryotic replication uses hundreds to tens of thousands of origins controlled by a two-step licensing/firing system to balance completeness against genome-stability risk.
4. Topoisomerases are strictly categorized by mechanism (Type I: one strand, no ATP; Type II: both strands, ATP-dependent) and by which supercoiling problem they solve — do not conflate DNA gyrase (positive supercoil relief) with Topoisomerase I (negative supercoil relief only, in E. coli).
5. Mitochondrial DNA replication uses its own dedicated, bacteriophage-related machinery (POLγ, TWINKLE helicase, mtSSB, POLRMT) and a distinct strand-displacement mechanism, not a smaller copy of nuclear replication.
6. The end-replication problem is an inescapable consequence of primer-dependent, 5′→3′-only polymerization at linear chromosome ends; telomerase (TERT + TERC) is the dedicated, RNA-templated solution, but its activity is tightly restricted in most somatic cells as an anti-cancer safeguard.
7. Cell-cycle progression into S phase (and thus replication initiation) is gated by cyclin-CDK complexes (e.g., Cyclin E-CDK2 releasing E2F via pRb phosphorylation), linking DNA replication timing directly to broader cell-cycle control.

## Connects To
- **Ch 4**: Nucleosome/histone octamer structure (introduced in Ch. 4) must be actively disassembled ahead of and reassembled behind the replication fork (histone chaperones FACT, Asf1, CAF-1, Rtt106), directly reusing Ch. 4's chromatin packaging concepts.
- **Ch 7**: DNA ligase's adenylation-based catalytic mechanism (AMP-lysine intermediate, nucleophilic attack, leaving-group chemistry) is a direct application of the general catalytic strategies (covalent catalysis, cofactor use) introduced in Ch. 7.
- **Ch 8**: Cyclin-CDK regulation of the cell cycle (and by extension, replication initiation) connects to Ch. 8's broader discussion of post-translational regulation and regulated protein degradation (cyclins are themselves degraded on a strict schedule, though detailed elsewhere).
- **Ch 8**: Histone PTMs (acetylation, methylation, ubiquitination — from Ch. 8.2) must be faithfully transmitted from parental to daughter nucleosomes during replication, linking epigenetic inheritance directly to the replication-coupled nucleosome assembly discussed here.
- **Ch 12**: DNA damage/repair pathways interact directly with replication (e.g., stalled/collapsed fork rescue, ROS-induced 8-oxoguanine damage at telomeres) and are covered in depth in Ch. 12.
- **Ch 5**: Restriction endonucleases and other DNA manipulation tools from Ch. 5 underlie many of the structural/biochemical techniques (e.g., isolating replication intermediates) referenced implicitly in this chapter's figures.
