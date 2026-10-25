---
name: pharmacological-knowledge-graph
description: Build evidence-traceable pharmacological knowledge graphs from books, papers and datasets.
version: 1.0.0
---

# Pharmacological Knowledge Graph Builder

## Goal
Convert scientific sources into a provenance-rich graph linking plants, constituents, targets, pathways, phenotypes, indications and safety. Do not equate traditional use, in-vitro effects or book claims with clinical efficacy.

## Workflow
1. Ingest EPUB/PDF/CSV and DOI/PMID/PMCID; preserve section/page and bibliography.
2. Normalize plant taxa, PubChem CID/InChIKey, HGNC/NCBI Gene, UniProt, Reactome/KEGG, MONDO/MeSH; never invent IDs.
3. Extract atomic subject-predicate-object claims with model, species, dose, duration, route, preparation, measured endpoint and direction.
4. Distinguish direct binding, pathway effects, in-silico predictions, hypotheses and extrapolations.
5. Attach citations and source locators to every evidence-bearing edge. Classify evidence: in_vitro, animal, human_observational, human_interventional, systematic_review, in_silico, traditional_use, secondary_book, hypothesis.
6. Extract safety: adverse events, pregnancy/lactation, drug interactions, contamination, dose limits.
7. Export nodes, edges, claims and references in JSON plus evidence matrix CSV; validate referential integrity.
8. Report contradictions, biases, uncertainties, and research gaps.

## Node ontology
Taxon, PlantPart, Preparation, Compound, Metabolite, Enzyme, Gene, Protein, Pathway, BiologicalProcess, Phenotype, Disease, Model, Study, Claim, SafetyEvent.

## Edge ontology
CONTAINS, PRECURSOR_OF, CONVERTED_BY, METABOLIZED_TO, BINDS, ACTIVATES, INHIBITS, UPREGULATES, DOWNREGULATES, PARTICIPATES_IN, ASSOCIATED_WITH, TESTED_IN, SUPPORTED_BY, CONTRADICTED_BY, HAS_ADVERSE_EVENT, INTERACTS_WITH, CONTRAINDICATED_IN.

## Mandatory edge fields
id, source, predicate, target, claim_id, evidence_level, verification_status, study_id, citation, locator, organism, model, dose, duration, route, preparation, effect_direction, notes, extracted_at.
Unknown fields must be null, not invented. verification_status: verified | reported_unverified | hypothesis | contradicted.

## Validation
- Unique node IDs and existing edge endpoints; each claim linked to a source.
- Direct binding claims require binding evidence, not pathway inference.
- Do not transfer purified-compound findings to whole plants without evidence.
- Do not extrapolate in-vitro dose to human exposure without pharmacokinetics.
- Clinical efficacy requires human outcomes with population, intervention, comparator and outcome.
- Keep contradictory studies as separate claims.

## Example
Moringa oleifera CONTAINS glucomoringin; glucomoringin PRECURSOR_OF moringin via myrosinase; moringin ASSOCIATED_WITH Nrf2/ARE activation (preclinical); moringin ASSOCIATED_WITH reduced NF-kB signaling (preclinical). Each scientific relation needs a verified source.

## Output
graph/nodes.json, graph/edges.json, graph/claims.json, sources/references.json, reports/evidence_matrix.csv, reports/safety.md, reports/gaps.md.

Usage: $pharmacological-knowledge-graph --input <source> --focus "Moringa oleifera" --output <dir>
This is a procedural skill, not an installed executable.
