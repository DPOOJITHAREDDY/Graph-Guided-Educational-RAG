"""
evaluate_query_analysis.py

Evaluates the QueryAnalyzer using the benchmark
dataset and reports multiple evaluation metrics.

Metrics

1. Intent Accuracy
2. Difficulty Accuracy
3. Concept Precision
4. Concept Recall
5. Exact Match Accuracy

Results are saved as CSV for later analysis.
"""

import csv
import json
import re

from pathlib import Path

from src.adaptive_learning.query_analyzer import QueryAnalyzer
from src.learning.concept_graph import ConceptGraph


# ==========================================================
# PATH CONFIGURATION
# ==========================================================

BASE_DIR = Path(
    __file__
).resolve().parent.parent


QUESTION_FILES = [

    BASE_DIR
    / "test_questions"
    / "beginner_questions.json",

    BASE_DIR
    / "test_questions"
    / "intermediate_questions.json",

    BASE_DIR
    / "test_questions"
    / "advanced_questions.json"

]


OUTPUT_FILE = (

    BASE_DIR

    / "results"

    / "query_analysis.csv"

)


# ==========================================================
# NORMALIZATION
# ==========================================================

def normalize(text):
    """
    Normalizes text before comparison.
    """

    text = text.lower()

    text = text.replace(
        "-",
        " "
    )

    text = re.sub(

        r"[^a-z0-9 ]",

        "",

        text

    )

    text = re.sub(

        r"\s+",

        " ",

        text

    )

    return text.strip()


def normalize_list(items):
    """
    Normalizes every concept.
    """

    normalized = set()

    for item in items:

        normalized.add(

            normalize(item)

        )

    return normalized


# ==========================================================
# DATASET LOADING
# ==========================================================

def load_questions():
    """
    Loads every benchmark question.
    """

    questions = []

    for file in QUESTION_FILES:

        with open(

            file,

            "r",

            encoding="utf-8"

        ) as f:

            questions.extend(

                json.load(f)

            )

    return questions


# ==========================================================
# QUERY ANALYZER
# ==========================================================

print("=" * 80)
print("LOADING KNOWLEDGE GRAPH")
print("=" * 80)

concept_graph = ConceptGraph()

concept_graph.load(
    "Machine_Learning"
)

vocabulary = list(
    concept_graph.graph.nodes()
)

print(
    f"Vocabulary Size : {len(vocabulary)}"
)

query_analyzer = QueryAnalyzer(
    vocabulary
)

print()

print("QUERY ANALYZER READY")

print()

# ==========================================================
# LOAD BENCHMARK
# ==========================================================

questions = load_questions()

print("=" * 80)

print("BENCHMARK LOADED")

print("=" * 80)

print(

    f"Questions Loaded : {len(questions)}"

)

print()


# ==========================================================
# METRIC COUNTERS
# ==========================================================

results = []

intent_correct = 0

difficulty_correct = 0

exact_match = 0

total_expected_concepts = 0

total_predicted_concepts = 0

total_correct_concepts = 0


print("=" * 80)

print("STARTING QUERY ANALYSIS EVALUATION")

print("=" * 80)

print()
# ==========================================================
# MAIN EVALUATION LOOP
# ==========================================================

for sample in questions:

    print("-" * 80)

    print(

        f"Question {sample['id']}"

    )

    print(

        sample["question"]

    )

    analysis = query_analyzer.analyze(

    sample["question"]

    )

    predicted_intent = (

        analysis.intent

    )

    predicted_difficulty = (

        analysis.difficulty

    )

    predicted_concepts = normalize_list(

        analysis.concepts

    )

    expected_intent = (

        sample["expected_intent"]

    )

    expected_difficulty = (

        sample["expected_difficulty"]

    )

    expected_concepts = normalize_list(

        sample["expected_concepts"]

    )

    # ------------------------------------------------------
    # Intent Evaluation
    # ------------------------------------------------------

    intent_ok = (

        predicted_intent

        ==

        expected_intent

    )

    if intent_ok:

        intent_correct += 1

    # ------------------------------------------------------
    # Difficulty Evaluation
    # ------------------------------------------------------

    difficulty_ok = (

        predicted_difficulty

        ==

        expected_difficulty

    )

    if difficulty_ok:

        difficulty_correct += 1

    # ------------------------------------------------------
    # Concept Evaluation
    # ------------------------------------------------------

    correct_concepts = (

        predicted_concepts

        &

        expected_concepts

    )

    total_correct_concepts += len(

        correct_concepts

    )

    total_expected_concepts += len(

        expected_concepts

    )

    total_predicted_concepts += len(

        predicted_concepts

    )

    # ------------------------------------------------------
    # Exact Match
    # ------------------------------------------------------

    exact = (

        intent_ok

        and

        difficulty_ok

        and

        predicted_concepts

        ==

        expected_concepts

    )

    if exact:

        exact_match += 1

    # ------------------------------------------------------
    # Store Result
    # ------------------------------------------------------

    results.append(

        {

            "id":

                sample["id"],

            "question":

                sample["question"],

            "expected_intent":

                expected_intent,

            "predicted_intent":

                predicted_intent,

            "expected_difficulty":

                expected_difficulty,

            "predicted_difficulty":

                predicted_difficulty,

            "expected_concepts":

                ", ".join(

                    sorted(

                        expected_concepts

                    )

                ),

            "predicted_concepts":

                ", ".join(

                    sorted(

                        predicted_concepts

                    )

                ),

            "intent_correct":

                intent_ok,

            "difficulty_correct":

                difficulty_ok,

            "exact_match":

                exact

        }

    )

    print(

        f"Intent      : {predicted_intent}"

    )

    print(

        f"Difficulty  : {predicted_difficulty}"

    )

    print(

        f"Concepts    : {analysis.concepts}"

    )

    print()
# ==========================================================
# METRIC CALCULATION
# ==========================================================

total_questions = len(

    questions

)

intent_accuracy = (

    intent_correct

    / total_questions

) * 100


difficulty_accuracy = (

    difficulty_correct

    / total_questions

) * 100


if total_predicted_concepts == 0:

    concept_precision = 0.0

else:

    concept_precision = (

        total_correct_concepts

        / total_predicted_concepts

    ) * 100


if total_expected_concepts == 0:

    concept_recall = 0.0

else:

    concept_recall = (

        total_correct_concepts

        / total_expected_concepts

    ) * 100


exact_match_accuracy = (

    exact_match

    / total_questions

) * 100


# ==========================================================
# CSV EXPORT
# ==========================================================

OUTPUT_FILE.parent.mkdir(

    parents=True,

    exist_ok=True

)

fieldnames = [

    "id",

    "question",

    "expected_intent",

    "predicted_intent",

    "expected_difficulty",

    "predicted_difficulty",

    "expected_concepts",

    "predicted_concepts",

    "intent_correct",

    "difficulty_correct",

    "exact_match"

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

    writer.writerows(

        results

    )


print()

print("=" * 80)

print("CSV FILE GENERATED")

print("=" * 80)

print(

    OUTPUT_FILE

)

print()
# ==========================================================
# FINAL SUMMARY
# ==========================================================

print("=" * 80)

print("QUERY ANALYSIS EVALUATION RESULTS")

print("=" * 80)

print()

print(

    f"Total Questions            : {total_questions}"

)

print(

    f"Intent Accuracy            : {intent_accuracy:.2f}%"

)

print(

    f"Difficulty Accuracy        : {difficulty_accuracy:.2f}%"

)

print(

    f"Concept Precision          : {concept_precision:.2f}%"

)

print(

    f"Concept Recall             : {concept_recall:.2f}%"

)

print(

    f"Exact Match Accuracy       : {exact_match_accuracy:.2f}%"

)

print()

print("=" * 80)

print("METRIC DETAILS")

print("=" * 80)

print(

    f"Correct Intent Predictions : {intent_correct}"

)

print(

    f"Correct Difficulty         : {difficulty_correct}"

)

print(

    f"Correct Concepts           : {total_correct_concepts}"

)

print(

    f"Expected Concepts          : {total_expected_concepts}"

)

print(

    f"Predicted Concepts         : {total_predicted_concepts}"

)

print(

    f"Exact Matches              : {exact_match}"

)

print()

print("=" * 80)

print("OUTPUT")

print("=" * 80)

print(

    f"CSV Results : {OUTPUT_FILE}"

)

print()

print("=" * 80)

print("QUERY ANALYSIS EVALUATION COMPLETED")

print("=" * 80)