class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        
        while xor:            
            count += 1
            xor = xor & (xor-1)
            
        return count
        
