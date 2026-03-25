# Approach: Prefix Sum

# Time: O(m * n)
# Space: O(1)

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        if total % 2:
            return False

        half = total // 2

        # Horizontal cut
        s = 0
        for i in range(len(grid) - 1):
            s += sum(grid[i])
            if s == half:
                return True

        # Vertical cut
        s = 0
        for j in range(len(grid[0]) - 1):
            s += sum(grid[i][j] for i in range(len(grid)))
            if s == half:
                return True

        return False
        
