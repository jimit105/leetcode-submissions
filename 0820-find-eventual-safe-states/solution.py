# Approach 2: Depth First Search

# Time: O(m + n), n = no. of nodes, m = no. of edges
# Space: O(m + n)

class Solution:
    # returns boolean indicating whether `node` is unsafe
    def dfs(self, node, adj, visit, in_stack) -> bool:
        if in_stack[node]:
            return True
        
        if visit[node]:
            return False

        visit[node] = True
        in_stack[node] = True

        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, in_stack):
                return True

        in_stack[node] = False
        return False


    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)

        visit = [False] * n
        in_stack = [False] * n

        for i in range(n):
            self.dfs(i, adj, visit, in_stack)

        safe_nodes = []
        for i in range(n):
            if not in_stack[i]:
                safe_nodes.append(i)

        return safe_nodes
