# Approach 1: Just Strings

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def process(idx, word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[0]
            return word + 'ma' + ('a' * idx)

        return ' '.join([process(i, w) for i, w in enumerate(sentence.split(), start = 1)])
        
