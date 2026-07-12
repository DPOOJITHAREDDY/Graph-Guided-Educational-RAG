from src.knowledge_graph.concept_validator import ConceptValidator


def main():

    validator = ConceptValidator()

    concepts = [

        "Random Forest",

        "Decision Tree",

        "Another Ensemble Technique",

        "Multiple Decision Tree",

        "Gradient Boosting",

        "Forest Prediction"

    ]

    print("=" * 80)
    print("CONCEPT VALIDATOR")
    print("=" * 80)
    print()

    for concept in concepts:

        result = validator.validate(
            concept
        )

        print()

        print(concept)

        print(result)


if __name__ == "__main__":

    main()