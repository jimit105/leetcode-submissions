# Approach 2: Single Iteration

# Time: O(n)
# Space: O(1)

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len = dec_len = max_len = 1

        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                inc_len += 1
                dec_len = 1 # Reset decreasing length

            elif nums[pos + 1] < nums[pos]:
                dec_len += 1
                inc_len = 1 # Reset increasing length

            else:
                inc_len = dec_len = 1 # Reset both 

            max_len = max(max_len, inc_len, dec_len)

        return max_len
        
