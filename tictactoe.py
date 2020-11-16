from typing import List, Tuple

IMPOSSIBLE = (-1, -1)
FIRST = "X"
SECOND = "O"

class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [(None, n)] * n
        self.cols = [(None, n)] * n
        self.diags = [(None, n)] * 2

    def attempt_grid_update(self,
                            line_to_change: List,
                            index: int,
                            player: int,
                            data: Tuple[None, int]) -> bool:
        occupant, remaining = data
        if self.can_update_line(occupant, player):
            line_to_change[index] = (player, remaining - 1)
            return remaining - 1 == 0
        else:
            line_to_change[index] = IMPOSSIBLE
        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        row_win = self.attempt_grid_update(self.rows, row, player, self.rows[row])
        col_win = self.attempt_grid_update(self.cols, col, player, self.cols[col])

        diag_win = False
        if row == col:
            diag_win = self.attempt_grid_update(self.diags, 0, player, self.diags[0])

        antidiag_win = False
        if col == self.n - 1 - row:
            antidiag_win = self.attempt_grid_update(
                self.diags, 1, player, self.diags[1])

        return player if row_win or col_win or diag_win or antidiag_win else 0

    def can_update_line(self, occupant, player):
        return occupant is None or occupant == player

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)