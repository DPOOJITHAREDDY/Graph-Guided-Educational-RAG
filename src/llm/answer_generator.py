"""
answer_generator.py

Generates answers using the configured LLM.
"""

from config.settings import (
    TEMPERATURE,
    MAX_OUTPUT_TOKENS
)

from src.llm.llm_factory import LLMFactory


class AnswerGenerator:
    """
    Generates answers using Gemini.
    """

    def __init__(self):

        self.model = LLMFactory().get_model()

    def generate(self, prompt):
        """
        Generate an answer from the prompt.

        Parameters
        ----------
        prompt : str

        Returns
        -------
        str
        """

        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_OUTPUT_TOKENS
            }
        )

        return response.text.strip()