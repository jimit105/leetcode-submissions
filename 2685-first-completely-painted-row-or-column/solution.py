# Approach 2: Brute Force Optimized with Counting

# m = no. of rows, n = no. of cols
# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        row_count, col_count = [0] * num_rows, [0] * num_cols
        num_to_pos = {}

        for row in range(num_rows):
            for col in range(num_cols):
                num_to_pos[mat[row][col]] = (row, col)

        for i in range(len(arr)):
            num = arr[i]
            row, col = num_to_pos[num]

            row_count[row] += 1
            col_count[col] += 1

            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i

        return -1
        
