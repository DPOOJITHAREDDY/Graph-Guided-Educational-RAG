from src.student_model.student_state import StudentState


def main():

    state = StudentState()

    # Simulate student answering questions

    state.update_profile(
        "Random Forest",
        True
    )

    state.update_profile(
        "Random Forest",
        True
    )

    state.update_profile(
        "Random Forest",
        False
    )

    state.update_profile(
        "Decision Tree",
        False
    )

    state.update_profile(
        "Decision Tree",
        True
    )

    print("=" * 80)
    print("STUDENT STATE")
    print("=" * 80)

    for profile in state.get_all_profiles().values():

        print(profile)

        print()


if __name__ == "__main__":

    main()