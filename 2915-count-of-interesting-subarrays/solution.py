# Approach: Prefix Sum

# Time: O(n)
# Space: O(min(n, modulo))

from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = Counter([0])
        res = 0
        prefix = 0

        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += count[(prefix - k + modulo) % modulo]
            count[prefix % modulo] += 1

        return res
        
