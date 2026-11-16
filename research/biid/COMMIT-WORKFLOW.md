# Incremental research commit workflow

Scope: `research/biid-erv-origin`; no direct research commits to `main`.

1. **One coherent change per commit.** Separate literature extraction, source corrections, coordinate verification, sequence extraction, analysis, and interpretation.
2. **Record provenance.** Every observation must include the primary source, accession/assembly, coordinates, retrieval date, method, and confidence. Label unverified data explicitly.
3. **Commit only validated content.** Read back each remote commit and confirm expected paths, counts and SHA before the next write.
4. **Preserve history.** No force-push, silent data overwrites, or squashing evidence corrections into prior commits. Supersede with a new version and changelog.
5. **Keep data and conclusions separate.** Candidate predictions must be registered before evaluation; source-level observations are not model verdicts.
6. **Honor the research firewall.** No cross-import of parallel-programme criteria, registered predictions, auxiliary dispositions or verdicts before the agreed comparison.
7. **Review gate.** Use a PR for any proposed merge to `main`; verify required checks and reviewer approvals before merging. No automatic merge.
8. **Source access constraints.** When only published coordinates are accessible, stop at a literature-derived manifest and do not claim computational sequence validation.

## Commit ledger

| Commit | Scope | Verification |
|---|---|---|
| `e6b9950` | Added 14 candidate loci with source and assembly caveats | GitHub file readback, 14 locus rows confirmed |
| Current commit | Added this workflow contract | Verify remote file and branch head after commit |

## Planned sequence
- R1: resolve assembly and coordinate conventions per locus
- R2: retrieve reference sequences with checksums
- R3: validate orthologous flanks and insertion boundaries
- R4: evaluate target-site duplications and shared disabling mutations
- R5: preregister and score model-discriminating predictions

**Status:** R1 incomplete; R2–R5 pending. No sequence-level results claimed.
