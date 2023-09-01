# Approach 3: DP + Least Significant Bit

# Time: O(n)
# Space: O(1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x >> 1] + (x & 1)

        return ans        
