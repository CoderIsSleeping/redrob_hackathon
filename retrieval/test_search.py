from retrieval.search import SemanticSearch

engine = SemanticSearch()

query = """
Backend Engineer

Python

REST API

Docker

AWS

Kafka

Spark
"""

results = engine.search(
    query=query,
    top_k=10
)

print("=" * 90)
print("TOP SEMANTIC MATCHES")
print("=" * 90)

for result in results:

    card = result["candidate"]

    print()

    print(f"Rank        : {result['rank']}")
    print(f"Similarity  : {result['similarity']}")
    print(f"Candidate   : {card['candidate_id']}")
    print(f"Headline    : {card['semantic']['headline']}")
    print(f"Industry    : {card['metadata']['industry']}")
    print(f"Experience  : {card['metadata']['experience_bucket']}")