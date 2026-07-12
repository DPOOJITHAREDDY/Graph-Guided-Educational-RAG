"""
concept_pipeline.py

Unified concept extraction pipeline.

This module is the single source of truth for generating
high-quality educational concepts from raw text.
"""

from src.knowledge_graph.candidate_extractor import CandidateExtractor
from src.knowledge_graph.concept_normalizer import ConceptNormalizer
from src.knowledge_graph.concept_cleaner import ConceptCleaner
from src.knowledge_graph.concept_scorer import ConceptScorer


class ConceptPipeline:
    """
    Complete concept extraction pipeline.
    """

    def __init__(self):

        self.extractor = CandidateExtractor()

        self.normalizer = ConceptNormalizer()

        self.cleaner = ConceptCleaner()

        self.scorer = ConceptScorer()

    def process(self, text):
        """
        Process raw text into scored educational concepts.

        Returns
        -------
        list[dict]
        """

        candidates = self.extractor.extract(text)

        concepts = []

        seen = set()

        for candidate in candidates:

            concept = self.normalizer.normalize(candidate)

            if not concept:
                continue

            concept = self.cleaner.clean(concept)

            if not concept:
                continue

            result = self.scorer.score(concept)

            if not result["accepted"]:
                continue

            name = result["concept"]

            if name in seen:
                continue

            seen.add(name)

            concepts.append(result)

        return concepts