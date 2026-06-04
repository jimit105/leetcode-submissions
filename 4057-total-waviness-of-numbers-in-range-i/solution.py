# Approach 1: Enumeration

# Time: O(num2 * log (num2))
# Space: O(log(num2))

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            s = str(n)
            return sum((a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:]))

        return sum(waviness(n) for n in range(num1, num2 + 1))

