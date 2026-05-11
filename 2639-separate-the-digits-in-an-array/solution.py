# Approach 2: Reverse Traversal

# Time: O(n log M), n = len(nums), M = max(nums)
# Space: O(1)

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            while x > 0:
                res.append(x % 10)
                x //= 10
            
        res.reverse()
        return res

