# Approach 1: Set Up Boundaries

# Time: O(m * n)
# Space: O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        up = left = 0
        right = cols - 1
        down = rows - 1

        while len(result) < rows * cols:
            # Traverse left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are on a different row
            if up != down:
                # Traverse right to left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are on a different col
            if left != right:
                # Traverse upwards
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

        
