# Approach 1: Sorting

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        weak_characters = 0
        max_defence = 0
        
        for _, d in properties:
            if d < max_defence:
                weak_characters += 1
            else:
                max_defence = d
                
        return weak_characters
        
        
        
