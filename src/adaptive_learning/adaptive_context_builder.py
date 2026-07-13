"""
adaptive_context_builder.py

Builds the complete adaptive learning context by combining

1. Query Analysis
2. Semantic Retrieval
3. Knowledge Graph Expansion
4. Student Knowledge State
"""

from src.adaptive_learning.adaptive_context import AdaptiveContext
from src.learning.concept_graph import ConceptGraph
from src.retrieval.retriever import Retriever
from src.student_model.student_state import StudentState


class AdaptiveContextBuilder:
    """
    Creates the unified AdaptiveContext object that is passed
    to the Prompt Constructor.
    """

    def __init__(self):

        self.retriever = Retriever()

        self.graph = ConceptGraph()

        self.student_state = StudentState()

    def build(
        self,
        subject,
        question,
        query_analysis,
    ):
        """
        Build the adaptive learning context.
        """

        # --------------------------------------------------
        # Load graph
        # --------------------------------------------------

        if self.graph.graph is None:
            self.graph.load(subject)

        # --------------------------------------------------
        # Semantic Retrieval
        # --------------------------------------------------

        retrieval_results = self.retriever.retrieve(
            subject=subject,
            query=question
        )

        # --------------------------------------------------
        # Graph Expansion
        # --------------------------------------------------

        related_concepts = []

        if query_analysis.requires_graph_expansion:

            seen = set()

            for concept in query_analysis.concepts:

                if not self.graph.has_concept(concept):
                    continue

                neighbors = self.graph.get_learning_neighbors(
                    concept
                )

                for neighbor, weight in neighbors:

                    if neighbor not in seen:

                        seen.add(neighbor)

                        related_concepts.append(
                            neighbor
                        )

        # --------------------------------------------------
        # Student Profiles
        # --------------------------------------------------

        student_profiles = []

        for concept in query_analysis.concepts:

            profile = self.student_state.get_profile(
                concept
            )

            student_profiles.append(
                profile
            )

        # --------------------------------------------------
        # Build Adaptive Context
        # --------------------------------------------------

        context = AdaptiveContext(

            question=question,

            query_analysis=query_analysis,

            retrieval_results=retrieval_results,

            related_concepts=related_concepts,

            student_profiles=student_profiles

        )

        return context