# Approach 2 - Using Input Array for Output

# Time: O(n)
# Space: O(1)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        return nums
