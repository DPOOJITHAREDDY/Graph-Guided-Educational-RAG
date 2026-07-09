"""
Analyze the quality of extracted concepts from the whole textbook.
"""

from collections import Counter

from config.settings import PROCESSED_DATA_PATH
from src.storage.storage_manager import StorageManager
from src.knowledge_graph.concept_extractor import ConceptExtractor


def main():

    extractor = ConceptExtractor()

    chunks = StorageManager.load(
        base_path=PROCESSED_DATA_PATH,
        subject="Machine_Learning",
        filename="chunks.pkl"
    )

    print("=" * 80)
    print("ANALYZING CONCEPT EXTRACTION")
    print("=" * 80)

    total_chunks = len(chunks)

    concept_counter = Counter()

    concepts_per_chunk = []

    for chunk in chunks:

        concepts = extractor.extract(
            chunk.page_content
        )

        concepts_per_chunk.append(len(concepts))

        concept_counter.update(concepts)

    print(f"\nChunks               : {total_chunks}")
    print(f"Unique Concepts      : {len(concept_counter)}")
    print(f"Total Concepts Found : {sum(concept_counter.values())}")
    print(
        f"Average / Chunk      : "
        f"{sum(concepts_per_chunk)/len(concepts_per_chunk):.2f}"
    )

    print("\n")
    print("=" * 80)
    print("TOP 100 MOST FREQUENT CONCEPTS")
    print("=" * 80)

    for concept, freq in concept_counter.most_common(100):

        print(f"{freq:4}  {concept}")


if __name__ == "__main__":
    main()