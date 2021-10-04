class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0

        for c in columnTitle:
            column_number *= 26
            column_number += ord(c) - ord("A") + 1
            
            
        return column_number
        
