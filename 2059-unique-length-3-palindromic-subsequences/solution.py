# Approach 1: Count Letters In-Between

# Time: O(n)
# Space: O(1), letters and between cannot grow beyond a size of 26, since s only contains letters of the English alphabet.

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            ans += len(between)

        return ans
        
