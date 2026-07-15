"""
evaluate_student_model.py

Evaluates Dynamic Knowledge Tracing using the
Student Model.
"""

import csv
from pathlib import Path

from src.student_model.student_profile import StudentProfile
from src.student_model.mastery_tracker import MasteryTracker

# ==========================================================
# OUTPUT
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_FILE = (
    BASE_DIR
    / "results"
    / "student_model_results.csv"
)

# ==========================================================
# TEST CONCEPTS
# ==========================================================

concepts = [

    "Random Forest",

    "Decision Tree",

    "Support Vector Machine",

    "Neural Network",

    "Gradient Descent"

]

# ==========================================================
# TRACKER
# ==========================================================

tracker = MasteryTracker()

results = []

print("=" * 80)
print("STUDENT MODEL EVALUATION")
print("=" * 80)

for concept in concepts:

    print()
    print("-" * 80)
    print(concept)
    print("-" * 80)

    profile = StudentProfile(
        concept=concept
    )

    # ------------------------------------------------------
    # Simulated Learning History
    # ------------------------------------------------------

    learning_sequence = [

        True,
        True,
        False,
        True,
        True

    ]

    for attempt, correct in enumerate(

        learning_sequence,

        start=1

    ):

        tracker.update(

            profile,

            correct

        )

        print(

            f"Attempt {attempt} | "

            f"Correct={correct} | "

            f"Mastery={profile.mastery:.2f} | "

            f"Confidence={profile.confidence:.2f}"

        )

        results.append(

            {

                "concept": concept,

                "attempt": attempt,

                "correct": correct,

                "mastery": profile.mastery,

                "confidence": profile.confidence,

                "total_attempts": profile.attempts,

                "correct_answers": profile.correct,

                "incorrect_answers": profile.incorrect

            }

        )

# ==========================================================
# SAVE CSV
# ==========================================================

OUTPUT_FILE.parent.mkdir(

    parents=True,

    exist_ok=True

)

fieldnames = [

    "concept",

    "attempt",

    "correct",

    "mastery",

    "confidence",

    "total_attempts",

    "correct_answers",

    "incorrect_answers"

]

with open(

    OUTPUT_FILE,

    "w",

    newline="",

    encoding="utf-8"

) as csvfile:

    writer = csv.DictWriter(

        csvfile,

        fieldnames=fieldnames

    )

    writer.writeheader()

    writer.writerows(results)

# ==========================================================
# SUMMARY
# ==========================================================

print()

print("=" * 80)
print("STUDENT MODEL EVALUATION COMPLETE")
print("=" * 80)

print(f"Concepts Evaluated : {len(concepts)}")

print(f"Learning Attempts  : {len(results)}")

print()

print("Results saved to:")

print(OUTPUT_FILE)

print()

print("=" * 80)