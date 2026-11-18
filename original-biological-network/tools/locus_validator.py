#!/usr/bin/env python3
"""Conservative offline exact-flank validation. Requires biopython.
Manifest: {"cases":[{"id":"x","species":"Pan troglodytes","status":"positive","fasta":"local.fa","left_flank":"ACGT...","right_flank":"ACGT...","insertion":"ACGT..."}]}
For empty-site calls set status=empty_site and omit insertion.
"""
import argparse
import json
from pathlib import Path
from Bio import SeqIO

def assess(case, root):
    result = {"id": case["id"], "species": case["species"], "status": "unresolved"}
    if case["status"] == "unresolved":
        result["reason"] = "No sequence evidence supplied"
        return result
    if case["status"] not in ("positive", "empty_site"):
        raise ValueError("Invalid status")
    left, right = case["left_flank"].upper(), case["right_flank"].upper()
    if min(len(left), len(right)) < 12 or any(x not in "ACGT" for x in left + right):
        result["reason"] = "Flanks require >=12 unambiguous bases"
        return result
    path = (root / case["fasta"]).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        result["reason"] = "FASTA missing or path outside manifest directory"
        return result
    matches = []
    with path.open() as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence = str(record.seq).upper()
            left_positions = [i for i in range(len(sequence)) if sequence.startswith(left, i)]
            right_positions = [i for i in range(len(sequence)) if sequence.startswith(right, i)]
            for l in left_positions:
                for r in right_positions:
                    if r >= l + len(left):
                        matches.append((record.id, l, r, sequence[l + len(left):r]))
    if len(matches) != 1:
        result["reason"] = f"Expected exactly one ordered flank pair, found {len(matches)}"
        return result
    contig, l, r, between = matches[0]
    result.update({"contig": contig, "left_0based": l, "right_0based": r, "interflank_length": len(between)})
    if case["status"] == "positive":
        insert = case.get("insertion", "").upper()
        if not insert or any(x not in "ACGT" for x in insert) or insert != between:
            result["reason"] = "Insertion absent, ambiguous, or not exact match"
            return result
        result["status"] = "sequence_consistent_positive"
    elif between == "":
        result["status"] = "sequence_consistent_empty_site"
    else:
        result["reason"] = "Expected empty interval, found sequence"
        return result
    result["reason"] = "Exact sequence comparison only; orthology and species absence unverified"
    return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("manifest")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    path = Path(args.manifest).resolve()
    data = json.loads(path.read_text())
    results = [assess(c, path.parent) for c in data["cases"]]
    output = {"schema_version": "0.1", "results": results, "limitations": [
        "No reverse-complement search or mismatches",
        "No orthology or assembly quality inference",
        "An empty site is not proof of species-wide absence",
        "Not a genome-wide ERV family search"]}
    Path(args.output).write_text(json.dumps(output, indent=2) + "\n")
    print(f"{len(results)} cases; {sum(r['status'].startswith('sequence_consistent') for r in results)} sequence-consistent")

if __name__ == "__main__":
    main()
