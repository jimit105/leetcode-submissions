# Approach: DFS + BFS

# Time: O(m * n)
# Space: O(m * n)

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)
        }

        opposite = {
            'U': 'D',
            'D': 'U',
            'L': 'R',
            'R': 'L'
        }

        # Store all reachable cells and target location
        visited = set()
        target = None

        # DFS to map the grid (Phase 1)
        def dfs(x, y):
            nonlocal target

            visited.add((x, y))

            if master.isTarget():
                target = (x, y)

            for dir_char, (dx, dy) in directions.items():
                next_x, next_y = x + dx, y + dy

                # If we can move in this direction and haven't visited the next cell
                if master.canMove(dir_char) and (next_x, next_y) not in visited:
                    master.move(dir_char) # Move forward
                    dfs(next_x, next_y) # Explore from new position
                    master.move(opposite[dir_char]) # Move back

        # Start DFS from (0, 0)
        dfs(0, 0)

        # If target is not found, return -1
        if target is None:
            return -1

        # BFS to find the shortest path to target (Phase 2)
        queue = [(0, 0, 0)] # (x, y, distance)
        visited_bfs = {(0, 0)}

        while queue:
            x, y, dist = queue.pop(0)

            if (x, y) == target:
                return dist

            for dx, dy in directions.values():
                next_x, next_y = x + dx, y + dy

                # Only consider cells that were found reachable in first phase (DFS)
                if (next_x, next_y) in visited and (next_x, next_y) not in visited_bfs:
                    visited_bfs.add((next_x, next_y))
                    queue.append((next_x, next_y, dist + 1))

        return -1

