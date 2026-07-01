"""
End-to-End AI Recruitment Pipeline

JD
 ↓
JD Agent
 ↓
Semantic Search
 ↓
Candidate Agent
 ↓
Ranking Agent
 ↓
Final Ranking
"""
import time
from agents.jd_agents import JDAgent
from agents.candidate_agent import CandidateAgent
from agents.ranking_agent import RankingAgent
from retrieval.search import SemanticSearch


class RecruitmentPipeline:

    def __init__(self):

        print("=" * 70)
        print("INITIALIZING AI RECRUITMENT PIPELINE")
        print("=" * 70)

        self.jd_agent = JDAgent()

        self.search = SemanticSearch()

        self.candidate_agent = CandidateAgent()

        self.ranking_agent = RankingAgent()

        print("\nPipeline Ready.\n")

    def run(self, job_description, top_k=100):

        start=time.perf_counter()

        print("=" * 70)
        print("STEP 1 : JD AGENT")
        print("=" * 70)

        rubric = self.jd_agent.analyse(job_description)

        print("Role :", rubric.role)
        print("Search Query :", rubric.search_query)

        print()

        print("=" * 70)
        print("STEP 2 : SEMANTIC SEARCH")
        print("=" * 70)

        retrieved = self.search.search(
            rubric.search_query,
            top_k=top_k
        )

        print(f"Retrieved {len(retrieved)} candidates.\n")

        print("=" * 70)
        print("STEP 3 : CANDIDATE ANALYSIS + RANKING")
        print("=" * 70)

        final_results = []

        for index, result in enumerate(retrieved, start=1):

            card = result["candidate"]

            evidence = result["evidence"]

            try:

                report = self.candidate_agent.analyse(
                    card,
                    evidence
                )

                score = self.ranking_agent.calculate_score(
                    rubric,
                    report,
                    card["behavior"]
                )

            except Exception as e:

                print(
                    f"[{index}/{len(retrieved)}] "
                    f"{card['candidate_id']} FAILED -> {e}"
                )

                continue

            final_results.append({

                "candidate_id": card["candidate_id"],

                "headline": card["semantic"]["headline"],

                "experience": card["metadata"]["experience_bucket"],

                "industry": card["metadata"]["industry"],

                "similarity": result["similarity"],

                "report": report,

                "ranking": score
            })

            print(
                f"[{index}/{len(retrieved)}] "
                f"{card['candidate_id']} "
                f"{score['decision']} "
                f"({score['overall_score']}%)"
            )

        search_end=time.perf_counter()

        print(
            f"semantic search : "
            f"{search_end-start:.2f} sec" 
        )

        final_results.sort(

            key=lambda x: x["ranking"]["overall_score"],

            reverse=True

        )

        end = time.perf_counter()

        print()

        print("=" * 70)
        print("PERFORMANCE")
        print("=" * 70)

        print(
            f"Total Time : {end-start:.2f} sec"
        )

        return rubric, final_results