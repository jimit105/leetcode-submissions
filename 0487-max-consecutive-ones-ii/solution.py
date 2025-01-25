# Approach 2: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        num_zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros == 2: # if the window is invalid, contract the window
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            longest_sequence = max(longest_sequence, right - left + 1)
            right += 1 # expand the sequence

        return longest_sequence
        
