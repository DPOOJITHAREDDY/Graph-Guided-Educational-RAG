"""
pdf_loader.py

Loads a single PDF and extracts page-wise text.
"""

from pathlib import Path
import fitz


class PDFLoader:

    def __init__(self, pdf_path):

        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

    def extract_text(self):

        document = fitz.open(self.pdf_path)

        pages = []

        for page_number, page in enumerate(document):

            pages.append(
                {
                    "subject": self.pdf_path.parent.name,
                    "document": self.pdf_path.name,
                    "page": page_number + 1,
                    "text": page.get_text("text").strip(),
                }
            )

        document.close()

        return pages