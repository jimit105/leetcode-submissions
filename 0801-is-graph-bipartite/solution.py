# Approach 1: Coloring by Depth-First Search

# Time: O(N + E), N = no. of node_idxs, E = no. of edges
# Space: O(N)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        for node_idx in range(len(graph)):
            if node_idx not in color:
                stack = [node_idx]
                color[node_idx] = 0

                while stack:
                    node_idx = stack.pop()
                    for neighbor in graph[node_idx]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = color[node_idx] ^ 1
                        elif color[neighbor] == color[node_idx]:
                            return False

        return True

