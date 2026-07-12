"""
concept_graph.py

Provides educational graph operations for the knowledge graph.
"""

from pathlib import Path

from config.settings import KNOWLEDGE_GRAPH_PATH
from src.knowledge_graph.graph_store import GraphStore
from src.learning.neighbor_filter import NeighborFilter


class ConceptGraph:
    """
    Wrapper around the knowledge graph providing
    educational graph operations.
    """

    def __init__(self):

        self.graph = None

        self.filter = NeighborFilter()

    def load(self, subject):
        """
        Load the knowledge graph for a subject.
        """

        filepath = (
            Path(KNOWLEDGE_GRAPH_PATH)
            / subject
            / "knowledge_graph.pkl"
        )

        self.graph = GraphStore.load(filepath)

        return self.graph

    def has_concept(self, concept):
        """
        Returns True if the concept exists.
        """

        if self.graph is None:
            return False

        return concept in self.graph

    def get_neighbors(self, concept):
        """
        Returns all neighboring concepts
        along with edge weights.
        """

        if self.graph is None:
            return []

        if concept not in self.graph:
            return []

        neighbors = []

        for neighbor in self.graph.neighbors(concept):

            weight = self.graph[concept][neighbor].get(
                "weight",
                1
            )

            neighbors.append(
                (neighbor, weight)
            )

        return neighbors

    def get_learning_neighbors(self, concept):
        """
        Returns only educationally useful neighbors.
        """

        if self.graph is None:
            return []

        if concept not in self.graph:
            return []

        neighbors = []

        for neighbor in self.graph.neighbors(concept):

            weight = self.graph[concept][neighbor].get(
                "weight",
                1
            )

            if self.filter.accept(
                neighbor,
                weight
            ):

                neighbors.append(
                    (neighbor, weight)
                )

        neighbors.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return neighbors