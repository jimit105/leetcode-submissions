# Approach 1: Insert characters in a new string

# Time: O(n)
# Space: O(n)

class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        freq = 1
        ans = s[0]

        for i in range(1, len(s)):
            if s[i] == prev:
                freq += 1
            else:
                prev = s[i]
                freq = 1

            if freq < 3:
                ans += s[i]

        return ans
