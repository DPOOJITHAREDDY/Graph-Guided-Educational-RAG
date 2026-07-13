from src.knowledge_graph.concept_scorer import ConceptScorer


def main():

    scorer = ConceptScorer()

    concepts = [

        "Random Forest",
        "Decision Tree",
        "Gradient Boosting",
        "Support Vector Machine",
        "Another Ensemble Technique",
        "Multiple Decision Tree",
        "Forest Prediction",
        "Model",
        "Print",
        "Feature Importance"

    ]

    print("=" * 80)
    print("CONCEPT SCORER")
    print("=" * 80)

    print()

    for concept in concepts:

        result = scorer.score(concept)

        print(result)

        print()


if __name__ == "__main__":
    main()