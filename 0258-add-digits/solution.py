# Approach 1 - Mathematical: Digital Root

# Time: O(1)
# Space: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        
