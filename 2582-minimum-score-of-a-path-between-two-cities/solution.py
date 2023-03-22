# Approach 1: Breadth First Search

from collections import deque

class Solution:
    def bfs(self, n, adj):
        visited = [False] * (n + 1)
        q = deque()
        ans = float('inf')

        q.append(1)

        while q:
            node = q.popleft()
            visited[node] = True

            for edge in adj[node]:
                ans = min(ans, edge[1])

                if not visited[edge[0]]:
                    q.append(edge[0])

        return ans


    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        return self.bfs(n, adj)
