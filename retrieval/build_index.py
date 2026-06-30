"""
Build FAISS Index

Loads precomputed embeddings
and creates a FAISS index.
"""

from pathlib import Path

import faiss
import numpy as np


EMBEDDINGS = Path(
    "data/processed/candidate_embeddings.npy"
)

OUTPUT_INDEX = Path(
    "data/processed/faiss.index"
)


def main():

    print("Loading embeddings...")

    embeddings = np.load(EMBEDDINGS)

    print("Embeddings Shape:", embeddings.shape)

    dimension = embeddings.shape[1]

    print("Creating FAISS Index...")

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    print("Indexed vectors:", index.ntotal)

    faiss.write_index(
        index,
        str(OUTPUT_INDEX)
    )

    print()

    print("=" * 60)
    print("FAISS INDEX CREATED")
    print("=" * 60)
    print()

    print("Dimension :", dimension)
    print("Total Vectors :", index.ntotal)


if __name__ == "__main__":
    main()