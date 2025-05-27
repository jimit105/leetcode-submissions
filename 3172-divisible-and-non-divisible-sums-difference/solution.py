# Approach 1: Traversal

# Time: O(n)
# Space: O(1)

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(x if x % m != 0 else -x for x in range(1, n + 1))
        
