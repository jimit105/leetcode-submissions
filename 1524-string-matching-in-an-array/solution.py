# Approach 1: Brute Force

# n = size of `words` array, m = length of longest string in `words`
# Time: O(m * n^2)
# Space: O(m * n)

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []

        for curr_word_idx in range(len(words)):
            for other_word_idx in range(len(words)):
                if curr_word_idx == other_word_idx:
                    continue
                if words[curr_word_idx] in words[other_word_idx]:
                    matching_words.append(words[curr_word_idx])
                    break

        return matching_words
    
