# Approach: Difference Array

# Time: O(n + limit)
# Space: O(limit)

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo = min(a, b) + 1
            hi = max(a, b) + limit
            # 2 moves for all targets
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            # 1 move in [lo, hi]
            diff[lo] -= 1
            diff[hi + 1] += 1
            # 0 moves at a+b
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        res = n
        cur = 0
        for t in range(2, 2 * limit + 1):
            cur += diff[t]
            res = min(res, cur)
        return res
