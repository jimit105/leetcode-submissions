# Approach 4 - Memorization (Top-Down)

# Time: O(n^2)
# Space: O(n^2)

from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @lru_cache(maxsize = None)
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            
            return path
        
        return min_path(0, 0)
        
