# Approach 2 - Bitwise Operators : Turn off the Rightmost 1-bit

# Time: O(1)
# Space: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0
        
