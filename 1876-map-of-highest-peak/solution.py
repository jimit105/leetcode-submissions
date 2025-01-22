# Approach 1: Breadth First Search

# m = no. of rows, n = no. of cols
# Time: O(m * n)
# Space: O(m * n)

from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        rows, cols = len(isWater), len(isWater[0])

        cell_heights = [[-1 for _ in range(cols)] for _ in range(rows)]

        # Queue for BFS
        cell_queue = deque()

        # Add all water cells to the queue and set their heights to 0
        for x in range(rows):
            for y in range(cols):
                if isWater[x][y] == 1:
                    cell_queue.append((x, y))
                    cell_heights[x][y] = 0
        
        height_of_next_layer = 1

        while cell_queue:
            layer_size = len(cell_queue)

            # Iterate all cells in the current layer
            for _ in range(layer_size):
                current_cell = cell_queue.popleft()

                for d in range(4):
                    neighbor_x = current_cell[0] + dx[d]
                    neighbor_y = current_cell[1] + dy[d]

                    if self._is_valid_cell(neighbor_x, neighbor_y, rows, cols) and cell_heights[neighbor_x][neighbor_y] == -1:

                        cell_heights[neighbor_x][neighbor_y] = height_of_next_layer
                        cell_queue.append((neighbor_x, neighbor_y))

            height_of_next_layer += 1

        return cell_heights

    def _is_valid_cell(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols
