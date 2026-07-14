"""
prompt_constructor.py

Constructs an adaptive educational prompt using the
AdaptiveContext object.
"""

from src.adaptive_learning.adaptive_context import AdaptiveContext


class PromptConstructor:
    """
    Builds a personalized prompt for the LLM based on

    - Query analysis
    - Student mastery
    - Retrieved knowledge
    - Knowledge graph
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

        difficulty_section = self._difficulty_section(
            context.query_analysis.difficulty
        )

        mastery_section = self._mastery_section(
            context.student_profiles
        )

        output_section = self._output_section()

        prompt = f"""
You are an expert AI tutor.

Your goal is NOT simply to answer the student's question.

Your goal is to maximize the student's understanding.

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
ADAPTIVE TEACHING STRATEGY
===========================================================

{difficulty_section}

{mastery_section}

===========================================================
STUDENT KNOWLEDGE STATE
===========================================================

{student_section}

===========================================================
RETRIEVED KNOWLEDGE
===========================================================

{retrieval_section}

===========================================================
RELATED CONCEPTS
===========================================================

{graph_section}

===========================================================
OUTPUT FORMAT
===========================================================

{output_section}

===========================================================
IMPORTANT RULES
===========================================================

1. Base the explanation primarily on the retrieved knowledge.

2. Do NOT invent facts outside the retrieved context.

3. Adapt the explanation according to the learner profile.

4. Mention related concepts only when they genuinely improve understanding.

5. Avoid unnecessary repetition.

6. Use educational language suitable for the learner.

7. End with a learning summary.
"""

        return prompt.strip()

    def _difficulty_section(self, difficulty):

        if difficulty == "beginner":

            return """
Learner Level:
Beginner

Teaching Requirements

• Use simple English.

• Explain step-by-step.

• Explain every technical term.

• Use one real-world analogy.

• Avoid mathematical notation.

• Use short paragraphs.

• Encourage learning.

• Finish with one easy review question.
"""

        if difficulty == "advanced":

            return """
Learner Level:
Advanced

Teaching Requirements

• Use technical terminology.

• Include mathematical intuition.

• Compare with related algorithms.

• Discuss assumptions.

• Explain strengths and limitations.

• Mention practical trade-offs.

• Include research-level insights when appropriate.

• Finish with one challenging conceptual question.
"""

        return """
Learner Level:
Intermediate

Teaching Requirements

• Balance intuition with technical depth.

• Include practical examples.

• Explain important terminology.

• Mention common mistakes.

• Explain advantages and disadvantages.

• Finish with one review question.
"""

    def _mastery_section(self, profiles):

        if not profiles:

            return """
No previous learning history is available.

Teach the topic from first principles.
"""

        lowest = min(
            profiles,
            key=lambda p: p.mastery
        )

        mastery = lowest.mastery

        if mastery < 0.30:

            return f"""
Current Mastery

Concept:
{lowest.concept}

Mastery:
{mastery:.2f}

Teaching Strategy

• Assume weak understanding.

• Reinforce fundamentals.

• Use intuitive explanations.

• Repeat important ideas naturally.

• Avoid skipping intermediate reasoning.

• Give one memorable example.
"""

        if mastery < 0.70:

            return f"""
Current Mastery

Concept:
{lowest.concept}

Mastery:
{mastery:.2f}

Teaching Strategy

• Assume partial understanding.

• Strengthen conceptual links.

• Include practical applications.

• Clarify confusing points.

• Reinforce key terminology.
"""

        return f"""
Current Mastery

Concept:
{lowest.concept}

Mastery:
{mastery:.2f}

Teaching Strategy

• Keep the explanation concise.

• Focus on deeper understanding.

• Introduce advanced insights.

• Connect with related concepts.

• Encourage higher-level thinking.
"""
    @staticmethod
    def _retrieval_section(results):

        """
        Formats retrieved documents.
        """

        if not results:

            return "No supporting documents were retrieved."

        sections = []

        for i, result in enumerate(results, start=1):

            sections.append(

                f"""
Document {i}

Confidence : {result.confidence:.2f}

Content

{result.document.page_content}
"""

            )

        return "\n\n".join(sections)

    @staticmethod
    def _graph_section(concepts):

        """
        Formats graph-expanded concepts.
        """

        if not concepts:

            return "No related concepts available."

        concepts = concepts[:10]

        return "\n".join(

            f"• {concept}"

            for concept in concepts

        )

    @staticmethod
    def _student_section(profiles):

        """
        Formats student knowledge state.
        """

        if not profiles:

            return "No student history available."

        lines = []

        for profile in profiles:

            lines.append(

                f"""
Concept : {profile.concept}

Mastery : {profile.mastery:.2f}

Confidence : {profile.confidence:.2f}

Attempts : {profile.attempts}

Correct : {profile.correct}

Incorrect : {profile.incorrect}
"""

            )

        return "\n".join(lines)

    @staticmethod
    def _output_section():

        """
        Defines the desired answer structure.
        """

        return """
Produce the response using the following structure.

1. Direct Answer

- Answer the student's question first.

2. Explanation

- Explain the concept clearly.
- Adapt to the learner level.

3. Practical Example

- Give one realistic example.

4. Related Concepts

- Mention only the most relevant related concepts.

5. Key Takeaways

- Summarize the most important points.

6. Review Question

- Ask ONE question that checks understanding.

7. Suggested Next Topic

- Recommend the next concept the student should learn.
"""