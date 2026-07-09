"""
concept_extractor.py

Concept Extractor V2
"""

import re
import spacy


class ConceptExtractor:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        # Generic English words
        self.generic_words = {

            "another", "default", "detail", "details",
            "summary", "introduction", "practice",
            "week", "mind", "people", "group",
            "groups", "time", "information",
            "component", "components",
            "topic", "topics",
            "image", "images",
            "print", "chapter", "section",
            "problem", "example",
            "examples"
        }

        # Programming words
        self.code_words = {

            "print",
            "fit",
            "predict",
            "transform",
            "score",
            "scores",
            "pipeline",
            "pipelines",
            "paramgrid",
            "gridsearchcv",
            "crossvalscore",
            "crossvalidate",
            "crossvalidator",
            "standardscaler",
            "countvectorizer",
            "tfidfvectorizer",
            "sklearndatasets",
            "plt",
            "matplotlib",
            "numpy",
            "pandas"
        }

    def clean(self, text):

        text = re.sub(r"\[[^\]]*\]", " ", text)
        text = re.sub(r"\([^)]*\)", " ", text)
        text = re.sub(r"\s+", " ", text)

        return text

    def is_code(self, phrase):

        p = phrase.lower()

        # CamelCase APIs
        if re.search(r"[a-z][A-Z]", phrase):
            return True

        # snake_case
        if "_" in phrase:
            return True

        # Variable names
        if re.fullmatch(r"[xyXY][a-zA-Z0-9]*", phrase):
            return True

        # API names
        if p in self.code_words:
            return True

        return False

    def normalize(self, phrase):

        doc = self.nlp(phrase)

        words = []

        for token in doc:

            if token.is_stop:
                continue

            if token.is_punct:
                continue

            lemma = token.lemma_

            if lemma.lower() in self.generic_words:
                continue

            words.append(lemma.title())

        return " ".join(words)

    def valid(self, phrase):

        if len(phrase) < 3:
            return False

        if any(char.isdigit() for char in phrase):
            return False

        if self.is_code(phrase):
            return False

        words = phrase.split()

        if len(words) == 1:

            word = words[0].lower()

            if word in self.generic_words:
                return False

            if len(word) < 4:
                return False

        return True

    def extract(self, text):

        text = self.clean(text)

        doc = self.nlp(text)

        concepts = set()

        for chunk in doc.noun_chunks:

            if chunk.root.pos_ == "PRON":
                continue

            phrase = self.normalize(chunk.text)

            if self.valid(phrase):
                concepts.add(phrase)

        return sorted(concepts)