# Approach 1: Two Pointers

# Time: O(N)
# Space: O(N)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        
        chars = list(s)
        left, right = 0, len(chars) - 1
        
        while left < right:
            left_char, right_char = chars[left], chars[right]
            
            if left_char in vowels and right_char in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
            elif left_char in vowels:
                right -= 1
                
            elif right_char in vowels:
                left += 1
                
            else:
                left += 1
                right -= 1
                
        return ''.join(chars)
        
