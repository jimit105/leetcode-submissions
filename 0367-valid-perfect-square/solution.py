# Approach 1: Binary Search
    
# Time: O(log N)
# Space: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guessed_square = x * x
            
            if guessed_square == num:
                return True
            elif guessed_square > num:
                right = x - 1
            else:
                left = x + 1
                
        return False
        
