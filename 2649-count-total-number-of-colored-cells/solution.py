# Approach 2: Math

# Time: O(1)
# Space: O(1)

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * (n - 1) * n // 2
        
