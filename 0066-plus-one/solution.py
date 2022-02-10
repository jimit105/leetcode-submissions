# Approach 1 - Schoolbook Addition with Carry

# Time: O(N)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n):
            idx = n - 1 - i
            
            if digits[idx] == 9:
                digits[idx] = 0
                
            else:
                digits[idx] += 1
                return digits
            
        # if all digits are 9
        return [1] + digits
        
