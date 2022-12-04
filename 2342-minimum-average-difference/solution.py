# Approach 3: Prefix Sum Optimized

# Time: O(N)
# Space: O(1)

import math

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = math.inf
        curr_prefix_sum = 0
        
        total_sum = 0
        for index in range(n):
            total_sum += nums[index]
            
        for index in range(n):
            curr_prefix_sum += nums[index]
            
            left_part_avg = curr_prefix_sum
            left_part_avg //= (index + 1)
            
            right_part_avg = total_sum - curr_prefix_sum
            # If right part have 0 elements, then we don't divide by 0.
            if index != n - 1:
                right_part_avg //= (n - index - 1)
                
            curr_diff = abs(left_part_avg - right_part_avg)
            
            if curr_diff < min_avg_diff:
                min_avg_diff = curr_diff
                ans = index
                
        return ans
        
