"""
Ranking Intelligence Engine V3

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
        partial = []
        missing = []

        capability_breakdown = {}

        candidate_capabilities = {
            capability.name: capability
            for capability in report.capabilities
        }

        # ======================================================
        # REQUIRED CAPABILITIES
        # ======================================================

        for capability in rubric.required_capabilities:

            name = capability.name
            importance = capability.importance

            maximum += importance

            if name in candidate_capabilities:

                candidate = candidate_capabilities[name]

                multiplier = LEVEL_SCORE.get(
                    candidate.level,
                    0
                )

                score = importance * multiplier

                obtained += score

                if multiplier >= 0.80:
                    matched.append(name)

                elif multiplier > 0:
                    partial.append(name)

                else:
                    missing.append(name)

                capability_breakdown[name] = {

                    "type": "Required",

                    "score": round(score, 2),

                    "importance": importance,

                    "level": candidate.level,

                    "percentage": round(
                        multiplier * 100,
                        1
                    )
                }

            else:

                missing.append(name)

                capability_breakdown[name] = {

                    "type": "Required",

                    "score": 0,

                    "importance": importance,

                    "level": "Missing",

                    "percentage": 0
                }

        # ======================================================
        # PREFERRED CAPABILITIES
        # (Worth 50% of Required)
        # ======================================================

        for capability in rubric.preferred_capabilities:

            name = capability.name
            importance = capability.importance

            maximum += importance * 0.5

            if name in candidate_capabilities:

                candidate = candidate_capabilities[name]

                multiplier = LEVEL_SCORE.get(
                    candidate.level,
                    0
                )

                score = (
                    importance
                    * 0.5
                    * multiplier
                )

                obtained += score

                capability_breakdown[name] = {

                    "type": "Preferred",

                    "score": round(score, 2),

                    "importance": importance,

                    "level": candidate.level,

                    "percentage": round(
                        multiplier * 100,
                        1
                    )
                }

            else:

                capability_breakdown[name] = {

                    "type": "Preferred",

                    "score": 0,

                    "importance": importance,

                    "level": "Missing",

                    "percentage": 0
                }

        # ======================================================
        # BONUSES
        # ======================================================

        growth_bonus = GROWTH_SCORE.get(
            report.growth_potential.level,
            0
        )

        consistency_bonus = CONSISTENCY_SCORE.get(
            report.consistency_analysis.status,
            0
        )

        availability_bonus = (
            behavior["availability_score"] * 5
        )

        obtained += (
            growth_bonus
            + consistency_bonus
            + availability_bonus
        )

        maximum += 15

        overall = round(
            (obtained / maximum) * 100,
            2
        )

        # ======================================================
        # DECISION
        # ======================================================

        if overall >= 90:

            decision = "Excellent Match"

        elif overall >= 80:

            decision = "Strong Match"

        elif overall >= 70:

            decision = "Good Match"

        elif overall >= 55:

            decision = "Potential Match"

        else:

            decision = "Weak Match"

        return {

            "overall_score": overall,

            "decision": decision,

            "obtained_score": round(
                obtained,
                2
            ),

            "maximum_score": round(
                maximum,
                2
            ),

            "matched_capabilities": matched,

            "partial_matches": partial,

            "missing_capabilities": missing,

            "capability_breakdown": capability_breakdown,

            "strengths": report.strengths,

            "risks": report.risks,

            "growth": report.growth_potential,

            "consistency": report.consistency_analysis
        }