# R2 synthetic extraction validation (2026-11-16)

## Executed test
The committed `tools/extract_reference.py` implementation was executed locally against a 12-base synthetic FASTA with chromosome ID `chrT` and sequence `ACGTACGTACGT`.

Manifest: `T001,chrT,3,6,TEST.1`; flank size 2 bases; output was generated successfully.

Observed:
- 1-based inclusive interval: 3–6
- 0-based half-open interval: 2–6
- SHA-256 of extracted sequence `GTAC`: `d6fcac3556d5f5e4ab0467905e0ba8a0217a39dbfcf4c8ce7ed58303dad2c009`
- 2 flanking bases on each side
- Full FASTA file SHA-256: `cf28787cabcb062588023eb69c2bbd2df32bcc47c599e923bf35da32711ac6dd`

## Limitations and follow-up
This is one positive smoke test, not comprehensive unit-test coverage. Error paths, empty input, malformed FASTA, duplicate chromosome IDs, large FASTA memory requirements, and transactional output handling are untested. The implementation loads the full FASTA into memory and should not be used for whole human genome extraction without redesign. Source coordinate conventions remain unresolved. No real reference sequence was retrieved or analyzed.

Next change: add automated positive/negative tests, then replace full-memory FASTA loading with indexed retrieval before GRCh38 work. Maintain one coherent commit per change and verify GitHub readback.
