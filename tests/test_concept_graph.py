from src.learning.concept_graph import ConceptGraph


def main():

    graph = ConceptGraph()

    graph.load(
        "Machine_Learning"
    )

    concept = "Random Forest"

    print("=" * 80)
    print("CONCEPT GRAPH")
    print("=" * 80)

    print()

    print("Concept:")
    print(concept)

    print()

    print("Learning Neighbors")

    for neighbor, weight in graph.get_learning_neighbors(concept):

        print(
            f"{neighbor:<45} weight={weight}"
        )


if __name__ == "__main__":
    main()