# Approach: Sliding Window

# n = len(s), m = len(t)
# Time: O(m + n)
# Space: O(m + n)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''

        t_count = Counter(t)
        required = len(t_count) # No. of unique chars in t

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0
        window_counts = {}

        left, right = 0, 0
        min_length = float('inf')
        min_start = 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # If all required characters are found in the window
            while left <= right and formed == required:
                char = s[left]

                # If the current window size is smaller than the min window size
                if min_length > right - left + 1:
                    min_length = right - left + 1
                    min_start = left

                window_counts[char] -= 1

                if char in t_count and window_counts[char] < t_count[char]:
                    # If the character is in t and its count in the window is less than its count in t
                    formed -= 1 
                left += 1 # shrink window

            right += 1 # expand window

        if min_length > len(s):
            return ''

        return s[min_start : min_start + min_length]

