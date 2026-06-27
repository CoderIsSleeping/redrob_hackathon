"""
Candidate Intelligence Card Builder

Converts raw candidate JSON into
a structured format used by all
AI intelligence layers.
"""

from preprocessing.feature_engineering import (
    calculate_notice_score,
    calculate_availability_score,
    get_experience_bucket,
    has_github_profile,
    normalize_github_score
)

def build_skills_text(skills):
    return ", ".join(skill["name"] for skill in skills)

def build_career_text(career_history):

    sections = []

    for job in career_history:

        text = (
            f"{job['title']} at {job['company']}. "
            f"{job['description']}"
        )

        sections.append(text)

    return "\n\n".join(sections)

def build_candidate_card(candidate):
    """
    Build a structured intelligence card
    for one candidate.
    """

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    notice_score = calculate_notice_score(
        signals["notice_period_days"]
    )

    github_score = normalize_github_score(
        signals["github_activity_score"]
    )

    availability = calculate_availability_score(
        signals["open_to_work_flag"],
        notice_score
    )

    card = {

        "candidate_id": candidate["candidate_id"],

        "semantic": {

            "headline": profile["headline"],

            "summary": profile["summary"],

            "skills_text": build_skills_text(candidate["skills"]),

            "career_text": build_career_text(candidate["career_history"])

        },

        "behavior": {

            "notice_score": notice_score,

            "availability_score": availability,

            "github_score": github_score,

            "has_github": has_github_profile(
                signals["github_activity_score"]
            ),

            "response_rate":
                signals["recruiter_response_rate"]

        },

        "metadata": {

            "experience_bucket":
                get_experience_bucket(
                    profile["years_of_experience"]
                ),

            "industry":
                profile["current_industry"],

            "company_size":
                profile["current_company_size"]

        }

    }

    return card



if __name__ == "__main__":
    import json
    from pathlib import Path

    DATA_PATH = Path("data/raw/candidates.jsonl")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        first_candidate = json.loads(next(f))

    card = build_candidate_card(first_candidate)

    from pprint import pprint

    pprint(card)