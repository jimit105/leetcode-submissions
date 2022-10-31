# Approach 1: Group by Category

# Time: O(M * N)
# Space: O(M + N)


# two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if (r - c) not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
                
        return True
        