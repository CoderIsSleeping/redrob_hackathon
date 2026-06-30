"""
Semantic Search Engine

Searches the FAISS index and returns
the complete Candidate Cards of the
Top-K semantic matches.
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

        print(f"\nLoaded {self.index.ntotal} vectors.")

    def search(self, query: str, top_k: int = 100):

        query_embedding = self.embedder.embed(query)

        distances, indices = self.index.search(
            query_embedding.reshape(1, -1),
            top_k
        )

        results = []

        for rank, (idx, similarity) in enumerate(
            zip(indices[0], distances[0]),
            start=1
        ):

            info = self.metadata[idx]

            candidate = self.cards[
                info["candidate_id"]
            ]

            results.append(
                {
                    "rank": rank,
                    "similarity": round(float(similarity), 4),
                    "candidate": candidate
                }
            )

        return results