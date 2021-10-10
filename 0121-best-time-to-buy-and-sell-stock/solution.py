class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            
            if profit > max_profit:
                max_profit = profit
                
            # if the current prices is less than buy, then the max_profit will be from buying current stock
            if buy > prices[i]:
                buy = prices[i]
                
        return max_profit
    
    
# Time: O(n) - single pass
# Space: O(1)
