"""
Test Concept Extractor V3
"""

from config.settings import PROCESSED_DATA_PATH
from src.storage.storage_manager import StorageManager
from src.knowledge_graph.concept_extractor_v3 import ConceptExtractorV3


def main():

    extractor = ConceptExtractorV3()

    chunks = StorageManager.load(
        base_path=PROCESSED_DATA_PATH,
        subject="Machine_Learning",
        filename="chunks.pkl"
    )

    chunk = chunks[300]

    print("=" * 80)
    print("TEXT")
    print("=" * 80)
    print(chunk.page_content)

    print("\n")

    concepts = extractor.extract(chunk.page_content)

    print("=" * 80)
    print("ACCEPTED CONCEPTS")
    print("=" * 80)

    for concept in concepts:

        print("-", concept)


if __name__ == "__main__":
    main()