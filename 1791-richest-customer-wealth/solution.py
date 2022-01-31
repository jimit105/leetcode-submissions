# Approach 1 - Row Sum Maximum

# Time: O(M.N)
# Space: O(1)

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        return max([sum(account) for account in accounts])
        
