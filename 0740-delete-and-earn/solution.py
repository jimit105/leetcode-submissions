# Approach 1 - Dynamic Programming

# Time: O(N log N) # due to sorting
# Space: O(N)

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        prev = None
        avoid, using = 0, 0
        
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
                
            prev = k
            
        return max(avoid, using)
        
