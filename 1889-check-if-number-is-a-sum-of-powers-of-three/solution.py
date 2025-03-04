# Approach 2: Optimized Iterative Approach

# Time: O(log n)
# Space: O(1)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0

        while 3 ** power <= n:
            power += 1
        
        while n > 0:
            if n >= 3 ** power:
                n -= 3 ** power

            # We cannot use the same power twice
            if n >= 3 ** power:
                return False

            power -= 1

        # n has reached 0
        return True
