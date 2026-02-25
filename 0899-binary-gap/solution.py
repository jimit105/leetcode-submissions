# Approach 1: Store Indexes

# Time: O(log n)
# Space: O(log n)

class Solution:
    def binaryGap(self, n: int) -> int:
        A = [i for i in range(32) if (n >> i) & 1]

        if len(A) < 2:
            return 0
        
        return max(A[i + 1] - A[i] for i in range(len(A) - 1))
        
