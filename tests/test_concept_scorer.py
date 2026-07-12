from src.knowledge_graph.concept_scorer import ConceptScorer


def main():

    scorer = ConceptScorer()

    concepts = [

        "Random Forest",

        "Decision Trees",

        "Classification And Regression",

        "Model",

        "Figure",

        "Print",

        "Bootstrap Sampling"

    ]

    print("=" * 80)

    print("CONCEPT SCORING")

    print("=" * 80)

    print()

    for concept in concepts:

        result = scorer.score(concept)

        print(result)

        print()


if __name__ == "__main__":

    main()