# Approach 1: Depth First Search
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/2864718/number-of-nodes-in-the-sub-tree-with-the-same-label/comments/1753388

# Time: O(n)
# Space: O(n)

import string

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        counts = [0] * len(string.ascii_lowercase)
        ans = [0] * n

        def dfs(node, parent):
            index = ord(labels[node]) - ord('a')
            previous = counts[index]
            counts[index] += 1

            for child in graph[node]:
                if child != parent:
                    dfs(child, node)

            ans[node] = counts[index] - previous

        dfs(0, -1)
        return ans

