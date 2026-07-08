from config.settings import PROCESSED_DATA_PATH

from src.ingestion.ingestion_pipeline import IngestionPipeline
from src.preprocessing.chunker import Chunker
from src.storage.storage_manager import StorageManager


pipeline = IngestionPipeline()

pages = pipeline.ingest()

chunker = Chunker()

chunks = chunker.create_chunks(pages)

subject = chunks[0].metadata["subject"]


StorageManager.save(
    data=chunks,
    base_path=PROCESSED_DATA_PATH,
    subject=subject,
    filename="chunks.pkl"
)


loaded_chunks = StorageManager.load(
    base_path=PROCESSED_DATA_PATH,
    subject=subject,
    filename="chunks.pkl"
)


print()

print("Original :", len(chunks))
print("Loaded   :", len(loaded_chunks))

print()

print(
    "Exists   :",
    StorageManager.exists(
        PROCESSED_DATA_PATH,
        subject,
        "chunks.pkl"
    )
)