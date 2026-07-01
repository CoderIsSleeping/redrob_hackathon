"""
AI Recruitment API
"""

from fastapi import FastAPI
from pydantic import BaseModel

from pipeline.recruitment_pipeline import RecruitmentPipeline


app = FastAPI(
    title="Redrob AI Recruitment API",
    version="1.0"
)

pipeline = RecruitmentPipeline()


class JDRequest(BaseModel):
    job_description: str
    top_k: int = 10


@app.get("/")
def home():

    return {
        "message": "AI Recruitment API Running"
    }


@app.post("/rank")
def rank_candidates(request: JDRequest):

    rubric, results = pipeline.run(
        request.job_description,
        top_k=request.top_k
    )

    response = []

    for rank, candidate in enumerate(results, start=1):

        score = candidate["ranking"]

        response.append({

            "rank": rank,

            "candidate_id": candidate["candidate_id"],

            "headline": candidate["headline"],

            "experience": candidate["experience"],

            "industry": candidate["industry"],

            "similarity": candidate["similarity"],

            "overall_score": score["overall_score"],

            "decision": score["decision"]

        })

    return {

        "role": rubric.role,

        "search_query": rubric.search_query,

        "summary": rubric.summary,

        "results": response

    }