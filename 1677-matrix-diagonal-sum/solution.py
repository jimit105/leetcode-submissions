# Approach: Iterating over Diagonal Elements

# Time: O(n), n = number of rows (or columns)
# Space: O(1)

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0

        for i in range(n):
            # primary diagonal
            ans += mat[i][i]

            # secondary diagonal
            ans += mat[n - 1 - i][i]

        # If n is odd, subtract the middle element as its added twice.
        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]

        return ans
