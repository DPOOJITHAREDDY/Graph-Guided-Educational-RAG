"""
mastery_tracker.py

Personalized Mastery Tracker

Improvements
------------
1. Diminishing learning gains
2. Adaptive forgetting
3. Confidence based on mastery + historical accuracy
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

            # ---------------------------------------
            # Diminishing learning
            # High mastery -> smaller improvement
            # ---------------------------------------

            gain = (
                self.learning_rate *
                (1.0 - profile.mastery)
            )

            profile.mastery = min(
                1.0,
                profile.mastery + gain
            )

        else:

            profile.incorrect += 1

            # ---------------------------------------
            # Adaptive forgetting
            # Strong knowledge is more resilient
            # ---------------------------------------

            loss = (
                self.forgetting_rate *
                profile.mastery
            )

            profile.mastery = max(
                0.0,
                profile.mastery - loss
            )

        # ---------------------------------------
        # Historical accuracy
        # ---------------------------------------

        if profile.attempts > 0:

            accuracy = (
                profile.correct /
                profile.attempts
            )

        else:

            accuracy = 0.0

        # ---------------------------------------
        # Confidence combines
        # long-term mastery
        # +
        # observed performance
        # ---------------------------------------

        profile.confidence = round(

            (
                0.6 * profile.mastery
                +
                0.4 * accuracy
            ),

            4

        )

        profile.last_reviewed = (
            datetime.now().isoformat()
        )

        return profile