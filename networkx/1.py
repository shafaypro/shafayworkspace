import networkx as nx
import matplotlib.pyplot as plot
G = nx.Graph()  # this creates agraph
#G.add_node(1)  # this adds a certain node in the graph
#listofnodes = [3, 4, 5, 6]  # a list of severat data as nodes
#G.add_nodes_from(listofnodes)  # adding of the nodes in the graph

#H = nx.path_graph(10)  # which is not in the graph , a specific path in a node
#G.add_nodes_from(H)  # Now the nodes of h will be copied in the nodes of G

# --------------------EDGES---------------
G.add_edge(1,2) # this is a tupple added as an edge since the tupple is in the form of edge,vertice
#G.add_edges_from(((3,5),(4,9)))
nx.draw(G)
plot.show()