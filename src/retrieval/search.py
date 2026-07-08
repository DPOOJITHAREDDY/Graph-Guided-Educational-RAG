"""
search.py

Provides a simple interface for semantic document search.
"""

from src.retrieval.retriever import Retriever


class SearchEngine:

    def __init__(self):

        self.retriever = Retriever()

    def search(self, subject, query):

        return self.retriever.retrieve(
            subject=subject,
            query=query
        )