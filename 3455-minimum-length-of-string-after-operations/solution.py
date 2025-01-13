# Approach 1: Using Hash Map

# n = len(s), k = len(character set)
# Time: O(n)
# Space: O(k) = O(1)

from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        char_freq = Counter(s)

        delete_count = 0

        for freq in char_freq.values():
            if freq % 2 == 1:
                # If frequency is odd, delete all except one
                delete_count += freq - 1
            else:
                # If frequency is even, delete all except two
                delete_count += freq - 2

        # Return the minimum length after deletions
        return len(s) - delete_count
        
