This is "harmonic" centrality metric realization for networkx library. 

It uses HyperLogLog algorithm and much more faster than standart algorithm from networkx.

---
Harmonic centrality is calculated as ![formula](http://upload.wikimedia.org/math/b/b/0/bb039f0850211e3f763c648178cb30b4.png).

Harmonic centrality is often better than classic centrality algorithms(PageRank, Katz, Closeness, Betweenness). See this: https://events.yandex.ru/lib/talks/1287/ video for details

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
