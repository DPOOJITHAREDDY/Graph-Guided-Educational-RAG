"""
query_analyzer.py

Analyzes student queries for adaptive learning.
"""

import re

from src.adaptive_learning.concept_filter import ConceptFilter
from src.adaptive_learning.query_analysis import QueryAnalysis
from src.adaptive_learning.query_concept_extractor import (
    QueryConceptExtractor,
)


class QueryAnalyzer:

    def __init__(self, vocabulary):

        self.extractor = QueryConceptExtractor(
            vocabulary
        )

        self.intent_patterns = {

            "compare": [
                "compare",
                "difference",
                "versus",
                "vs"
            ],

            "quiz": [
                "quiz",
                "test me",
                "mcq"
            ],

            "summary": [
                "summary",
                "summarize"
            ],

            "definition": [
                "define",
                "definition",
                "what is"
            ],

            "example": [
                "example",
                "examples"
            ],

            "application": [
                "application",
                "applications",
                "use case"
            ],

            "revision": [
                "revise",
                "revision",
                "review"
            ],

            "explain": [
                "explain",
                "understand",
                "teach"
            ]

        }

    @staticmethod
    def normalize(query):

        query = query.lower()

        query = re.sub(
            r"\s+",
            " ",
            query
        )

        return query.strip()

    def detect_intent(self, query):

        normalized = self.normalize(query)

        for intent, keywords in self.intent_patterns.items():

            for keyword in keywords:

                if keyword in normalized:

                    return intent

        return "general"

    @staticmethod
    def detect_difficulty(query):

        query = query.lower()

        beginner = {

            "easy",
            "simple",
            "basic",
            "beginner"

        }

        advanced = {

            "advanced",
            "research",
            "mathematical",
            "proof"

        }

        if any(word in query for word in beginner):

            return "beginner"

        if any(word in query for word in advanced):

            return "advanced"

        return "intermediate"

    @staticmethod
    def requires_graph(intent):

        return intent in {

            "compare",
            "explain",
            "application"

        }

    @staticmethod
    def requires_personalization(intent):

        return intent not in {

            "definition"

        }

    def analyze(self, query):

        concepts = self.extractor.extract(query)

        concepts = ConceptFilter.filter(
            concepts
        )

        intent = self.detect_intent(query)

        difficulty = self.detect_difficulty(query)

        return QueryAnalysis(

            original_query=query,

            normalized_query=self.normalize(query),

            intent=intent,

            difficulty=difficulty,

            concepts=concepts,

            requires_graph_expansion=self.requires_graph(
                intent
            ),

            requires_personalization=self.requires_personalization(
                intent
            )

        )