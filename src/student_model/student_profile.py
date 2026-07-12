"""
student_profile.py

Represents the student's knowledge state for a concept.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class StudentProfile:

    concept: str

    mastery: float = 0.0

    confidence: float = 0.0

    attempts: int = 0

    correct: int = 0

    incorrect: int = 0

    difficulty: float = 0.5

    last_reviewed: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )