# Approach 1: Build String
# Time: O(M + N)
# Space: O(N + M)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(st):
            ans = []
            for c in st:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        
        return build(s) == build(t)
        
