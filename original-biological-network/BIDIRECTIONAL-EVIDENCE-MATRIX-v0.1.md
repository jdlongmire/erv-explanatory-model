# Bidirectional cross-lineage ERV evidence matrix v0.1

**Date:** 2026-11-18. **Status:** Literature-level screening only; no assembly-aware locus validation.

## Operational definitions

- **A:** Human positive; one or more non-ape mammals positive; chimpanzee, bonobo, gorilla and orangutan negative.
- **B:** One or more nonhuman apes positive; one or more non-ape mammals positive; human negative.
- **Family-level positive:** a verified homologous ERV family member; does not imply the same genomic insertion.
- **Locus-level positive:** insertion at an orthologous locus with verified flanks, boundaries and appropriate synteny.
- **Negative:** independently inspected orthologous region or sensitive family survey showing absence, with assembly and method limits recorded.
- **Unresolved:** no adequate data; must never be coded as negative.

“Non-ape” includes monkeys in a literal taxonomic sense, but for the more demanding cross-kind hypothesis this matrix separately records **non-ape primates** and **non-primate mammals**. Created-kind boundaries are not inferred from morphological distance alone.

## Screening table

| Candidate / reference | Human | Nonhuman apes | Non-ape primates | Non-primate mammals | Track A | Track B | Level / caveat |
|---|---|---|---|---|---|---|---|
| PTERV1, Yohn et al. (2005) | Absent in surveyed human genome | Chimpanzee and gorilla positive; orangutan absent; bonobo status not established here | Old World monkeys positive | Unresolved | No | **Partial B** | Family distribution; 287 mapped integrations, ~95.8% nonorthologous; no verified non-primate mammal positive |
| Orthologous HERV loci, Johnson and Coffin (1999) | Positive at studied loci | Multiple primate orthologues and polymorphisms | Some primate comparisons | Unresolved | No | No | Strong inherited-locus comparator, not target pattern |
| Human-specific HERV-K (HML-2) insertions | Candidate human positives | Some sites absent in other apes | Unresolved | Unresolved | **Candidate A only** | No | Requires locus-by-locus verification; no verified non-primate mammal match |
| ERV-Fc-related family across mammals | Reported family presence | Other apes not excluded | Unresolved | Reported family presence | No verified A | No verified B | Broad family similarity insufficient for exclusion pattern; primary citation and genomic loci pending audit |
| ERV-V-related envelope homologues | Reported in primates | Other apes not excluded | Unresolved | Reported in some distant mammalian lineages | No verified A | No verified B | Functional homology and orthology must be disentangled; primary citation pending audit |

## Evidence grades

- **HIGH, primary literature:** PTERV1 distribution in the surveyed species and predominantly nonorthologous mapped insertions (Yohn et al., 2005).
- **HIGH, primary literature:** orthologous ERV loci and inherited sequence variation supply strong primate phylogenetic information (Johnson and Coffin, 1999).
- **UNCERTAIN:** Any fully qualified A pattern in the stipulated species.
- **UNCERTAIN:** Any fully qualified B pattern including a non-primate mammal.
- **UNCERTAIN:** Original design as the actual historical origin of any candidate locus.

## Analysis protocol

1. Register candidate family, locus identifier, assembly build, accession and coordinate; record the exact source of each proposed positive.
2. Search the human, chimpanzee, bonobo, gorilla, orangutan, macaque, mouse, dog and cattle genomes as appropriate; species selection is an explicit analysis choice.
3. Separate family search from synteny/orthology verification. Record assembly gaps, copy number, deletions, reference bias and false negatives.
4. Evaluate both A and B using the same sensitivity, specificity, presence/absence criteria and evidence thresholds.
5. At candidate loci, inspect flanking sequence, target-site duplications, LTR structure, shared substitutions and gene-conversion signals.
6. Evaluate vertical inheritance, independent integration, horizontal transmission, ancestral polymorphism, loss, and original placement with constrained assumptions.
7. Record failures and nonmatches, not just attractive examples.

## Primary-source anchors

Yohn, C.T. et al. (2005) ‘Lineage-specific expansions of retroviral insertions within the genomes of African great apes but not humans and orangutans’, *PLoS Biology*, 3(4), e110. https://doi.org/10.1371/journal.pbio.0030110

Johnson, W.E. and Coffin, J.M. (1999) ‘Constructing primate phylogenies from ancient retrovirus sequences’, *PNAS*, 96(18), pp. 10254–10260. https://doi.org/10.1073/pnas.96.18.10254

**Provenance:** Source article text and bibliographic metadata checked against the publicly accessible primary papers on 2026-11-18. Other candidates are explicitly carried as unverified leads, not validated findings. No genomic sequences were downloaded or aligned.
