# Approach 1: Breadth First Search

# Time: O(m * n)
# Space: O(m * n)

from queue import Queue

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        def bfs(x, y):
            q = Queue()
            q.put((x, y))
            is_closed = True
            dir_x, dir_y = [0, 1, 0, -1], [-1, 0, 1, 0]

            while not q.empty():
                x, y = q.get()
                visit[x][y] = True
                for i in range(4):
                    r, c = x + dir_x[i], y + dir_y[i]
                    if r < 0 or r >= m or c < 0 or c >= n:
                        is_closed = False
                    elif grid[r][c] == 0 and not visit[r][c]:
                        q.put((r, c))

            return is_closed

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and bfs(i, j):
                    count += 1

        return count
                        
