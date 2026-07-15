from pathlib import Path

from config.settings import KNOWLEDGE_GRAPH_PATH
from src.knowledge_graph.graph_pipeline import GraphPipeline

SUBJECT = "Machine_Learning"

save_path = (
    Path(KNOWLEDGE_GRAPH_PATH)
    / SUBJECT
    / "knowledge_graph.pkl"
)

pipeline = GraphPipeline()

pipeline.build(
    subject=SUBJECT,
    save_path=save_path
)

print("\nKnowledge Graph rebuilt successfully.")