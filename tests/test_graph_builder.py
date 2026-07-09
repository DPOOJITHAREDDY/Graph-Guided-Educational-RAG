"""
Test Graph Builder
"""

from src.knowledge_graph.graph_builder import GraphBuilder


def main():

    builder = GraphBuilder()

    builder.add_chunk(
        "chunk_1",
        [
            "Decision Tree",
            "Entropy",
            "Information Gain",
            "Classification"
        ]
    )

    builder.add_chunk(
        "chunk_2",
        [
            "Decision Tree",
            "Random Forest",
            "Classification"
        ]
    )

    graph = builder.get_graph()

    print("=" * 60)
    print("GRAPH SUMMARY")
    print("=" * 60)

    print("Nodes :", builder.number_of_nodes())
    print("Edges :", builder.number_of_edges())

    print("\nNodes\n")

    for node in graph.nodes():
        print(node)

    print("\nEdges\n")

    for u, v, data in graph.edges(data=True):
        print(f"{u} <---> {v}  weight={data['weight']}")


if __name__ == "__main__":
    main()