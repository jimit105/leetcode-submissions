# Approach 1: Dynamic Programming (Iterative)

# Time: O(high)
# Space: O(high)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        mod = 10 ** 9 + 7

# check if the current string can be made by append zero `0`s or one `1`s
        for end in range(1, high + 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod

        return sum(dp[low : high + 1]) % mod
