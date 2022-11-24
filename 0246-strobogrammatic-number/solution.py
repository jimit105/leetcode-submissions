# Approach 1: Make a Rotated Copy

# Time: O(N)
# Space: O(N)

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9' :'6'}
        
        rotated_string_array = []
        
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_array.append(rotated_digits[c])
            
        rotated_string = ''.join(rotated_string_array)
        
        return rotated_string == num
        
