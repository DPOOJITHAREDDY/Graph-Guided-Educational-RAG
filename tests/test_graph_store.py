"""
Test Graph Store
"""

from pathlib import Path

from src.knowledge_graph.graph_builder import GraphBuilder
from src.knowledge_graph.graph_store import GraphStore


def main():

    builder = GraphBuilder()

    builder.add_chunk(
        "chunk1",
        [
            "Decision Tree",
            "Entropy",
            "Information Gain"
        ]
    )

    graph = builder.get_graph()

    save_path = Path(
        "data/knowledge_graph/Machine_Learning/knowledge_graph.pkl"
    )

    GraphStore.save(
        graph,
        save_path
    )

    loaded_graph = GraphStore.load(
        save_path
    )

    print("\nLoaded Graph")

    print("Nodes :", loaded_graph.number_of_nodes())
    print("Edges :", loaded_graph.number_of_edges())


if __name__ == "__main__":
    main()