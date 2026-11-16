# R1 coordinate provenance and normalization audit v0.1
Date: 2026-11-16. Scope: first eight HERV-K HML-2 candidates in `candidate-loci-v0.1.md`.

## Verified source identity
- [S1] Pasternack, Paulsen and Nath (2025), *Frontiers in Genetics* 16:1498978, DOI 10.3389/fgene.2025.1498978, PMID 39931732, PMCID PMC11807958. Source study examines 222 individuals with long-read DNA sequencing, focusing on 6q14.1 and 7p22.1a.
- [S2] Kyriakou, E. and Magiorkinis, G. (2025), 'Compilation of all known HERV-K HML-2 proviral integrations', *Mobile DNA* 16:21, DOI 10.1186/s13100-025-00359-8, PMID 40336055, PMCID PMC12057132. Table 1 explicitly distinguishes hg19 from hg38 coordinates; supplemental catalogue supplies both assemblies and accession details.

## Source-level coordinate confirmation (not FASTA verification)
| Candidate | Source | hg38 coordinate from published source | Strand | Outcome |
|---|---|---|---|---|
| L001, 6q14.1 | S1 | chr6:77716945-77726366 | Not independently verified | Source locus; exact boundary and coordinate convention pending |
| L002, 7p22.1a | S1 | chr7:4576460-4591897 | Not independently verified | Source locus; tandem architecture/polymorphism requires caution |
| L003, 19q11 | S1 | chr19:27637590-27646453 | Not independently verified | Source locus; exact boundary pending |
| L004, 11q22.1 | S1 | chr11:101695063-101704528 | Not independently verified | Source locus; exact boundary pending |
| L005, 1p36.21(327) | S2 Table 1 | chr1:13012447-13021988 | - | Verified published hg38 interval |
| L006, 6q11.1 | S2 Table 1 | chr6:60654987-60660975 | + | Verified published hg38 interval |
| L007, 11p15.4(495) | S2 Table 1 | chr11:4459435-4461473 | - | Verified published hg38 interval |
| L008, 11q12.3(281) | S2 Table 1 | chr11:62368491-62370999 | - | Verified published hg38 interval |

## Methodological caveats
1. Source coordinate reproduction is distinct from independent assembly validation. This audit has not downloaded GRCh38 FASTA or checked the bases at any locus.
2. The [S2] catalogue explicitly reports corrections and refinements to earlier coordinates; avoid substituting hg19 intervals for hg38.
3. HERV-K 7p22.1 may occur in structurally different forms. A single reference interval is insufficient to characterize the cohort. [S1] reports tandem repeat-like structures in a subset and additional deletions/insertions.
4. Coordinate origin and endpoint inclusion conventions are not established by the source snippets examined. Do not run interval arithmetic or sequence extraction until conventions are documented.
5. L009–L014 remain unverified for assembly and/or genomic locus identity; their inclusion in the candidate manifest is not an endorsement.

## R2 reproducibility contract
For each locus capture: NCBI assembly accession and patch version; reference FASTA URL and SHA-256; chromosome accession; 1-based inclusive source interval; normalized 0-based half-open BED interval; reference allele and flanking sequence SHA-256; tool and version; extraction date; source DOI; audit status. Conversion to BED requires source convention verification. Store compact manifests and scripts in Git; do not commit whole-genome reference FASTA.

## Research firewall
This audit uses public primary publications only. No parallel-programme hypotheses, preregistrations or verdicts are imported.

## Sources
- https://doi.org/10.3389/fgene.2025.1498978
- https://doi.org/10.1186/s13100-025-00359-8
