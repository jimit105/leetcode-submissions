# Approach 2 - HashMap

# Time: O(N)
# Space: O(1)

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        
        for ch in t:
            if ch not in count_s or count_s[ch] == 0:
                return ch
            else:
                count_s[ch] -= 1
        
