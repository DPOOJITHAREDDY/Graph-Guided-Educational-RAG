"""
query_analyzer.py

Analyzes student queries for adaptive learning.
"""

import re

from src.adaptive_learning.query_analysis import QueryAnalysis
from src.adaptive_learning.query_concept_extractor import (
    QueryConceptExtractor,
)


class QueryAnalyzer:
    """
    Converts a raw student question into a structured
    QueryAnalysis object.
    """

    def __init__(self, concept_vocabulary):

        self.extractor = QueryConceptExtractor(
            concept_vocabulary
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
    def _normalize(query):

        query = query.lower()

        query = re.sub(
            r"\s+",
            " ",
            query
        )

        return query.strip()

    def _detect_intent(self, query):

        normalized = self._normalize(query)

        for intent, keywords in self.intent_patterns.items():

            for keyword in keywords:

                if keyword in normalized:

                    return intent

        return "general"

    @staticmethod
    def _detect_difficulty(query):

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
    def _requires_graph(intent):

        return intent in {
            "compare",
            "explain",
            "application"
        }

    @staticmethod
    def _requires_personalization(intent):

        return intent != "definition"

    def analyze(self, query):

        concepts = self.extractor.extract(query)

        intent = self._detect_intent(query)

        difficulty = self._detect_difficulty(query)

        return QueryAnalysis(

            original_query=query,

            normalized_query=self._normalize(query),

            intent=intent,

            difficulty=difficulty,

            concepts=concepts,

            requires_graph_expansion=self._requires_graph(
                intent
            ),

            requires_personalization=self._requires_personalization(
                intent
            )
        )