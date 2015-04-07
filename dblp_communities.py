#!/usr/bin/python
import json, community
import networkx as nx
import matplotlib.pyplot as plt

data_filename = 'dblp_coauthorship.json'
g = nx.Graph()

with open(data_filename, 'r') as data_file:
    data = json.load(data_file)
    for line in data[:1000]:
        g.add_edge(line[0], line[1])

nx.transitivity(g)
part = community.best_partition(g)
count = list(set([i for i in part.values()]))
mod = community.modularity(part, g)
values = [part.get(node) for node in g.nodes()]
nx.draw_networkx(g, cmap=plt.get_cmap('jet'), node_color=values, node_size=30, with_labels=False)
plt.show()

print "Number of nodes: ", g.number_of_nodes()    
print "Number of edges: ", g.number_of_edges()
print "Number of communities: ", len(count)
print "Modularity: ", mod
