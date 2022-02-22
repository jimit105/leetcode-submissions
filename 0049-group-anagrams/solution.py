# Approach 1 - Categorize by Sorted String

# Time: O(n k log k), n = length of strs, k = max lenth of string in strs
# Space: O(n*k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)
            
        return hashmap.values()
        
