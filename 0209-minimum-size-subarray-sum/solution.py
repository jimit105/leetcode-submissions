# Approach: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_of_curr_window = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sum_of_curr_window += nums[right]

            while sum_of_curr_window >= target:
                res = min(res, right - left + 1)
                sum_of_curr_window -= nums[left]
                left += 1

        return res if res != float('inf') else 0
