# Approach: Greedy

# Time: O(n)
# Space: O(1)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1 = min(nums)
        m2 = max(nums)
        return k * (m2 - m1)

