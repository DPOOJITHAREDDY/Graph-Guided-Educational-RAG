"""
metadata.py

Creates standardized metadata for every document chunk.
"""

from datetime import datetime


class MetadataManager:

    @staticmethod
    def create(
        subject,
        document,
        page,
        source_type="Textbook"
    ):

        return {

            "subject": subject,

            "document": document,

            "page": page,

            "source_type": source_type,

            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "version": 1
        }