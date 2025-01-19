# Approach: BFS + Priority Queue

# m = no. of rows, n = no. of cols
# Time: O(m * n * log(mn))
# Space: O(m * n)

import heapq

class Solution:
    # Class to store the height and coordinates of a cell in the grid
    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col

        # Comparison method for the priority queue (min-heap)
        def __lt__(self, other):
            return self.height < other.height

    def _is_valid_cell(self, row, col, num_rows, num_cols):
        return 0 <= row < num_rows and 0 <= col < num_cols

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Direction arrays
        d_row = [0, 0, -1, 1]
        d_col = [-1, 1, 0, 0]

        num_rows = len(heightMap)
        num_cols = len(heightMap[0])

        visited = [[False] * num_cols for _ in range(num_rows)]

        # Priority queue (min-heap) to process boundary cells in increasing height order
        boundary = []

        # Add the first and last column cells to the boundary and mark them as visited
        for i in range(num_rows):
            heapq.heappush(boundary, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary, self.Cell(heightMap[i][num_cols - 1], i, num_cols - 1))
            visited[i][0] = visited[i][num_cols - 1] = True

        # Add the first and last row cells to the boundary and mark them as visited
        for i in range(num_cols):
            heapq.heappush(boundary, self.Cell(heightMap[0][i], 0, i))
            heapq.heappush(boundary, self.Cell(heightMap[num_rows - 1][i], num_rows - 1, i))
            visited[0][i] = visited[num_rows - 1][i] = True

        # Result
        total_water_volume = 0

        # Process cells in the boundary (min-heap will always pop the smallest height)
        while boundary:
            # Pop the cell with the smallest height from the boundary
            current_cell = heapq.heappop(boundary)

            current_row = current_cell.row
            current_col = current_cell.col
            min_boundary_height = current_cell.height

            # Explore all 4 neighboring cells
            for direction in range(4):
                neighbor_row = current_row + d_row[direction]
                neighbor_col = current_col + d_col[direction]

                if (self._is_valid_cell(neighbor_row, neighbor_col, num_rows, num_cols) and not visited[neighbor_row][neighbor_col]):
                    neighbor_height = heightMap[neighbor_row][neighbor_col]

                    # If the neighbor's height is less than the current boundary height, water can be trapped
                    if neighbor_height < min_boundary_height:
                        total_water_volume += min_boundary_height - neighbor_height

                    # Push the neighbor into the boundary with updated height (to prevent water leakage)
                    heapq.heappush(boundary, self.Cell(max(neighbor_height, min_boundary_height), neighbor_row, neighbor_col))
                    visited[neighbor_row][neighbor_col] = True

        return total_water_volume





        
