from src.knowledge_graph.concept_pipeline import ConceptPipeline


def main():

    pipeline = ConceptPipeline()

    text = """
    Random Forest is an ensemble learning algorithm
    built using multiple decision trees.

    Feature importance is commonly used to explain
    Random Forest predictions.

    Gradient Boosting is another ensemble technique.
    """

    concepts = pipeline.process(text)

    print("=" * 80)
    print("CONCEPT PIPELINE")
    print("=" * 80)

    print()

    for concept in concepts:

        print(concept)


if __name__ == "__main__":

    main()