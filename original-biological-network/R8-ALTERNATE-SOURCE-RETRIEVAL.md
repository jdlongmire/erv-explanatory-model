# R8: Alternate-source retrieval and ERV-Fc screening

**Date:** 18 November 2026. **Status:** Primary supplementary data located via alternate publication mirror; complete workbook unavailable for computational analysis.

## Retrieval record
- Publisher eLife figure page: https://elifesciences.org/articles/12704/figures — web search index exposes primary source-data descriptions, but live site presents JavaScript challenge.
- Figure 2 source data 2 DOI: https://doi.org/10.7554/eLife.12704.006 — direct open unavailable in the web interface.
- Authors' supplementary dataset mirrored on ResearchGate: https://www.researchgate.net/publication/306503091_Figure_2-source_data_2 — searchable rendered text exposes portions of the table, including taxonomy and its provenance. **Not equivalent to obtaining the complete XLSX.**
- PMC full primary paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC4798954/ — text accessible through indexed web results.
- Container HTTPS request to publisher failed due to DNS resolution. **No file downloaded; no sequence alignment or CSV screening executed.**

## Primary-paper observations recovered
Diehl et al. (2016) report ERV-Fc coding sequences in 28 species, multiple lineages in some primates and carnivores, a solo ERV-Fc LTR in orangutan, and an HERV-Fc1 env locus shared among great apes. The study identifies separate primate and carnivore ERV-Fc lineages and infers multiple cross-species transmission events.

**Consequence:** A family-level positive in human and dog does not satisfy A when other great apes are also family-positive; likewise an ape-and-dog family match does not satisfy B when human is positive. Specific sublineages must be compared with all relevant apes under equivalent assay resolution.

## Current candidate decisions
| Candidate | A | B | Reason |
|---|---|---|---|
| Broad ERV-Fc | Does not qualify | Does not qualify | Family is present across great apes and non-primate mammals |
| HERV-Fc1 env | Does not qualify | Does not qualify | Shared across great apes |
| Narrow ERV-Fc sublineage | Unverified | Unverified | Complete source table and sequence comparison unavailable |
| CERV1/PERV | Unverified | Unverified | Receptor compatibility alone is not shared ERV sequence evidence |

## Required next execution
1. Obtain full `elife-12704-fig2-data2-v1.xlsx` and genome-build companion `elife-12704-fig2-data1-v1.xlsx` from the publisher or author mirror.
2. Preserve original file hashes and publication DOI provenance.
3. Inspect exact column names and normalize each host/sublineage row to the existing screening CSV schema.
4. Treat unlisted taxa as unresolved, never negative. Verify sublineage similarity and any reported absence with genome assembly checks.
5. Only then report a complete A or B positive.

## Epistemic disposition
**HIGH:** Primary article reports broad ERV-Fc distribution, multiple lineages, and shared great-ape HERV-Fc1 env.

**UNCERTAIN:** Either exact exclusion pattern at sublineage resolution.

**Operational:** The alternate mirror establishes an additional retrieval route but does not resolve the need for complete workbook bytes.

Reference: Diehl, W.E. et al. (2016), *eLife* 5:e12704, https://doi.org/10.7554/eLife.12704.
