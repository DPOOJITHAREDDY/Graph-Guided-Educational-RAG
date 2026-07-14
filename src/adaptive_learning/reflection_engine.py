"""
reflection_engine.py

Evaluates the quality of an educational response.
"""

import re

from src.adaptive_learning.reflection_result import ReflectionResult


class ReflectionEngine:
    """
    Evaluates generated educational responses using
    concept coverage, grounding and confidence.
    """

    UNCERTAINTY_WORDS = {
        "maybe",
        "perhaps",
        "possibly",
        "might",
        "probably",
        "generally",
        "typically"
    }

    MISCONCEPTION_PATTERNS = {
        "i don't know",
        "not sure",
        "cannot determine",
        "insufficient information"
    }

    @staticmethod
    def normalize(text):

        text = text.lower()

        text = re.sub(
            r"[^\w\s]",
            " ",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    def reflect(
        self,
        answer,
        adaptive_context
    ):

        normalized_answer = self.normalize(
            answer
        )

        # --------------------------------------------------
        # Scores
        # --------------------------------------------------

        understanding_score = 1.0
        coverage_score = 1.0
        grounding_score = 1.0
        difficulty_alignment_score = 1.0
        confidence_score = 1.0

        # --------------------------------------------------
        # Collections
        # --------------------------------------------------

        strengths = []

        weak_concepts = []

        covered_concepts = []

        missing_concepts = []

        detected_misconceptions = []

        unsupported_claims = []

        uncertainty_phrases = []

        recommended_review = []

        next_learning_topics = []

        # --------------------------------------------------
        # Concept Coverage
        # --------------------------------------------------

        for concept in adaptive_context.query_analysis.concepts:

            normalized_concept = self.normalize(
                concept
            )

            if normalized_concept in normalized_answer:

                strengths.append(concept)

                covered_concepts.append(
                    concept
                )

            else:

                weak_concepts.append(
                    concept
                )

                missing_concepts.append(
                    concept
                )

                understanding_score -= 0.20

                coverage_score -= 0.20

        # --------------------------------------------------
        # Retrieved Concepts
        # --------------------------------------------------

        retrieved_hits = 0

        if adaptive_context.retrieved_concepts:

            for concept in adaptive_context.retrieved_concepts:

                normalized = self.normalize(
                    concept
                )

                if normalized in normalized_answer:

                    retrieved_hits += 1

            grounding_score = min(

                1.0,

                retrieved_hits /
                max(
                    1,
                    len(
                        adaptive_context.retrieved_concepts
                    )
                )

            )

        # --------------------------------------------------
        # Difficulty Alignment
        # --------------------------------------------------

        difficulty = (
            adaptive_context
            .query_analysis
            .difficulty
        )

        word_count = len(answer.split())

        if difficulty == "beginner":

            if word_count > 500:

                difficulty_alignment_score = 0.70

        elif difficulty == "advanced":

            if word_count < 120:

                difficulty_alignment_score = 0.70

        # --------------------------------------------------
        # Uncertainty
        # --------------------------------------------------

        for word in self.UNCERTAINTY_WORDS:

            if re.search(
                rf"\b{word}\b",
                normalized_answer
            ):

                uncertainty_phrases.append(
                    word
                )

                confidence_score -= 0.05

        # --------------------------------------------------
        # Misconceptions
        # --------------------------------------------------

        for pattern in self.MISCONCEPTION_PATTERNS:

            if pattern in normalized_answer:

                detected_misconceptions.append(
                    pattern
                )

                confidence_score -= 0.20

        # --------------------------------------------------
        # Review Recommendations
        # --------------------------------------------------

        for concept in weak_concepts:

            recommended_review.append(
                concept
            )

        for concept in adaptive_context.related_concepts[:5]:

            next_learning_topics.append(
                concept
            )

        # --------------------------------------------------
        # Clamp Scores
        # --------------------------------------------------

        understanding_score = max(
            0.0,
            min(
                1.0,
                understanding_score
            )
        )

        coverage_score = max(
            0.0,
            min(
                1.0,
                coverage_score
            )
        )

        grounding_score = max(
            0.0,
            min(
                1.0,
                grounding_score
            )
        )

        difficulty_alignment_score = max(
            0.0,
            min(
                1.0,
                difficulty_alignment_score
            )
        )

        confidence_score = max(
            0.0,
            min(
                1.0,
                confidence_score
            )
        )

        overall_score = round(

            (
                understanding_score
                + coverage_score
                + grounding_score
                + difficulty_alignment_score
                + confidence_score

            ) / 5,

            4

        )

        should_review = (

            overall_score < 0.70

        )

        if should_review:

            feedback = (
                "Review recommended before progressing."
            )

        else:

            feedback = (
                "Learning objective achieved."
            )

        return ReflectionResult(

            understanding_score=round(
                understanding_score,
                4
            ),

            confidence_score=round(
                confidence_score,
                4
            ),

            coverage_score=round(
                coverage_score,
                4
            ),

            grounding_score=round(
                grounding_score,
                4
            ),

            difficulty_alignment_score=round(
                difficulty_alignment_score,
                4
            ),

            overall_score=overall_score,

            strengths=strengths,

            weak_concepts=weak_concepts,

            covered_concepts=covered_concepts,

            missing_concepts=missing_concepts,

            detected_misconceptions=detected_misconceptions,

            unsupported_claims=unsupported_claims,

            uncertainty_phrases=uncertainty_phrases,

            recommended_review=recommended_review,

            next_learning_topics=next_learning_topics,

            feedback=feedback,

            should_review=should_review

        )