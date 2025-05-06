# Approach 1: Build As Required

# Time: O(n)
# Space: O(1)

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
        
