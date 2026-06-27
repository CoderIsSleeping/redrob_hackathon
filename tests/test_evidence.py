import json

from preprocessing.evidence_extractor import EvidenceExtractor

with open("data/processed/candidate_cards.jsonl", "r", encoding="utf-8") as f:
    card = json.loads(next(f))

extractor = EvidenceExtractor()

result = extractor.extract(card)

for capability, info in result.items():

    print(capability)

    print(info)

    print("-" * 40)