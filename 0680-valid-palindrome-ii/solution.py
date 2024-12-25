# Approach: Two Pointers

# Time: O(n)
# Space: O(1)

class Solution:
    def check_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.check_palindrome(s, i, j - 1) or self.check_palindrome(s, i+ 1, j)
            i += 1
            j -= 1

        return True
