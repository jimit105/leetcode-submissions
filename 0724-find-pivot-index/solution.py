# Approach 1 - Prefix Sum

# Time: O(n)
# Space: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        
        for i, x in enumerate(nums):
            if left_sum == (s - left_sum - x):
                return i
            left_sum += x
            
        return -1
        
