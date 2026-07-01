from pipeline.run_pipeline import RecruitmentPipeline

JD = """
We are hiring a Backend Engineer.

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

pipeline = RecruitmentPipeline()

results = pipeline.rank_candidates(
    JD,
    top_k=5
)

print()

print("=" * 90)
print("FINAL RANKING")
print("=" * 90)

for rank, result in enumerate(results, start=1):

    report = result["score"]

    print()

    print(f"Rank        : {rank}")

    print(f"Candidate   : {result['candidate_id']}")

    print(f"Headline    : {result['headline']}")

    print(f"Similarity  : {result['similarity']}")

    print(f"Score       : {report.overall_score:.2f}")

    print(f"Decision    : {report.decision}")