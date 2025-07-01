# Approach 1: One-time traversal

# Time: O(n)
# Space: O(1)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, ans = len(word), 1

        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans
