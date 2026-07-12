"""
concept_normalizer.py

Normalizes candidate phrases into clean educational concepts.
"""

import re

import spacy


class ConceptNormalizer:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.leading_words = {

            "the",
            "a",
            "an",
            "this",
            "that",
            "these",
            "those"

        }

        self.trailing_words = {

            "task",
            "tasks",
            "problem",
            "problems",
            "method",
            "methods",
            "approach",
            "approaches",
            "model",
            "models"

        }

    def normalize(self, phrase):

        phrase = phrase.strip()

        phrase = re.sub(r"\s+", " ", phrase)

        doc = self.nlp(phrase)

        words = []

        for token in doc:

            if token.is_punct:
                continue

            words.append(token.text)

        # Remove leading words

        while words and words[0].lower() in self.leading_words:

            words.pop(0)

        # Remove trailing generic words

        while words and words[-1].lower() in self.trailing_words:

            words.pop()

        phrase = " ".join(words)

        phrase = phrase.strip()

        # Standard capitalization

        phrase = phrase.title()

        return phrase