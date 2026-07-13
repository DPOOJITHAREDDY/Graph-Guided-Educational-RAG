"""
query_analysis.py

Data model representing the analyzed user query.
"""

from dataclasses import dataclass, field


@dataclass
class QueryAnalysis:
    """
    Structured representation of a student's query.

    This object is passed throughout the adaptive learning
    pipeline instead of using dictionaries.
    """

    # Original user question
    original_query: str

    # Cleaned version used internally
    normalized_query: str

    # Detected user intent
    # Examples:
    # explain, compare, quiz, summary, definition...
    intent: str

    # Estimated learner difficulty
    # beginner / intermediate / advanced
    difficulty: str

    # Concepts detected in the query
    concepts: list[str] = field(default_factory=list)

    # Should related concepts be retrieved
    requires_graph_expansion: bool = False

    # Should student mastery influence retrieval
    requires_personalization: bool = True