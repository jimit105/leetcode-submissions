# Approach 1: Depth First Search

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for adj in graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    dfs(adj)

        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)

        return count
