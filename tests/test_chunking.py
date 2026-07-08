from src.ingestion.ingestion_pipeline import IngestionPipeline
from src.preprocessing.chunker import Chunker

pipeline = IngestionPipeline()

pages = pipeline.ingest()

chunker = Chunker()

chunks = chunker.create_chunks(pages)

print("=" * 80)
print("Total Chunks :", len(chunks))
print("=" * 80)

print()

print(chunks[0])

print()

print("=" * 80)
print("Metadata")
print("=" * 80)

print(chunks[0].metadata)

print()

print("=" * 80)
print("Chunk Preview")
print("=" * 80)

print(chunks[0].page_content[:1200])