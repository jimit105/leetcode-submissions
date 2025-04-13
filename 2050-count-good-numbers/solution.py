# Approach 1: Fast Exponentiation

# Time: O(log n)
# Space: O(1)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # Calculate x ^ y % mod
        def quick_mul(x, y):
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret

        return quick_mul(5, (n + 1) // 2) * quick_mul(4, n // 2) % mod
        
