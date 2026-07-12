"""
neighbor_filter.py

Filters graph neighbors for educational relevance.
"""

import re


class NeighborFilter:
    """
    Filters graph neighbors before they are used for
    knowledge tracing.
    """

    def __init__(self):

        self.stop_concepts = {

            "Figure",
            "Model",
            "Method",
            "Category",
            "Collection",
            "Idea",
            "Reason",
            "Result",
            "Word",
            "Number",
            "Case",
            "Kind",
            "Look",
            "Hour",
            "Weekday",
            "August",
            "Sense",
            "Story",
            "Process"

        }

    def accept(self, concept, weight):
        """
        Returns True if the concept is suitable
        for knowledge tracing.
        """

        # Remove weak relationships

        if weight < 2:
            return False

        # Remove generic concepts

        if concept in self.stop_concepts:
            return False

        # Remove OCR artifacts

        if "‐" in concept:
            return False

        if "-" in concept and len(concept.split()) == 1:
            return False

        if re.search(r"[=|]", concept):
            return False

        return True