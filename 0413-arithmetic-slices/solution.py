# Approach 4 - Dynamic Programming

# Time: O(n)
# Space: O(n)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        total = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1]  == nums[i-1] - nums[i - 2]:
                dp[i] = 1 + dp[i - 1]
                total += dp[i]
                
        return total
        
