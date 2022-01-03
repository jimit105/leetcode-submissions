# Approach 3 - Sliding Window Optimized (using Hash Table/dict)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        
        # store the current index of char
        mp = {}
        
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
                
            res = max(res, j-i+1)
            mp[s[j]] = j+1
            
        return res
            
