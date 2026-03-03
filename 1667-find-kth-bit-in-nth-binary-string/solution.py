# Approach 1: Brute Force

# Time: O(2^n)
# Space: O(2^n)

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        seq = "0"

        for i in range(1, n):
            if k <= len(seq):
                break
            seq += "1"

            inverted = ''.join("1" if bit == "0" else "0" for bit in seq[:-1])
            seq += inverted[::-1]

        return seq[k - 1]

