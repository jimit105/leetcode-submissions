# Approach 2: Track Using Two Arrays

# m = no. of rows, n = no. of columns
# Time: O(m * n)
# Space: O(m + n)

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        result += 1

        return result
        
