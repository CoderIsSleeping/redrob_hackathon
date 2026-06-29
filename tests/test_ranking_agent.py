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

print("=" * 60)
print("FINAL RANK")
print("=" * 60)

for k, v in result.items():
    print(k, ":", v)