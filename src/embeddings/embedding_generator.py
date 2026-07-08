"""
embedding_generator.py

Generates normalized embeddings using Sentence Transformers.
"""

import numpy as np
from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Handles embedding generation for documents and queries.
    """

    def __init__(self):

        print("\nLoading embedding model...")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print("Embedding model loaded successfully.\n")

    @staticmethod
    def _normalize(embeddings):
        """
        Normalize embeddings to unit vectors.
        """

        norms = np.linalg.norm(
            embeddings,
            axis=1,
            keepdims=True
        )

        return embeddings / norms

    def embed_documents(self, documents):
        """
        Generate normalized embeddings for document chunks.
        """

        texts = [
            doc.page_content
            for doc in documents
        ]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        embeddings = self._normalize(embeddings)

        return embeddings.astype("float32")

    def embed_query(self, query):
        """
        Generate normalized embedding for a user query.
        """

        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        embedding = embedding.reshape(1, -1)

        embedding = self._normalize(embedding)

        return embedding.astype("float32")[0]

    def embedding_dimension(self):
        """
        Return embedding dimension.
        """

        return self.model.get_embedding_dimension()