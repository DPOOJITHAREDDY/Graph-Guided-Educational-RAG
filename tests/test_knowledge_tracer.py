from src.student_model.student_state import StudentState
from src.student_model.knowledge_tracer import KnowledgeTracer


def main():

    state = StudentState()

    tracer = KnowledgeTracer()

    tracer.process_answer(
        state,
        "Random Forest",
        True
    )

    tracer.process_answer(
        state,
        "Random Forest",
        True
    )

    tracer.process_answer(
        state,
        "Random Forest",
        False
    )

    tracer.process_answer(
        state,
        "Decision Tree",
        True
    )

    tracer.process_answer(
        state,
        "Decision Tree",
        False
    )

    print("=" * 80)
    print("KNOWLEDGE TRACING")
    print("=" * 80)

    for profile in state.get_all_profiles().values():

        print(profile)
        print()


if __name__ == "__main__":

    main()