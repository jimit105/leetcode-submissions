# Approach 1 - String Processing in Pipeline

from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        banned = set(banned)
        
        words = normalized_str.split()
        counter_words = Counter(words)
        
        for word, freq in counter_words.most_common():
            if word not in banned:
                return word
        
