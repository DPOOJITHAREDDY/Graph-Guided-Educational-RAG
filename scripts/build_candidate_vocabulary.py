"""
Build Candidate Vocabulary

Runs ConceptExtractorV3 on all chunks and builds
a vocabulary with occurrence statistics.
"""

import json
from collections import defaultdict

from config.settings import PROCESSED_DATA_PATH
from src.storage.storage_manager import StorageManager
from src.knowledge_graph.concept_extractor_v3 import ConceptExtractorV3


def main():

    print("=" * 80)
    print("BUILDING CANDIDATE VOCABULARY")
    print("=" * 80)

    extractor = ConceptExtractorV3()

    chunks = StorageManager.load(
        base_path=PROCESSED_DATA_PATH,
        subject="Machine_Learning",
        filename="chunks.pkl"
    )

    vocabulary = defaultdict(
        lambda: {
            "frequency": 0,
            "chunks": set()
        }
    )

    total_chunks = len(chunks)

    for index, chunk in enumerate(chunks, start=1):

        if index % 50 == 0:
            print(f"Processed {index}/{total_chunks}")

        concepts = extractor.extract(chunk.page_content)

        for concept in concepts:

            vocabulary[concept]["frequency"] += 1
            vocabulary[concept]["chunks"].add(index)

    results = []

    for concept, info in vocabulary.items():

        results.append({

            "concept": concept,

            "frequency": info["frequency"],

            "document_frequency": len(info["chunks"])

        })

    results.sort(

        key=lambda x: (

            -x["frequency"],
            x["concept"]

        )

    )

    with open(
        "data/candidate_vocabulary.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False
        )

    print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print("Unique Concepts :", len(results))

    print("\nTop 25 Concepts\n")

    for item in results[:25]:

        print(
            f"{item['frequency']:>4}   "
            f"{item['concept']}"
        )


if __name__ == "__main__":

    main()