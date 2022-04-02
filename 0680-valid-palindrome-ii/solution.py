# Approach: Two Pointers

# Time: O(N)
# Space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)
            i += 1
            j -= 1
            
        return True
        
