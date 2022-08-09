# Approach 1: Dynamic Programming
    
# Time: O(N^2)
# Space: O(N)

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        arr.sort()
        dp = [1] * len(arr)
        
        index = {x: i for i, x in enumerate(arr)}
        
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:   # arr[i] will be the left child
                    right = x / arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD
                        
        return sum(dp) % MOD
        
