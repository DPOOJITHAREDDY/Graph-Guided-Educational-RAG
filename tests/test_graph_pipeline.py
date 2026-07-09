"""
Test Graph Pipeline
"""

from pathlib import Path

from src.knowledge_graph.graph_pipeline import GraphPipeline


def main():

    pipeline = GraphPipeline()

    pipeline.build(
        subject="Machine_Learning",
        save_path=Path(
            "data/knowledge_graph/Machine_Learning/knowledge_graph.pkl"
        )
    )


if __name__ == "__main__":
    main()