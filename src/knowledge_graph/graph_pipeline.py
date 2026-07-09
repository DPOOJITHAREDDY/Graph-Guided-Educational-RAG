"""
graph_pipeline.py

Builds the complete knowledge graph from processed document chunks.
"""

import time

from config.settings import PROCESSED_DATA_PATH

from src.storage.storage_manager import StorageManager
from src.knowledge_graph.concept_extractor import ConceptExtractor
from src.knowledge_graph.graph_builder import GraphBuilder
from src.knowledge_graph.graph_store import GraphStore


class GraphPipeline:

    def __init__(self):

        self.extractor = ConceptExtractor()
        self.builder = GraphBuilder()

    def build(self, subject, save_path):

        start = time.time()

        print("=" * 80)
        print("LOADING CHUNKS")
        print("=" * 80)

        chunks = StorageManager.load(
            base_path=PROCESSED_DATA_PATH,
            subject=subject,
            filename="chunks.pkl"
        )

        if chunks is None:
            raise FileNotFoundError("chunks.pkl not found.")

        print(f"Loaded {len(chunks)} chunks.\n")

        print("=" * 80)
        print("BUILDING KNOWLEDGE GRAPH")
        print("=" * 80)

        for chunk in chunks:

            concepts = self.extractor.extract(
                chunk.page_content
            )

            self.builder.add_chunk(
                chunk.metadata["chunk_id"],
                concepts
            )

        graph = self.builder.get_graph()

        GraphStore.save(
            graph,
            save_path
        )

        elapsed = time.time() - start

        print("\n")
        print("=" * 80)
        print("GRAPH SUMMARY")
        print("=" * 80)

        print(f"Nodes : {graph.number_of_nodes()}")
        print(f"Edges : {graph.number_of_edges()}")
        print(f"Time  : {elapsed:.2f} seconds")