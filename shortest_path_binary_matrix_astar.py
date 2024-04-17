import collections
import heapq
import math
import unittest


class ShortestPathSolver:
    _DIRECTIONS = [
        (dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)
    ]

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.parents = collections.defaultdict(lambda: None)

    def _within_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _neighbors(self, row: int, col: int) -> list[int]:
        for dx, dy in self._DIRECTIONS:
            x, y = (row + dx, col + dy)
            new_vertex = (x, y)
            if self._within_bounds(x, y) and self.grid[x][y] == 0:
                yield new_vertex

    def _estimate(self, point: list[int]) -> float:
        # Computes the Chebyshev distance to goal point
        return max(abs(point[0] - self.rows + 1), abs(point[1] - self.cols + 1))

    def shortest_path(self) -> list[int]:
        path = []
        vertex = (self.rows - 1, self.cols - 1)
        while vertex:
            path.append(vertex)
            vertex = self.parents[vertex]
        return reversed(path)

    def compute_shortest_path_length(self) -> int:
        if self.grid[0][0] or self.grid[self.rows - 1][self.cols - 1]:
            return -1

        distances = collections.defaultdict(lambda: math.inf)
        start_point = (0, 0)
        heap = [(self._estimate(start_point), start_point)]
        distances[start_point] = 0
        seen = set()

        while heap:
            _, vertex = heapq.heappop(heap)
            if vertex in seen:
                continue
            if vertex == (self.rows - 1, self.cols - 1):
                return distances[vertex] + 1
            seen.add(vertex)

            for new_vertex in self._neighbors(*vertex):
                if new_vertex in seen:
                    continue
                cost_to_new = distances[vertex] + 1
                if cost_to_new < distances[new_vertex]:
                    self.parents[new_vertex] = vertex
                    f_score = cost_to_new + self._estimate(new_vertex)
                    distances[new_vertex] = cost_to_new
                    heapq.heappush(heap, (f_score, new_vertex))
        return -1


class ShortestPathSolverTests(unittest.TestCase):
    def test_valid_grid(self):
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0],
        ]
        solver = ShortestPathSolver(grid)
        expected = 10
        shortest_len = solver.compute_shortest_path_length()
        self.assertEqual(
            expected,
            shortest_len,
            f"Shortest path did not match expected! Got {shortest_len}; expected {expected}",
        )

    def test_invalid_grid(self):
        grid = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 0],
        ]
        solver = ShortestPathSolver(grid)
        expected = -1
        shortest_len = solver.compute_shortest_path_length()
        self.assertEqual(
            expected,
            shortest_len,
            f"Shortest path did not match expected: got {shortest_len}, expected {expected}",
        )


if __name__ == "__main__":
    unittest.main()
