# R4 execution record: offline locus validator

**Date:** 2026-11-18  
**Branch:** `research/biid-erv-origin`

## Implemented
- `tools/locus_validator.py`: exact forward-strand ordered-flank search on supplied local FASTA; positive insertion or empty-site classification; unresolved status on missing/ambiguous evidence.
- `tools/test_locus_validator.py`: six synthetic tests covering positive, empty, mismatch, nonempty interval, duplicate flanks and missing FASTA.

## Validation
Six synthetic unit tests passed locally against an equivalent implementation; local code was also syntax-compiled. GitHub files were committed and read back byte-for-byte. The precise committed version has **not** been executed in a fresh checkout. The test fixtures contain fabricated sequences for software verification, not genomic evidence.

## Blockers
Direct HTTPS retrieval from NCBI and UCSC failed from the local computational environment on 2026-11-18. No real genome FASTA, flank coordinates, target-site duplications or orthology chains were obtained. NCBI's documented `datasets summary genome taxon` command was independently checked in official documentation; no live metadata call succeeded.

## Scientific safeguards
- Exact sequence matches alone cannot establish orthology.
- Negative calls require assembly-aware syntenic empty sites, repeat-sensitive search and population assessment.
- A/B full cross-kind targets remain unverified.
- The 2026 LINC00662–PTERV1 case is a **partial Track B** published-evidence candidate only.
- The validator does not search reverse complements or permit mismatches; failure is **unresolved**, not absence.

## To run in a network-enabled analysis environment
```bash
python3 -m pip install biopython
cd original-biological-network/tools
python3 -m unittest -v test_locus_validator.py
python3 assembly_manifest.py --output assembly-manifest.json
python3 locus_validator.py /path/to/manifest.json --output /path/to/locus-results.json
```

The locus manifest must contain locally retrieved FASTA files and experimentally or independently mapped flanking sequences. Record accession versions, reference assembly builds, provenance and checksums separately. Do not manufacture missing sequence input.

## Next scientific milestone
Resolve the published LINC00662–PTERV1 locus and both flanks to versioned chimpanzee/bonobo/human/orangutan assemblies. Then independently investigate non-primate mammal family-level homologs, keeping exact-locus tests separate.
