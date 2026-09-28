# Chapter 10: Transcription and RNA Processing

## Core Idea
Transcription converts a DNA template into RNA through a universally conserved multi-subunit RNA polymerase mechanism (initiation → elongation → termination), but eukaryotes layer a vastly more elaborate control system on top — a >100-protein preinitiation complex, structural editing of the transcript itself (capping, splicing, polyadenylation) — that together determine which RNA molecules actually reach a functional, exportable, translatable state.

## Frameworks Introduced
- **Bacterial Transcription Initiation Pathway (RNAP Holoenzyme → RPc → RPo)**: the stepwise named model for how bacterial RNA polymerase finds and opens a promoter.
  - How: the five-subunit RNAP core (α₂ββ'ω) associates with a sigma factor (e.g., housekeeping σ⁷⁰, stress-induced σ³⁸) to form the holoenzyme → holoenzyme binds promoter DNA forming the closed complex (RPc) → sigma recognizes the -35 and -10 elements (an adenine at position -11 flips out of the duplex into a sigma recognition pocket, nucleating melting) → DNA strands separate to form the open complex (RPo) with an exposed "transcription bubble" → RNA synthesis begins and sigma dissociates, leaving the catalytic core to elongate alone.
  - When to use: reference model for prokaryotic promoter recognition and the mechanistic basis of sigma-factor-dependent gene selection.
- **The Preinitiation Complex (PIC) Assembly Model (eukaryotic Pol II)**: explains why eukaryotic transcription initiation requires so much more machinery than bacterial initiation.
  - How: TFIID (a ~20-subunit, 3-lobed, conformationally plastic complex built around TATA-binding protein/TBP plus 13 TAFs) engages the core promoter in a multi-stage process — Lobe C first engages downstream DNA and positions TBP for "scanning," TFIIA stabilizes TBP-DNA engagement via Lobe B, TBP then bends the DNA (inserting phenylalanine residues into the minor groove, creating a double kink) and detaches from Lobe A, opening a docking site for TFIIB, which recruits Pol II (pre-bound to TFIIF) → TFIIH's ATP-dependent translocase activity converts the closed complex to an open complex by unwinding 11-15 bp around the start site → Pol II escapes the promoter (often after abortive transcription of 3-10 nt products) and pauses 20-100 bases in before converting to a processive elongation complex.
  - When to use: the reference framework for any question about how a specific human gene's transcription is turned on, and why >100 proteins are required where bacteria need ~6.
- **Trigger-Loop/Bridge-Helix Elongation and Backtrack-Recovery Model**: explains both normal nucleotide addition and how RNAP recovers from errors.
  - How: normal cycle = trigger loop (TL) folds in response to correct NTP binding → NTP incorporation with pyrophosphate release → translocation resets the active site. Misincorporation or thermodynamically unfavorable sequence can cause backtracking (RNAP slips backward, extruding the 3' RNA end into the secondary channel), which arrests transcription; single-nucleotide backtracks are resolved by intrinsic TL-catalyzed hydrolysis, while longer backtracks require GreA/GreB factors, which insert into the secondary channel, displace the TL, and stimulate a much faster hydrolytic cleavage that regenerates a clean 3' end.
- **Intrinsic vs. Rho-Dependent Termination (prokaryotes)**: two mechanistically distinct ways bacteria stop transcription.
  - How (intrinsic): an inverted-repeat sequence in the nascent RNA folds into a stem-loop hairpin immediately followed by a run of U residues; hairpin formation destabilizes the weak rU:dA hybrid in the RNA:DNA hybrid, and RNAP disengages without any additional protein factor. How (Rho-dependent): Rho, a hexameric ATP-dependent RNA:DNA helicase, loads at a C-rich, unstructured "Rut" site via its primary binding site, translocates along the nascent RNA (tethered-tracking model) using its secondary binding site as the ATP-driven motor, and catches up to and dislodges RNAP (~20% of E. coli transcripts terminate this way).
- **Splicing / Spliceosome Assembly Pathway (E → A → B → B* → C complexes)**: the named stepwise model for intron removal from pre-mRNA.
  - How: U1 snRNP binds the 5' splice site and SF1/U2AF recognize the branch point sequence (BPS), polypyrimidine tract, and 3' splice site (Complex E) → U2 snRNP binds the BPS (Complex A) → the pre-formed U4/U6-U5 tri-snRNP joins (Complex B) → U1 and U4 are released and RNA-RNA/RNA-protein rearrangements activate the catalytic core (Complex B*) → first transesterification: the branchpoint adenosine 2'-OH attacks the 5' splice site phosphate, releasing free exon 1 and forming a lariat intermediate → second transesterification (Complex C): exon 1's 3'-OH attacks the 3' splice site, ligating the exons and releasing the intron as a lariat, which is degraded; snRNPs are recycled.
  - When to use: reference model for how a single gene generates multiple mRNA isoforms via alternative splicing (exon skipping, alternative 5'/3' splice sites, intron retention, mutually exclusive exons).

## Key Concepts
- **Sigma factor (σ)**: dissociable RNAP subunit that confers promoter-sequence specificity in bacteria (e.g., σ⁷⁰ for housekeeping genes, σ³⁸ for stationary phase); its release after initiation lets the catalytic core elongate processively.
- **Preinitiation complex (PIC)**: the >100-protein assembly (GTFs TFIIA/B/D/E/F/H, Pol II, Mediator) that must form at a Pol II core promoter before mRNA synthesis can begin.
- **TATA-binding protein (TBP)**: the DNA-bending subunit of TFIID that nucleates PIC assembly by distorting the TATA box into a sharp double kink.
- **Enhancer / eRNA**: a distal, orientation-independent regulatory DNA element; many enhancers themselves recruit Pol II and produce short, unstable enhancer RNAs (eRNAs), blurring the classic enhancer/promoter distinction; the Mediator complex physically loops enhancers to promoters.
- **Rho factor**: hexameric ATPase/helicase responsible for factor-dependent transcription termination in bacteria via the tethered-tracking mechanism.
- **Torpedo (kinetic) vs. allosteric termination models**: the two proposed (non-mutually-exclusive) mechanisms for eukaryotic Pol II termination after polyadenylation-site cleavage — Torpedo: the exonuclease XRN2/Rat1p degrades the downstream cleaved transcript 5'→3' and catches/dislodges Pol II; Allosteric: binding of termination signals downstream of the pA site triggers a Pol II conformational change that promotes disassembly.
- **5' cap (m⁷G cap)**: 7-methylguanylate added co-transcriptionally via an unusual 5'-5' triphosphate linkage; recognized by the cap-binding complex (CBC) for nuclear export, later replaced by eIF4E/eIF4G for cytoplasmic translation; protects the transcript from 5' exonucleolytic decay.
- **Cleavage and polyadenylation (CPA) machinery**: >80-protein complex (core subcomplexes CPSF, CstF, CFI, CFII) that recognizes the AAUAAA polyadenylation signal (PAS), cleaves the transcript at a CA dinucleotide, and adds ~50-100 non-templated adenosines.
- **Alternative polyadenylation (APA)**: use of one of multiple PAS sites within a transcript, altering 3'UTR content and post-transcriptional regulatory potential; estimated to affect ~70% of the human transcriptome.
- **Alternative splicing (AS)**: regulated inclusion/exclusion of exons via exonic/intronic splicing enhancers and silencers (ESE/ESS/ISE/ISS) read by SR proteins and hnRNPs, vastly expanding proteome diversity from a fixed set of genes.
- **Ribozyme**: an RNA molecule with catalytic activity; the ribosome's peptidyl transferase center (rRNA-based) and the spliceosome's catalytic core (snRNA-based) are the two central examples introduced in this chapter.

## Mental Models
- Think of sigma factors as "interchangeable read heads": swapping which sigma is loaded onto the same catalytic RNAP core redirects the whole transcriptional program (housekeeping vs. stress) without changing the enzyme's chemistry.
- Use the TFIID/PIC assembly as the template for "eukaryotic gene activation is combinatorial and staged" — no single factor decides transcription; each stage (TBP release, TFIIA stabilization, TFIIH-driven melting) is a checkpoint, and regulatory inputs (activators, Mediator, chromatin state) can act at any one of them.
- Treat backtracking + Gre-factor cleavage as "proofreading during elongation," conceptually parallel to a DNA polymerase's exonuclease proofreading (Ch. 9) but operating on RNA instead of DNA.
- Think of the spliceosome and the 3' CPA machinery as running on the same design principle: cis-acting sequence elements (splice sites/PAS) recruited by large multi-subunit machines that assemble stepwise, with each intermediate complex representing a regulatory checkpoint that can be exploited for alternative outcomes (alternative splicing, alternative polyadenylation).

## Anti-patterns / Common Misconceptions
- **"RNA polymerase alone finds bacterial promoters"**: false — the catalytic core cannot recognize -35/-10 elements on its own; a sigma factor is obligatory for promoter-specific initiation, and different sigma factors redirect the same core enzyme to different gene sets.
- **"Eukaryotic transcription initiation resembles bacterial initiation, just with more proteins doing the same job"**: the mechanisms diverge qualitatively — bacteria have a single holoenzyme that directly opens the promoter, while eukaryotes require ATP-dependent TFIIH translocase activity to convert the PIC from closed to open, a step with no bacterial equivalent.
- **"Introns are simply junk removed from mRNA"**: incorrect — beyond removal, intron sequences and the splicing process itself contribute to gene regulation, mRNA transport, and (via alternative splicing) major expansion of protein diversity from a fixed genome.
- **"Termination is a passive process where RNAP simply falls off at the end of a gene"**: false for both domains — bacterial termination requires either a specific hairpin+U-tract structure (intrinsic) or active Rho-mediated pursuit; eukaryotic Pol II termination requires coordinated cleavage/polyadenylation and either exonucleolytic pursuit (Torpedo) or allosteric remodeling.
- **"The poly(A) tail's only job is stabilizing the 3' end"**: it has (at least) five distinct roles covered in the chapter — defining transcript length, enabling nuclear export, enhancing translation efficiency, marking transcripts for degradation, and influencing overall protein output.

## Key Equations & Reference Tables

**Bacterial RNAP core composition:** α₂ββ'ω (5 subunits) + dissociable σ subunit = holoenzyme.

**Eukaryotic RNA polymerases:**

| Polymerase | Product | Subunit count |
|---|---|---|
| Pol I | Majority of rRNA | 14 |
| Pol II | All mRNA + most regulatory/untranslated RNA | 12 |
| Pol III | tRNA, 5S rRNA, other short structured RNAs | 17 |

**Core promoter elements recognized in PIC assembly:** TATA box (~-30 bp, bound by TBP), BRE, Inr, DPE (Figure 10.10).

**RNA levels in a typical mammalian cell (approximate, Figure 10.5):** rRNA ≈ 90% of total cellular RNA mass; tRNA lower mass but higher molar concentration than rRNA; mRNA/snRNA/snoRNA 1-2 orders of magnitude below rRNA/tRNA; lincRNAs ~2 orders of magnitude below total mRNA; human transcriptome yields >100,000 distinct lncRNAs vs. ~20,000 protein-coding genes.

**Poly(A) signal consensus:** canonical hexamer AAUAAA (or close variants ATTAAA, TATAAA), located 10-35 nt upstream of the cleavage site (usually a CA dinucleotide).

**5' cap structure:** 7-methylguanylate (m⁷G) linked via 5'→5' triphosphate bond; Cap-1 = additional 2'-O-methylation on the first ribose; Cap-2 = on the first two riboses.

**Spliceosome components:** 5 snRNPs (U1, U2, U4, U5, U6) + ~200 associated proteins; key cis-elements = 5' splice site, branch point sequence (BPS), polypyrimidine tract, 3' splice site.

## Worked Example
**Tracing one Pol II-transcribed human mRNA from PIC assembly to a mature, export-ready transcript (synthesizing Sections 10.3-10.5):**

1. TFIID's Lobe C engages downstream core-promoter DNA, positioning TBP to "scan" upstream sequence for the TATA box while inhibitory TAND1/TAND2 regions of TAF1 are released.
2. TFIIA joins via Lobe B, stabilizing TBP's DNA engagement; TBP inserts phenylalanine side chains into the minor groove, bending the DNA into a double kink and detaching from Lobe A — this steric change opens a docking surface for TFIIB.
3. TFIIB recruits Pol II (pre-associated with TFIIF); TFIIE and TFIIH complete PIC assembly. TFIIH's ATP-dependent translocase unwinds ~11-15 bp around the transcription start site, converting the closed PIC to an open complex and positioning template ssDNA in the Pol II active site.
4. Pol II synthesizes several short (3-10 nt) abortive transcripts before achieving promoter escape; most PIC components (TFIID, TFIIA, TFIIE, TFIIH) remain promoter-bound for efficient re-initiation, while Pol II, TFIIB, and TFIIF must be freshly recruited for the next round.
5. Pol II often pauses 20-100 nt into the gene (promoter-proximal pause) before converting to a processive elongation complex; elongation proceeds via the trigger-loop/bridge-helix cycle, with GreA/GreB-independent or -dependent backtrack recovery as needed.
6. Co-transcriptionally, the capping enzyme complex adds the m⁷G cap to the 5' end as soon as it emerges from RNAP, protecting it from degradation and recruiting the cap-binding complex (CBC).
7. As RNAP transcribes through exon-intron boundaries, the spliceosome assembles co-transcriptionally (Complex E → A → B → B* → C) at each intron, executing the two-step transesterification reaction to remove introns as lariats and ligate exons; alternative splicing factors (SR proteins, hnRNPs) can direct exon skipping or alternative splice-site choice at this stage.
8. When Pol II transcribes past the AAUAAA polyadenylation signal, the CPSF/CstF/CFI/CFII machinery assembles, CPSF3 cleaves the transcript at the CA dinucleotide, and poly(A) polymerase adds ~50-100 adenosines — if multiple PAS sites exist, alternative polyadenylation determines which 3'UTR is used.
9. Downstream of cleavage, either the Torpedo mechanism (XRN2/Rat1p degrading the remaining nascent transcript and dislodging Pol II) or allosteric Pol II conformational change (or both, per the unified model) terminates transcription.
10. The capped, spliced, polyadenylated mature mRNA is bound by CBC and exported through the nuclear pore complex; after a "pioneer round" of translation, CBC is replaced by eIF4E/eIF4G (eIF4F) for standard cap-dependent translation in the cytoplasm (see Ch. 11).

## Key Takeaways
1. Sigma factors, not the RNAP catalytic core, determine bacterial promoter specificity — a single core enzyme can be redirected to entirely different gene sets by swapping sigma subunits.
2. Eukaryotic Pol II initiation is fundamentally more complex than bacterial initiation because it requires an active, ATP-dependent step (TFIIH translocase) to open the promoter — there is no bacterial equivalent of this step.
3. Elongation is not error-free or uniform: RNAP pauses and backtracks routinely, and recovery relies on either intrinsic trigger-loop hydrolysis or GreA/GreB-catalyzed cleavage, directly analogous in purpose (if not mechanism) to DNA polymerase proofreading.
4. Bacterial termination is bimodal — intrinsic (hairpin + U-tract, factor-independent) or Rho-dependent (helicase-driven pursuit) — while eukaryotic Pol II termination is coupled to 3' end processing via Torpedo and/or allosteric mechanisms.
5. mRNA maturation (5' capping, splicing, 3' cleavage/polyadenylation) is not passive "cleanup" but an active, co-transcriptional regulatory layer — alternative splicing and alternative polyadenylation are major sources of proteomic and regulatory diversity from a fixed genome.
6. The ribosome and spliceosome are both ribozymes at their catalytic core (rRNA and snRNA respectively), underscoring RNA's dual role as both information carrier and catalyst in gene expression.

## Connects To
- **Ch 9**: The replisome's use of processivity clamps and dedicated helicases parallels RNAP's own translocation/processivity machinery (trigger loop, bridge helix); both chapters also share the theme of specialized machines resolving DNA secondary structure ahead of a moving enzyme.
- **Ch 11**: The mature mRNA produced here (capped, spliced, polyadenylated) is the direct substrate for translation initiation — cap-dependent scanning in Ch. 11 depends explicitly on the m⁷G cap and eIF4F complex introduced here.
- **Ch 12**: Transcription-coupled nucleotide excision repair (TC-NER) uses RNA Pol II stalling at DNA lesions as its damage-recognition signal, directly linking this chapter's elongation machinery to Ch. 12's DNA repair pathways.
- **Ch 13**: The PIC/TFIID assembly process and enhancer/Mediator looping described here are the direct mechanistic target of the transcription factors, chromatin remodelers, and histone modifications covered in Ch. 13's discussion of transcriptional control and epigenetics.
