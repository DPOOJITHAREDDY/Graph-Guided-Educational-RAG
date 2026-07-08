"""
storage_manager.py

Generic storage manager for saving and loading project artifacts.
"""

import pickle
from pathlib import Path


class StorageManager:

    @staticmethod
    def save(data, base_path, subject, filename):
        """
        Save any Python object to the specified project directory.
        """

        subject_folder = Path(base_path) / subject
        subject_folder.mkdir(parents=True, exist_ok=True)

        filepath = subject_folder / filename

        with open(filepath, "wb") as file:
            pickle.dump(data, file)

        print(f"Saved: {filepath}")

    @staticmethod
    def load(base_path, subject, filename):
        """
        Load a previously saved Python object.
        """

        filepath = Path(base_path) / subject / filename

        if not filepath.exists():
            return None

        with open(filepath, "rb") as file:
            return pickle.load(file)

    @staticmethod
    def exists(base_path, subject, filename):
        """
        Check whether an artifact already exists.
        """

        filepath = Path(base_path) / subject / filename

        return filepath.exists()