# Approach 1: Dijkstra's Algorithm

# m = len(edges)
# Time: O((n + m) log n)
# Space: O(n + m)

from collections import defaultdict
import heapq

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        mark_set = set(marked)
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {s: 0}

        min_heap = [(0, s)]

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if node in mark_set:
                return dist[node]

            for next_node, weight in adj[node]:
                new_dist = distance + weight

                if new_dist < dist.get(next_node, float('inf')):
                    dist[next_node] = new_dist
                    heapq.heappush(min_heap, (new_dist, next_node))

        return -1

        
