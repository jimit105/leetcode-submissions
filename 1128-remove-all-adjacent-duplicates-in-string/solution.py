# Approach 2: Stack

# n = string length, d = total length of all duplicates
# Time: O(n)
# Space: O(n - d)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
        
