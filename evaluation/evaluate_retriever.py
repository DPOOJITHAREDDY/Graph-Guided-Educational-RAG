"""
evaluate_retriever.py

Evaluates semantic retrieval performance of the
Adaptive Educational RAG system.
"""

import csv
import json
import time
from pathlib import Path

from src.retrieval.retriever import Retriever

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

QUESTION_FILES = [

    BASE_DIR / "test_questions" / "beginner_questions.json",

    BASE_DIR / "test_questions" / "intermediate_questions.json",

    BASE_DIR / "test_questions" / "advanced_questions.json"

]

OUTPUT_FILE = (

    BASE_DIR

    / "results"

    / "retrieval_results.csv"

)

SUBJECT = "Machine_Learning"


# ==========================================================
# LOAD QUESTIONS
# ==========================================================

def load_questions():

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
# INITIALIZATION
# ==========================================================

print("=" * 80)
print("LOADING RETRIEVER")
print("=" * 80)

retriever = Retriever()

print("\nRETRIEVER READY\n")

questions = load_questions()

print("=" * 80)
print("BENCHMARK LOADED")
print("=" * 80)

print(f"Questions Loaded : {len(questions)}")

print()

results = []

total_time = 0.0

total_confidence = 0.0

retrieval_count = 0

successful = 0

print("=" * 80)
print("STARTING RETRIEVAL EVALUATION")
print("=" * 80)

for sample in questions:

    question = sample["question"]

    print()

    print("-" * 80)

    print(question)

    start = time.perf_counter()

    retrieved = retriever.retrieve(

        subject=SUBJECT,

        query=question

    )

    elapsed = time.perf_counter() - start

    total_time += elapsed

    if retrieved:

        successful += 1

    for result in retrieved:

        retrieval_count += 1

        total_confidence += result.confidence

        print(

            f"[{result.rank}] "

            f"Confidence={result.confidence:.3f} "

            f"Distance={result.distance:.3f}"

        )

        preview = (

            result.document.page_content

            .replace("\n", " ")

            [:120]

        )

        print(preview)

        print()

        results.append(

            {

                "question": question,

                "rank": result.rank,

                "confidence": result.confidence,

                "distance": result.distance,

                "retrieval_time": result.retrieval_time,

                "content": result.document.page_content

            }

        )
# ==========================================================
# METRICS
# ==========================================================

total_questions = len(questions)

average_time = (

    total_time / total_questions

    if total_questions else 0.0

)

average_confidence = (

    total_confidence / retrieval_count

    if retrieval_count else 0.0

)

success_rate = (

    successful / total_questions

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

    "rank",

    "confidence",

    "distance",

    "retrieval_time",

    "content"

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

print("RETRIEVAL EVALUATION RESULTS")

print("=" * 80)

print(f"Total Questions           : {total_questions}")

print(f"Successful Retrievals     : {successful}")

print(f"Success Rate              : {success_rate:.2f}%")

print(f"Average Retrieval Time    : {average_time:.4f} seconds")

print(f"Average Confidence        : {average_confidence:.4f}")

print(f"Total Retrieved Chunks    : {retrieval_count}")

print()

print(f"Detailed results saved to:")

print(OUTPUT_FILE)

print()

print("=" * 80)

print("RETRIEVAL EVALUATION COMPLETE")

print("=" * 80)