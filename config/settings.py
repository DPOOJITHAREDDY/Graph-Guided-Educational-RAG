"""
settings.py

Global configuration for the Graph-Guided Educational RAG project.
"""

# ==========================================================
# DATA PATHS
# ==========================================================

KNOWLEDGE_BASE_PATH = "data/knowledge_base"

PROCESSED_DATA_PATH = "data/processed"

VECTOR_DB_PATH = "data/vector_db"

KNOWLEDGE_GRAPH_PATH = "data/knowledge_graph"


# ==========================================================
# CHUNKING
# ==========================================================

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150


# ==========================================================
# EMBEDDING MODEL
# ==========================================================

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# ==========================================================
# VECTOR DATABASE
# ==========================================================

TOP_K = 5


# ==========================================================
# KNOWLEDGE GRAPH
# ==========================================================

GRAPH_SEARCH_DEPTH = 2


# ==========================================================
# HALLUCINATION DETECTION
# ==========================================================

CONFIDENCE_THRESHOLD = 0.75


# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "Graph-Guided Educational RAG"

VERSION = "1.0.0"

# ==========================
# Gemini
# ==========================

LLM_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.2

MAX_OUTPUT_TOKENS = 1024