# Approach 2: DFS

# Time: O(mn)
# Space: O(mn)

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0

        self.top = self.bottom = x
        self.left = self.right = y

        def dfs(x, y):
            if (x < 0 or y < 0 or
                x >= len(image) or y >= len(image[0]) or
                image[x][y] == '0'):
                return

            image[x][y] = '0' # Mark visited black pixel as white

            self.top = min(self.top, x)
            self.bottom = max(self.bottom, x + 1)
            self.left = min(self.left, y)
            self.right = max(self.right, y + 1)

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        dfs(x, y)
        return (self.right - self.left) * (self.bottom - self.top)
        
