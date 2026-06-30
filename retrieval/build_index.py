"""
Build FAISS Index

Loads precomputed embeddings
and builds a searchable FAISS index.
"""

from pathlib import Path

import faiss
import numpy as np


EMBEDDINGS_PATH = Path(
    "data/processed/candidate_embeddings.npy"
)

INDEX_PATH = Path(
    "data/processed/faiss.index"
)


def main():

    print("=" * 60)
    print("LOADING EMBEDDINGS")
    print("=" * 60)

    embeddings = np.load(EMBEDDINGS_PATH)

    print(f"Shape : {embeddings.shape}")

    dimension = embeddings.shape[1]

    print()
    print("Creating IndexFlatIP...")

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    print("Vectors Indexed :", index.ntotal)

    faiss.write_index(
        index,
        str(INDEX_PATH)
    )

    print()

    print("=" * 60)
    print("FAISS INDEX BUILT SUCCESSFULLY")
    print("=" * 60)

    print()

    print(f"Embedding Dimension : {dimension}")
    print(f"Total Candidates    : {index.ntotal}")

    print()

    print(f"Saved Index -> {INDEX_PATH}")


if __name__ == "__main__":
    main()