# Approach 2 - Binary Search

# Time: O(n*log m), Space: O(1)

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            total_time = 0
            
            for pile in piles:
                total_time += math.ceil(pile / mid)
                
            if total_time <= h:
                right = mid
            else:
                left = mid + 1
                
        return right
