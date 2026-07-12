"""
graph_node_selector.py

Selects concepts that should become
knowledge graph nodes.
"""


class GraphNodeSelector:
    """
    Filters vocabulary concepts before
    graph construction.
    """

    def __init__(self):

        self.generic_concepts = {

            "Data",
            "Datum",
            "Feature",
            "Tree",
            "Forest",
            "Parameter",
            "Prediction",
            "Point",
            "Value",
            "Method",
            "Model",
            "Process",
            "Result",
            "Reason",
            "Idea",
            "Category",
            "Collection",
            "Choice",
            "Word",
            "Number",
            "Case",
            "Kind",
            "Story",
            "Look",
            "Hour",
            "Weekday",
            "August"

        }

    def select(self, concepts):
        """
        Returns only concepts suitable
        as graph nodes.
        """

        selected = []

        for concept in concepts:

            if concept in self.generic_concepts:
                continue

            if len(concept.split()) == 1:

                # Keep only meaningful single-word concepts

                if concept not in {

                    "Regression",
                    "Classification",
                    "Clustering",
                    "Entropy",
                    "Accuracy",
                    "Precision",
                    "Recall"

                }:
                    continue

            selected.append(concept)

        return selected