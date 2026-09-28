# Chapter 1: The Foundations of Biochemistry

## Core Idea
Life is chemistry organized in space and time: a cell is a compartmentalized chemical factory whose reactions are governed by the same thermodynamic and equilibrium principles (ΔG, Keq, Le Chatelier's Principle) that govern any chemical system, while water, buffers, and functional-group chemistry set the physical and chemical stage on which the genetic code and evolution operate.

## Frameworks Introduced
- **ΔG = ΔG° + RTlnQ (the two contributions to free energy)**: The total driving force of a reaction is the sum of an intrinsic-stability term (ΔG°, independent of concentration, reflected in Keq) and a concentration term (RTlnQ).
  - When to use: To explain why two reactions with very different Keq (e.g., HCl vs. acetic acid) can have different driving forces at the same starting concentrations, and why adding reactant/product shifts ΔG.
  - How: Compute ΔG° from Keq (ΔG° = −RTlnKeq); compute Q from current concentrations; sum the two terms. At equilibrium ΔG = 0 and ΔG° = −RTlnKeq.
- **Le Chatelier's Principle**: A reaction at equilibrium, when perturbed, shifts in the direction that relieves the perturbation.
  - When to use: Predicting the direction a reaction shifts after adding/removing reactant or product, or adding/removing heat.
  - How: Add reactant → shifts toward products; add product → shifts toward reactants; remove either → shifts to replace it; add heat to exothermic reaction → shifts toward reactants (and vice versa for endothermic).
- **Gibbs Free Energy / Enthalpy-Entropy framework (G = H − TS)**: Spontaneity of a reaction is determined by ΔG = ΔH − TΔS at constant T, P, which is equivalent to ΔStot = ΔSsys + ΔSsurr (Second Law: ΔStot > 0 for any spontaneous process).
  - When to use: Explaining why some endothermic reactions (e.g., Ba(OH)2·8H2O + NH4SCN, or water evaporation) are still spontaneous.
  - How: ΔSsurr = −ΔHsys/T; combine with ΔSsys (dispersal of matter) to get ΔStot; multiply by −T to get ΔGsys = ΔHsys − TΔSsys.
- **Boltzmann Entropy (S = k ln W)**: Entropy is a measure of the number of microscopic arrangements (W, "Wahrscheinlichkeit" = probability) available to a system, not simply "disorder."
  - When to use: Explaining why non-polar solutes lower water's entropy (ordering water molecules around them) and why amphiphile self-assembly (micelles, bilayers, protein folding) is entropy-driven.
  - How: S = k ln W for molecules; S = R ln W per mole; entropy is additive/logarithmic (ln Wsys = ln Wsolute + ln Wsolvent).
- **Lock-and-Key vs. Induced Fit models of enzyme–substrate binding**: Two models for how enzymes achieve substrate specificity.
  - When to use: Explaining enzyme-substrate shape complementarity.
  - How: Lock-and-key — substrate fits the enzyme's active site with no conformational change; induced fit — substrate binding causes the enzyme to change shape to better bind/mediate the reaction.
- **Henderson-Hasselbalch equation / buffering**: pH = pKa + log([A⁻]/[HA]) describes how a weak acid/base pair resists pH change ("Uninterruptible Proton Supplier").
  - When to use: Predicting buffer pH, buffering range, and charge state of ionizable groups (including multi-pKa molecules like amino acids).
  - How: Buffer is strongest (titration curve flattest) when [A⁻] = [HA], i.e., pH = pKa; effective buffering range is roughly pKa ± 1; rule of thumb — pH > 1 unit above pKa, group is deprotonated; pH > 1 unit below pKa, group is protonated.

## Key Concepts
- **Metabolism**: The sum of catabolic (breakdown, energy-releasing) and anabolic (synthesis, energy-consuming) enzyme-catalyzed reactions that sustain an organism.
- **Prokaryotic vs. eukaryotic cells**: Prokaryotes (~1000× smaller) have a single circular chromosome in a nucleoid with no membrane-bound organelles; eukaryotes have a true nucleus and compartmentalized organelles.
- **Active vs. passive transport**: Passive/facilitated diffusion moves molecules down a concentration gradient without energy input; active transport (primary, e.g., Na+/K+ ATPase; or secondary, e.g., Na+/glucose symporter) moves molecules against a gradient using energy.
- **Uniporter/symporter/antiporter**: Classification of transport proteins by whether they move one molecule, two molecules in the same direction, or two molecules in opposite directions.
- **Equilibrium constant (Keq)**: A concentration-independent ratio of product to reactant concentrations at equilibrium; Keq > 1 favors products, Keq < 1 favors reactants.
- **Standard state / ΔG°'**: Free energy change under defined standard conditions (1 M reactants/products, 1 atm, 25°C); the biochemical convention (ΔG°') assumes pH 7 ([H3O+] = 10⁻⁷ M) rather than 1 M H+.
- **Hydrophobic effect**: The entropically driven exclusion of non-polar groups from water, which orders water molecules around non-polar solutes (decreasing entropy) and is relieved when non-polar groups self-associate.
- **Zwitterion / pKa / pI**: A molecule with both positive and negative charges and zero net charge at its isoelectric point (pI), calculated as the average of the two pKa values flanking the neutral form.
- **Hydrogen bond**: A weak (1–29 kJ/mol), short-range (2.2–4.0 Å) attractive interaction between a partially positive H (bonded to an electronegative atom) and an electronegative atom elsewhere; individually weak but collectively strong (e.g., DNA base pairing).
- **Codon / reading frame / genetic code**: Triplet sets of nucleotide bases (64 possible codons, 3 of which are stop codons: amber/UAG, opal/UGA, ochre/UAA) that specify amino acids; the reading frame is set by the start codon (AUG).
- **Homolog / ortholog / paralog / analog**: Homologs share a common ancestor; orthologs are homologs in different species (from speciation); paralogs are homologs within one species (from gene duplication); analogs have independent evolutionary origins but convergent function.
- **Epigenetics**: Heritable changes in gene expression induced by environment/experience that occur without altering the underlying DNA sequence.

## Mental Models
- Use the "ball on a hill" analogy for ΔG: a ball spontaneously rolls to lower potential energy just as a reaction proceeds spontaneously toward lower free energy (ΔG < 0); at equal heights (ΔG = 0) there is no net movement (equilibrium).
- Think of weak acids as "Uninterruptible Proton Suppliers" (UPS) — like a battery backup, they release or absorb protons to buffer pH within about one unit of their pKa.
- Think of the cell as a crowded chemical factory, not a dilute test tube: macromolecular crowding stabilizes folded proteins, limits diffusion, and creates localized microenvironments — lab experiments in dilute solution may not reflect in vivo behavior.
- Use entropy as "spreadedness" (number of accessible microstates, W), not "disorder" — this correctly explains why dissolving non-polar molecules in water is unfavorable (it orders water) and why micelle/bilayer formation and protein folding are entropically favorable (they free ordered water).

## Anti-patterns / Common Misconceptions
- **"Exothermic = spontaneous"**: Wrong — spontaneity depends on ΔG (both ΔH and ΔS), not ΔH alone; the reaction of Ba(OH)2·8H2O with NH4SCN is endothermic yet spontaneous because ΔS increases sharply (solid + solid → liquid + gas + solid, more disordered products).
- **"[H+] always equals [A−] for a weak acid HA"**: Only true when HA dissociates in pure water; in any other solution (with pre-existing H+/OH−), the concentrations are affected unequally and must be calculated via Henderson-Hasselbalch.
- **"Entropy is macroscopic disorder like a messy room"**: Misleading — entropy (S = k ln W) is a measure of the number of microscopic arrangements (positional and thermal), not a subjective sense of tidiness.
- **Confusing "primary/secondary/tertiary" between alcohols and amines**: In alcohols, classification depends on how many carbons the OH-bearing carbon is attached to; in amines, it depends on how many carbons the nitrogen itself is bonded to — these are different criteria.

## Key Equations & Reference Tables

**Free energy:**
```
ΔG = ΔGstab + ΔGconc = ΔG° + RT ln Qrx
ΔG = ΔH − TΔS          (at constant T, P)
ΔG < 0 → reaction proceeds toward products
ΔG = 0 → equilibrium
ΔG > 0 → reaction proceeds toward reactants
```

**Thermodynamics:**
```
ΔEsys = q + w = q − PextΔV     (First Law)
ΔH = ΔEsys + PextΔV            (enthalpy, constant P)
S = k ln W                      (Boltzmann; per molecule)
S = R ln W                      (per mole)
ΔSsurr = −ΔHsys / T
ΔStot = ΔSsurr + ΔSsys > 0     (Second Law, any spontaneous process)
```

**Acid-base:**
```
pH = −log[H+]        pOH = −log[OH−]        pH + pOH = 14
pKa = −log Ka
pH = pKa + log([A−]/[HA])     (Henderson-Hasselbalch)
```

**Table 1.1 Average Cellular and Extracellular Ion Concentrations**

| Ion | Inside (mM) | Outside (mM) |
|---|---|---|
| Na+ | 140 | 5 |
| K+ | 12 | 140 |
| Cl− | 4 | 15 |
| Ca2+ | 1 μM | 2 |

**Hydrogen bond strength**: ranges from ~1–2 kJ/mol (very weak) to ~29 kJ/mol (fairly strong), effective over 2.2–4.0 Å — much weaker than covalent bonds but collectively significant (e.g., in DNA base pairing).

**Weak acid pKa examples**: carbonic acid pKa = 6.37; formic acid pKa = 3.75 (lower pKa = stronger acid).

## Worked Example
**Comparing HCl and acetic acid dissociation in water (why one is "irreversible" and one isn't):**

Both HCl(aq) + H2O → H3O+ + Cl− and CH3CO2H(aq) + H2O ⇌ H3O+ + CH3CO2− start at 0.1 M acid, 0 M products (t=0).

- At t=0: RTlnQrx is identical for both (same concentrations, no products yet). But ΔG° is very negative for HCl (strong acid, high intrinsic instability) and positive for acetic acid (weak acid, more stable). So ΔG(HCl) ≪ ΔG(acetic acid) — HCl's reaction is driven much more strongly toward products.
- At equilibrium: ΔG = 0 for both. For HCl, essentially all acid has dissociated (~10⁻¹⁰ M HCl remains), so Keq ≫ 1; concentration terms now favor HCl re-formation but are overwhelmed by the intrinsic instability term. For acetic acid, 99% remains undissociated (only ~0.001 M product forms) — concentration favors products but is countered by the intrinsic stability of the reactant (Keq ≪ 1).
- Conclusion: ΔG° (from Keq, intrinsic reactant/product stability) and RTlnQ (from concentration) are independent, additive contributions to ΔG; a reaction's apparent "irreversibility" reflects a very unfavorable ΔG°, not the absence of a reverse reaction.

**Buffer capacity check**: Adding 0.01 mol HCl to 1 L pure water (pH 7) drops pH to 2 (5-unit change). Adding the same amount to 1 L of 1 M acetate buffer (pH 4.76) only drops pH to 4.74 (0.02-unit change) — demonstrating buffering. But if the buffer concentration is only 0.01 M (insufficient capacity — only 0.005 M A− available to absorb 0.01 M H+), the pH falls sharply to ~2.30, showing that buffer capacity is limited by buffer concentration, not just by having a pKa near the target pH.

## Key Takeaways
1. ΔG has two independent, additive components — intrinsic stability (ΔG°, from Keq) and concentration (RTlnQ) — and both must be considered to predict reaction direction and extent.
2. Spontaneity is governed by ΔG (or equivalently ΔStot of system + surroundings), not by ΔH alone; endothermic reactions can be spontaneous if entropy increases enough.
3. Entropy is best understood as the number of accessible microstates (S = k ln W), which correctly explains hydrophobic effects, micelle/bilayer self-assembly, and protein folding as entropy-driven (via water release), not disorder-driven.
4. Buffers work because a weak acid/conjugate base pair can donate or absorb protons; buffering is strongest at pH = pKa and is limited by buffer concentration (capacity).
5. The genetic code is a triplet (codon) code with 64 codons (61 sense + 3 stop: amber, opal, ochre) read in a single reading frame set by the start codon.
6. Sequence homology (ortholog/paralog/analog) is a powerful but imperfect predictor of protein function — up to 10–25% of homology-based annotations are estimated to be incorrect (e.g., pancreatic ribonuclease vs. angiogenin).
7. Cells are crowded, not dilute, environments — macromolecular crowding stabilizes native protein structure, restricts diffusion, and can create localized functional microenvironments (e.g., lipid rafts, phase-separated RNA/protein particles).

## Connects To
- **Ch 2**: The hydrophobic effect and entropy-driven self-assembly introduced here directly explain protein folding, secondary/tertiary structure stabilization, and membrane protein behavior.
- **Ch 4/9**: The genetic code, codons, reading frames, and mutation types introduced here are expanded into full DNA structure, replication, and repair mechanisms.
- **Ch 6/7**: The enzyme lock-and-key/induced-fit models and general thermodynamics (ΔG, Keq) here underpin enzyme kinetics and catalytic mechanisms covered later.
- **Ch 13**: The brief introduction to epigenetics here is developed fully into transcriptional control and epigenetic regulation mechanisms.
