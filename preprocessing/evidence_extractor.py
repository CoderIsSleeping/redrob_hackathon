"""
Evidence Extraction Module

Extracts recruiter-level capabilities
from candidate semantic information.
"""

from dataclasses import dataclass


@dataclass
class Capability:

    score: float

    evidence: list


class EvidenceExtractor:

    def __init__(self):

        self.capabilities = {

            "backend": [
                "backend",
                "rest api",
                "express",
                "node",
                "jwt",
                "authentication",
                "microservice",
                "flask",
                "django"
            ],

            "data_engineering": [
                "spark",
                "kafka",
                "airflow",
                "etl",
                "data pipeline",
                "dbt",
                "snowflake"
            ],

            "ml": [
                "tensorflow",
                "pytorch",
                "llm",
                "transformer",
                "fine-tuning",
                "rag",
                "embedding",
                "milvus"
            ],

            "cloud": [
                "aws",
                "azure",
                "gcp",
                "cloud"
            ],

            "devops": [
                "docker",
                "kubernetes",
                "jenkins",
                "github actions",
                "ci/cd"
            ],

            "leadership": [
                "led",
                "managed",
                "mentored",
                "owned",
                "owner",
                "team lead"
            ],

            "product": [
                "production",
                "customer",
                "deployed",
                "shipping",
                "release"
            ]
        }

    def extract(self, candidate_card):

        text = " ".join([
            candidate_card["semantic"]["headline"],
            candidate_card["semantic"]["summary"],
            candidate_card["semantic"]["career_text"],
            candidate_card["semantic"]["skills_text"]
        ]).lower()

        results = {}

        for capability, keywords in self.capabilities.items():

            found = []

            for keyword in keywords:

                if keyword in text:
                    found.append(keyword)

            score = len(found) / len(keywords)

            results[capability] = Capability(
                score=round(score, 2),
                evidence=found
            )

        return results