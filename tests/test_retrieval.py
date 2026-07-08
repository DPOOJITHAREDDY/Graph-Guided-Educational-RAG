"""
test_retrieval.py

Integration test for the retrieval engine.
"""

from config.settings import PROCESSED_DATA_PATH

from src.storage.storage_manager import StorageManager
from src.retrieval.embedding_indexer import EmbeddingIndexer
from src.retrieval.vector_store import VectorStore
from src.retrieval.search import SearchEngine


def main():

    subject = "Machine_Learning"

    print("=" * 80)
    print("Loading document chunks...")
    print("=" * 80)

    chunks = StorageManager.load(
        base_path=PROCESSED_DATA_PATH,
        subject=subject,
        filename="chunks.pkl"
    )

    if chunks is None:
        raise FileNotFoundError(
            "No chunks found. Run preprocessing first."
        )

    print(f"Loaded {len(chunks)} chunks.\n")

    vector_store = VectorStore()

    if not vector_store.exists(subject):

        print("=" * 80)
        print("Building FAISS Index...")
        print("=" * 80)

        indexer = EmbeddingIndexer()

        index, documents = indexer.build_index(chunks)

        vector_store.save(
            index=index,
            documents=documents,
            subject=subject
        )

        print("\nVector database created successfully.\n")

    else:

        print("Existing vector database found.\n")

    search_engine = SearchEngine()

    while True:

        query = input(
            "Enter your question (type 'exit' to quit): "
        ).strip()

        if query.lower() == "exit":
            break

        results = search_engine.search(
            subject=subject,
            query=query
        )

        print("\n")
        print("=" * 80)
        print("RETRIEVAL SUMMARY")
        print("=" * 80)

        print(f"Query             : {query}")
        print(f"Retrieved Chunks  : {len(results)}")

        if results:
            print(
                f"Retrieval Time    : "
                f"{results[0].retrieval_time:.4f} seconds"
            )

        print("\n")
        print("=" * 80)
        print("TOP RETRIEVED DOCUMENTS")
        print("=" * 80)

        for result in results:

            doc = result.document

            print(f"\nResult #{result.rank}")
            print("-" * 80)

            print(f"Distance      : {result.distance:.4f}")
            print(f"Confidence    : {result.confidence:.4f}")

            print(f"Subject       : {doc.metadata['subject']}")
            print(f"Document      : {doc.metadata['document']}")
            print(f"Page          : {doc.metadata['page']}")
            print(f"Chunk ID      : {doc.metadata['chunk_id']}")

            print("\nPreview\n")

            print(doc.page_content[:600])

            print("\n" + "=" * 80)


if __name__ == "__main__":
    main()