# Approach 1: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        longest_window = 0
        start = 0 # left-end of the window

        for i in range(len(nums)):
            zero_count += 1 if nums[i] == 0 else 0

            while zero_count > 1:
                zero_count -= 1 if nums[start] == 0 else 0
                start += 1

            longest_window = max(longest_window, i - start)

        return longest_window

