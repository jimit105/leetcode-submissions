# Approach 1 - Breadth-First Search

# Time: O(N)
# Space: O(N)

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        # build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        queue.append((-1, -1))
        
        
        
        # Because the while loop will add one more minute when it try to find the neighbors of last rotten orange. Since that the last rotten orange won't affect any other orange so we shouldn't include that round. Also, if there isn't any fresh orange(fresh_orange = 0), the function will simply return -1.
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1: # processing of first round is complete
                minutes_elapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:   # this is rotten orange
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))
                            
        return minutes_elapsed if fresh_oranges == 0 else -1
                    
                
                    
