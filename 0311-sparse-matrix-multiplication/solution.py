# Approach 2: List of Lists

# Time: O(m * k * n)
# Space: O(m * k + k * n)

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        def compress_matrix(matrix):
            rows, cols = len(matrix), len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix


        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        A = compress_matrix(mat1)
        B = compress_matrix(mat2)

        ans = [[0] * n for _ in range(m)]

        for mat1_row in range(m):
            for elem1, mat1_col in A[mat1_row]:
                for elem2, mat2_col in B[mat1_col]:
                    ans[mat1_row][mat2_col] += elem1 * elem2

        return ans
