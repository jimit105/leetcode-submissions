# Approach 1 - Bit by Bit

class Solution:
    def reverseBits(self, n: int) -> int:
        ans, power = 0, 31
        while n:
            
            # retrieve the right most bit and reverse to correct position
            ans += (n & 1) << power
            n = n >> 1
            power -= 1
            
        return ans
        
