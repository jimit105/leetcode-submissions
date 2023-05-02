# Approach 2: Track the Sign of the Product

# Time: O(n)
# Space: O(1)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign *= -1

        return sign
            
        
