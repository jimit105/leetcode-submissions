# Time: O(n)
# Space: O(k), k = number of unique chars in string

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        max_odd = float('-inf')
        min_even = float('inf')

        for count in freq.values():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)

        return max_odd - min_even
        
