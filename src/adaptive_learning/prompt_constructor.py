"""
prompt_constructor.py

Constructs the final prompt sent to the LLM using the
AdaptiveContext object.
"""

from src.adaptive_learning.adaptive_context import AdaptiveContext


class PromptConstructor:
    """
    Builds a structured educational prompt from the
    adaptive learning context.
    """

    def build(self, context: AdaptiveContext) -> str:

        retrieval_section = self._retrieval_section(
            context.retrieval_results
        )

        graph_section = self._graph_section(
            context.related_concepts
        )

        student_section = self._student_section(
            context.student_profiles
        )

        prompt = f"""
You are an expert AI tutor.

Your objective is to teach the student rather than simply answer the question.

===========================================================
QUESTION
===========================================================

{context.question}

===========================================================
QUERY ANALYSIS
===========================================================

Intent:
{context.query_analysis.intent}

Difficulty:
{context.query_analysis.difficulty}

Detected Concepts:
{", ".join(context.query_analysis.concepts)}

===========================================================
RETRIEVED KNOWLEDGE
===========================================================

{retrieval_section}

===========================================================
RELATED CONCEPTS
===========================================================

{graph_section}

===========================================================
STUDENT KNOWLEDGE STATE
===========================================================

{student_section}

===========================================================
INSTRUCTIONS
===========================================================

1. Answer the student's question accurately.
2. Adapt the explanation to the detected difficulty.
3. Focus on concepts with low mastery.
4. Use the retrieved knowledge as the primary source.
5. Mention related concepts only when they improve understanding.
6. Avoid hallucinating facts outside the provided context.
7. End with a short learning summary.
"""

        return prompt.strip()

    @staticmethod
    def _retrieval_section(results):

        if not results:
            return "No supporting documents retrieved."

        sections = []

        for result in results:

            sections.append(
                result.document.page_content
            )

        return "\n\n".join(sections)

    @staticmethod
    def _graph_section(concepts):

        if not concepts:
            return "None"

        return ", ".join(concepts)

    @staticmethod
    def _student_section(profiles):

        if not profiles:
            return "No student history available."

        lines = []

        for profile in profiles:

            lines.append(

                f"{profile.concept}\n"
                f"Mastery: {profile.mastery:.2f}\n"
                f"Confidence: {profile.confidence:.2f}\n"
                f"Attempts: {profile.attempts}\n"
                f"Correct: {profile.correct}\n"
                f"Incorrect: {profile.incorrect}"

            )

        return "\n\n".join(lines)