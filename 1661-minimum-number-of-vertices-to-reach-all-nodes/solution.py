# Approach: In-Degree Count

# Time: O(N + E), N = no. of vertices, E = no. of edges
# Space: O(N)

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_incoming_edge_exists = [False] * n

        for edge in edges:
            is_incoming_edge_exists[edge[1]] = True

        required_nodes = []

        for vertex, value in enumerate(is_incoming_edge_exists):
            if not value:
                required_nodes.append(vertex)

        return required_nodes

