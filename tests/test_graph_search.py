"""
Test Graph Search
"""

from pathlib import Path

from src.knowledge_graph.graph_store import GraphStore
from src.knowledge_graph.graph_search import GraphSearch


def main():

    graph = GraphStore.load(
        Path(
            "data/knowledge_graph/Machine_Learning/knowledge_graph.pkl"
        )
    )

    search = GraphSearch(graph)

    print("=" * 60)
    print("GRAPH SEARCH")
    print("=" * 60)

    while True:

        concept = input(
            "\nEnter concept (or exit): "
        ).strip()

        if concept.lower() == "exit":
            break

        related = search.related_concepts(concept)

        if not related:

            print("Concept not found.")
            continue

        print("\nRelated Concepts\n")

        for neighbor, weight in related:

            print(
                f"{neighbor:25} weight={weight}"
            )


if __name__ == "__main__":
    main()