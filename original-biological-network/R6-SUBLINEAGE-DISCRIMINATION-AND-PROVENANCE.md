# R6: Sublineage discrimination and provenance audit

**Date:** 18 November 2026. **Status:** Primary-paper interpretation and source-data locator audit; supplemental workbook not independently parsed.

## Question
Can a *defined* ERV sublineage, rather than a broad retroviral family or receptor interference group, satisfy:
- **A:** human + non-primate mammal positive; other great apes negative;
- **B:** nonhuman great ape + non-primate mammal positive; human negative?

Presence must be measured at the same sequence-resolution as absence. The hypothesis permits post-Fall cross-kind transmission as a historical possibility; the genomic data do not date the Fall.

## Direct primary-source findings

### ERV-Fc (Diehl et al., 2016)
- Figure 2 source data 1 enumerates genome builds and sequence acquisition methods; **source data 2** enumerates recovered ERV-Fc lineages, host taxa, viral sequences and RepBase crosswalks. These are the correct source tables for a sublineage-by-host audit.
- ERV-Fc was identified across at least 11 mammalian orders. Several distinct lineages occur within some primate and carnivore genomes.
- The paper describes an **HERV-Fc1 env locus shared among all great apes**. Human, chimpanzee and bonobo orthologues retain open env reading frames; the gorilla orthologue is disrupted. This is not a human- or ape-exclusion signature.
- ERV-Fc2 and ERV-Fc1 occur in carnivores; the carnivore ERV-Fc1 lineage includes recombinant ERV-W-like envelope sequence and evidence for multiple transmissions. This does not establish a primate/non-primate *sublineage* match with the required exclusions.
- The paper explicitly notes that some species are negative for ERV-Fc at the surveyed family level, and that assembly quality and coverage differ.

**Assessment:** Broad ERV-Fc is non-discriminating for A/B; a narrower sublineage might qualify but must be demonstrated from the host-lineage table and then independently checked for complete ape exclusions. **A unverified; B unverified.**

### CERV1 and PERV (2025)
- CERV1 is reported in chimpanzee, bonobo, gorilla and multiple Old World monkey species, absent from human and orangutan surveys.
- Human SLC52A2 and related transporters confer susceptibility to CERV1 and PERV in experimental cell systems; reciprocal viral interference indicates an overlapping receptor/interference group.
- **Receptor compatibility is not evidence of genomic sequence identity or shared endogenization.** Pig PERV-positive and ape CERV1-positive cannot be counted as a B signature until a defined viral-sequence homolog passes the required identity/classification criteria.

**Assessment:** Strong cross-mammal *mechanistic feasibility* evidence, not a verified cross-mammal ERV distribution.

## Auditable data retrieval targets

1. ERV-Fc host lineage table: https://doi.org/10.7554/eLife.12704.006 (Figure 2 source data 2, XLSX).
2. ERV-Fc assembly coverage table: https://doi.org/10.7554/eLife.12704.005 (Figure 2 source data 1, XLSX).
3. ERV-Fc Gag and Pol alignments: primary article Figure 4 source data files, linked from https://elifesciences.org/articles/12704.
4. CERV1–PERV primary paper: https://pubmed.ncbi.nlm.nih.gov/40574751/ ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC12202039/.

## Reproducible screening specification

For each *sublineage* in source data 2, construct rows with source-defined lineage name, sequence identifier, host species, sequence region (gag/pol/env), genomic assembly version, recovery method, and detection confidence. Evaluate A and B with explicit missing-data status. No species not listed in the supplement may be assumed negative. Verify candidate sublineage identity with aligned homologous regions; reject matches that rely solely on a shared receptor or broad gammaretroviral classification.

Required reporting columns: `candidate_id,sequence_region,human,chimpanzee,bonobo,gorilla,orangutan,nonprimate_species,nonprimate_status,assembly_quality,signature_resolution,classification,evidence_link,limitations`.

Acceptance criteria: A or B requires a positive non-primate mammal, a positive stipulated primate, and adequately tested absence across all excluded great apes at the **same sublineage resolution**. A qualifying family-level signature does not imply orthologous integration.

## Evidence status

**HIGH:** The primary studies report ERV-Fc cross-mammalian distribution and recombination, shared great-ape HERV-Fc1 env orthology, and experimental CERV1/PERV receptor interference.

**UNCERTAIN:** A complete sublineage-specific A or B pattern. The eLife supplementary workbook has been located by DOI but **not downloaded, parsed or independently audited** in this increment. No genome-wide presence/absence analysis or sequence alignment performed.

## Sources

Diehl, W.E. et al. (2016), 'Tracking interspecies transmission and long-term evolution of an ancient retrovirus using the genomes of modern mammals', *eLife*, 5:e12704. https://doi.org/10.7554/eLife.12704

'Riboflavin transporter: evidence of a role as entry receptor for chimpanzee endogenous retrovirus' (2025), primary experimental study, PMID 40574751. https://pubmed.ncbi.nlm.nih.gov/40574751/

**Provenance note:** All factual findings above are from the primary article texts, not from the uninspected spreadsheet contents. No invented sublineage-specific species negatives are recorded.
