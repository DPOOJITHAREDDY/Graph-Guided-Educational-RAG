"""
embedding_indexer.py

Builds a FAISS index from document chunks.
"""

import faiss

from src.embeddings.embedding_generator import EmbeddingGenerator


class EmbeddingIndexer:
    """
    Creates a FAISS index from document chunks.
    """

    def __init__(self):

        self.embedding_generator = EmbeddingGenerator()

    def build_index(self, documents):
        """
        Build a FAISS index from document chunks.
        """

        embeddings = self.embedding_generator.embed_documents(
            documents
        )

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings)

        return index, documents