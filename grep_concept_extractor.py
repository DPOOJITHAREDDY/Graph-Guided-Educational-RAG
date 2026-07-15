from pathlib import Path

for file in Path(".").rglob("*.py"):
    if file.name == "grep_concept_extractor.py":
        continue

    text = file.read_text(encoding="utf-8", errors="ignore")

    if "ConceptExtractor(" in text:
        print(file)