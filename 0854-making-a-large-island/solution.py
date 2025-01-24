# Approach 2: Component Sizes

# Time: O(n ^ 2)
# Space: O(n ^ 2)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def get_neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in get_neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in get_neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))

        return ans
        
