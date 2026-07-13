"""
reflection_engine.py

Performs self-reflection on the generated educational response.
"""

import re

from src.adaptive_learning.reflection_result import ReflectionResult


class ReflectionEngine:
    """
    Performs lightweight reflection on the generated answer.

    Future versions can replace this with LLM-based reflection
    without changing the public interface.
    """

    def reflect(
        self,
        answer: str,
        adaptive_context
    ) -> ReflectionResult:

        answer_lower = answer.lower()

        understanding_score = 1.0
        confidence_score = 1.0

        detected_misconceptions = []
        weak_concepts = []
        strengths = []

        # ----------------------------------------
        # Check concept coverage
        # ----------------------------------------

        for concept in adaptive_context.query_analysis.concepts:

            if concept.lower() in answer_lower:

                strengths.append(concept)

            else:

                weak_concepts.append(concept)

                understanding_score -= 0.20

        # ----------------------------------------
        # Detect uncertainty
        # ----------------------------------------

        uncertainty_words = {

            "maybe",
            "possibly",
            "might",
            "probably",
            "perhaps"

        }

        for word in uncertainty_words:

            if re.search(rf"\b{word}\b", answer_lower):

                confidence_score -= 0.10

        # ----------------------------------------
        # Detect explicit misconceptions
        # ----------------------------------------

        misconception_patterns = [

            "i don't know",
            "not sure",
            "cannot determine",
            "insufficient information"

        ]

        for pattern in misconception_patterns:

            if pattern in answer_lower:

                detected_misconceptions.append(pattern)

                confidence_score -= 0.20

        understanding_score = max(
            0.0,
            min(
                1.0,
                understanding_score
            )
        )

        confidence_score = max(
            0.0,
            min(
                1.0,
                confidence_score
            )
        )

        should_review = (

            understanding_score < 0.60

            or

            confidence_score < 0.60

        )

        feedback = (

            "Review recommended."

            if should_review

            else

            "Learning objective achieved."

        )

        return ReflectionResult(

            understanding_score=understanding_score,

            confidence_score=confidence_score,

            detected_misconceptions=detected_misconceptions,

            weak_concepts=weak_concepts,

            strengths=strengths,

            feedback=feedback,

            should_review=should_review

        )