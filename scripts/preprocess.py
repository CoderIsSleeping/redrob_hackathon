"""
Dataset Preprocessing Script

Converts the raw Redrob dataset
into Candidate Intelligence Cards.
"""

import json
from pathlib import Path

from preprocessing.candidate_card import build_candidate_card

RAW_DATA = Path("data/raw/candidates.jsonl")

OUTPUT = Path("data/processed/candidate_cards.jsonl")

def preprocess_dataset():

    processed = 0

    with open(RAW_DATA, "r", encoding="utf-8") as infile, \
         open(OUTPUT, "w", encoding="utf-8") as outfile:

        for line in infile:

            candidate = json.loads(line)

            card = build_candidate_card(candidate)

            outfile.write(json.dumps(card))

            outfile.write("\n")

            processed += 1

            if processed % 10000 == 0:
                print(f"Processed {processed} candidates")

    print("Done!")

if __name__ == "__main__":

    preprocess_dataset()