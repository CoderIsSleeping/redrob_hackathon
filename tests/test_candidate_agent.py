import json

from agents.candidate_agent import CandidateAgent
from preprocessing.evidence_extractor import EvidenceExtractor


with open(
    "data/processed/candidate_cards.jsonl",
    "r",
    encoding="utf-8",
) as f:

    card = json.loads(next(f))


extractor = EvidenceExtractor()

evidence = extractor.extract(card)

agent = CandidateAgent()

report = agent.analyse(card, evidence)

print("=" * 60)
print("PROFILE")
print("=" * 60)

print(report.candidate_profile)

print()

print("=" * 60)
print("CAPABILITIES")
print("=" * 60)

for capability in report.capabilities:

    print(capability)

    print()

print("=" * 60)
print("STRENGTHS")
print("=" * 60)

for strength in report.strengths:

    print("-", strength)

print()

print("=" * 60)
print("RISKS")
print("=" * 60)

for risk in report.risks:

    print("-", risk)

print()

print("=" * 60)
print("GROWTH")
print("=" * 60)

print(report.growth_potential)

print()

print("=" * 60)
print("CONSISTENCY")
print("=" * 60)

print(report.consistency_analysis)

print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(report.summary)