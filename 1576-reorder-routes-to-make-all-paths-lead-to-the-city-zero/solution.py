# Approach 1: Depth First Search

class Solution:
    def dfs(self, adj, visited, from_node):
        change = 0
        visited[from_node] = True

        for to_node in adj[from_node]:
            if not visited[abs(to_node)]:
                change += self.dfs(adj, visited, abs(to_node)) + (1 if to_node > 0 else 0)
        
        return change


    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for conn in connections:
            adj[conn[0]].append(conn[1])
            adj[conn[1]].append(-conn[0])

        return self.dfs(adj, visited, 0)
