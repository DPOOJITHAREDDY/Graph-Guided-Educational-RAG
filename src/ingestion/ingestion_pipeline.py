"""
ingestion_pipeline.py

Runs the complete document ingestion process.
"""

from src.ingestion.document_manager import DocumentManager
from src.ingestion.pdf_loader import PDFLoader


class IngestionPipeline:

    def __init__(self):

        self.manager = DocumentManager()

    def ingest(self):

        all_pages = []

        subjects = self.manager.get_subjects()

        print("\nAvailable Subjects")

        for subject in subjects:
            print(f"• {subject}")

        print()

        pdfs = self.manager.get_all_pdfs()

        print(f"Found {len(pdfs)} PDF(s).\n")

        for pdf in pdfs:

            print(f"Reading {pdf.name}")

            loader = PDFLoader(pdf)

            pages = loader.extract_text()

            all_pages.extend(pages)

        print("\nDocument ingestion completed.\n")

        return all_pages