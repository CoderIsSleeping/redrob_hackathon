"""
Semantic Search Engine

Loads the FAISS index and retrieves
the Top-K most similar candidates.
"""

import json
from pathlib import Path

import faiss

from retrieval.embedder import EmbeddingEngine

INDEX_PATH = Path("data/processed/faiss.index")
IDS_PATH = Path("data/processed/candidate_ids.json")
CARDS_PATH = Path("data/processed/candidate_cards.jsonl")


class SemanticSearch:

    def __init__(self):

        print("Loading FAISS index...")

        self.index = faiss.read_index(str(INDEX_PATH))

        print("Loading metadata...")

        with open(IDS_PATH, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        print("Loading candidate cards...")

        self.cards = {}

        with open(CARDS_PATH, "r", encoding="utf-8") as f:

            for line in f:

                card = json.loads(line)

                self.cards[card["candidate_id"]] = card

        self.embedder = EmbeddingEngine()

        print()

        print(f"Loaded {self.index.ntotal} vectors.")

    def search(self, query: str, top_k: int = 100):

        query_vector = self.embedder.embed(query)

        distances, indices = self.index.search(
            query_vector.reshape(1, -1),
            top_k
        )

        results = []

        for rank, (idx, similarity) in enumerate(
            zip(indices[0], distances[0]),
            start=1
        ):

            candidate = self.metadata[idx]

            card = self.cards[candidate["candidate_id"]]

            results.append(
                {
                    "rank": rank,
                    "candidate_id": candidate["candidate_id"],
                    "headline": card["semantic"]["headline"],
                    "experience": candidate["experience_bucket"],
                    "industry": card["metadata"]["industry"],
                    "similarity": round(float(similarity), 4)
                }
            )

        return results