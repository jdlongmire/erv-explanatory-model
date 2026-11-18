#!/usr/bin/env python3
"""R2: collect reproducible NCBI reference-assembly metadata, no presence calls.

Requires the NCBI 'datasets' CLI installed and internet access.
Usage: python3 assembly_manifest.py --output assembly-manifest.json
"""
import argparse
import datetime
import json
import shutil
import subprocess
import sys
from pathlib import Path

SPECIES = {
    "human": "Homo sapiens",
    "chimpanzee": "Pan troglodytes",
    "bonobo": "Pan paniscus",
    "gorilla": "Gorilla gorilla",
    "orangutan": "Pongo abelii",
    "rhesus macaque": "Macaca mulatta",
    "mouse": "Mus musculus",
    "dog": "Canis lupus familiaris",
    "cattle": "Bos taurus",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="assembly-manifest.json")
    args = ap.parse_args()
    if not shutil.which("datasets"):
        sys.exit("BLOCKED: NCBI datasets CLI not found; install ncbi-datasets-cli.")
    out = {"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "method": "datasets summary genome taxon <name> --reference",
           "entries": [], "limitations": [
               "Reference selection is a candidate, not verified locus coverage.",
               "No ERV sequence alignment, synteny or absence inference performed.",
               "An empty reference response is unresolved, not biological absence."]}
    failures = 0
    for label, taxon in SPECIES.items():
        command = ["datasets", "summary", "genome", "taxon", taxon,
                   "--reference", "--limit", "5"]
        try:
            p = subprocess.run(command, capture_output=True, text=True, timeout=120)
            if p.returncode:
                raise RuntimeError(p.stderr.strip()[:500] or f"exit {p.returncode}")
            data = json.loads(p.stdout)
            reports = data.get("reports", [])
            out["entries"].append({
                "label": label, "taxon": taxon, "status": "metadata_retrieved" if reports else "unresolved",
                "assemblies": [
                    {"accession": r.get("accession"),
                     "assembly_name": r.get("assembly_info", {}).get("assembly_name"),
                     "assembly_level": r.get("assembly_info", {}).get("assembly_level"),
                     "refseq_category": r.get("assembly_info", {}).get("refseq_category")}
                    for r in reports],
                "command": command})
            if not reports:
                failures += 1
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
            failures += 1
            out["entries"].append({"label": label, "taxon": taxon,
                                   "status": "retrieval_failed", "error": str(exc),
                                   "command": command})
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    print(f"Wrote {args.output}; {len(out['entries'])} taxa; {failures} unresolved/failed.")
    if failures:
        sys.exit(2)

if __name__ == "__main__":
    main()
