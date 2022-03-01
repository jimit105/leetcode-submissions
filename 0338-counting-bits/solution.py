# Approach 4 - DP + Last Set Bit

# Time: O(N)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
            
        return ans
        
