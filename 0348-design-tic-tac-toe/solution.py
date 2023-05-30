# Approach 2: Optimized

# Time: O(1)
# Space: O(n)

class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.rows)

        if player == 1:
            curr_player = 1
        else:
            curr_player = -1

        self.rows[row] += curr_player
        self.cols[col] += curr_player

        if row == col:
            self.diagonal += curr_player

        if col == n - row - 1:
            self.anti_diagonal += curr_player

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.anti_diagonal) == n:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
