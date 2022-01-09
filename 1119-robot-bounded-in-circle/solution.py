# Approach 1 - One Pass

# Time: O(n)
# Space: O(1)

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # north = 0, east = 1, south = 2, west = 3
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # x, y
        # For north (0), x = x + 0, y = y + 1
        # For east (1), x = x + 1, y = y + 0
        # For south (2), x = x + 0, y = y -1
        # For west (3), x = x - 1, y = y + 0
        
        x = y = 0
        idx = 0 # north
        
        for i in instructions:
            if i == 'L':    
                idx = (idx + 3) % 4  # idx = idx - 1
            elif i == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
                
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        
        return (x == 0 and y == 0) or idx != 0
        
        
