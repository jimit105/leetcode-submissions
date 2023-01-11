# Approach 1: Depth First Search
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/2864715/minimum-time-to-collect-all-apples-in-a-tree/comments/1752768

# Time: O(n)
# Space: O(n)

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            res = 0
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    children_time = dfs(neighbor)
                    if children_time > 0 or hasApple[neighbor]:
                        res += children_time + 2

            return res

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        return dfs(0)
