# Approach 2: Advanced Graph Theory + Iterative Depth-First Search

# Time: O(n)
# Space: O(n)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)

        return len(seen) == n
        
