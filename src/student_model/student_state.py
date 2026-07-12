"""
student_state.py

Stores the student's knowledge profiles.
"""

from src.student_model.student_profile import StudentProfile


class StudentState:

    def __init__(self):

        self.profiles = {}

    def get_profile(self, concept):

        if concept not in self.profiles:

            self.profiles[concept] = StudentProfile(
                concept=concept
            )

        return self.profiles[concept]

    def get_all_profiles(self):

        return self.profiles