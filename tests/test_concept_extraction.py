"""
test_concept_extraction.py
"""

from config.settings import PROCESSED_DATA_PATH

from src.storage.storage_manager import StorageManager
from src.knowledge_graph.concept_extractor import ConceptExtractor


def main():

    print("=" * 80)
    print("TESTING CONCEPT EXTRACTION")
    print("=" * 80)

    chunks = StorageManager.load(
        base_path=PROCESSED_DATA_PATH,
        subject="Machine_Learning",
        filename="chunks.pkl"
    )

    if chunks is None:
        print("Chunks not found.")
        return

    print(f"\nLoaded {len(chunks)} chunks.\n")

    extractor = ConceptExtractor()

    while True:

        chunk_number = input(
            "\nEnter chunk number (or 'exit'): "
        ).strip()

        if chunk_number.lower() == "exit":
            break

        if not chunk_number.isdigit():
            print("Enter a valid number.")
            continue

        chunk_number = int(chunk_number)

        if chunk_number >= len(chunks):
            print("Chunk out of range.")
            continue

        chunk = chunks[chunk_number]

        print("\n")
        print("=" * 80)
        print("TEXT")
        print("=" * 80)

        print(chunk.page_content)

        concepts = extractor.extract(chunk.page_content)

        print("\n")
        print("=" * 80)
        print("CONCEPTS")
        print("=" * 80)

        for concept in concepts:
            print("-", concept)


if __name__ == "__main__":
    main()