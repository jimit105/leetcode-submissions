# Approach: Greedy - Duplicate Removal for Positive Numbers

# Time: O(n)
# Space: O(n)

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos_num_set = set([num for num in nums if num > 0])
        return max(nums) if len(pos_num_set) == 0 else sum(pos_num_set)
        
