"""
learning_update_engine.py

Updates the student model after every learning interaction.
"""

from src.student_model.mastery_tracker import MasteryTracker


class LearningUpdateEngine:
    """
    Updates student mastery using the reflection results.
    """

    def __init__(self):

        self.mastery_tracker = MasteryTracker()

    def update(
        self,
        adaptive_context,
        reflection_result
    ):
        """
        Update all student profiles.

        Returns
        -------
        list
            Updated StudentProfile objects.
        """

        updated_profiles = []

        for profile in adaptive_context.student_profiles:

            correct = (

                profile.concept
                not in reflection_result.weak_concepts

            )

            updated_profile = self.mastery_tracker.update(

                profile=profile,

                correct=correct

            )

            updated_profiles.append(
                updated_profile
            )

        return updated_profiles