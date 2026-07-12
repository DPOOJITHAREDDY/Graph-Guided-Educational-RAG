"""
concept_scorer.py

Scores normalized candidate concepts.
"""

import re


class ConceptScorer:

    def __init__(self):

        self.generic_words = {

            "model",
            "figure",
            "table",
            "result",
            "number",
            "point",
            "case",
            "value",
            "method",
            "problem",
            "task",
            "application",
            "book",
            "chapter",
            "section"

        }

        self.programming_words = {

            "print",
            "fit",
            "predict",
            "transform",
            "score",
            "python",
            "numpy",
            "pandas",
            "matplotlib",
            "plt"

        }

    def score(self, concept):

        reasons = []

        score = 0

        words = concept.split()

        # --------------------------
        # Multi-word bonus
        # --------------------------

        if len(words) >= 2:

            score += 2

            reasons.append("Multi-word concept")

        # --------------------------
        # Long phrase bonus
        # --------------------------

        if len(words) >= 3:

            score += 1

            reasons.append("Descriptive phrase")

        # --------------------------
        # Programming penalty
        # --------------------------

        lower = concept.lower()

        if lower in self.programming_words:

            score -= 5

            reasons.append("Programming keyword")

        # --------------------------
        # Generic word penalty
        # --------------------------

        if lower in self.generic_words:

            score -= 4

            reasons.append("Generic textbook word")

        # --------------------------
        # Variable names
        # --------------------------

        if re.fullmatch(r"[xyXY][a-zA-Z0-9_]*", concept):

            score -= 5

            reasons.append("Variable name")

        accepted = score >= 2

        return {

            "concept": concept,

            "score": score,

            "accepted": accepted,

            "reasons": reasons

        }