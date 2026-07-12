from src.student_model.student_profile import StudentProfile


def main():

    profile = StudentProfile(
        concept="Random Forest"
    )

    print("=" * 60)
    print("STUDENT PROFILE")
    print("=" * 60)

    print(profile)


if __name__ == "__main__":
    main()
    