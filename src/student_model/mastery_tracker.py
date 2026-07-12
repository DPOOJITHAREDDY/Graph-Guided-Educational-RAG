"""
mastery_tracker.py

Updates the student's mastery for concepts.
"""

from datetime import datetime


class MasteryTracker:

    def __init__(
        self,
        learning_rate=0.10,
        forgetting_rate=0.15
    ):

        self.learning_rate = learning_rate
        self.forgetting_rate = forgetting_rate

    def update(
        self,
        profile,
        correct
    ):

        profile.attempts += 1

        if correct:

            profile.correct += 1

            profile.mastery = min(
                1.0,
                profile.mastery + self.learning_rate
            )

        else:

            profile.incorrect += 1

            profile.mastery = max(
                0.0,
                profile.mastery - self.forgetting_rate
            )

        profile.confidence = profile.mastery

        profile.last_reviewed = datetime.now().isoformat()

        return profile