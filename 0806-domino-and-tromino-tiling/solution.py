# Approach 1: Dynamic Programming (Top-down)

# Time: O(n)
# Space: O(n)

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def p(n):
            if n == 2:
                return 1
            return (p(n - 1) + f(n - 2)) % MOD

        @cache
        def f(n):
            if n <= 2:
                return n
            return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD

        return f(n)
        
