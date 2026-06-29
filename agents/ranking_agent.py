"""
Ranking Intelligence Engine V2

Produces an explainable normalized score.
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

    def calculate_score(self, rubric, report, behavior):

        obtained = 0
        maximum = 0

        matched = []
        missing = []

        capability_breakdown = {}

        candidate_capabilities = {
            capability.name: capability
            for capability in report.capabilities
        }

        # -------------------------------
        # Required Capabilities
        # -------------------------------

        for required in rubric.required_capabilities:

            maximum += required.importance

            if required.name in candidate_capabilities:

                candidate = candidate_capabilities[required.name]

                multiplier = LEVEL_SCORE.get(candidate.level, 0)

                score = required.importance * multiplier

                obtained += score

                matched.append(required.name)

                capability_breakdown[required.name] = {
                    "score": round(score, 2),
                    "importance": required.importance,
                    "level": candidate.level
                }

            else:

                missing.append(required.name)

                capability_breakdown[required.name] = {
                    "score": 0,
                    "importance": required.importance,
                    "level": "Missing"
                }

        # -------------------------------
        # Bonuses
        # -------------------------------

        growth_bonus = GROWTH_SCORE[
            report.growth_potential.level
        ]

        consistency_bonus = CONSISTENCY_SCORE[
            report.consistency_analysis.status
        ]

        availability_bonus = (
            behavior["availability_score"] * 5
        )

        obtained += (
            growth_bonus
            + consistency_bonus
            + availability_bonus
        )

        maximum += 15

        overall = (obtained / maximum) * 100

        overall = round(overall, 2)

        # -------------------------------
        # Decision
        # -------------------------------

        if overall >= 95:

            decision = "Excellent Match"

        elif overall >= 90:

            decision = "Strong Match"

        elif overall >= 75:

            decision = "Good Match"

        elif overall >= 60:

            decision = "Potential Match"

        else:

            decision = "Weak Match"

        return {

            "overall_score": overall,

            "decision": decision,

            "obtained_score": round(obtained, 2),

            "maximum_score": maximum,

            "matched_capabilities": matched,

            "missing_capabilities": missing,

            "capability_breakdown": capability_breakdown,

            "strengths": report.strengths,

            "risks": report.risks,

            "growth": report.growth_potential,

            "consistency": report.consistency_analysis
        }