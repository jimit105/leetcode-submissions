# Approach: Backtracking
    
# Time: O(N!)
# Space: O(N^2)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # Helper Function
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base Case - When all queens have been placed
            if row == n:
                ans.append(create_board(state))
                return
            
            for col in range(n):
                curr_diag = row - col
                curr_anti_diag = row + col
                
                # If the queen cannot be placed
                if col in cols or curr_diag in diagonals or curr_anti_diag in anti_diagonals:
                    continue
                    
                
                # Place the queen
                cols.add(col)
                diagonals.add(curr_diag)
                anti_diagonals.add(curr_anti_diag)
                state[row][col] = 'Q'
                
                
                # Move to the next row
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)
                
                
                # All valid paths have been explored in the above function call, so remove the queen
                cols.remove(col)
                diagonals.remove(curr_diag)
                anti_diagonals.remove(curr_anti_diag)
                state[row][col] = '.'
                
                
        ans = []
        empty_board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
        
