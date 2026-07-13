"""
adaptive_context.py

Data model representing the complete adaptive learning context
that will be passed to the Prompt Constructor.
"""

from dataclasses import dataclass, field

from src.models.retrieval_result import RetrievalResult
from src.student_model.student_profile import StudentProfile


@dataclass
class AdaptiveContext:
    """
    Unified context object for adaptive learning.

    This object combines:
    - Query analysis
    - Retrieved knowledge
    - Graph expansion
    - Student knowledge state
    """

    question: str

    query_analysis: object

    retrieval_results: list[RetrievalResult] = field(
        default_factory=list
    )

    related_concepts: list[str] = field(
        default_factory=list
    )

    student_profiles: list[StudentProfile] = field(
        default_factory=list
    )