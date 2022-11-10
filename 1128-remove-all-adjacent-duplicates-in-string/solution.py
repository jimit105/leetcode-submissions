# Approach 2: Stack

# Time: O(N)
# Space: O(N - D), D = length of all duplicates

class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        
        for ch in s:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
                
        return ''.join(output)
        
