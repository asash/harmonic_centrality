from HLL import HyperLogLog
import networkx
from collections import defaultdict

def harmonic_centrality(G, max_distance=6):
    harmonic = defaultdict(lambda: 0)
    t_steps_set = defaultdict(lambda: defaultdict(lambda: HyperLogLog(10)))
    for node in G.nodes_iter():
        t_steps_set[node][0].add(str(node))
    for distance in range(1, max_distance + 1):
        for node in G.nodes_iter():
            t_steps_set[node][distance].merge(t_steps_set[node][distance-1])
            for next_node in networkx.all_neighbors(G, node):
                t_steps_set[node][distance].merge(t_steps_set[next_node][distance - 1])
            harmonic[node] += (t_steps_set[node][distance].cardinality() - t_steps_set[node][distance - 1].cardinality())/distance
    return dict(harmonic)
