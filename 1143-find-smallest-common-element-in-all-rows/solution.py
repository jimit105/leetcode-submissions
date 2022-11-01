# Approach 1: Count Elements
    

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = [0] * 10001
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(m):
                count[mat[i][j]] += 1
                if count[mat[i][j]] == n:
                    return mat[i][j]
                
        return -1
        
