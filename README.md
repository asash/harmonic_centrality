This is "harmonic" centrality metric realisation for networkx library. 

It uses HyperLogLog algorithm and much more faster than standart algorithm from networkx


example usage:
```python

from networkx import Graph
from harmonic_centrality import harmonic_centrality
G = Graph()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)
harmonic = harmonic_centrality(G)

for node in harmonic:
    print node, harmonic[node]
```

output:
```
1 4.33868071575
2 3.61485913805
3 3.61485913805
4 2.89174614742
```
