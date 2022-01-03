class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = text.count(' ')
        if num_spaces < 1:
            return text
        words = text.strip().split()
        num_words = len(words)
        
        spaces = (num_spaces // (num_words-1)) if num_words > 1 else 0
        extra_spaces = num_spaces - spaces * (num_words-1)
        
        
        return (spaces * ' ').join(words) + (extra_spaces * ' ')
        
        
    
