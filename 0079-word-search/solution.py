# Approach: Depth First Search

# n = no. of rows, m = no. of columns, l = length of word
# Time: O(n * m * 4^l)
# Space: O(l)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            # Base case: we've matched all characters in word
            if k == len(word):
                return True

            # Check boundaries and if current cell matches current character
            if (i < 0 or i >= rows or
                j < 0 or j >= cols or
                board[i][j] != word[k]):
                return False

            # Mark as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Try all four directions
            result = (dfs(i + 1, j, k + 1) or # down
                     dfs(i - 1, j, k + 1) or  # up
                     dfs(i, j + 1, k + 1) or # right
                     dfs(i, j - 1, k + 1)) # left

            # Restore the cell
            board[i][j] = temp

            return result

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
            
        
