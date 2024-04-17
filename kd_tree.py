import math


class Node:
    """A node in a k-d tree."""

    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right


class KdTree:
    """A k-d tree data structure."""

    def __init__(self, points):
        self.root = self.build(points, 0)

    def build(self, points, depth):
        """Build a k-d tree from a list of points."""
        if not points:
            return None
        axis = depth % 2
        points = sorted(points, key=lambda point: point[axis])
        median_index = len(points) // 2
        return Node(
            point=points[median_index],
            left=self.build(points[:median_index], depth + 1),
            right=self.build(points[median_index + 1 :], depth + 1),
        )

    def closest_point(self, query: list[int]) -> list[int]:
        self.best_dist = math.inf
        self._closest = None
        self._closest_point(self.root, query, 0)
        return self._closest

    def _closest_point(self, node, query_pt, depth) -> None:
        if node is None:
            return

        distance = math.dist(node.point, query_pt)
        if distance < self.best_dist:
            self.best_dist = distance
            self._closest = node.point
        axis = depth % 2
        child, other_child = node.left, node.right
        if query_pt[axis] >= node.point[axis]:
            child, other_child = node.right, node.left
        self._closest_point(child, query_pt, depth + 1)
        if self.best_dist > abs(query_pt[axis] - node.point[axis]):
            self._closest_point(other_child, query_pt, depth + 1)

    def total_points_in_circle(self, center, radius):
        self._total_points = 0
        self._calc_points_in_circle(self.root, center, radius, 0)
        return self._total_points

    def _calc_points_in_circle(self, node, center, radius, depth):
        if node is None:
            return

        distance = math.dist(node.point, center)
        if distance <= radius:
            self._total_points += 1

        axis = depth % 2
        if center[axis] < node.point[axis]:
            child = node.left
            other_child = node.right
        else:
            child = node.right
            other_child = node.left
        self._calc_points_in_circle(child, center, radius, depth + 1)
        if radius >= abs(center[axis] - node.point[axis]):
            self._calc_points_in_circle(other_child, center, radius, depth + 1)


def brute_force_closest(points: list[int], query) -> list[int]:
    min_dist = math.inf
    closest = None
    for p in points:
        dist = math.dist(query, p)
        if dist < min_dist:
            min_dist = dist
            closest = p

    return closest


def load_points():
    points = []
    with open("test_points.txt") as f:
        for line in f:
            x, y = map(int, line.split(","))
            points.append([x, y])
    return points


if __name__ == "__main__":
    # points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    points = load_points()

    tree = KdTree(points)
    for p in points:
        closest = tree.closest_point(p)
        assert closest == p
    import random

    num_queries = 1000
    for i in range(num_queries):
        x, y = random.randint(-1000, 1000), random.randint(-1000, 1000)
        query = (x, y)
        ans = tree.closest_point(query)
        truth = brute_force_closest(points, query)
        if ans != truth:
            if math.dist(ans, query) != math.dist(truth, query):
                raise Exception(
                    f"Not the closest point: Got - {ans} [dist: {math.dist(ans, query)}], expected - {truth} [dist: {math.dist(truth, query)}]."
                    f"Query Point: {query}"
                )
