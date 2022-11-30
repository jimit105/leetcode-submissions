# Approach: Memoization

# https://leetcode.com/problems/valid-palindrome-iii/discuss/804788/Python-Quick-Solution-during-interview

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @lru_cache(None)
        def helper(lo, hi, k):
            while lo < hi:
                if s[lo] == s[hi]:
                    lo, hi = lo + 1, hi - 1
                elif k > 0:
                    return helper(lo, hi - 1, k - 1) or helper(lo + 1, hi, k - 1)
                else:
                    return False
            return True
        
        return helper(0, len(s) - 1, k)
        
