# Approach: Depth First Search

# V = no. of vertices, E = no. of edges
# Time: O(V + E)
# Space: O(V)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0: unvisited, 1: visiting, 2: safe
        state = [0] * n
        safe = []

        def dfs(node):
            # If node is being visited, we found a cycle
            if state[node] == 1:
                return False

            # If node has been fully visited, return if it's safe
            if state[node] == 2:
                return True

            # Mark node as being visited
            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # Mark node as safe
            state[node] = 2
            return True

        for i in range(n):
            if dfs(i):
                safe.append(i)
        
        return safe
        
