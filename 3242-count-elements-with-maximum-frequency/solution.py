# Approach 3: One-Pass Sum Max Frequencies

# Time: O(n)
# Space: O(n)

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        total_freq = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            curr_freq = freq[num]

            if curr_freq > max_freq:
                max_freq = curr_freq
                total_freq = curr_freq

            elif curr_freq == max_freq:
                total_freq += curr_freq

        return total_freq
        
