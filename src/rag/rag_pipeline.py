"""
rag_pipeline.py

End-to-end Retrieval-Augmented Generation (RAG) pipeline.
"""

from src.retrieval.search import SearchEngine
from src.llm.prompt_builder import PromptBuilder
from src.llm.answer_generator import AnswerGenerator
from src.llm.response_formatter import ResponseFormatter


class RAGPipeline:
    """
    Complete RAG pipeline.
    """

    def __init__(self):

        self.search_engine = SearchEngine()
        self.prompt_builder = PromptBuilder()
        self.answer_generator = AnswerGenerator()
        self.response_formatter = ResponseFormatter()

    def ask(self, subject, query):
        """
        Run the complete RAG pipeline.

        Parameters
        ----------
        subject : str

        query : str

        Returns
        -------
        dict
        """

        # Step 1: Retrieve relevant chunks
        retrieval_results = self.search_engine.search(
            subject=subject,
            query=query
        )

        # Step 2: Build prompt
        prompt = self.prompt_builder.build_prompt(
            query=query,
            retrieval_results=retrieval_results
        )

        # Step 3: Generate answer
        answer = self.answer_generator.generate(prompt)

        # Step 4: Format response
        response = self.response_formatter.format_response(
            answer=answer,
            retrieval_results=retrieval_results
        )

        return response