"""
retriever.py

Retrieves the most relevant document chunks from the FAISS vector store.
"""

import time
import numpy as np

from config.settings import TOP_K
from src.embeddings.embedding_generator import EmbeddingGenerator
from src.models.retrieval_result import RetrievalResult
from src.retrieval.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant chunks for a user query.
    """

    def __init__(self):

        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = VectorStore()

    @staticmethod
    def distance_to_confidence(distance):
        """
        Convert L2 distance into an approximate confidence score.
        """

        confidence = max(0.0, 1.0 - (distance / 2.0))

        return round(confidence, 4)

    def retrieve(self, subject, query, top_k=TOP_K):

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        if not self.vector_store.exists(subject):
            raise FileNotFoundError(
                f"No vector database found for subject '{subject}'."
            )

        start_time = time.perf_counter()

        index, documents = self.vector_store.load(subject)

        query_embedding = self.embedding_generator.embed_query(query)

        query_embedding = np.asarray(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = index.search(
            query_embedding,
            top_k
        )

        retrieval_time = time.perf_counter() - start_time

        results = []

        for rank, (distance, idx) in enumerate(
            zip(distances[0], indices[0]),
            start=1
        ):

            if idx == -1:
                continue

            result = RetrievalResult(
                rank=rank,
                distance=float(distance),
                confidence=self.distance_to_confidence(distance),
                document=documents[idx],
                retrieval_time=retrieval_time
            )

            results.append(result)

        return results