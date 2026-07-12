"""
concept_cleaner.py

Performs structural cleaning and canonicalization of normalized concepts.
"""

import json
import re

import spacy


class ConceptCleaner:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.leading_words = {

            "all",
            "each",
            "every",
            "this",
            "that",
            "these",
            "those",
            "your",
            "our",
            "their",
            "its",
            "his",
            "her"

        }

        with open(
            "resources/canonical_terms.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.canonical_terms = json.load(file)

    def clean(self, concept):

        concept = concept.strip()

        # --------------------------------
        # Remove leading symbols
        # --------------------------------

        concept = re.sub(r"^[^A-Za-z]+", "", concept)

        # --------------------------------
        # Remove chapter prefixes
        # Example:
        # Chapter 2 Supervised Learning
        # -> Supervised Learning
        # --------------------------------

        concept = re.sub(
            r"^Chapter\s+\d+\s*",
            "",
            concept,
            flags=re.IGNORECASE
        )

        # --------------------------------
        # Remove multiple spaces
        # --------------------------------

        concept = re.sub(r"\s+", " ", concept)

        words = concept.split()

        # --------------------------------
        # Remove leading generic words
        # --------------------------------

        while words and words[0].lower() in self.leading_words:
            words.pop(0)

        if not words:
            return ""

        doc = self.nlp(" ".join(words))

        cleaned = []

        # --------------------------------
        # Canonicalization
        # --------------------------------

        for token in doc:

            lower = token.text.lower()

            if lower in self.canonical_terms:

                cleaned.append(
                    self.canonical_terms[lower]
                )

            else:

                cleaned.append(
                    token.text
                )

        concept = " ".join(cleaned)

        concept = re.sub(r"\s+", " ", concept)

        concept = concept.title().strip()

        return concept