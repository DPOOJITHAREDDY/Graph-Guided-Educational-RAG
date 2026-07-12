"""
graph_builder.py

Builds a clean educational knowledge graph
from extracted concepts.
"""

import networkx as nx

from src.knowledge_graph.graph_node_selector import GraphNodeSelector


class GraphBuilder:
    """
    Builds a weighted educational knowledge graph.
    """

    # Prevent very large chunks from creating
    # dense noisy graphs.
    MAX_GRAPH_CONCEPTS = 20

    def __init__(self):

        self.graph = nx.Graph()

        self.selector = GraphNodeSelector()

    def add_chunk(
        self,
        chunk_id,
        concepts
    ):
        """
        Add one document chunk to the graph.
        """

        # ------------------------------------
        # Select only graph-worthy concepts
        # ------------------------------------

        concepts = self.selector.select(concepts)

        # ------------------------------------
        # Remove duplicates
        # ------------------------------------

        unique_concepts = []

        seen = set()

        for concept in concepts:

            concept = concept.strip()

            if not concept:
                continue

            if concept in seen:
                continue

            seen.add(concept)

            unique_concepts.append(concept)

        # ------------------------------------
        # Prevent extremely dense chunks
        # ------------------------------------

        unique_concepts = unique_concepts[
            : self.MAX_GRAPH_CONCEPTS
        ]

        # ------------------------------------
        # Add nodes
        # ------------------------------------

        for concept in unique_concepts:

            if not self.graph.has_node(concept):

                self.graph.add_node(

                    concept,

                    node_type="concept"

                )

        # ------------------------------------
        # Build weighted co-occurrence edges
        # ------------------------------------

        for i in range(len(unique_concepts)):

            for j in range(i + 1, len(unique_concepts)):

                source = unique_concepts[i]

                target = unique_concepts[j]

                if source == target:
                    continue

                if self.graph.has_edge(
                    source,
                    target
                ):

                    self.graph[source][target]["weight"] += 1

                    self.graph[source][target]["chunks"].add(
                        chunk_id
                    )

                else:

                    self.graph.add_edge(

                        source,

                        target,

                        weight=1,

                        chunks={chunk_id}

                    )

    def get_graph(self):

        return self.graph

    def number_of_nodes(self):

        return self.graph.number_of_nodes()

    def number_of_edges(self):

        return self.graph.number_of_edges()

    def clear(self):
        """
        Clears the graph.
        """

        self.graph.clear()