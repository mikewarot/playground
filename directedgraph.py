import networkx as nx
from ipywidgets import interact, IntSlider
import matplotlib.pyplot as plt
def generate_graph(nodecount):
    # Generate a random acyclic directed graph
    graph = nx.gnr_graph(nodecount, 0.3)

    # Display the graph
    nx.draw(graph, with_labels=True)
    plt.show()

interact(generate_graph, nodecount=IntSlider(min=1, max=20, step=1, value=10))
