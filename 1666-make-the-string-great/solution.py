# Approach 3: Stack
    
# Time: O(n)
# Space: O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for curr_char in list(s):
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
                
        return ''.join(stack)
        
