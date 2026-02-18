# Approach 2: Divide by Two

# Time: O(w), here O(1), w = number of bits in n
# Space: O(1)

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, curr = divmod(n, 2)
        while n:
            if curr == n % 2:
                return False
            n, curr = divmod(n, 2)

        return True

