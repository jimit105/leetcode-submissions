# Approach 1: Depth First Search, Recursive

# Time: O(n^3)
# Space: O(n^2)

import collections

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def dfs(curr, visited):
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            return len(visited)

        answer = 0
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))

        return answer

