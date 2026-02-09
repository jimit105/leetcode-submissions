# Approach: Hash Set + Sum Formula
# Time: O(n)
# Space: O(n)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        dup = 0

        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)

        missing = n * (n + 1) // 2 - sum(seen)

        return [dup, missing]
