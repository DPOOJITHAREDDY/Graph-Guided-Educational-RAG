"""
document_manager.py

Scans the knowledge base and discovers all PDF documents.
"""

from pathlib import Path


class DocumentManager:

    def __init__(self, knowledge_base="data/knowledge_base"):
        self.knowledge_base = Path(knowledge_base)

    def get_all_pdfs(self):
        """
        Recursively find every PDF in every subject folder.
        """

        return sorted(self.knowledge_base.rglob("*.pdf"))

    def get_subjects(self):
        """
        Return all available subjects.
        """

        return sorted(
            folder.name
            for folder in self.knowledge_base.iterdir()
            if folder.is_dir()
        )