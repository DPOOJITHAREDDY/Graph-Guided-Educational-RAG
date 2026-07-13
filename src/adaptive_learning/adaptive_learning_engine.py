"""
adaptive_learning_engine.py

Main orchestration engine for the adaptive educational RAG system.
"""

from src.adaptive_learning.query_analyzer import QueryAnalyzer
from src.adaptive_learning.adaptive_context_builder import (
    AdaptiveContextBuilder,
)
from src.adaptive_learning.prompt_constructor import (
    PromptConstructor,
)
from src.adaptive_learning.reflection_engine import (
    ReflectionEngine,
)
from src.adaptive_learning.learning_update_engine import (
    LearningUpdateEngine,
)
from src.learning.concept_graph import ConceptGraph
from src.llm.llm_factory import LLMFactory


class AdaptiveLearningEngine:
    """
    Complete adaptive learning pipeline.

    Pipeline:

    Question
        ↓
    Query Analyzer
        ↓
    Adaptive Context Builder
        ↓
    Prompt Constructor
        ↓
    Gemini
        ↓
    Reflection Engine
        ↓
    Learning Update Engine
    """

    def __init__(self, subject):

        self.subject = subject

        # -----------------------------
        # Load Knowledge Graph
        # -----------------------------

        concept_graph = ConceptGraph()

        concept_graph.load(subject)

        vocabulary = list(
            concept_graph.graph.nodes()
        )

        # -----------------------------
        # Initialize Modules
        # -----------------------------

        self.query_analyzer = QueryAnalyzer(
            vocabulary
        )

        self.context_builder = (
            AdaptiveContextBuilder()
        )

        self.prompt_constructor = (
            PromptConstructor()
        )

        self.reflection_engine = (
            ReflectionEngine()
        )

        self.learning_update_engine = (
            LearningUpdateEngine()
        )

        # -----------------------------
        # Gemini Model
        # -----------------------------

        self.model = (
            LLMFactory()
            .get_model()
        )

    def answer_question(
        self,
        question
    ):

        # -----------------------------
        # Analyze Question
        # -----------------------------

        query_analysis = (
            self.query_analyzer.analyze(
                question
            )
        )

        # -----------------------------
        # Build Adaptive Context
        # -----------------------------

        adaptive_context = (
            self.context_builder.build(
                subject=self.subject,
                question=question,
                query_analysis=query_analysis
            )
        )

        # -----------------------------
        # Build Prompt
        # -----------------------------

        prompt = (
            self.prompt_constructor.build(
                adaptive_context
            )
        )

        # -----------------------------
        # Gemini Response
        # -----------------------------

        response = (
            self.model.generate_content(
                prompt
            )
        )

        answer = response.text

        # -----------------------------
        # Reflection
        # -----------------------------

        reflection = (
            self.reflection_engine.reflect(
                answer,
                adaptive_context
            )
        )

        # -----------------------------
        # Update Student Model
        # -----------------------------

        profiles = (
            self.learning_update_engine.update(
                adaptive_context,
                reflection
            )
        )

        return {

            "answer": answer,

            "reflection": reflection,

            "profiles": profiles,

            "context": adaptive_context

        }