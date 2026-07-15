"""
candidate_extractor.py

Generates candidate educational concepts from text.

This module maximizes concept recall while filtering
obvious textbook metadata and structural noise.
"""

import re

import spacy


class CandidateExtractor:

    MAX_PHRASE_LENGTH = 6

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.metadata_words = {

            "author",
            "publisher",
            "copyright",
            "edition",
            "cover",
            "preface",
            "appendix",
            "chapter",
            "isbn",
            "index",
            "editor",
            "designer",
            "proofreader",
            "copyeditor",
            "illustrator",
            "revision",
            "history",
            "trademark",
            "license",
            "department",
            "address",
            "street",
            "media",
            "inc",
            "corporate",
            "sale"

        }

        self.ml_acronyms = {

            "CNN",
            "RNN",
            "LSTM",
            "GRU",
            "GAN",
            "SVM",
            "PCA",
            "LDA",
            "KNN",
            "RAG",
            "GPT",
            "BERT",
            "ROC",
            "AUC",
            "FAISS"

        }

    def clean_text(self, text):

        text = re.sub(r"http\S+", " ", text)

        text = re.sub(r"\S+@\S+", " ", text)

        text = text.replace("_", " ")

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def _valid_phrase(self, phrase):

        phrase = phrase.strip()

        if len(phrase) < 3:
            return False

        words = phrase.split()

        if len(words) > self.MAX_PHRASE_LENGTH:
            return False

        if phrase.isnumeric():
            return False

        lower = phrase.lower()

        if any(word in lower for word in self.metadata_words):
            return False

        if re.fullmatch(r"[\W_]+", phrase):
            return False

        return True

    def extract(self, text):

        text = self.clean_text(text)

        doc = self.nlp(text)

        candidates = set()

        # ---------------------------------------
        # Acronyms
        # ---------------------------------------

        for token in doc:

            if token.text.upper() in self.ml_acronyms:

                candidates.add(token.text.upper())

        # ---------------------------------------
        # Noun Chunks
        # ---------------------------------------

        for chunk in doc.noun_chunks:

            if chunk.root.pos_ == "PRON":
                continue

            phrase = chunk.text.strip()

            if self._valid_phrase(phrase):

                candidates.add(phrase)

        # ---------------------------------------
        # Named Entities
        # ---------------------------------------

        for ent in doc.ents:

            phrase = ent.text.strip()

            if self._valid_phrase(phrase):

                candidates.add(phrase)

        # ---------------------------------------
        # Compound Nouns
        # ---------------------------------------

        for token in doc:

            if token.dep_ != "compound":
                continue

            phrase = f"{token.text} {token.head.text}"

            if self._valid_phrase(phrase):

                candidates.add(phrase)

        # ---------------------------------------
        # Hyphenated Technical Terms
        # ---------------------------------------

        for token in doc:

            if "-" in token.text:

                if self._valid_phrase(token.text):

                    candidates.add(token.text)

        return sorted(candidates)