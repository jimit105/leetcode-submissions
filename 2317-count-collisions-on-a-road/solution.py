# Approach 2: Counting

# Time: O(n)
# Space: O(1)

class Solution:
    def countCollisions(self, directions: str) -> int:
        dirs = directions.lstrip('L').rstrip('R')
        return len(dirs) - dirs.count('S')
