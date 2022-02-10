# Approach 2 - Bit Manipulation

# Time: O(N+M)
# Space: O(max(N, M))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        
        while y:
            x, y = x ^ y, (x & y) << 1
            
        return '{0:b}'.format(x)
        
