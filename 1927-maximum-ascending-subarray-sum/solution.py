# Approach 2: Linear Scan

# Time: O(n)
# Space: O(1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_subarray_sum = nums[0]

        for curr_idx in range(1, len(nums)):
            if nums[curr_idx] <= nums[curr_idx - 1]:
                # If the current element is not greater than the previous one, update maxSum
                max_sum = max(max_sum, curr_subarray_sum)
                curr_subarray_sum = 0
            curr_subarray_sum += nums[curr_idx]

        # Final check after the loop ends to account for the last ascending subarray
        return max(max_sum, curr_subarray_sum)
        
