# Approach 2 - Greedy with Stack

# Time: O(N)
# Space: O(N)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_stack = []
        
        for digit in num:
            while k and num_stack and num_stack[-1] > digit:
                num_stack.pop()
                k -= 1
                
            num_stack.append(digit)
            
        final_stack = num_stack[:-k] if k else num_stack
        
        return ''.join(final_stack).lstrip("0") or "0"
        
