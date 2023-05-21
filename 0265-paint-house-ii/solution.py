# Approach 1: Memoization

# Time: O(n * k^2)
# Space: O(n * k)

from functools import lru_cache
import math

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])

        @lru_cache(maxsize=None)
        def memo_solve(house_num, color):
            if house_num == n - 1:
                return costs[house_num][color]

            cost = math.inf
            for next_color in range(k):
                if next_color == color:
                    continue
                cost = min(cost, memo_solve(house_num + 1, next_color))

            return costs[house_num][color] + cost

        cost = math.inf
        for color in range(k):
            cost = min(cost, memo_solve(0, color))

        return cost
