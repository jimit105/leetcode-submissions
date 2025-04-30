# Approach 2: Convert to String

# N = len(nums), M = max(nums)
# Time: O(N * log M)
# Space: O(log M)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            len_ = len(str(num))
            if len_ % 2 == 0:
                result += 1

        return result
        
