import networkx as nx
import matplotlib.pyplot as plt
import sys

def generate_graph(nodecount):
    # Generate a random acyclic directed graph
    graph = nx.gnr_graph(nodecount, 0.3)

    # Display the graph
    nx.draw(graph, with_labels=True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dag_cli.py <nodecount>")
        sys.exit(1)

    nodecount = int(sys.argv[1])
    generate_graph(nodecount)