# Approach 1: Hash Map

from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        answer = 0
        central = False
        
        for word, word_count in count.items():
            
            # if the word is palindrome
            if word[0] == word[1]:
                if word_count %2 == 0:
                    answer += word_count
                else:
                    answer += word_count - 1
                    central = True
                    
            else:
                answer += min(word_count, count[word[1] + word[0]])
                
        if central:
            answer += 1
            
        return 2 * answer
        
