#!/usr/bin/env python3
"""Conservative ERV host-by-sublineage screening of a locally supplied CSV.

CSV columns: lineage,species,sequence_id,region,assay_status,evidence
assay_status: present | absent | unresolved. Missing species remain unresolved.
Never infer a negative from an unlisted species.
"""
import argparse,csv,json
from collections import defaultdict

APES = ["Homo sapiens","Pan troglodytes","Pan paniscus","Gorilla gorilla","Pongo abelii","Pongo pygmaeus"]
HUMAN = APES[0]
OTHER = APES[1:]
NONPRIMATE = {"Canis lupus familiaris","Felis catus","Mus musculus","Rattus norvegicus","Sus scrofa","Ailuropoda melanoleuca","Bos taurus","Equus caballus"}

def evaluate(rows):
    by=defaultdict(lambda: defaultdict(set))
    for r in rows:
        status=r["assay_status"].strip().lower()
        if status not in ("present","absent","unresolved"): raise ValueError("invalid assay_status")
        by[r["lineage"].strip()][r["species"].strip()].add(status)
    out=[]
    for lineage, species in sorted(by.items()):
        def s(t):
            v=species.get(t,set())
            return next(iter(v)) if len(v)==1 else "unresolved"
        nonprimate=[x for x in sorted(NONPRIMATE) if s(x)=="present"]
        ape_negative=all(s(x)=="absent" for x in OTHER)
        ape_positive=any(s(x)=="present" for x in OTHER)
        a=s(HUMAN)=="present" and bool(nonprimate) and ape_negative
        b=s(HUMAN)=="absent" and bool(nonprimate) and ape_positive
        out.append({"lineage":lineage,"human":s(HUMAN),"other_apes":{x:s(x) for x in OTHER},
                    "nonprimate_positives":nonprimate,"A":a,"B":b,
                    "note":"Only explicitly recorded absences count; taxon list is nonexhaustive."})
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("csv_file")
    args=p.parse_args()
    with open(args.csv_file,newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        expected={"lineage","species","sequence_id","region","assay_status","evidence"}
        if not expected.issubset(set(reader.fieldnames or [])): raise ValueError("missing columns")
        rows=list(reader)
    print(json.dumps(evaluate(rows),indent=2))
if __name__=="__main__": main()
