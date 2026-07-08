"""
vector_store.py

Handles saving and loading FAISS indexes.
"""

import faiss
import pickle
from pathlib import Path

from config.settings import VECTOR_DB_PATH

FAISS_INDEX_FILE = "faiss.index"
METADATA_FILE = "metadata.pkl"


class VectorStore:
    """
    Handles persistent storage of FAISS indexes and document metadata.
    """

    def __init__(self):

        self.base_path = Path(VECTOR_DB_PATH)

    def save(self, index, documents, subject):

        subject_folder = self.base_path / subject
        subject_folder.mkdir(parents=True, exist_ok=True)

        index_path = subject_folder / FAISS_INDEX_FILE
        metadata_path = subject_folder / METADATA_FILE

        faiss.write_index(index, str(index_path))

        with open(metadata_path, "wb") as file:
            pickle.dump(documents, file)

        print(f"\nFAISS index saved to : {index_path}")
        print(f"Metadata saved to    : {metadata_path}")

    def load(self, subject):

        subject_folder = self.base_path / subject

        index_path = subject_folder / FAISS_INDEX_FILE
        metadata_path = subject_folder / METADATA_FILE

        if not index_path.exists():
            raise FileNotFoundError(f"FAISS index not found: {index_path}")

        if not metadata_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {metadata_path}")

        index = faiss.read_index(str(index_path))

        with open(metadata_path, "rb") as file:
            documents = pickle.load(file)

        return index, documents

    def exists(self, subject):

        subject_folder = self.base_path / subject

        index_path = subject_folder / FAISS_INDEX_FILE
        metadata_path = subject_folder / METADATA_FILE

        return index_path.exists() and metadata_path.exists()