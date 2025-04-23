# Approach: Hashmap

# Time: O(n log n)
# Space: O(log n)

from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = Counter()

        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashmap[key] += 1

        max_value = max(hashmap.values())
        count = sum(1 for v in hashmap.values() if v == max_value)
        return count
        
