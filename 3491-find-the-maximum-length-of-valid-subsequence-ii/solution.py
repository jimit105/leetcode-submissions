# Approach: Dynamic Programming

# Time: O(k^2 + n * k)
# Space: O(k^2)

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)] # dp[i][j] represents the length of sequence ending with remainder j where the previous remainder was i
        res = 0

        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res

