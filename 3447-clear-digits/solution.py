# Approach 2: Stack

# Time: O(n)
# Space: O(n)

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isdigit() and stack:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
        
