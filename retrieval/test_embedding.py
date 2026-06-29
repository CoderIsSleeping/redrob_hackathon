import json

from retrieval.embedder import EmbeddingEngine
from retrieval.retrieval_text import RetrievalTextGenerator

with open(
    "data/processed/candidate_cards.jsonl",
    "r",
    encoding="utf-8"
) as f:

    card = json.loads(next(f))

generator = RetrievalTextGenerator()

document = generator.generate(card)

engine = EmbeddingEngine()

embedding = engine.embed(document)

print("=" * 70)
print("EMBEDDING GENERATED")
print("=" * 70)

print()

print("Dimension :", len(embedding))

print()

print("First 10 values")

print(embedding[:10])