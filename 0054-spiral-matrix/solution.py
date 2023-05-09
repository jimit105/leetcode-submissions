# Approach: Set Up Boundaries

# Time: O(m * n), m = number of rows, n = number of columns
# Space: O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = 0
        left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Left to Right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Downwards
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            if up != down:
                # Right to Left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            if left != right:
                # Upwards
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
