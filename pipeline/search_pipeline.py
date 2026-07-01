"""
Search Pipeline

JD
 ↓
JD Agent
 ↓
Semantic Search
 ↓
Top K Candidate Cards
"""

from agents.jd_agents import JDAgent
from retrieval.search import SemanticSearch


class SearchPipeline:

    def __init__(self):

        print("Initializing Search Pipeline...")

        self.jd_agent = JDAgent()

        self.search_engine = SemanticSearch()

        print("Search Pipeline Ready.\n")

    def search(self, job_description, top_k=100):

        print("=" * 70)
        print("STEP 1 : JD AGENT")
        print("=" * 70)

        rubric = self.jd_agent.analyse(job_description)

        print(f"Role : {rubric.role}")
        print(f"Search Query : {rubric.search_query}")

        print()

        print("=" * 70)
        print("STEP 2 : SEMANTIC SEARCH")
        print("=" * 70)

        candidates = self.search_engine.search(
            rubric.search_query,
            top_k=top_k
        )

        print(f"Retrieved {len(candidates)} candidates.\n")

        return rubric, candidates