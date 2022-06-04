# Approach 2 - Bit Manipulation Trick

# Time: O(n)
# Space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= (n - 1)
        return count
        
