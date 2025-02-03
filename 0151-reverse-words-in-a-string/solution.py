# Approach 1: Built-in Split + Reverse

# Time: O(n)
# Space: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
        
