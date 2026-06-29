import json

from agents.candidate_agent import CandidateAgent
from agents.jd_agents import JDAgent
from agents.ranking_agent import RankingAgent
from preprocessing.evidence_extractor import EvidenceExtractor

# Load Candidate Card
with open(
    "data/processed/candidate_cards.jsonl",
    "r",
    encoding="utf-8"
) as f:

    card = json.loads(next(f))

# Sample Job Description
jd = """
We are looking for a Backend Engineer.

Requirements

- Python
- REST APIs
- AWS
- Docker
- Production systems

Nice to Have

- Kafka
- Spark

Must have excellent communication skills.
"""

# Build all reports
jd_agent = JDAgent()
rubric = jd_agent.analyse(jd)

extractor = EvidenceExtractor()
evidence = extractor.extract(card)

candidate_agent = CandidateAgent()
report = candidate_agent.analyse(card, evidence)

ranking = RankingAgent()

result = ranking.calculate_score(
    rubric,
    report,
    card["behavior"]
)

print("=" * 70)
print("FINAL AI RECRUITMENT REPORT")
print("=" * 70)

print()

print("Overall Score :", result["overall_score"], "%")
print("Decision      :", result["decision"])

print()

print("Obtained Score :", result["obtained_score"])
print("Maximum Score  :", result["maximum_score"])

print()

print("=" * 70)
print("MATCHED CAPABILITIES")
print("=" * 70)

for capability in result["matched_capabilities"]:
    print("✓", capability)

print()

print("=" * 70)
print("PARTIAL MATCHES")
print("=" * 70)

for capability in result["partial_matches"]:
    print("◐", capability)

print()

print("=" * 70)
print("MISSING CAPABILITIES")
print("=" * 70)

for capability in result["missing_capabilities"]:
    print("✗", capability)

print()

print("=" * 70)
print("CAPABILITY BREAKDOWN")
print("=" * 70)

for capability, info in result["capability_breakdown"].items():

    print(capability)
    print(info)
    print()

print("=" * 70)
print("STRENGTHS")
print("=" * 70)

for strength in result["strengths"]:
    print("✓", strength)

print()

print("=" * 70)
print("RISKS")
print("=" * 70)

for risk in result["risks"]:
    print("⚠", risk)

print()

print("=" * 70)
print("GROWTH POTENTIAL")
print("=" * 70)

print(result["growth"])

print()

print("=" * 70)
print("CONSISTENCY")
print("=" * 70)

print(result["consistency"])