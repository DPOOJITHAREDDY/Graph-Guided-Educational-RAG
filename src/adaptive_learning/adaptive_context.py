"""
adaptive_context.py

Data model representing the complete adaptive learning context
passed throughout the adaptive educational pipeline.
"""

from dataclasses import dataclass, field

from src.models.retrieval_result import RetrievalResult
from src.student_model.student_profile import StudentProfile


@dataclass
class AdaptiveContext:
    """
    Unified context shared across the adaptive learning pipeline.

    This object contains everything required for:

    - Prompt construction
    - Reflection
    - Student modelling
    - Adaptive tutoring
    """

    # --------------------------------------------------
    # Original Question
    # --------------------------------------------------

    question: str

    # --------------------------------------------------
    # Query Analysis
    # --------------------------------------------------

    query_analysis: object

    # --------------------------------------------------
    # Retrieval
    # --------------------------------------------------

    retrieval_results: list[RetrievalResult] = field(
        default_factory=list
    )

    # Plain text extracted from retrieved chunks.
    # Used by Prompt Builder and Reflection Engine.
    retrieved_context: str = ""

    # Concepts detected from retrieved documents.
    # Allows Reflection to compare expected concepts
    # with generated explanations.
    retrieved_concepts: list[str] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Knowledge Graph
    # --------------------------------------------------

    related_concepts: list[str] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Student Model
    # --------------------------------------------------

    student_profiles: list[StudentProfile] = field(
        default_factory=list
    )