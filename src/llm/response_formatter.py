"""
response_formatter.py

Formats the final RAG response.
"""


class ResponseFormatter:
    """
    Formats the generated answer together with source references.
    """

    def format_response(self, answer, retrieval_results):
        """
        Format answer and references.

        Parameters
        ----------
        answer : str

        retrieval_results : List[RetrievalResult]

        Returns
        -------
        dict
        """

        references = []

        seen = set()

        for result in retrieval_results:

            document = result.document

            reference = {
                "subject": document.metadata["subject"],
                "document": document.metadata["document"],
                "page": document.metadata["page"]
            }

            key = (
                reference["document"],
                reference["page"]
            )

            if key not in seen:

                seen.add(key)

                references.append(reference)

        return {
            "answer": answer,
            "references": references
        }