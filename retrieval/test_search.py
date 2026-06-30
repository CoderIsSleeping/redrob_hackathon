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

results = engine.search(query=query, top_k=10)

print("=" * 90)
print("TOP SEMANTIC MATCHES")
print("=" * 90)

for candidate in results:

    print()

    print(f"Rank        : {candidate['rank']}")
    print(f"Candidate   : {candidate['candidate_id']}")
    print(f"Headline    : {candidate['headline']}")
    print(f"Experience  : {candidate['experience']}")
    print(f"Industry    : {candidate['industry']}")
    print(f"Similarity  : {candidate['similarity']}")