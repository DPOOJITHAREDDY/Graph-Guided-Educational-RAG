"""
chunker.py

Converts extracted pages into LangChain Documents
and splits them into semantic chunks.
"""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import CHUNK_SIZE, CHUNK_OVERLAP
from src.preprocessing.text_cleaner import TextCleaner
from src.utils.metadata import MetadataManager


class Chunker:
    """
    Converts page-wise extracted text into LangChain Documents
    and splits them into semantic chunks.
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def create_chunks(self, pages):

        documents = []

        # Step 1: Convert extracted pages into LangChain Documents
        for page in pages:

            cleaned_text = TextCleaner.clean(page["text"])

            metadata = MetadataManager.create(
                subject=page["subject"],
                document=page["document"],
                page=page["page"],
                source_type="Textbook"
            )

            document = Document(
                page_content=cleaned_text,
                metadata=metadata
            )

            documents.append(document)

        # Step 2: Split into semantic chunks
        chunks = self.splitter.split_documents(documents)

        # Step 3: Add unique chunk IDs
        for index, chunk in enumerate(chunks, start=1):

            chunk.metadata["chunk_id"] = f"chunk_{index:06d}"

        return chunks