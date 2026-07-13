"""
concept_scorer.py

Scores educational concepts using structural
heuristics and a Machine Learning domain lexicon.
"""

import json
import re


class ConceptScorer:

    def __init__(self):

        with open(
            "resources/ml_keywords.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.ml_keywords = json.load(file)

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
            "section",
            "thing",
            "item"

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

        self.descriptive_words = {

            "another",
            "different",
            "multiple",
            "various",
            "several",
            "many",
            "some",
            "other",
            "certain"

        }

        self.weak_endings = {

            "technique",
            "approach",
            "method",
            "process"

        }

    def score(self, concept):

        score = 0

        reasons = []

        words = concept.split()

        lower_words = [
            word.lower()
            for word in words
        ]

        lower = concept.lower()

        # ----------------------------------
        # Multi-word concepts
        # ----------------------------------

        if len(words) >= 2:

            score += 2

            reasons.append(
                "Multi-word concept"
            )

        if len(words) >= 3:

            score += 1

            reasons.append(
                "Descriptive phrase"
            )

        # ----------------------------------
        # ML keyword bonus
        # ----------------------------------

        for keyword, weight in self.ml_keywords.items():

            keyword_words = keyword.split()

            if all(
                word in lower
                for word in keyword_words
            ):

                score += weight

                reasons.append(
                    f"ML keyword: {keyword}"
                )

        # ----------------------------------
        # Programming penalty
        # ----------------------------------

        if lower in self.programming_words:

            score -= 5

            reasons.append(
                "Programming keyword"
            )

        # ----------------------------------
        # Generic textbook words
        # ----------------------------------

        if lower in self.generic_words:

            score -= 4

            reasons.append(
                "Generic textbook word"
            )

        # ----------------------------------
        # Variable names
        # ----------------------------------

        if re.fullmatch(
            r"[xyXY][a-zA-Z0-9_]*",
            concept
        ):

            score -= 5

            reasons.append(
                "Variable name"
            )

        # ----------------------------------
        # Starts with descriptive words
        # ----------------------------------

        if lower_words:

            if lower_words[0] in self.descriptive_words:

                score -= 3

                reasons.append(
                    "Descriptive beginning"
                )

        # ----------------------------------
        # Weak endings
        # ----------------------------------

        if lower_words:

            if lower_words[-1] in self.weak_endings:

                score -= 2

                reasons.append(
                    "Weak ending"
                )

        # ----------------------------------
        # Numeric concepts
        # ----------------------------------

        if any(
            char.isdigit()
            for char in concept
        ):

            score -= 1

            reasons.append(
                "Contains digits"
            )

        accepted = score >= 3

        return {

            "concept": concept,

            "score": score,

            "accepted": accepted,

            "reasons": reasons

        }