from src.adaptive_learning.adaptive_learning_engine import AdaptiveLearningEngine


def print_header(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_list(items, limit=8):
    if not items:
        print("None identified.")
        return

    for item in items[:limit]:
        print(f"- {item}")

    if len(items) > limit:
        print(f"... and {len(items) - limit} more")


def main():

    print("=" * 80)
    print("        GRAPH-GUIDED EDUCATIONAL RAG")
    print("        LIVE ADAPTIVE LEARNING DEMO")
    print("=" * 80)

    print("\nInitializing system...")

    engine = AdaptiveLearningEngine("Machine_Learning")

    print("\nSystem ready.")
    print("Type 'exit' to stop the demo.")

    while True:

        print("\n" + "-" * 80)

        question = input("Ask your question: ").strip()

        if question.lower() == "exit":

            print("\nExiting demo...")

            break

        if not question:
            continue

        print("\nGenerating answer...")

        result = engine.answer_question(question)

        context = result["context"]

        # --------------------------------------------------
        # ANSWER
        # --------------------------------------------------

        print_header("ANSWER")

        print(result["answer"])

        input("\nPress ENTER to view the system analysis...")

        # --------------------------------------------------
        # QUERY ANALYSIS
        # --------------------------------------------------

        print_header("QUERY ANALYSIS")

        analysis = context.query_analysis

        print(f"Intent      : {analysis.intent}")
        print(f"Difficulty  : {analysis.difficulty}")
        print(f"Concepts    : {analysis.concepts}")

        # --------------------------------------------------
        # HYBRID RETRIEVAL
        # --------------------------------------------------

        print_header("HYBRID RETRIEVAL")

        retrieval_results = context.retrieval_results

        print(f"Retrieved chunks : {len(retrieval_results)}")

        if retrieval_results:

            avg_confidence = (
                sum(r.confidence for r in retrieval_results)
                / len(retrieval_results)
            )

            total_time = sum(
                r.retrieval_time
                for r in retrieval_results
            )

            print(
                f"Average confidence : "
                f"{avg_confidence:.4f}"
            )

            print(
                f"Total retrieval time : "
                f"{total_time:.4f} seconds"
            )

            print("\nTop retrieved results:")

            for r in retrieval_results[:3]:

                print(
                    f"  Rank {r.rank} | "
                    f"Confidence: {r.confidence:.4f} | "
                    f"Distance: {r.distance:.4f}"
                )

        else:

            print("No retrieval results found.")

        # --------------------------------------------------
        # RETRIEVED CONCEPTS
        # --------------------------------------------------

        print_header("RETRIEVED CONCEPTS")

        print_list(
            context.retrieved_concepts,
            limit=8
        )

        # --------------------------------------------------
        # KNOWLEDGE GRAPH
        # --------------------------------------------------

        print_header("KNOWLEDGE GRAPH")

        related = context.related_concepts

        print(
            f"Related concepts found : "
            f"{len(related)}"
        )

        if related:

            print("\nTop related concepts:")

            # Display the concepts that were actually
            # selected during graph expansion together
            # with their graph edge weights.

            displayed = set()

            for concept in analysis.concepts:

                neighbors = (
                    engine.context_builder.graph
                    .get_learning_neighbors(concept)
                )

                for neighbor, weight in neighbors:

                    if neighbor not in related:
                        continue

                    if neighbor in displayed:
                        continue

                    displayed.add(neighbor)

                    print(
                        f"- {neighbor} "
                        f"| Weight: {weight:.4f}"
                    )

                    if len(displayed) >= 8:
                        break

                if len(displayed) >= 8:
                    break

            if not displayed:

                print_list(
                    related,
                    limit=8
                )

            if len(related) > 8:

                print(
                    f"... and "
                    f"{len(related) - 8} more"
                )

        else:

            print("No related concepts identified.")

        # --------------------------------------------------
        # ADAPTIVE CONTEXT
        # --------------------------------------------------

        print_header("ADAPTIVE CONTEXT")

        print(f"Question : {context.question}")

        print("\nLearner knowledge used:")

        if context.student_profiles:

            for profile in context.student_profiles:

                print(
                    f"- {profile.concept} | "
                    f"Mastery: {profile.mastery:.3f} | "
                    f"Confidence: {profile.confidence:.3f} | "
                    f"Attempts: {profile.attempts}"
                )

        else:

            print("No previous learner profile found.")

        # --------------------------------------------------
        # REFLECTION
        # --------------------------------------------------

        print_header("REFLECTION")

        reflection = result["reflection"]

        print(
            f"Understanding        : "
            f"{reflection.understanding_score:.4f}"
        )

        print(
            f"Coverage             : "
            f"{reflection.coverage_score:.4f}"
        )

        print(
            f"Grounding            : "
            f"{reflection.grounding_score:.4f}"
        )

        print(
            f"Confidence           : "
            f"{reflection.confidence_score:.4f}"
        )

        print(
            f"Difficulty Alignment : "
            f"{reflection.difficulty_alignment_score:.4f}"
        )

        print(
            f"Overall Score        : "
            f"{reflection.overall_score:.4f}"
        )

        print(
            f"Should Review        : "
            f"{reflection.should_review}"
        )

        if reflection.weak_concepts:

            print(
                f"Weak Concepts        : "
                f"{reflection.weak_concepts}"
            )

        if reflection.next_learning_topics:

            print(
                f"Next Learning Topics : "
                f"{reflection.next_learning_topics[:5]}"
            )

        # --------------------------------------------------
        # UPDATED LEARNER MODEL
        # --------------------------------------------------

        print_header("UPDATED LEARNER MODEL")

        profiles = result["profiles"]

        if profiles:

            for profile in profiles:

                print(
                    f"Concept    : "
                    f"{profile.concept}"
                )

                print(
                    f"Mastery    : "
                    f"{profile.mastery:.3f}"
                )

                print(
                    f"Confidence : "
                    f"{profile.confidence:.3f}"
                )

                print(
                    f"Attempts   : "
                    f"{profile.attempts}"
                )

                print(
                    f"Correct    : "
                    f"{profile.correct}"
                )

                print(
                    f"Incorrect  : "
                    f"{profile.incorrect}"
                )

                print()

        else:

            print("No learner profile was updated.")

        print("-" * 80)

        print(
            "Interaction added to the learner model."
        )

        print("-" * 80)


if __name__ == "__main__":
    main()