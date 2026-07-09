"""
graph_search.py

Search utilities for the knowledge graph.
"""

import networkx as nx


class GraphSearch:

    def __init__(self, graph):

        self.graph = graph

    def neighbors(self, concept):

        if concept not in self.graph:
            return []

        return sorted(list(self.graph.neighbors(concept)))

    def related_concepts(self, concept, top_k=10):

        if concept not in self.graph:
            return []

        neighbors = []

        for neighbor in self.graph.neighbors(concept):

            weight = self.graph[concept][neighbor]["weight"]

            neighbors.append((neighbor, weight))

        neighbors.sort(key=lambda x: x[1], reverse=True)

        return neighbors[:top_k]

    def shortest_path(self, source, target):

        try:
            return nx.shortest_path(
                self.graph,
                source,
                target
            )

        except nx.NetworkXNoPath:
            return None

        except nx.NodeNotFound:
            return None