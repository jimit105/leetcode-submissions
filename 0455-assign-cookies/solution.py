# Approach 1: Greedy, Two Pointer

# Time: O(n log n + m log m), n = size of array `g`, m = size of array `s`
# Space: O(m + n)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        content_children = 0
        cookie_idx = 0

        while cookie_idx < len(s) and content_children < len(g):
            if s[cookie_idx] >= g[content_children]:
                content_children += 1
            cookie_idx += 1

        return content_children
        
