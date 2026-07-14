"""
test_engine_import.py

Runs one complete adaptive learning query and
prints intermediate analysis.
"""

from src.adaptive_learning.adaptive_learning_engine import (
    AdaptiveLearningEngine
)

print("=" * 80)
print("CREATING ENGINE")
print("=" * 80)

engine = AdaptiveLearningEngine(
    "Machine_Learning"
)

print("\nENGINE CREATED SUCCESSFULLY\n")

question = "Explain Random Forest in simple terms."

print("=" * 80)
print("QUESTION")
print("=" * 80)
print(question)

print("\n")

# -------------------------------------------------------
# Query Analysis
# -------------------------------------------------------

analysis = engine.query_analyzer.analyze(
    question
)

print("=" * 80)
print("QUERY ANALYSIS")
print("=" * 80)

print(f"Intent      : {analysis.intent}")
print(f"Difficulty  : {analysis.difficulty}")
print(f"Concepts    : {analysis.concepts}")

print("\nGenerating answer...\n")

# -------------------------------------------------------
# Adaptive Pipeline
# -------------------------------------------------------

result = engine.answer_question(
    question
)

print("=" * 80)
print("ANSWER")
print("=" * 80)

print(result["answer"])

print("\n")

print("=" * 80)
print("REFLECTION")
print("=" * 80)

print(result["reflection"])

print("\n")

print("=" * 80)
print("UPDATED STUDENT PROFILES")
print("=" * 80)

for profile in result["profiles"]:

    print(profile)