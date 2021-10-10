class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Brian Kernighan's Algorithm
        
        while left < right:
            right = right & (right-1)
            
        return left & right
