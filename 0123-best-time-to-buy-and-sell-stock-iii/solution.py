# Approach 1 - Bidirectional Dynamic Programming

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        left_min, right_max = prices[0], prices[-1]
        
        n = len(prices)
        left_profits = [0] * n
        right_profits = [0] * (n + 1)
        
        for l in range(1, n):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])
            
            r = n - 1 - l
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])
            
        max_profit = 0
        for i in range(0, n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
            
        return max_profit
