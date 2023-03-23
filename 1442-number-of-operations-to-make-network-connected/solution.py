# Approach 1: Depth First Search

# Time: O(n + e), n = no. of nodes, e = no. of edges(connections)
# Space: O(n + e)

class Solution:
    def dfs(self, node, adj, visited):
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited)


    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj = [[] for _ in range(n)]

        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])

        num_connected_components = 0
        visited = [False for _ in range(n)]

        for i in range(n):
            if not visited[i]:
                num_connected_components += 1
                self.dfs(i, adj, visited)


        return num_connected_components - 1
