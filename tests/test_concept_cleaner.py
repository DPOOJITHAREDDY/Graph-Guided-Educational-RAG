from src.knowledge_graph.concept_cleaner import ConceptCleaner


def main():

    cleaner = ConceptCleaner()

    samples = [

        "| Chapter",

        "Chapter 2 Supervised Learning",

        "Each Feature",

        "Your Data",

        "Decision Trees",

        "Data Points",

        "Random Forests",

        "Training Sets"

    ]

    print("=" * 80)
    print("CONCEPT CLEANER")
    print("=" * 80)

    for sample in samples:

        cleaned = cleaner.clean(sample)

        print(f"{sample:<40} -> {cleaned}")


if __name__ == "__main__":
    main()