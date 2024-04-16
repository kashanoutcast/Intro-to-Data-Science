# April 16, 2024
# CSC461 – Assignment 3 - Q1 & Q2
# Ch. M. Kashan Akram
# FA21-BSE-066
# Create an undirected graph described by the adjacency matrix & run Dijkstra

import networkx as nx
import matplotlib.pyplot as plt
import random

#Q1

G = nx.Graph()

nodes = ["A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(nodes)

edges = [("A","C"),("A","E"),("A","G"), ("B","B"), ("B","F"), ("C","A"), ("C","F"), ("C","G"), ("D","E"), ("E","A"), ("E","D"), ("F","B"), ("F","C"), ("F","G"), ("G","A"), ("G","C"), ("G","F")]
G.add_edges_from(edges)

#Three loops exist within the graph. One between A,C & G, another between C,G & F and another with B itself

#Q2

for u, v in edges:
    G[u][v]['weight'] = random.randint(1, 10)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

shortest_path = nx.dijkstra_path(G, source="A", target="B")
shortest_path_length = nx.dijkstra_path_length(G, source="A", target="B")

print("Shortest Path:", shortest_path)
print("Length of Shortest Path:", shortest_path_length)