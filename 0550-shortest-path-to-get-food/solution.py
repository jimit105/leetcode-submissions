# Approach 1: Breadth-First Search (BFS)

# m = no. of rows, n = no. of cols
# Time: O(m * n)
# Space: O(m * n)

from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])

        start = next((i, j) 
                    for i in range(rows) 
                    for j in range(cols)
                    if grid[i][j] == '*'
                    )
        
        queue = deque([start])
        steps = 1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dx, dy in dirs:
                    new_row, new_col = row + dx, col + dy

                    if self._is_valid(grid, new_row, new_col):
                        if grid[new_row][new_col] == '#':
                            return steps

                        grid[new_row][new_col] = 'X'
                        queue.append((new_row, new_col))

            steps += 1

        return -1

    def _is_valid(self, grid, row, col):
        return (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and grid[row][col] != 'X'
        )
