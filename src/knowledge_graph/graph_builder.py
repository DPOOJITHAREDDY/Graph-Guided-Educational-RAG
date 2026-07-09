"""
graph_builder.py

Builds a knowledge graph from extracted concepts.
"""

import networkx as nx


class GraphBuilder:

    def __init__(self):
        self.graph = nx.Graph()

    def add_chunk(self, chunk_id, concepts):

        # Remove duplicates while preserving order
        unique_concepts = []

        for concept in concepts:
            concept = concept.strip()

            if concept and concept not in unique_concepts:
                unique_concepts.append(concept)

        # Add concept nodes
        for concept in unique_concepts:

            if not self.graph.has_node(concept):

                self.graph.add_node(
                    concept,
                    node_type="concept"
                )

        # Connect every concept inside the same chunk
        for i in range(len(unique_concepts)):
            for j in range(i + 1, len(unique_concepts)):

                c1 = unique_concepts[i]
                c2 = unique_concepts[j]

                if self.graph.has_edge(c1, c2):

                    self.graph[c1][c2]["weight"] += 1

                    self.graph[c1][c2]["chunks"].add(chunk_id)

                else:

                    self.graph.add_edge(
                        c1,
                        c2,
                        weight=1,
                        chunks={chunk_id}
                    )

    def get_graph(self):
        return self.graph

    def number_of_nodes(self):
        return self.graph.number_of_nodes()

    def number_of_edges(self):
        return self.graph.number_of_edges()