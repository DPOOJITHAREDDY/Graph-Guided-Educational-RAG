"""
knowledge_tracer.py

Tracks and updates the student's knowledge state.
"""

from src.student_model.mastery_tracker import MasteryTracker


class KnowledgeTracer:

    def __init__(self):

        self.mastery_tracker = MasteryTracker()

    def process_answer(
        self,
        student_state,
        concept,
        correct
    ):

        profile = student_state.get_profile(concept)

        self.mastery_tracker.update(
            profile,
            correct
        )

        return profile