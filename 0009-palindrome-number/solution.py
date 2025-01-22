# Approach: Reverse Number and compare

# Time: O(log x)
# Space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False

        # Single digit numbers are palindrome
        if x < 10:
            return True

        # Reverse the number and compare
        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num
        
