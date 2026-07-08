"""
text_cleaner.py

Performs basic text cleaning before chunking.
"""

import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove tabs
        text = text.replace("\t", " ")

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        return text.strip()