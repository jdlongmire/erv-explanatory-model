# BIID ERV evidence matrix v0.2 (source-level observations, not yet locus-resolved)
Date: 2026-11-16. Status: primary literature extracted; genomic reanalysis pending.

## Evidence ledger

| ID | System/locus | Observed primary result | Method / limitations | Relevance to model discrimination | Source | Confidence |
|---|---|---|---|---|---|---|
| E01 | HERV-K18 and other primate orthologous ERVs | Orthologous integration and LTR sequence variation support primate phylogenetic reconstruction | PCR, sequencing, phylogenetic comparison; original reference assemblies and selected loci | M1 predicts inherited orthology and correlated mutations; BIID must make a distinguishable prediction | Johnson & Coffin (1999), DOI 10.1073/pnas.96.18.10254, PMID 10468595 | HIGH for reported observations |
| E02 | PTERV1, chimpanzee/gorilla/Old World monkeys | 275/287 evaluable integration locations (95.8%) classified nonorthologous | BAC end-sequence mapping; 24 ambiguous locations could represent up to 12 shared sites; not base-pair resolved | Strong evidence for lineage-specific insertions; not evidence of beneficial ancestral intent | Yohn et al. (2005), DOI 10.1371/journal.pbio.0030110, PMID 15737067 | HIGH for study result, limited mapping resolution |
| E03 | PtERV1, chimpanzee and gorilla | High-resolution study mapped 540 elements, reported 99.8% nonorthology and one orthologous source element | Improved great-ape assemblies; study-level counts require careful denominator and element-type reconciliation before cross-study numerical comparison | Demonstrates why ambiguous loci require improved assemblies; consistent with ancestral source and later expansions | High-resolution comparative analysis of great ape genomes (2018), PMC6178954 | HIGH for reported study result |
| E04 | Mouse syncytin-A | Knockout causes placental failure and embryonic lethality | Targeted knockout; function in mouse placentation, not direct evidence of original viral function | Functional co-option is established; historical direction remains unproven for BIID | Dupressoir et al. (2009), DOI 10.1073/pnas.0902925106, PMID 19564597 | HIGH |

## Required locus-level columns
Locus identifier; family; genome assembly/version; accession; reference coordinate; species; orthologous flanks and synteny; insertion boundary; target-site duplications; LTR sequences and divergence; shared disabling substitutions; empty-site validation; genome quality; functional assay; primary citation; extraction method; M1 prediction; M2 prediction; M3 prediction; uncertainty.

## Registered hypotheses
None. The comparisons below are candidate discriminators requiring preregistration before any targeted dataset scoring.

### Candidate discriminators
1. Does BIID predict a specific, reproducible genomic address mechanism that independently produces orthologous insertions plus shared derived substitutions without inheritance?
2. Does BIID predict identifiable ancestral host-beneficial regulatory modules that predate pathogenic forms, with directionality inferred from independently rooted phylogenies?
3. Does BIID predict a genomic signature or species distribution not already anticipated by vertical inheritance, horizontal infection, selection, or co-option?

### Decision rule
Do not interpret present functionality as proof of beneficial origin. Do not interpret nonrandom integration preference as sufficient to explain identical orthologous loci. Compare likelihoods or calibrated prediction accuracy using predeclared datasets and penalize added assumptions. A BIID mechanism that generates no unique testable consequences remains underdetermined rather than empirically supported.

## Primary sources
- Johnson, W.E. and Coffin, J.M. (1999) 'Constructing primate phylogenies from ancient retrovirus sequences', *PNAS*, 96(18), pp. 10254–10260. https://doi.org/10.1073/pnas.96.18.10254
- Yohn, C.T. et al. (2005) 'Lineage-Specific Expansions of Retroviral Insertions within the Genomes of African Great Apes but Not Humans and Orangutans', *PLoS Biology*, 3(4), e110. https://doi.org/10.1371/journal.pbio.0030110
- 'High-resolution comparative analysis of great ape genomes' (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC6178954/ [Full bibliographic metadata pending]
- Dupressoir, A. et al. (2009) 'Syncytin-A knockout mice demonstrate the critical role in placentation of a fusogenic, endogenous retrovirus-derived, envelope gene', *PNAS*, 106(29), pp. 12127–12132. https://doi.org/10.1073/pnas.0902925106

## Research firewall
Only publicly available primary observations and citation corrections are imported. No model criteria, predictions, dispositions, or verdicts from parallel DFM or Christian Designism ERV programmes have been imported. This matrix does not register predictions on their behalf.
