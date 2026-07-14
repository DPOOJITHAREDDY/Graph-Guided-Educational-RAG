"""
test_graph_audit.py

Generates a complete audit report for the knowledge graph.
"""

from collections import Counter

from src.learning.concept_graph import ConceptGraph


SUBJECT = "Machine_Learning"


graph = ConceptGraph()
graph.load(SUBJECT)

G = graph.graph

print("=" * 80)
print("KNOWLEDGE GRAPH AUDIT")
print("=" * 80)

print(f"Nodes : {G.number_of_nodes()}")
print(f"Edges : {G.number_of_edges()}")

print("\n")

# ----------------------------------------------------
# Single vs Multi-word
# ----------------------------------------------------

single = []
multi = []

for node in G.nodes():

    if len(node.split()) == 1:
        single.append(node)
    else:
        multi.append(node)

print(f"Single-word concepts : {len(single)}")
print(f"Multi-word concepts  : {len(multi)}")

print("\n")

# ----------------------------------------------------
# Highest Degree Nodes
# ----------------------------------------------------

print("=" * 80)
print("TOP 50 CONCEPTS")
print("=" * 80)

degrees = sorted(
    G.degree(),
    key=lambda x: x[1],
    reverse=True
)

for node, degree in degrees[:50]:

    print(f"{node:<40} {degree}")

print("\n")

# ----------------------------------------------------
# Lowest Degree
# ----------------------------------------------------

print("=" * 80)
print("LOWEST DEGREE CONCEPTS")
print("=" * 80)

for node, degree in degrees[-50:]:

    print(f"{node:<40} {degree}")

print("\n")

# ----------------------------------------------------
# Single-word Frequency
# ----------------------------------------------------

print("=" * 80)
print("MOST COMMON SINGLE-WORD CONCEPTS")
print("=" * 80)

counter = Counter(single)

for concept, count in counter.most_common(100):

    print(f"{concept:<30} {count}")

print("\n")

# ----------------------------------------------------
# Noise Candidates
# ----------------------------------------------------

noise = []

for node in G.nodes():

    if len(node) < 3:
        noise.append(node)
        continue

    if any(ch in node for ch in "│├└┐┌─═╔╗╚╝"):
        noise.append(node)

print("=" * 80)
print("SUSPECTED NOISE")
print("=" * 80)

for node in sorted(noise):

    print(node)

print("\n")

print("=" * 80)
print("AUDIT COMPLETE")
print("=" * 80)