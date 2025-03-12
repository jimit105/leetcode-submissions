# Approach 2: Binary Search

# Time: O(log n)
# Space: O(1)

from bisect import bisect_right, bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(nums) - bisect_right(nums, 0), bisect_left(nums, 0))
        
