from pipeline.recruitment_pipeline import RecruitmentPipeline

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

rubric, results = pipeline.run(

    JD,

    top_k=5

)

print()

print("=" * 90)
print("FINAL RANKING")
print("=" * 90)

for rank, result in enumerate(results, start=1):

    score = result["ranking"]

    print()

    print(f"Rank        : {rank}")

    print(f"Candidate   : {result['candidate_id']}")

    print(f"Headline    : {result['headline']}")

    print(f"Similarity  : {result['similarity']}")

    print(f"Score       : {score['overall_score']}")

    print(f"Decision    : {score['decision']}")