# Approach: Hash Table + Enumeration

# n = len(word), c = size of character set, here 26
# Time: O(n + c^2)
# Space: O(c)

from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1

        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)

            res = min(res, deleted)

        return res
        
