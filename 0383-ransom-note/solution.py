# Approach 3 - One HashMap

# Time: O(m), m = length of magazine

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letters = Counter(magazine)
        
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            
            letters[c] -= 1
            
        return True
        
        
        
