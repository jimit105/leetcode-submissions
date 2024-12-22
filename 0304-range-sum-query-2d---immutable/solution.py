# Approach 4: Caching Smarter

# m = no. of rows, n = no. of cols
# Time: O(1) per query, O(mn) for pre-computation
# Space: O(mn)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] \
                                        + self.dp[r][c + 1] \
                                        - self.dp[r][c] \
                                        + matrix[r][c]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] \
            - self.dp[row1][col2 + 1] \
            - self.dp[row2 + 1][col1] \
            + self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
