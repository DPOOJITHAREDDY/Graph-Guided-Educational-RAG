"""
prompt_builder.py

Builds prompts for the Gemini model using retrieved documents.
"""


class PromptBuilder:
    """
    Builds grounded prompts for educational question answering.
    """

    def __init__(self):
        pass

    def build_prompt(self, query, retrieval_results):
        """
        Build the prompt using the retrieved chunks.

        Parameters
        ----------
        query : str
            User question

        retrieval_results : List[RetrievalResult]

        Returns
        -------
        str
        """

        context = []

        for result in retrieval_results:

            document = result.document

            context.append(
                f"""
Source:
Subject: {document.metadata['subject']}
Document: {document.metadata['document']}
Page: {document.metadata['page']}

Content:
{document.page_content}
"""
            )

        context = "\n\n".join(context)

        prompt = f"""
You are an intelligent educational tutor.

Your job is to answer ONLY using the provided textbook context.

Instructions:

1. Answer only from the provided context.
2. If the answer is not available, clearly say:
   "The provided textbook does not contain enough information."
3. Explain concepts clearly.
4. Use simple language suitable for engineering students.
5. If appropriate, include examples from the context.
6. Never invent facts.
7. Never use outside knowledge.

======================================================
TEXTBOOK CONTEXT
======================================================

{context}

======================================================
QUESTION
======================================================

{query}

======================================================
ANSWER
======================================================
"""

        return prompt