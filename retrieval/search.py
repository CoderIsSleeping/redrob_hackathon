"""
Semantic Search Engine

Returns Candidate Card + Precomputed Evidence
for the Top-K semantic matches.
"""

import json
from pathlib import Path

import faiss

from retrieval.embedder import EmbeddingEngine

INDEX_PATH = Path("data/processed/faiss.index")
IDS_PATH = Path("data/processed/candidate_ids.json")
CARDS_PATH = Path("data/processed/candidate_cards.jsonl")
EVIDENCE_PATH = Path("data/processed/candidate_evidence.jsonl")


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

        print("Loading evidence store...")

        self.evidence = {}

        with open(EVIDENCE_PATH, "r", encoding="utf-8") as f:

            for line in f:

                item = json.loads(line)

                self.evidence[item["candidate_id"]] = item["evidence"]

        self.embedder = EmbeddingEngine()

        print()

        print(f"Loaded {self.index.ntotal} vectors.")

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

            candidate_id = info["candidate_id"]

            results.append(
                {
                    "rank": rank,
                    "similarity": round(float(similarity), 4),
                    "candidate": self.cards[candidate_id],
                    "evidence": self.evidence[candidate_id]
                }
            )

        return results