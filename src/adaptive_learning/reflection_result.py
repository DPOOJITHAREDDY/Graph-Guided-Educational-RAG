"""
reflection_result.py

Data model representing the reflection produced after
an LLM response.
"""

from dataclasses import dataclass, field


@dataclass
class ReflectionResult:
    """
    Stores the educational reflection generated after an answer.
    """

    understanding_score: float

    confidence_score: float

    detected_misconceptions: list[str] = field(
        default_factory=list
    )

    weak_concepts: list[str] = field(
        default_factory=list
    )

    strengths: list[str] = field(
        default_factory=list
    )

    feedback: str = ""

    should_review: bool = False