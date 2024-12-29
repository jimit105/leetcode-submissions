# Approach 2: Frequency Table and Counting

# m = length of `order`, n = length of `s`
# Time: O(m + n)
# Space: O(n)

from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_counts = Counter(s)
        result = ''

        for char in order:
            if char in char_counts:
                result += char * char_counts[char]
                del char_counts[char]

        result += ''.join(char * count for char, count in char_counts.items())

        return result
        
