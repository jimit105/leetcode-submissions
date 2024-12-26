# Approach 2: Binary Exponentiation (Iterative)

# Time: O(log n)
# Space: O(1)

class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -1 * n
            x = 1.0 / x

        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n //= 2

        return result


    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
        
