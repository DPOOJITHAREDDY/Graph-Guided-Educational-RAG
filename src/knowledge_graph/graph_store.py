"""
graph_store.py

Save and load the knowledge graph.
"""

import pickle
from pathlib import Path


class GraphStore:

    @staticmethod
    def save(graph, filepath):

        filepath = Path(filepath)

        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, "wb") as f:
            pickle.dump(graph, f)

        print(f"Knowledge graph saved to {filepath}")

    @staticmethod
    def load(filepath):

        filepath = Path(filepath)

        if not filepath.exists():
            raise FileNotFoundError(filepath)

        with open(filepath, "rb") as f:
            graph = pickle.load(f)

        return graph