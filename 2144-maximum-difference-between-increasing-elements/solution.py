# Approach: Prefix Minimum Value

# Time: O(n)
# Space: O(1)

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans, pre_min = -1, nums[0]

        for i in range(1, n):
            if nums[i] > pre_min:
                ans = max(ans, nums[i] - pre_min)
            else:
                pre_min = nums[i]

        return ans
