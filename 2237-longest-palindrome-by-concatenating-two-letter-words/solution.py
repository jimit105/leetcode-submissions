# Approach 1: Hash Map

from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        ans = 0
        central = False

        for word, word_count in count.items():
            # If the word is palindrome
            if word[0] == word[1]:
                if word_count % 2 == 0:
                    ans += word_count
                else:
                    ans += word_count - 1
                    central = True
            elif word[0] < word[1]:
                ans += 2 * min(word_count, count[word[1] + word[0]])

        if central:
            ans += 1

        return 2 * ans
