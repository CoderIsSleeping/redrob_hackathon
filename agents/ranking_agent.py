"""
Ranking Intelligence Engine

Combines recruiter requirements with
candidate intelligence to produce
an explainable score.
"""

LEVEL_SCORE = {
    "Production": 1.00,
    "Professional": 0.90,
    "Academic": 0.60,
    "Personal Projects": 0.45,
    "Learning": 0.30
}

GROWTH_SCORE = {
    "High": 5,
    "Medium": 3,
    "Low": 0
}

CONSISTENCY_SCORE = {
    "High": 5,
    "Medium": 2,
    "Low": 0
}


class RankingAgent:

    def __init__(self):
        pass

    def calculate_score(
        self,
        rubric,
        report,
        behavior
    ):

        capability_score = 0

        breakdown = {}

        candidate_capabilities = {
            c.name: c
            for c in report.capabilities
        }

        for capability in rubric.required_capabilities:

            name = capability.name

            importance = capability.importance

            if name in candidate_capabilities:

                level = candidate_capabilities[name].level

                multiplier = LEVEL_SCORE.get(level, 0)

                score = importance * multiplier

            else:

                score = 0

            breakdown[name] = round(score, 2)

            capability_score += score

        growth_bonus = GROWTH_SCORE[
            report.growth_potential.level
        ]

        consistency_bonus = CONSISTENCY_SCORE[
            report.consistency_analysis.status
        ]

        availability_bonus = (
            behavior["availability_score"] * 5
        )

        overall = (
            capability_score
            + growth_bonus
            + consistency_bonus
            + availability_bonus
        )

        if overall >= 90:
            decision = "Excellent Match"

        elif overall >= 80:
            decision = "Strong Match"

        elif overall >= 65:
            decision = "Good Match"

        elif overall >= 50:
            decision = "Potential Match"

        else:
            decision = "Weak Match"

        return {

            "overall_score": round(overall, 2),

            "decision": decision,

            "capability_breakdown": breakdown,

            "growth_bonus": growth_bonus,

            "consistency_bonus": consistency_bonus,

            "availability_bonus": round(
                availability_bonus,
                2
            )
        }