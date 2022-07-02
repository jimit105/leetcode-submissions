# Approach 1: Hash Set
    
# Time: O(S), S = sum of lengths of words in `words`
# Space: O(S)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        seen = {
            "".join(morse_codes[ord(c) - ord('a')] for c in word)
            for word in words
        }
        
        return len(seen)
        
