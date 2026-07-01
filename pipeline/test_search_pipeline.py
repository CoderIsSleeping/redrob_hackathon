from pipeline.search_pipeline import SearchPipeline


JD = """
We are looking for a Backend Engineer.

Requirements

Python

REST APIs

Docker

AWS

Kafka

Spark

Minimum 3 years experience.

Excellent communication skills.
"""


pipeline = SearchPipeline()

rubric, candidates = pipeline.search(
    JD,
    top_k=10
)

print("=" * 90)
print("TOP RETRIEVED CANDIDATES")
print("=" * 90)

for candidate in candidates:

    card = candidate["candidate"]

    print()

    print(f"Rank        : {candidate['rank']}")
    print(f"Similarity  : {candidate['similarity']}")
    print(f"Candidate   : {card['candidate_id']}")
    print(f"Headline    : {card['semantic']['headline']}")
    print(f"Experience  : {card['metadata']['experience_bucket']}")
    print(f"Industry    : {card['metadata']['industry']}")