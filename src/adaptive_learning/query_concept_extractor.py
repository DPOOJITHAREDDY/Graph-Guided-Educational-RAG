"""
query_concept_extractor.py

Extracts high-quality educational concepts from a user's query
using the knowledge graph vocabulary.
"""

import re


class QueryConceptExtractor:
    """
    Matches graph concepts inside a query.

    Improvements:
    - Longest phrase matching
    - Removes overlapping matches
    - Removes noisy graph nodes
    - Removes duplicates
    """

    def __init__(self, vocabulary):

        self.vocabulary = []

        for concept in vocabulary:

            if not self._is_valid_concept(concept):
                continue

            normalized = self._normalize(concept)

            if not normalized:
                continue

            self.vocabulary.append(
                (
                    concept,
                    normalized
                )
            )

        # Longest concepts first
        self.vocabulary.sort(
            key=lambda item: len(item[1]),
            reverse=True
        )

    @staticmethod
    def _normalize(text):

        text = text.lower()

        text = re.sub(r"[^\w\s]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def _is_valid_concept(concept):
        """
        Remove obvious garbage from the graph.
        """

        concept = concept.strip()

        if len(concept) < 3:
            return False

        # Reject concepts without letters
        if not re.search(r"[A-Za-z]", concept):
            return False

        # Reject drawing characters
        if any(ch in concept for ch in "│├└┐┌─═╔╗╚╝"):
            return False

        # Reject punctuation-only strings
        if re.fullmatch(r"[\W_]+", concept):
            return False

        return True

    def extract(self, query):

        normalized_query = self._normalize(query)

        matches = []

        occupied = []

        for original, normalized in self.vocabulary:

            pattern = r"\b" + re.escape(normalized) + r"\b"

            for match in re.finditer(pattern, normalized_query):

                start, end = match.span()

                # Skip overlaps with longer concepts
                overlap = False

                for s, e in occupied:

                    if start < e and end > s:
                        overlap = True
                        break

                if overlap:
                    continue

                occupied.append((start, end))
                matches.append(
                    (
                        start,
                        original
                    )
                )

        # Preserve query order
        matches.sort(key=lambda x: x[0])

        detected = []

        seen = set()

        for _, concept in matches:

            if concept not in seen:

                seen.add(concept)

                detected.append(concept)

        return detected