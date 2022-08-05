# Approach 1: Top-Down Dynamic Programming

# Let T be the target value, N be the number of elements
# Time: O(T*N)
# Space: O(T)

import functools

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # Potential Optimization
        nums.sort()
        
        @functools.lru_cache(maxsize = None)
        def combs(remain):
            if remain == 0:
                return 1
            
            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)
                    
                # Potential Optimization
                else:
                    break
                    
            return result
        
        return combs(target)
        
