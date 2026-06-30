"""
Build Embedding Dataset

Reads all Candidate Cards,
creates retrieval documents,
generates embeddings,
and saves them to disk.
"""

import json
import numpy as np
from pathlib import Path

from retrieval.embedder import EmbeddingEngine
from retrieval.retrieval_text import RetrievalTextGenerator


INPUT_FILE = Path("data/processed/candidate_cards.jsonl")

OUTPUT_EMBEDDINGS = Path(
    "data/processed/candidate_embeddings.npy"
)

OUTPUT_IDS = Path(
    "data/processed/candidate_ids.json"
)


def main():

    generator = RetrievalTextGenerator()

    engine = EmbeddingEngine()

    texts = []

    metadata = []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            card = json.loads(line)

            texts.append(
                generator.generate(card)
            )

            metadata.append(
                {
                    "candidate_id": card["candidate_id"],
                    "experience_bucket": card["metadata"][
                        "experience_bucket"
                    ]
                }
            )

    print(f"Loaded {len(texts)} candidates")

    embeddings = engine.embed_batch(texts)

    np.save(
        OUTPUT_EMBEDDINGS,
        embeddings
    )

    with open(
        OUTPUT_IDS,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=2
        )

    print()

    print("=" * 60)

    print("Embedding Dataset Built")

    print("=" * 60)

    print()

    print("Embeddings Shape :", embeddings.shape)

    print("Metadata Saved   :", len(metadata))


if __name__ == "__main__":
    main()