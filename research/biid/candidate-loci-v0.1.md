# ERV candidate-locus manifest v0.1

Status: **literature-extracted coordinates only**. Date: 2026-11-16. No reference FASTA, flanking alignments, target-site duplications or empty sites have been independently downloaded or validated. Coordinates below retain the source's reported format; coordinate convention (0-based/1-based, inclusive/exclusive) must be checked before computational use.

| ID | Family | Published locus | Assembly | Reported interval | Strand | Source | Analysis readiness |
|---|---|---|---|---|---|---|---|
| L001 | HERV-K HML-2 | 6q14.1 | GRCh38/hg38 | chr6:77716945-77726366 | Unverified | [S1] | Source coordinates only |
| L002 | HERV-K HML-2 | 7p22.1a | GRCh38/hg38 | chr7:4576460-4591897 | Unverified | [S1] | Source coordinates only |
| L003 | HERV-K HML-2 | 19q11 | GRCh38/hg38 | chr19:27637590-27646453 | Unverified | [S1] | Source coordinates only |
| L004 | HERV-K HML-2 | 11q22.1 | GRCh38/hg38 | chr11:101695063-101704528 | Unverified | [S1] | Source coordinates only |
| L005 | HERV-K HML-2 | 1p36.21(327) | GRCh38/hg38 | chr1:13012447-13021988 | - | [S2] | Source coordinates only |
| L006 | HERV-K HML-2 | 6q11.1 | GRCh38/hg38 | chr6:60654987-60660975 | + | [S2] | Source coordinates only |
| L007 | HERV-K HML-2 | 11p15.4(495) | GRCh38/hg38 | chr11:4459435-4461473 | - | [S2] | Source coordinates only |
| L008 | HERV-K HML-2 | 11q12.3(281) | GRCh38/hg38 | chr11:62368491-62370999 | - | [S2] | Source coordinates only |
| L009 | HERV-K HML-2 solo LTR | solo-1p35.1 | Source assembly to verify | chr1:33529117-33530085 | + | [S3] | Assembly unresolved |
| L010 | HERV-K HML-2 solo LTR | solo-3p12.3 | Source assembly to verify | chr3:75586870-75587898 | + | [S3] | Assembly unresolved |
| L011 | HERV-K HML-2 solo LTR | solo-7p14.3 | Source assembly to verify | chr7:30758200-30759205 | - | [S3] | Assembly unresolved |
| L012 | PTERV1 | source PtERV1, shared chimp/gorilla | Chimp/gorilla reference assemblies, to verify | Human orthology near chromosome 19; exact locus not yet extracted | Unverified | [S4] | Coordinates pending |
| L013 | PTERV1 | shared element mapped to gorilla chr2 | Source assembly to verify | gorilla chr2:143467521-143467682 (reported interval; element boundary unclear) | Unverified | [S5] | Mapping reconciliation pending |
| L014 | PTERV1 | chimpanzee counterpart to L013 | Source assembly to verify | chimpanzee chr2:143467889-143468851 | Unverified | [S5] | Mapping reconciliation pending |

**Do not equate L012 and L013** without confirming their exact flanking alignments, assemblies, and study definitions. In particular, the reported chr2 intervals in [S5] are not interchangeable with the chromosome-19 human-orthologous source PtERV1 locus described in [S4].

## Primary research sources
- [S1] 'Characterization of novel human endogenous retrovirus structures on chromosomes 6 and 7' (2025), https://pmc.ncbi.nlm.nih.gov/articles/PMC11807958/ ; loci in Methods. Bibliographic author details to verify.
- [S2] 'Compilation of all known HERV-K HML-2 proviral integrations' (2025), https://pmc.ncbi.nlm.nih.gov/articles/PMC12057132/ ; Table 1.
- [S3] Xue et al. (2020), 'Identification of the distribution of human endogenous retroviruses K (HML-2) by PCR-based target enrichment sequencing', https://pmc.ncbi.nlm.nih.gov/articles/PMC7201656/ ; Table 2.
- [S4] 'High-resolution comparative analysis of great ape genomes' (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC6178954/ ; source PtERV1 discussion and supplementary Table S7.
- [S5] 'Gorilla genome structural variation reveals evolutionary parallelisms with chimpanzee', https://genome.cshlp.org/highwire_display/entity_view/node/1030174/full ; Figure 2.

## Next verification gates
1. Confirm publication metadata, exact coordinate system and assembly for each source.
2. Download and checksum reference FASTA and relevant assembly accession/version; record immutable source URL and retrieval date.
3. Extract ±2 kb flanks, align to corresponding species, and distinguish true orthology from repeat-driven multi-mapping.
4. Call target-site duplications, 5'/3' LTR boundaries and shared disabling substitutions using documented software versions.
5. Record empty-site and polymorphism evidence with a per-locus confidence grade.
6. Only after verification, score pre-registered discriminating predictions. No predictions are registered here.

## Research independence
Public primary genomic evidence only. This manifest imports no parallel-programme model criteria or verdicts.
