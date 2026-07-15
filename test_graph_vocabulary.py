from src.learning.concept_graph import ConceptGraph

SUBJECT = "Machine_Learning"

graph = ConceptGraph()
graph.load(SUBJECT)

print("=" * 80)
print("GRAPH INFORMATION")
print("=" * 80)

print(f"Nodes : {graph.graph.number_of_nodes()}")
print(f"Edges : {graph.graph.number_of_edges()}")

print("\nFIRST 100 CONCEPTS\n")

for concept in list(graph.graph.nodes())[:100]:
    print(concept)