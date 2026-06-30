"""
Build Evidence Store

Runs the rule-based Evidence Extractor
for every candidate and stores the output.
"""

import json
from pathlib import Path

from preprocessing.evidence_extractor import EvidenceExtractor

INPUT_FILE = Path("data/processed/candidate_cards.jsonl")
OUTPUT_FILE = Path("data/processed/candidate_evidence.jsonl")


def main():

    extractor = EvidenceExtractor()

    total = 0

    with open(INPUT_FILE, "r", encoding="utf-8") as fin, \
         open(OUTPUT_FILE, "w", encoding="utf-8") as fout:

        for line in fin:

            card = json.loads(line)

            evidence = extractor.extract(card)

            output = {
                "candidate_id": card["candidate_id"],
                "evidence": {
                    key: {
                        "score": value.score,
                        "evidence": value.evidence
                    }
                    for key, value in evidence.items()
                }
            }

            fout.write(json.dumps(output) + "\n")

            total += 1

            if total % 5000 == 0:
                print(f"Processed {total} candidates")

    print()
    print("=" * 60)
    print("EVIDENCE STORE CREATED")
    print("=" * 60)
    print(f"Total Candidates : {total}")


if __name__ == "__main__":
    main()