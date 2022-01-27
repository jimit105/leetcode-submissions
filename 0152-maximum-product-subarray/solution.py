# Approach - Kadane's Algorithm

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_prod = prev_max = prev_min = nums[0]
        
        for i in range(1, len(nums)):
            curr_min = min(prev_max  * nums[i], prev_min * nums[i], nums[i])
            curr_max = max(prev_max  * nums[i], prev_min * nums[i], nums[i])
            prev_min, prev_max = curr_min, curr_max
            max_prod = max(max_prod, curr_max)
            
        return max_prod
        
