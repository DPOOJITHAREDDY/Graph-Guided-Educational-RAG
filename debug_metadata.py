from src.retrieval.vector_store import VectorStore

store = VectorStore()

index, docs = store.load("Machine_Learning")

print("=" * 80)
print("DOCUMENT TYPE")
print("=" * 80)
print(type(docs[0]))

print()

print("=" * 80)
print("FIRST DOCUMENT")
print("=" * 80)
print(docs[0])

print()

print("=" * 80)
print("ATTRIBUTES")
print("=" * 80)

try:
    print(vars(docs[0]))
except Exception:
    print(docs[0].__dict__)