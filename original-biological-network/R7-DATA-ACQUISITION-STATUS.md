# R7: Supplementary dataset acquisition and screening status

**Date:** 18 November 2026

## Execution attempt
Target: Diehl et al. (2016), *eLife* 5:e12704, Figure 2 source data 2, DOI https://doi.org/10.7554/eLife.12704.006.

- eLife article page returned a JavaScript/client challenge in web retrieval.
- Supplement DOI was inaccessible through web retrieval.
- A direct container HTTPS attempt to the eLife CDN failed at DNS resolution.
- A PMC alternate was blocked by a browser challenge.
- **No spreadsheet was downloaded or inspected. No sublineage-level genomic conclusions were generated.**

## Recovery artifact
`tools/screen_erv_lineages.py` is a conservative CSV screening script. Once source data is available, manually normalize the host-by-lineage table to its documented CSV schema. A candidate A/B result requires explicit positives and negatives; missing species are unresolved.

**Limitations:** The script uses a nonexhaustive fixed non-primate mammal taxon list and checks six named great-ape taxa. It does not verify taxonomy, assembly quality, orthology, sequence identity, or whether assay 'absent' is adequately supported. A positive output is a **screening candidate**, never a verified signature.

## Disposition
**Blocked by external supplementary-data access.** The exact A and B exclusion patterns remain unverified. No biological conclusion should be inferred from this access failure.
