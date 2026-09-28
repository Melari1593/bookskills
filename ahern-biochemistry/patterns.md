# Patterns & Techniques

## Protein Purification Scheme
**When to use**: Tracking and comparing the effectiveness of successive purification steps.
**How**: Total Protein = [protein]×volume; Total Activity = [activity]×volume; Specific Activity = Total Activity÷Total Protein; Yield% = (Activity at step N ÷ Activity at step 1)×100; Purification Level = Specific Activity(N)÷Specific Activity(1).
**Trade-offs**: Specific activity should rise and total protein fall at each good step; a plateau/drop signals lost protein, denaturation, or lost cofactor — not just a bad separation choice. (Ch3)

## Chromatography Method Selection
**When to use**: Choosing a separation step by the protein property you can exploit.
**How**: Size exclusion (molecular size) → ion exchange (net charge) → HIC (surface hydrophobicity, high→low salt) → affinity (specific ligand, e.g. His-tag/Ni²⁺). Combine 2–3 orthogonal principles sequentially for a real scheme.
**Trade-offs**: FPLC (low pressure, aqueous) preserves native/active conformation; HPLC (high pressure, often organic solvents) is higher-resolution but frequently denatures. (Ch3)

## Structure-Elucidation Method Selection
**When to use**: Choosing X-ray crystallography, NMR, or cryo-EM to solve a 3D structure.
**How**: X-ray needs a crystal, any size, ~2 Å static resolution. NMR is solution-state, captures dynamics, but limited to <~40 kDa (slow tumbling broadens peaks), needs isotope labeling. Cryo-EM needs no crystal, handles huge complexes (ribosome), near-atomic resolution, least sample required, but captures a frozen snapshot not dynamics.
**Trade-offs**: No method dominates on all axes (resolution / sample / size / dynamics) — techniques are complementary, not competing. (Ch3)

## SDS-PAGE vs. Native PAGE
**When to use**: SDS-PAGE for molecular weight; Native PAGE when charge/shape information must be preserved.
**How**: SDS coats protein with uniform negative charge (masks intrinsic charge, migration ∝ size only); DTT breaks disulfides for full denaturation. Native PAGE omits SDS — migration depends on charge+size+shape combined. (Ch3)

## PCR Amplification
**When to use**: Need many copies of a known, specific DNA region fast (before sequencing, cloning, genotyping).
**How**: Repeated cycles of denaturation (~95°C) → annealing (50–65°C) → elongation (~75–80°C) with a thermostable polymerase and two flanking primers; exponential until ~30–40-cycle plateau.
**Trade-offs**: qPCR adds fluorescent monitoring for quantification; RT-PCR adds a reverse-transcription step for mRNA/expression analysis — don't conflate the three. (Ch5)

## Sequencing Platform Selection
**When to use**: Sanger for a single gold-standard long read (~400–500 bp) from one template; NGS (Illumina/454/Ion Torrent/Nanopore) for whole-genome or large-scale work.
**How**: NGS trades per-read length for massive parallelism, depth, speed, and cost (~$1,000/genome vs. Sanger's historical cost); Nanopore/454 buck the short-read trend with longer reads. (Ch5)

## Restriction/Ligase Cloning
**When to use**: Inserting a gene of interest into a vector for propagation, study, or expression.
**How**: Cut vector + insert with compatible restriction enzymes (sticky or blunt ends) at/near a multiple cloning site → ligate → transform → select on the vector's marker (e.g. antibiotic resistance) → verify by digest or sequencing.
**Trade-offs**: TOPO cloning (topoisomerase-charged vector) and Gateway cloning (site-specific recombination) skip restriction/ligase entirely when speed matters more than positional control. (Ch5)

## Cloning Vector Selection by Insert Size
**When to use**: Choosing a vector once insert size is known.
**How**: Plasmid (≤~15 kb) → cosmid (28–45 kb) → BAC (≤350 kb) → YAC (>1 Mb) → human artificial chromosome (no practical limit). (Ch5)

## Michaelis-Menten Kinetic Analysis
**When to use**: Characterizing any enzyme's catalytic efficiency/substrate affinity, or comparing enzymes competing for shared substrate.
**How**: v = Vmax[S]/(Km+[S]); linearize via Lineweaver-Burk (1/v vs 1/[S]) to extract Km, Vmax graphically — but this overweights low-[S]/high-error points; Eadie-Hofstee/Hanes are less biased. (Ch6)

## Inhibitor-Type Diagnosis
**When to use**: Determining an inhibitor's mechanism from kinetic data.
**How**: Competitive → ↑Km, Vmax unchanged, overcome by excess substrate, shares y-intercept on Lineweaver-Burk. Noncompetitive → Km unchanged, ↓Vmax, not overcome, shares x-intercept. Uncompetitive → both ↓, parallel lines. (Ch6)

## Allosteric Model Selection (MWC vs. KNF)
**When to use**: Explaining cooperative, non-Michaelis-Menten (sigmoidal) enzyme/protein behavior.
**How**: MWC (concerted/symmetry) — all subunits share one conformation (T or R) at once, obligatory switch-like cooperativity. KNF (sequential) — subunits convert individually via induced fit with only mild neighbor influence, graded response.
**Trade-offs**: Use MWC for steep all-or-none switches; KNF for smoother, partial responses. (Ch6, Ch8)

## Enzyme Catalytic-Strategy Identification
**When to use**: Explaining how a specific active site lowers activation energy.
**How**: Look for a nucleophilic residue (covalent catalysis), a proton-relay residue (acid-base), charged/H-bonding groups near the transition state (electrostatic), an anhydrous pocket (desolvation), evidence of pre-organization (approximation), induced conformational strain (strain distortion), or a required metal/coenzyme (cofactor catalysis). Most real mechanisms combine 2+ strategies. (Ch7)

## Zymogen Activation Cascade
**When to use**: Explaining how destructive enzymes (proteases, caspases, clotting factors) avoid premature activity.
**How**: Synthesize as an inactive precursor with an inhibitory propeptide → a specific trigger protease (e.g. enteropeptidase) removes it → conformational change forms the active site → the newly active enzyme often activates the next zymogen in a cascade. A co-packaged inhibitor (e.g. PSTI) neutralizes any leaked premature activity as a second safeguard. (Ch8)

## Ubiquitin-Mediated Degradation Targeting
**When to use**: Explaining regulated (non-lysosomal) protein turnover.
**How**: E1 (activates Ub) → E2 (conjugates) → E3 (confers substrate specificity, ~600–700 human E3s) → Lys48-linked polyubiquitin chain → 26S proteasome recognition, deubiquitination, ATP-dependent unfolding, degradation.
**Trade-offs**: Mono-/multi-mono-ubiquitination is usually a non-degradative signal (localization, activity change), not a destruction tag. (Ch8)

## DNA Repair Pathway Selection
**When to use**: The first diagnostic step for any DNA-damage question — identify lesion type first.
**How**: Single mismatched base (replication error) → MMR. Oxidized/alkylated single base → BER (short/long-patch). Bulky helix-distorting adduct/UV dimer → NER (GG-NER genome-wide, TC-NER at stalled Pol II). Double-strand break → NHEJ (any cell-cycle phase, lower fidelity) or HR (S/G2/M only, needs sister chromatid, high fidelity). Unrepaired lesion blocking a fork → TLS bypass (error-prone, preserves replication over accuracy). (Ch12)

## Bacterial Operon Regulatory-Logic Diagnosis
**When to use**: Reasoning about any bacterial gene-control scenario.
**How**: Ask (1) repressible (on by default, shut off by end-product, e.g. trp) or inducible (off by default, turned on by substrate, e.g. lac)? (2) Does it integrate multiple signals (AND-gate, e.g. lac needs lactose present AND glucose absent via CAP-cAMP)? (3) Is there transcription-translation coupling available (attenuation/riboswitches — prokaryote-only, no nuclear envelope separating the processes)? (Ch13)

## Eukaryotic Transcriptional Activation Requirement
**When to use**: Explaining why a gene with an intact TF binding motif may still not be expressed.
**How**: Productive transcription requires BOTH a competent, activated transcription factor AND accessible chromatin (open by nucleosome remodeling/histone acetylation) at that locus — ~99.8% of predicted TF motifs are unoccupied in vivo precisely because chromatin state gates access independently of TF availability. (Ch13)
