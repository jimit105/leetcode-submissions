# Approach 5: Constant Space Dynamic Programming
    
# Time: O(n)
# Space: O(1)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = 0
        sum_ = 0
        
        for i in range(2, len(nums)):
            if (nums[i] - nums[i-1]) == (nums[i-1] - nums[i-2]):
                dp += 1
                sum_ += dp
            else:
                dp = 0
                
        return sum_
        
