# R3: LINC00662–PTERV1 primary-evidence case study

**18 November 2026** | **Evidence status: published experimental and comparative evidence; independent sequence reanalysis pending**

## Primary paper and underlying data

*Retroviral insertions contributed to the divergence of human and chimpanzee brains* (2026), peer-reviewed article at https://pmc.ncbi.nlm.nih.gov/articles/PMC13693685/ ; PubMed https://pubmed.ncbi.nlm.nih.gov/42913018/ . Associated NCBI BioProject **PRJEB104347** (registered 29 November 2025): https://www.ncbi.nlm.nih.gov/bioproject/1371173 .

The paper reports a **6,915-nt PTERV1 insertion** in the first intron of the chimpanzee LINC00662 genomic region. It reports that the insertion occurs in chimpanzee and bonobo, is absent in human and orangutan, and that the approximately 300-kb containing region is absent in gorilla and macaque. The latter is **structural noncomparability**, not evidence for a verified empty insertion site in gorilla or macaque. The paper experimentally reports that CRISPR removal of the chimpanzee insertion restored LINC00662 expression in induced pluripotent stem cells, and connects the silencing to spreading DNA methylation.

**HIGH confidence:** these claims are reported in a primary research article with described experimental work. **UNCERTAIN:** independent reanalysis, exact assembly accession/coordinate, junctions and target-site duplications, and any non-primate mammalian ortholog.

## What the result establishes

1. A concrete, functionally consequential lineage-specific viral insertion exists in the studied genomic context, based on published evidence.
2. Chimpanzee and bonobo are positive at the reported locus, with human and orangutan negative.
3. Gorilla and macaque require special handling because the corresponding larger segment is absent, precluding a simple insertion-empty-site inference.
4. A negative regulatory effect in the present experimental context **does not establish** that the insertion was originally beneficial or that the original biological network existed.

## Track classification

**Track B: partial, not complete.** Nonhuman ape positives and human absence are supported at the reported locus; the required non-primate mammal positive is not established. The published paper's lineage-specificity finding is consistent with conventional infection/inheritance histories and does not discriminate original design.

## Registered sequence-validation checklist

- [ ] Retrieve supplementary tables and determine chimpanzee, bonobo, human and orangutan assembly accession.versions.
- [ ] Extract the PTERV1 insertion and both host flanks with exact coordinate convention and accession.
- [ ] Align flanks to corresponding human and orangutan orthologous intervals.
- [ ] Document structural absence in gorilla/macaque separately from empty insertion sites.
- [ ] Check mouse, dog and cattle for homologous PTERV1 family sequences **and separately** for syntenic locus; record nonhits as unresolved until detection sensitivity is established.
- [ ] Confirm target-site duplications, LTR boundaries, copy number, repeat masking, and alternative paralogs.
- [ ] Preserve raw accession identifiers, retrieval timestamps, command versions and checksums.
- [ ] Compare original placement, independent viral insertion, vertical inheritance, ancestral polymorphism and deletion under equal evidentiary criteria.

## Correction to the earlier research inventory

The earlier R1 audit marked bonobo PTERV1 status unresolved. This 2026 primary article expressly reports PTERV1 elements in bonobos, and identifies a bonobo-positive LINC00662 insertion. **This corrects the bonobo status for this specific locus and supports family-level presence.** It does not establish that bonobos possess every PTERV1 locus present in chimpanzees.

## Computational tooling correction

The assembly metadata collector initially used `--reference`, which can exclude usable non-reference ape assemblies. It was revised to retrieve up to 20 candidate assemblies per species and require manual selection. NCBI's primary command documentation: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/command-line/datasets/summary/genome/ . Metadata retrieval is still unexecuted in the current environment.

## Decision

Advance LINC00662–PTERV1 as the first **experimental locus validation target**. The research remains at published-evidence extraction. No independently validated complete A or B cross-kind signature has yet been obtained.
