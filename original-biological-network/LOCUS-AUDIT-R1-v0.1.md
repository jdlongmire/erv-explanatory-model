# Cross-lineage ERV locus audit, research increment R1

**Date:** 18 November 2026  
**Status:** Primary-literature extraction and candidate triage. **No fresh reference-assembly sequence alignment or absence validation performed.**

## Question

Identify independently checkable candidate ERV loci for two symmetric targets:

- **A:** human and non-ape mammal positive, chimpanzee/bonobo/gorilla/orangutan negative.
- **B:** nonhuman ape and non-ape mammal positive, human negative.

Report primate-only comparators separately from non-primate mammals. A family-level match is not an orthologous insertion. A single sampled negative genome is not proof of absence across populations.

## Primary-source findings and candidates

| ID | Source-grounded observation | Candidate status | Next required check |
|---|---|---|---|
| B-PTERV1-2005 | Yohn et al. mapped 287 PTERV1 sites in chimpanzee, gorilla and Old World monkey comparisons; about 95.8% were nonorthologous. The study reported absence in humans and Asian apes. | **Partial B only**: the non-ape comparators are monkeys; non-primate mammal positive is unverified | Identify a genuine non-primate mammal homolog; recheck current assemblies and bonobo |
| B-PTERV1-2011 | Gorilla structural-variation study mapped 263 full-length gorilla PTERV1 integrations and reported ~99.6% nonorthology relative to chimpanzee; one mapped chimp–gorilla correspondence was described. | Primates-only corroboration; historical assembly coordinates, not current locus validation | Resolve reported orthologous site and its current reference coordinates |
| B-PTERV1-2018 | Improved great-ape assemblies identified one chimp–gorilla orthologous “source PtERV1” locus, reported absent from modern humans, with most other PTERV1 insertions nonorthologous. | **Important qualification**: a locus-level exception to broad nonorthology, still no non-primate mammal positive | Reconcile the source-locus interpretation and alternative incomplete-lineage-sorting account |
| A-HML2-2005 | Genome-wide HERV-K(HML2) survey reported 113 human-specific insertions relative to the compared chimpanzee reference, including 15 full-length elements and 98 solo LTRs. | **A candidate pool, not an A match** | Check bonobo, gorilla, orangutan and non-primate mammal homologs; confirm per-locus synteny |
| A/B-HML2-2015 | Direct amplification found 15 loci: 10 human-specific, two chimpanzee-specific and three shared, including insertional polymorphism not fully represented in assemblies. | Negative-call calibration; possible ape-positive pool | Obtain supplementary locus names/flanks, then non-primate search |
| A/B-HML2-2018 | Study used RepeatMasker tracks in hg38, panTro5, gorGor5 and ponAbe2 and liftOver/BEDTools to classify species-specific and shared insertions. | Reproducible method precedent; older nonhuman assemblies | Re-run on current assemblies and record liftOver failure modes |

## A concrete coordinate lead requiring re-mapping

The gorilla structural-variation primary paper's figure caption reports one chimp–gorilla PTERV1 mapping correspondence using **historical coordinates**:

- gorilla `chr2:143467521-143467682`
- chimpanzee `chr2:143467889-143468851`

These are **not verified current assembly coordinates** and must not be fed directly into modern sequence retrieval without assembly identification, coordinate convention and liftover. A later high-resolution study identified an orthologous “source PtERV1” with a locus related to human chromosome 19; these descriptions should **not be assumed to refer to the same insertion** without direct reconciliation.

The 2005 Yohn paper's figure includes a chimpanzee BAC accession `AC097267` and human chromosome 16 Build 34 comparison as a candidate example of a chimpanzee-specific insertion. This is a historical accession and mapping lead, **not** a verified modern genomic coordinate.

## Method and acceptance criteria for R2

1. Retrieve each paper's supplemental locus tables from its publisher or archival primary article page; retain publication date, file URL and source provenance.
2. Extract locus identifiers, original assemblies and 0/1-based coordinate conventions. Flag incomplete metadata.
3. Acquire current NCBI/UCSC reference assembly accessions and versions for human, chimpanzee, bonobo, gorilla, orangutan, rhesus macaque, mouse, dog and cattle.
4. Translate coordinates with documented chain files or perform two-flank alignment; do not rely on a single liftOver hit.
5. For each positive, verify LTR/internal sequence, junctions and target-site duplications; for each negative, establish a high-quality orthologous empty site or a sensitive, adequately documented family-level negative search.
6. Distinguish assembly absence, sampled-population absence, and true lineage absence.
7. Preserve both the published historical interpretation and alternative explanations, including independent infection, shared ancestral integration, polymorphism, incomplete lineage sorting and loss.
8. Report exact A/B matches only after all stipulated species checks pass.

## Interpretation constraints

A bidirectional distribution pattern is **not** intrinsically evidence for original design. It can arise from known cross-species transmission, lineage-specific integration, ancestral polymorphism, deletion or incomplete lineage sorting. Original placement needs additional independent causal constraints. Current **full A = unverified** and **full B = unverified**.

## Primary sources

- Yohn, C.T. et al. (2005) ‘Lineage-specific expansions of retroviral insertions within the genomes of African great apes but not humans and orangutans’, *PLoS Biology*, 3(4), e110. https://doi.org/10.1371/journal.pbio.0030110
- ‘Gorilla genome structural variation reveals evolutionary parallelisms with chimpanzee’ (2011), *Genome Research*, 21, pp. 1640–1649. https://genome.cshlp.org/content/21/10/1640
- ‘High-resolution comparative analysis of great ape genomes’ (2018). Primary article https://pmc.ncbi.nlm.nih.gov/articles/PMC6178954/
- ‘Genomewide screening reveals high levels of insertional polymorphism in the human endogenous retrovirus family HERV-K(HML2): implications for present-day activity’ (2005), *Journal of Virology*, 79, pp. 12507–12514. https://doi.org/10.1128/JVI.79.19.12507-12514.2005
- ‘Genome-wide amplification of proviral sequences reveals new polymorphic HERV-K(HML-2) proviruses in humans and chimpanzees that are absent from genome assemblies’ (2015). https://doi.org/10.1186/s12977-015-0162-8
- ‘Gorillas have been infected with the HERV-K (HML-2) endogenous retrovirus much more recently than humans and chimpanzees’ (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6347686/

**Evidence provenance:** Literature observations from publisher/PMC primary article text reviewed 18 November 2026. DOI metadata and supplementary data not exhaustively audited. No sequence downloads, checksum calculations, orthology alignments, or independent genome-wide absence tests have been performed.
