# Approach 1: Depth First Search

from collections import defaultdict

class Solution:
    def dfs(self, node, adj, visit):
        count = 1
        visit[node] = True
        if node not in adj:
            return count
        for neighbor in adj[node]:
            if not visit[neighbor]:
                count += self.dfs(neighbor, adj, visit)
        return count


    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        num_pairs = 0
        size_of_component = 0
        remaining_nodes = n

        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                size_of_component = self.dfs(i, adj, visit)
                num_pairs += size_of_component * (remaining_nodes - size_of_component)
                remaining_nodes -= size_of_component

        return num_pairs
