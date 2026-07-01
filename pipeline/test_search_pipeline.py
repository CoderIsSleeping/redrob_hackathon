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

for result in candidates:

    card = result["candidate"]

    print()

    print(f"Rank        : {result['rank']}")
    print(f"Similarity  : {result['similarity']}")
    print(f"Candidate   : {card['candidate_id']}")
    print(f"Headline    : {card['semantic']['headline']}")
    print(f"Experience  : {card['metadata']['experience_bucket']}")
    print(f"Industry    : {card['metadata']['industry']}")

    capabilities = []

    for name, value in result["evidence"].items():

        if value["score"] >= 0.20:
            capabilities.append(name)

    print(f"Capabilities: {', '.join(capabilities)}")