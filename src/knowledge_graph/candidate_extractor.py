"""
candidate_extractor.py

Generates candidate educational concepts from text.
This module DOES NOT decide whether something is a concept.
It only generates high-quality candidates.
"""

import re
import spacy


class CandidateExtractor:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

    def clean_text(self, text):

        # Remove URLs
        text = re.sub(r"http\S+", " ", text)

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def extract(self, text):

        text = self.clean_text(text)

        doc = self.nlp(text)

        candidates = set()

        # -----------------------------
        # 1. Noun Chunks
        # -----------------------------
        for chunk in doc.noun_chunks:

            phrase = chunk.text.strip()

            if len(phrase) > 2:
                candidates.add(phrase)

        # -----------------------------
        # 2. Named Entities
        # -----------------------------
        for ent in doc.ents:

            if len(ent.text) > 2:
                candidates.add(ent.text)

        # -----------------------------
        # 3. Compound Nouns
        # -----------------------------
        for token in doc:

            if token.dep_ == "compound":

                phrase = token.text + " " + token.head.text

                candidates.add(phrase)

        return sorted(candidates)