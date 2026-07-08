"""
llm_factory.py

Loads and provides the configured LLM.
"""

import os

import google.generativeai as genai

from dotenv import load_dotenv


class LLMFactory:
    """
    Creates Gemini model instances.
    """

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        genai.configure(api_key=api_key)

    def get_model(self):

        return genai.GenerativeModel(
            "gemini-2.5-flash"
        )