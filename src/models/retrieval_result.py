"""
retrieval_result.py

Data model representing a retrieved document.
"""

from dataclasses import dataclass


@dataclass
class RetrievalResult:
    """
    Represents one retrieved document.
    """

    rank: int

    distance: float

    confidence: float

    document: object

    retrieval_time: float