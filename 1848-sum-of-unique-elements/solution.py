# Time: O(n)
# Space: O(n)

from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)

        total = 0
        for key, value in counter.items():
            if value == 1:
                total += key
        
        return total

