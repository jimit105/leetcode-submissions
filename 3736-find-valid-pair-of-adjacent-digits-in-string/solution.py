# Time: O(n)
# Space: O(1)

from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)

        for i in range(len(s) - 1):
            first = s[i]
            second = s[i + 1]

            if (first != second and
                freq[first] == int(first) and
                freq[second] == int(second)):

                return first + second

        return ''
        
