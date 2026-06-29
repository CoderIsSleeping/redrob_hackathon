"""
Retrieval Text Generator

Creates an embedding-friendly document
for semantic search.
"""

from preprocessing.evidence_extractor import EvidenceExtractor


class RetrievalTextGenerator:

    def __init__(self):

        self.extractor = EvidenceExtractor()

    def generate(self, card):

        semantic = card["semantic"]

        metadata = card["metadata"]

        evidence = self.extractor.extract(card)

        capabilities = []

        for capability, info in evidence.items():

            if info.score >= 0.20:

                capabilities.append(
                    capability.replace("_", " ")
                )

        retrieval_text = f"""
Role
{semantic.get("headline","")}

Experience
{metadata.get("experience_bucket","")}

Professional Summary
{semantic.get("summary","")}

Career History
{semantic.get("career_text","")}

Core Capabilities
{", ".join(capabilities)}
"""

        return retrieval_text.strip()