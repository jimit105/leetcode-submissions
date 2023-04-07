# Approach 1: Depth First Search

from itertools import chain, product

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            grid[r][c] = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    dfs(nr, nc)

        for r, c in chain(product([0, rows - 1], range(cols)), product(range(1, rows - 1), [0, cols - 1])):
            if grid[r][c]:
                dfs(r, c)

        return sum(grid[r][c] for r, c in product(range(rows), range(cols)))

