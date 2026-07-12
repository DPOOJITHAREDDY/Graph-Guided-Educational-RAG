"""
concept_extractor_v3.py

Final Concept Extraction Pipeline (V3)

Pipeline:

Candidate Extraction
        ↓
Normalization
        ↓
Cleaning
        ↓
Scoring
        ↓
Accepted Concepts
"""

from src.knowledge_graph.candidate_extractor import CandidateExtractor
from src.knowledge_graph.concept_normalizer import ConceptNormalizer
from src.knowledge_graph.concept_cleaner import ConceptCleaner
from src.knowledge_graph.concept_scorer import ConceptScorer


class ConceptExtractorV3:

    def __init__(self):

        self.candidate_extractor = CandidateExtractor()
        self.normalizer = ConceptNormalizer()
        self.cleaner = ConceptCleaner()
        self.scorer = ConceptScorer()

    def extract(self, text):

        candidates = self.candidate_extractor.extract(text)

        accepted = []
        seen = set()

        for candidate in candidates:

            # Step 1: Normalize
            concept = self.normalizer.normalize(candidate)

            if not concept:
                continue

            # Step 2: Clean
            concept = self.cleaner.clean(concept)

            if not concept:
                continue

            # Step 3: Score
            result = self.scorer.score(concept)

            if result["accepted"]:

                if concept not in seen:

                    accepted.append(concept)
                    seen.add(concept)

        return sorted(accepted)