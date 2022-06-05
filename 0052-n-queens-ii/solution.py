# Approach 1 - Backtracking

# Time: O(N!)
# Space: O(N)

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, cols):
            # Base Case - When all queens have been placed
            if row == n:
                return 1
            
            solutions = 0
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
                
                
                # Move to the next row
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)
                
                
                # All valid paths have been explored in the above function call, so remove the queen
                cols.remove(col)
                diagonals.remove(curr_diag)
                anti_diagonals.remove(curr_anti_diag)
                
                
            return solutions
        
        return backtrack(0, set(), set(), set())
        
