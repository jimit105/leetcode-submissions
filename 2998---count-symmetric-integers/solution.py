# Approach 1: Enumeration

# Time: O(high - low)
# Space: O(1)

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for x in range(low, high + 1):
            if x < 100 and x % 11 == 0:
                res += 1
            if 1000 <= x < 10000:
                left = x // 1000 + x % 1000 // 100
                right = x % 100 // 10 + x  % 10
                if left == right:
                    res += 1
        return res
        
