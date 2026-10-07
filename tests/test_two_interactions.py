from src.adaptive_learning.adaptive_learning_engine import AdaptiveLearningEngine

engine = AdaptiveLearningEngine("Machine_Learning")

questions = [
    "Explain Random Forest in simple terms.",
    "How does Random Forest work and why is it better than a single Decision Tree?"
]

for i, question in enumerate(questions, 1):

    print("\n" + "=" * 80)
    print(f"INTERACTION {i}")
    print("=" * 80)

    print(f"\nQUESTION:\n{question}")

    analysis = engine.query_analyzer.analyze(question)

    print("\nQUERY ANALYSIS")
    print("-" * 40)
    print(f"Intent     : {analysis.intent}")
    print(f"Difficulty : {analysis.difficulty}")
    print(f"Concepts   : {analysis.concepts}")

    print("\nGenerating answer...\n")

    result = engine.answer_question(question)

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(result["answer"])

    print("\n" + "=" * 80)
    print("REFLECTION")
    print("=" * 80)
    print(result["reflection"])

    print("\n" + "=" * 80)
    print("UPDATED STUDENT PROFILES")
    print("=" * 80)

    for profile in result["profiles"]:
        print(profile)