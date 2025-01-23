# Approach 2: Hash Set

# m = len(jewels), n = len(stones)
# Time: O(m + n)
# Space: O(m)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)

        return sum(s in Jset for s in stones)
        
