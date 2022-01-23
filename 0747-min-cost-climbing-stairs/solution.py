# Approach 2 - Top-Down Dynamic Programming (Recursion + Memoization)

# Time: O(N)
# Space: O(N)

from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache(maxsize = None)
        def minimum_cost(i):
            if i <= 1:
                return 0
            
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
                        
            return min(down_one, down_two)
        
        return minimum_cost(len(cost))
        
