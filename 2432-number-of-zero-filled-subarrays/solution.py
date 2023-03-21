# Approach: Count the number of consecutive 0's

# Time: O(n)
# Space: O(1)

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        num_subarray = 0

        for num in nums:
            if num == 0:
                num_subarray += 1
            else:
                num_subarray = 0

            ans += num_subarray

        return ans
