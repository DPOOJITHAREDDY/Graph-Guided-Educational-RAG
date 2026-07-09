"""
Test Hybrid Retrieval
"""

from src.hybrid.hybrid_retriever import HybridRetriever


def main():

    retriever = HybridRetriever()

    while True:

        query = input(
            "\nQuestion (or exit): "
        )

        if query.lower() == "exit":
            break

        result = retriever.retrieve(
            subject="Machine_Learning",
            query=query
        )

        print("\n")
        print("=" * 80)
        print("GRAPH EXPANDED CONCEPTS")
        print("=" * 80)

        for concept in result["expanded_concepts"]:

            print("-", concept)

        print("\n")
        print("=" * 80)
        print("RETRIEVED DOCUMENTS")
        print("=" * 80)

        for item in result["retrieval_results"]:

            print(
                f"Page {item.document.metadata['page']} "
                f"Confidence={item.confidence:.2f}"
            )


if __name__ == "__main__":
    main()