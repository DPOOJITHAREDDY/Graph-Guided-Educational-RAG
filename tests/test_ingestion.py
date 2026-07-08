from src.ingestion.ingestion_pipeline import IngestionPipeline

pipeline = IngestionPipeline()

pages = pipeline.ingest()

print("=" * 80)
print("Total Pages:", len(pages))
print("=" * 80)

print("\nFirst Page:\n")

print("Subject :", pages[0]["subject"])
print("Document:", pages[0]["document"])
print("Page    :", pages[0]["page"])

print()

print(pages[0]["text"][:1500])