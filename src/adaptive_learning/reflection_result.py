"""
reflection_result.py

Data model representing the educational reflection
generated after the LLM produces an answer.
"""

from dataclasses import dataclass, field


@dataclass
class ReflectionResult:
    """
    Stores the evaluation of an educational response.
    """

    # --------------------------------------------------
    # Overall Scores
    # --------------------------------------------------

    understanding_score: float

    confidence_score: float

    coverage_score: float

    grounding_score: float

    difficulty_alignment_score: float

    overall_score: float

    # --------------------------------------------------
    # Concept Analysis
    # --------------------------------------------------

    strengths: list[str] = field(
        default_factory=list
    )

    weak_concepts: list[str] = field(
        default_factory=list
    )

    covered_concepts: list[str] = field(
        default_factory=list
    )

    missing_concepts: list[str] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Quality Analysis
    # --------------------------------------------------

    detected_misconceptions: list[str] = field(
        default_factory=list
    )

    unsupported_claims: list[str] = field(
        default_factory=list
    )

    uncertainty_phrases: list[str] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Recommendations
    # --------------------------------------------------

    recommended_review: list[str] = field(
        default_factory=list
    )

    next_learning_topics: list[str] = field(
        default_factory=list
    )

    feedback: str = ""

    should_review: bool = False