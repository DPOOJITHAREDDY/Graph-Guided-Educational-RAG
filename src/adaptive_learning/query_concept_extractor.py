"""
query_concept_extractor.py

Extracts educational concepts mentioned in a user's query
using a predefined concept vocabulary.
"""

import re


class QueryConceptExtractor:
    """
    Detects concepts explicitly mentioned in a query.

    The extractor receives a concept vocabulary and performs
    deterministic matching against the user's query.
    """

    def __init__(self, vocabulary):

        self.vocabulary = []

        for concept in sorted(vocabulary, key=len, reverse=True):

            self.vocabulary.append(
                (
                    concept,
                    self._normalize(concept)
                )
            )

    @staticmethod
    def _normalize(text):

        text = text.lower()

        text = re.sub(
            r"[^\w\s]",
            " ",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    def extract(self, query):

        normalized_query = self._normalize(query)

        detected = []

        for concept, normalized_concept in self.vocabulary:

            pattern = (
                r"\b"
                + re.escape(normalized_concept)
                + r"\b"
            )

            if re.search(pattern, normalized_query):

                detected.append(concept)

        return detected