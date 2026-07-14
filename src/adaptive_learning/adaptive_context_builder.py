"""
adaptive_context_builder.py

Builds the complete adaptive learning context by combining

1. Query Analysis
2. Semantic Retrieval
3. Knowledge Graph Expansion
4. Student Knowledge State
"""

import re

from src.adaptive_learning.adaptive_context import AdaptiveContext
from src.learning.concept_graph import ConceptGraph
from src.retrieval.retriever import Retriever
from src.student_model.student_state import StudentState


class AdaptiveContextBuilder:
    """
    Creates the unified AdaptiveContext object.
    """

    def __init__(self):

        self.retriever = Retriever()

        self.graph = ConceptGraph()

        self.student_state = StudentState()

    @staticmethod
    def _extract_concepts(text):

        """
        Lightweight concept extraction from retrieved text.

        This is intentionally simple because the
        retrieved concepts are only used for
        reflection and evaluation.
        """

        candidates = set()

        pattern = r"\b[A-Z][A-Za-z0-9]*(?:\s+[A-Z][A-Za-z0-9]*)*\b"

        for match in re.findall(pattern, text):

            match = match.strip()

            if len(match) < 3:
                continue

            candidates.add(match)

        return sorted(candidates)

    def build(
        self,
        subject,
        question,
        query_analysis,
    ):

        if self.graph.graph is None:

            self.graph.load(subject)

        # --------------------------------------------------
        # Retrieval
        # --------------------------------------------------

        retrieval_results = self.retriever.retrieve(

            subject=subject,

            query=question

        )

        # --------------------------------------------------
        # Retrieved Context
        # --------------------------------------------------

        retrieved_context = "\n\n".join(

            result.document.page_content

            for result in retrieval_results

        )

        retrieved_concepts = self._extract_concepts(

            retrieved_context

        )

        # --------------------------------------------------
        # Graph Expansion
        # --------------------------------------------------

        related_concepts = []

        seen = set()

        if query_analysis.requires_graph_expansion:

            for concept in query_analysis.concepts:

                if concept not in self.graph.graph:

                    continue

                for neighbor in self.graph.graph.neighbors(concept):

                    if neighbor in seen:

                        continue

                    seen.add(neighbor)

                    related_concepts.append(neighbor)

        # --------------------------------------------------
        # Student Profiles
        # --------------------------------------------------

        student_profiles = []

        for concept in query_analysis.concepts:

            student_profiles.append(

                self.student_state.get_profile(

                    concept

                )

            )

        # --------------------------------------------------
        # Build Adaptive Context
        # --------------------------------------------------

        return AdaptiveContext(

            question=question,

            query_analysis=query_analysis,

            retrieval_results=retrieval_results,

            retrieved_context=retrieved_context,

            retrieved_concepts=retrieved_concepts,

            related_concepts=related_concepts,

            student_profiles=student_profiles

        )