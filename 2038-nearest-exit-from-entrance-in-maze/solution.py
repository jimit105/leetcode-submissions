# Approach 1: Breadth First Search

import collections

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1,0), (-1, 0), (0, 1), (0, -1))
        
        start_row, start_col = entrance
        maze[start_row][start_col] = '+'
        
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_dist = queue.popleft()
            
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '.':
                    if next_row in [0, rows - 1] or next_col in [0, cols - 1]:
                        return curr_dist + 1
                    
                    maze[next_row][next_col] = '+'
                    queue.append([next_row, next_col, curr_dist + 1])
                    
        return -1
        
