#!/usr/bin/env python3
"""BIID R2 reference extraction helper. Requires user-supplied reference FASTA.

No network access, automatic assembly guessing, or unverified coordinate conversion.
Input TSV columns: locus_id,chrom,start_1based,end_1based,assembly_accession.
Output TSV includes sequence and flanks SHA-256, assembly ID and coordinates.
"""
import argparse
import csv
import hashlib
from pathlib import Path

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_fasta(path):
    sequences = {}
    current = None
    with open(path, encoding="ascii") as handle:
        for line in handle:
            if line.startswith(">"):
                current = line[1:].strip().split()[0]
                if current in sequences:
                    raise ValueError(f"Duplicate sequence ID: {current}")
                sequences[current] = []
            elif current is not None:
                sequences[current].append(line.strip().upper())
    return {key: "".join(parts) for key, parts in sequences.items()}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fasta", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--flank", type=int, default=2000)
    parser.add_argument("--assembly-accession", required=True)
    args = parser.parse_args()
    if args.flank < 0:
        parser.error("--flank must be nonnegative")
    seqs = load_fasta(args.fasta)
    fields = ["locus_id", "assembly_accession", "chrom", "start_1based", "end_1based",
              "start_0based", "end_0based", "sequence_sha256", "flanks_sha256",
              "reference_fasta_sha256", "flank_bases_left", "flank_bases_right"]
    fasta_hash = digest(Path(args.fasta).read_bytes())
    with open(args.manifest, newline="", encoding="utf-8") as src, open(args.output, "w", newline="", encoding="utf-8") as dest:
        reader = csv.DictReader(src, delimiter="\t")
        required = {"locus_id", "chrom", "start_1based", "end_1based", "assembly_accession"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Missing manifest fields: " + repr(required - set(reader.fieldnames or [])))
        writer = csv.DictWriter(dest, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in reader:
            if row["assembly_accession"] != args.assembly_accession:
                raise ValueError("Assembly mismatch at " + row["locus_id"])
            chrom = row["chrom"]
            if chrom not in seqs:
                raise ValueError("Reference sequence absent: " + chrom)
            start, end = int(row["start_1based"]), int(row["end_1based"])
            sequence = seqs[chrom]
            if not (1 <= start <= end <= len(sequence)):
                raise ValueError("Out-of-bounds locus: " + row["locus_id"])
            a, b = start - 1, end
            left, right = sequence[max(0, a-args.flank):a], sequence[b:min(len(sequence), b+args.flank)]
            writer.writerow({"locus_id": row["locus_id"], "assembly_accession": args.assembly_accession,
                             "chrom": chrom, "start_1based": start, "end_1based": end,
                             "start_0based": a, "end_0based": b,
                             "sequence_sha256": digest(sequence[a:b].encode("ascii")),
                             "flanks_sha256": digest((left+"|"+right).encode("ascii")),
                             "reference_fasta_sha256": fasta_hash,
                             "flank_bases_left": len(left), "flank_bases_right": len(right)})
if __name__ == "__main__":
    main()
