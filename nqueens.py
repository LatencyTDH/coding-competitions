from typing import List, Set
import pprint

class NQueensSolver(object):
    def __init__(self, n: int):
        self.n = n
        
    def get_all_solutions(self):
        self.rows = [0] * self.n
        self.cols = [0] * self.n
        self.diags = [0] * (2 * self.n + 1)
        self.antidiags = [0] * (2 * self.n + 1)
        self.solution = set()
        self.ways = []

        self._solve(0)
        return self.ways

    def _solve(self, piece: int):
        if piece == self.n:
            return True

        r = piece
        for c in range(self.n):
            if self.can_place_queen(r, c):
                diag_index = r - c + self.n - 1
                antidiag_index = r + c

                self.solution.add((r, c))
                self.rows[r] = self.cols[c] = self.diags[diag_index] = \
                self.antidiags[antidiag_index] = 1

                if self._solve(piece + 1):
                    self.ways.append(self.queen_representation(self.solution))

                self.rows[r] = self.cols[c] = \
                self.diags[diag_index] = self.antidiags[antidiag_index] = 0
                self.solution.remove((r, c))

        return False

    def can_place_queen(self, row: int, col: int):
        return (self.rows[row] != 1 
                and self.cols[col] != 1 
                and self.diags[row - col + self.n - 1] != 1
                and self.antidiags[row + col] != 1)

    def queen_representation(self, queen_locs: Set) -> List[str]:
        board = [['.'] * self.n for _ in range(self.n)]
        for row, col in queen_locs:
            board[row][col] = 'Q'
        return ["".join(row) for row in board]


if __name__ == '__main__':
    solver = NQueensSolver(8)
    solution_grids = solver.get_all_solutions()
    pprint.pprint(solution_grids)
    print(len(solution_grids)) 
