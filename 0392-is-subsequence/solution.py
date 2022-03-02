# Approach 2 - Two-Pointers

# Time: O(T), T = length of target string
# Space: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
        
        p_left, p_right = 0, 0
        
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
            
        return p_left == LEFT_BOUND
  
        
