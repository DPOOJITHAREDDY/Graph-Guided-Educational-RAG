"""
evaluate_reflection.py

Evaluates the Reflection Engine using a
small representative benchmark.
"""

import time
import csv
from pathlib import Path

from google.api_core.exceptions import ResourceExhausted

from src.adaptive_learning.adaptive_learning_engine import (
    AdaptiveLearningEngine
)

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_FILE = (
    BASE_DIR
    / "results"
    / "reflection_results.csv"
)

SUBJECT = "Machine_Learning"

# ==========================================================
# REPRESENTATIVE BENCHMARK
# ==========================================================

questions = [

    {
        "question": "Explain Random Forest in simple terms."
    },

    {
        "question": "Compare Precision and Recall."
    },

    {
        "question": "Explain why feature scaling is important for Support Vector Machine."
    },

    {
        "question": "Explain Retrieval Augmented Generation from a research perspective."
    },

    {
        "question": "Explain how a Knowledge Graph improves Retrieval Augmented Generation from a research perspective."
    }

]

# ==========================================================
# INITIALIZATION
# ==========================================================

print("=" * 80)
print("LOADING ADAPTIVE LEARNING ENGINE")
print("=" * 80)

engine = AdaptiveLearningEngine(
    SUBJECT
)

print("\nENGINE READY\n")

print("=" * 80)
print("BENCHMARK LOADED")
print("=" * 80)

print(f"Questions Loaded : {len(questions)}")

print()

results = []

total_understanding = 0.0
total_confidence = 0.0
total_coverage = 0.0
total_grounding = 0.0
total_alignment = 0.0
total_overall = 0.0

review_count = 0

print("=" * 80)
print("STARTING REFLECTION EVALUATION")
print("=" * 80)

for sample in questions:

    question = sample["question"]

    print()
    print("-" * 80)
    print(question)

    while True:

        try:

            result = engine.answer_question(
                question
            )

            break

        except ResourceExhausted as e:

            print("\n" + "=" * 80)
            print("GEMINI QUOTA EXCEEDED")
            print("=" * 80)
            print(e)
            print("Waiting 60 seconds...\n")

            time.sleep(60)

    reflection = result["reflection"]

    print(
        f"Overall Score        : {reflection.overall_score:.4f}"
    )

    print(
        f"Understanding        : {reflection.understanding_score:.4f}"
    )

    print(
        f"Coverage             : {reflection.coverage_score:.4f}"
    )

    print(
        f"Grounding            : {reflection.grounding_score:.4f}"
    )

    print(
        f"Confidence           : {reflection.confidence_score:.4f}"
    )

    print(
        f"Difficulty Alignment : {reflection.difficulty_alignment_score:.4f}"
    )

    print(
        f"Review Required      : {reflection.should_review}"
    )

    print()

    total_understanding += (
        reflection.understanding_score
    )

    total_confidence += (
        reflection.confidence_score
    )

    total_coverage += (
        reflection.coverage_score
    )

    total_grounding += (
        reflection.grounding_score
    )

    total_alignment += (
        reflection.difficulty_alignment_score
    )

    total_overall += (
        reflection.overall_score
    )

    if reflection.should_review:
        review_count += 1

    results.append(

        {

            "question": question,

            "overall_score":
                reflection.overall_score,

            "understanding_score":
                reflection.understanding_score,

            "coverage_score":
                reflection.coverage_score,

            "grounding_score":
                reflection.grounding_score,

            "confidence_score":
                reflection.confidence_score,

            "difficulty_alignment_score":
                reflection.difficulty_alignment_score,

            "strengths":
                ", ".join(
                    reflection.strengths
                ),

            "weak_concepts":
                ", ".join(
                    reflection.weak_concepts
                ),

            "covered_concepts":
                ", ".join(
                    reflection.covered_concepts
                ),

            "missing_concepts":
                ", ".join(
                    reflection.missing_concepts
                ),

            "recommended_review":
                ", ".join(
                    reflection.recommended_review
                ),

            "next_learning_topics":
                ", ".join(
                    reflection.next_learning_topics
                ),

            "feedback":
                reflection.feedback,

            "should_review":
                reflection.should_review

        }

    )

# ==========================================================
# METRICS
# ==========================================================

total_questions = len(questions)

average_understanding = (
    total_understanding / total_questions
    if total_questions else 0.0
)

average_confidence = (
    total_confidence / total_questions
    if total_questions else 0.0
)

average_coverage = (
    total_coverage / total_questions
    if total_questions else 0.0
)

average_grounding = (
    total_grounding / total_questions
    if total_questions else 0.0
)

average_alignment = (
    total_alignment / total_questions
    if total_questions else 0.0
)

average_overall = (
    total_overall / total_questions
    if total_questions else 0.0
)

review_rate = (
    review_count / total_questions
) * 100

# ==========================================================
# SAVE CSV
# ==========================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

fieldnames = [

    "question",

    "overall_score",

    "understanding_score",

    "coverage_score",

    "grounding_score",

    "confidence_score",

    "difficulty_alignment_score",

    "strengths",

    "weak_concepts",

    "covered_concepts",

    "missing_concepts",

    "recommended_review",

    "next_learning_topics",

    "feedback",

    "should_review"

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
print("REFLECTION EVALUATION RESULTS")
print("=" * 80)

print(f"Total Questions              : {total_questions}")
print(f"Average Overall Score        : {average_overall:.4f}")
print(f"Average Understanding        : {average_understanding:.4f}")
print(f"Average Coverage             : {average_coverage:.4f}")
print(f"Average Grounding            : {average_grounding:.4f}")
print(f"Average Confidence           : {average_confidence:.4f}")
print(f"Average Difficulty Alignment : {average_alignment:.4f}")
print(f"Review Required              : {review_count}")
print(f"Review Rate                  : {review_rate:.2f}%")

print()
print("Results saved to:")
print(OUTPUT_FILE)

print()

print("=" * 80)
print("REFLECTION EVALUATION COMPLETE")
print("=" * 80)