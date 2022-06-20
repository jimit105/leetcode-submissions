# Approach 2 - First Occurence Transformation

# Time: O(n)
# Space: O(n)

class Solution:
    def transform_string(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for idx, char in enumerate(s):
            if char not in index_mapping:
                index_mapping[char] = idx
            new_str.append(str(index_mapping[char]))
            
        return ' '.join(new_str)
    
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform_string(s) == self.transform_string(t)
