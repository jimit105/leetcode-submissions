# Approach 1: DFS + BFS

# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1

        # Find any land cell, and we treat it as a cell of island A
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    break

        # Recursively check the neighboring land cell of current cell grid[x][y] and add all land cells of island A to bfs_queue
        def dfs(x, y):
            grid[x][y] = 2
            bfs_queue.append((x, y))
            for curr_x, curr_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= curr_x < n and 0 <= curr_y <n and grid[curr_x][curr_y] == 1:
                    dfs(curr_x, curr_y)

        # Add all land cells of island A to bfs_queue.
        bfs_queue = []
        dfs(first_x, first_y)

        distance = 0
        while bfs_queue:
            new_bfs = []
            for x, y in bfs_queue:
                for curr_x, curr_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= curr_x < n and 0 <= curr_y < n:
                        if grid[curr_x][curr_y] == 1:
                            return distance
                        elif grid[curr_x][curr_y] == 0:
                            new_bfs.append((curr_x, curr_y))
                            grid[curr_x][curr_y] = -1

            # Start next round of BFS with distance + 1
            bfs_queue = new_bfs
            distance += 1

