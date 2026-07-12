"""
Test Candidate Extractor
"""

from src.knowledge_graph.candidate_extractor import CandidateExtractor


def main():

    extractor = CandidateExtractor()

    text = """
    Random Forest is an ensemble learning algorithm based on
    Decision Trees. It is widely used for Classification and
    Regression tasks. The model uses Bootstrap Sampling.
    """

    candidates = extractor.extract(text)

    print("=" * 60)

    print("CANDIDATES")

    print("=" * 60)

    for candidate in candidates:
        print(candidate)


if __name__ == "__main__":
    main()