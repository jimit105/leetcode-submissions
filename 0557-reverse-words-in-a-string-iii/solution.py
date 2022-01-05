class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = list(map(lambda x: x[::-1], words))
        return ' '.join(words)
        
