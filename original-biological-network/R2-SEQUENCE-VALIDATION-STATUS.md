# R2 sequence validation protocol and execution status

**18 November 2026** | **Status: partially implemented; live genomic retrieval blocked in current execution environment**

## What was attempted
- NCBI Datasets metadata endpoint connectivity was tested from the execution container.
- Result: HTTPS connection failure; the NCBI `datasets` executable was also absent.
- No assembly FASTA, genome interval, orthology chain, locus alignment or sequence checksum was retrieved.
- GitHub connector read/create operations were available and verified; repository branch `research/biid-erv-origin` is used.

## Implemented reproducible step
`tools/assembly_manifest.py` queries NCBI Datasets for candidate reference assembly metadata across nine taxa, records accessions, assembly names, status, and errors in JSON. It is a **metadata collector**, not a sequence validator. It is designed to fail with nonzero exit status on unresolved taxa.

### Run in a network-enabled research environment

```bash
conda install -c conda-forge ncbi-datasets-cli
python3 tools/assembly_manifest.py --output assembly-manifest.json
```

Review the output before choosing assemblies. Do not automatically assume a species has one canonical reference or that two assemblies have compatible coordinate conventions.

## Sequence validation gates (not yet executed)

1. Resolve published locus names, BAC accessions, original assembly versions and original coordinates from primary supplementary tables.
2. Record accession.version, download URL, retrieval date, checksums, coordinate convention and annotation release.
3. Extract the insertion plus at least two independently mapped flanking regions; align flanks across species.
4. Evaluate assembly continuity, synteny, LTR/internal element features, target-site duplications, structural variation and alternative paralogs.
5. For absence, verify an orthologous empty site in a high-quality assembly; record sample limitations and population polymorphism.
6. Independently evaluate both cross-lineage target patterns, preserving all failures and ambiguous results.
7. Separate family homology from exact insertion orthology and report confidence for each call.

## Primary reference for acquisition method
NCBI Datasets documentation: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/download-genome/
NCBI Datasets metadata documentation: https://ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/get-genome-metadata/

## Findings to date
- Full Track A: **UNVERIFIED**.
- Full Track B with non-primate mammal: **UNVERIFIED**.
- PTERV1 remains a **partial Track B** literature-level example involving Old World monkeys.
- No claim of successful sequence-level analysis, new locus confirmation, or empirical support for original placement is warranted.

## Research integrity and next decision
When a network-enabled computational runtime is available, execute the metadata collector, then prioritize a *single* PTERV1 locus with independently documented flanks before attempting genome-wide comparison. The original-design hypothesis remains conjectural; do not score a model until its empirical prerequisites are satisfied.
