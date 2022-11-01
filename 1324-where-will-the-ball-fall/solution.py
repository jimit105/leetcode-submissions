# Approach 1: Depth First Search

# Time: O(M * N)
# Space: O(M)

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):           
            if i == m:
                return j
            elif 0 <= (j_new := j + grid[i][j]) < n and grid[i][j] == grid[i][j_new]:
                return dfs(i+1, j_new)
            else:
                return -1
            
        return [dfs(0, j) for j in range(n)]
        
