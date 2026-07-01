"""
End-to-End Recruitment Pipeline

JD
 ↓
JD Agent
 ↓
Semantic Search
 ↓
Evidence
 ↓
Candidate Agent
 ↓
Ranking Engine
"""

import json
from pathlib import Path

from agents.jd_agents import JDAgent
from agents.candidate_agent import CandidateAgent

from retrieval.search import SemanticSearch

from preprocessing.evidence_extractor import EvidenceExtractor

from agents.ranking_agent import RankingAgent


CARDS = Path("data/processed/candidate_cards.jsonl")
EVIDENCE = Path("data/processed/candidate_evidence.jsonl")


class RecruitmentPipeline:

    def __init__(self):

        print("Initializing Recruitment Pipeline...\n")

        self.jd_agent = JDAgent()

        self.search_engine = SemanticSearch()

        self.extractor = EvidenceExtractor()

        self.candidate_agent = CandidateAgent()

        self.ranker = RankingAgent()

        print("\nPipeline Ready.\n")

    def rank_candidates(self, jd: str, top_k: int = 100):

        print("=" * 70)
        print("STEP 1 : JD AGENT")
        print("=" * 70)

        rubric = self.jd_agent.analyse(jd)

        print("Role :", rubric.role)
        print("Search Query :", rubric.search_query)

        print()

        print("=" * 70)
        print("STEP 2 : SEMANTIC SEARCH")
        print("=" * 70)

        candidates = self.search_engine.search(
            rubric.search_query,
            top_k=top_k
        )

        print(f"Retrieved {len(candidates)} candidates.\n")

        results = []

        for i, item in enumerate(candidates, start=1):

            card = item["candidate"]

            evidence = self.extractor.extract(card)

            report = self.candidate_agent.analyse(
                card,
                evidence
            )

            score = self.ranker.rank(
                rubric,
                report,
                card["behavior"]
            )

            results.append(
                {
                    "candidate_id": card["candidate_id"],
                    "headline": card["semantic"]["headline"],
                    "similarity": item["similarity"],
                    "score": score
                }
            )

            print(
                f"[{i}/{len(candidates)}] "
                f"{card['candidate_id']} "
                f"Done"
            )

        results.sort(
            key=lambda x: x["score"].overall_score,
            reverse=True
        )

        return results