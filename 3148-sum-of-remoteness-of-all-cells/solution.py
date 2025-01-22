# Approach 1: Depth First Search

# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        # Direction arrays
        self.dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)

        # Total sum of all non-blocked cells
        total_sum = sum(val for row in grid for val in row if val != -1)

        result = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] > 0:
                    # arr[0] = sum of reachable cells
                    # arr[1] = count of reachable cells
                    arr = [0, 0]
                    self.dfs(grid, row, col, arr)
                    result += (total_sum - arr[0]) * arr[1]

        return result

    # DFS to find sum and count of all cells reachable from (row, col)
    def dfs(self, grid, row, col, arr):
        arr[0] += grid[row][col]
        arr[1] += 1
        grid[row][col] = -1 # Mark as visited

        for di, dj in self.dir:
            new_row, new_col = row + di, col + dj
            if self.is_valid(grid, new_row, new_col):
                self.dfs(grid, new_row, new_col, arr)

    def is_valid(self, grid, row, col):
        n = len(grid)
        return 0 <= row < n and 0 <= col < n and grid[row][col] > 0

        
        
