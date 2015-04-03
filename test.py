import networkx as nx

G=nx.Graph()

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

G.add_edge('a','b')
# G.add_edge(1,2)

G.add_edge('b','c')
G.add_edge('b','c')

print G.number_of_edges()