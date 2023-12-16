import networkx as nx
import matplotlib.pyplot as plt

# Generate a random acyclic directed graph
graph = nx.gnr_graph(10, 0.3)

# Display the graph
nx.draw(graph, with_labels=True)
plt.show()
