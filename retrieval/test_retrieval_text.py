import json

from retrieval.retrieval_text import RetrievalTextGenerator

with open(
    "data/processed/candidate_cards.jsonl",
    "r",
    encoding="utf-8"
) as f:

    card = json.loads(next(f))

generator = RetrievalTextGenerator()

text = generator.generate(card)

print("=" * 70)
print("FINAL RETRIEVAL DOCUMENT")
print("=" * 70)
print()
print(text)