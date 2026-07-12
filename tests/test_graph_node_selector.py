from src.knowledge_graph.graph_node_selector import GraphNodeSelector


def main():

    selector = GraphNodeSelector()

    concepts = [

        "Random Forest",
        "Decision Tree",
        "Feature",
        "Model",
        "Data",
        "Bootstrap Sampling",
        "Gradient Boosting",
        "Accuracy",
        "Tree",
        "Prediction",
        "ROC Curve",
        "Precision",
        "Recall"

    ]

    selected = selector.select(concepts)

    print("=" * 80)
    print("GRAPH NODE SELECTOR")
    print("=" * 80)

    print()

    for concept in selected:

        print(concept)


if __name__ == "__main__":
    main()