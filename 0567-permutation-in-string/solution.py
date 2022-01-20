from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2, c1 = len(s1), len(s2), Counter(s1)
        
        for i in range(n2-n1+1):
            if Counter(s2[i:i+n1]) == c1:
                return True
            
        return False
        
