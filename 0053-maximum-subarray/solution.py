# Approach 2 - Dynamic Programming

# Time: O(N)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            current_subarray = max(current_subarray + num, num)
            max_subarray = max(max_subarray, current_subarray)
            
        return max_subarray
