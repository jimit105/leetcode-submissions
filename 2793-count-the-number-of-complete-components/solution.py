# Approach 1: Adjacency List

# m = len(edges)
# Time: O(n + m log n)
# Space: O(n + m)

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        component_freq = defaultdict(int)
        
        for vertex in range(n):
            graph[vertex] = [vertex]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1

        return sum(1 for neighbors, freq in component_freq.items() if len(neighbors) == freq)
