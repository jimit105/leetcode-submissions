# Approach 3 - Dynamic Programming

# Time: O(r*c)

import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        rows, cols = len(mat), len(mat[0])
        dist = [[math.inf for j in range(cols)] for i in range(rows)]
        
        # First Pass: Check for Left and Top
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
                        
        # Second Pass: Check for Bottom and Right
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < cols - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
                    
        return dist
