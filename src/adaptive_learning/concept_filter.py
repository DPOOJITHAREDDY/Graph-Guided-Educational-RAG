"""
concept_filter.py

Filters knowledge graph concepts before they enter
the adaptive learning pipeline.
"""

import re


class ConceptFilter:
    """
    Removes generic, noisy and non-educational concepts.
    """

    GENERIC_WORDS = {

        "book",
        "figure",
        "table",
        "page",
        "section",
        "chapter",
        "guide",
        "author",
        "publisher",
        "cover",
        "release",
        "copyright",
        "license",
        "website",
        "documentation",
        "reference",
        "appendix",
        "preface",
        "content",
        "introduction",
        "overview",

        "simple",
        "easy",
        "basic",
        "good",
        "bad",
        "large",
        "small",
        "different",
        "many",
        "several",
        "another",
        "various",
        "other",

        "thing",
        "kind",
        "case",
        "number",
        "word",
        "datum",
        "point",
        "book"

    }

    ML_SINGLE_WORDS = {

        "algorithm",
        "classifier",
        "regression",
        "classification",
        "dataset",
        "feature",
        "parameter",
        "prediction",
        "accuracy",
        "cluster",
        "embedding",
        "transformer",
        "attention",
        "token",
        "optimizer",
        "gradient",
        "tree",
        "forest",
        "bagging",
        "boosting",
        "neuron",
        "activation",
        "kernel"

    }

    @staticmethod
    def is_valid(concept):

        concept = concept.strip()

        if len(concept) < 3:
            return False

        if any(ch in concept for ch in "│├└┐┌─═╔╗╚╝"):
            return False

        if re.fullmatch(r"[\W_]+", concept):
            return False

        words = concept.lower().split()

        # Multi-word concepts are generally good
        if len(words) >= 2:
            return True

        word = words[0]

        if word in ConceptFilter.GENERIC_WORDS:
            return False

        if word in ConceptFilter.ML_SINGLE_WORDS:
            return True

        return False

    @classmethod
    def filter(cls, concepts):

        accepted = []

        seen = set()

        for concept in concepts:

            if not cls.is_valid(concept):
                continue

            if concept in seen:
                continue

            seen.add(concept)

            accepted.append(concept)

        return accepted