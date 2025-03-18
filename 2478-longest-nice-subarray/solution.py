# Approach 2: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0 # Track bits used in current window
        window_start = 0
        max_length = 0

        for window_end in range(len(nums)):
            # If current number shares bits with window, shrink window from left until there's no bit conflict
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[window_start] # Remove leftmost element's bits
                window_start += 1

            # Add current number to window
            used_bits |= nums[window_end]

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

        
