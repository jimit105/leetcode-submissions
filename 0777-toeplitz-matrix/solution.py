# Approach 2: Compare With Top-Left Neighbor

# m = no. of rows, n = no. of cols
# Time: O(m * n)
# Space: O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                    for r, row in enumerate(matrix)
                    for c, val in enumerate(row))

