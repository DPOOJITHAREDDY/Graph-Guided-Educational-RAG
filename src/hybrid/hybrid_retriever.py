"""
hybrid_retriever.py

Hybrid Retriever:
FAISS Retrieval + Knowledge Graph Expansion
"""

from pathlib import Path

from src.retrieval.retriever import Retriever
from src.knowledge_graph.graph_store import GraphStore
from src.knowledge_graph.graph_search import GraphSearch
from src.knowledge_graph.concept_extractor import ConceptExtractor


class HybridRetriever:

    def __init__(self):

        self.retriever = Retriever()
        self.extractor = ConceptExtractor()

    def retrieve(self, subject, query):

        # -----------------------------
        # Step 1 : Semantic Retrieval
        # -----------------------------

        results = self.retriever.retrieve(
            subject=subject,
            query=query
        )

        # -----------------------------
        # Step 2 : Load Graph
        # -----------------------------

        graph = GraphStore.load(
            Path(
                f"data/knowledge_graph/{subject}/knowledge_graph.pkl"
            )
        )

        graph_search = GraphSearch(graph)

        expanded_concepts = set()

        # -----------------------------
        # Step 3 : Expand Concepts
        # -----------------------------

        for result in results:

            text = result.document.page_content

            concepts = self.extractor.extract(text)

            for concept in concepts:

                expanded_concepts.add(concept)

                related = graph_search.related_concepts(
                    concept,
                    top_k=5
                )

                for neighbour, _ in related:

                    expanded_concepts.add(neighbour)

        return {

            "retrieval_results": results,

            "expanded_concepts": sorted(
                expanded_concepts
            )
        }