# Approach 1: Using Counter

# Time: O(N)

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
            
        return -1
        
