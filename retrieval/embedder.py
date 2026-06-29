"""
Embedding Engine

Uses BAAI/bge-small-en-v1.5
to generate semantic embeddings.
"""

from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingEngine:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        print("Embedding model loaded.")

    def embed(self, text: str):

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding

    def embed_batch(self, texts):

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return np.asarray(embeddings)