# Approach - Sliding Window

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, k = len(haystack), len(needle)
        
        if haystack[0 : k] == needle:
            return 0
        
        for i in range(k, n):
            if haystack[i - k + 1 : i + 1] == needle:
                return i - k + 1
            
        return -1
        
