# Approach 3: BFS from Houses to Empty Land (Optimized)

from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        total_sum = [[0] * cols for _ in range(rows)]

        def bfs(row, col, curr_count):
            min_dist = float('inf')
            queue = deque()
            queue.append([row, col, 0])

            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for d in dirs:
                    next_row, next_col = curr_row + d[0], curr_col + d[1]
                    
                    if (0 <= next_row < rows and
                        0 <= next_col < cols and
                        grid[next_row][next_col] == -curr_count):
                        total_sum[next_row][next_col] += curr_step + 1
                        min_dist = min(min_dist, total_sum[next_row][next_col])
                        grid[next_row][next_col] -= 1
                        queue.append([next_row, next_col, curr_step + 1])

            return min_dist

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_dist = bfs(row, col, count)
                    count += 1
                    if min_dist == float('inf'):
                        return -1

        return min_dist
