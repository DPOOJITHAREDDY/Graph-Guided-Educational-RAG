"""
test_rag.py

Integration test for the complete RAG pipeline.
"""

from src.rag.rag_pipeline import RAGPipeline


def main():

    subject = "Machine_Learning"

    rag = RAGPipeline()

    print("=" * 80)
    print("GRAPH-GUIDED EDUCATIONAL RAG")
    print("=" * 80)

    while True:

        query = input(
            "\nAsk a question (type 'exit' to quit): "
        ).strip()

        if query.lower() == "exit":
            break

        print("\nGenerating answer...\n")

        response = rag.ask(
            subject=subject,
            query=query
        )

        print("=" * 80)
        print("ANSWER")
        print("=" * 80)

        print(response["answer"])

        print("\n")
        print("=" * 80)
        print("REFERENCES")
        print("=" * 80)

        for reference in response["references"]:

            print(
                f"- {reference['document']} "
                f"(Page {reference['page']})"
            )

        print("\n")


if __name__ == "__main__":
    main()