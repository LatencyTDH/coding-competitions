import collections
import math
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = math.inf

        # set up groups for each x- and y-value
        horizontal = collections.defaultdict(set)
        vertical = collections.defaultdict(set)
        for x, y in points:
            horizontal[y].add(x)
            vertical[x].add(y)

        groups = horizontal
        if len(vertical) < len(horizontal):
            groups = vertical

        candidates = sorted(groups)
        size = len(groups)
        for i in range(size):
            for j in range(i + 1, size):
                a1 = candidates[i]
                a2 = candidates[j]

                # find identical x-values
                both = sorted(groups[a1] & groups[a2])
                for index in range(len(both) - 1):
                    b1, b2 = both[index], both[index + 1]
                    area = (a2 - a1) * (b2 - b1)
                    if area < min_area:
                        min_area = area

        return min_area if min_area != math.inf else 0


if __name__ == "__main__":
    s = Solution()
    res = s.minAreaRect(
        [
            [36219, 4673],
            [26311, 36047],
            [26311, 4673],
            [36219, 16024],
            [17010, 16024],
            [26311, 6287],
            [22367, 6287],
            [17010, 36047],
            [17010, 6287],
            [22367, 16024],
            [36219, 6287],
            [22367, 4673],
            [17010, 4673],
            [36219, 36047],
        ]
    )
    assert res == 6365616
    assert (
        s.minAreaRect(
            [
                [12462, 26300],
                [6658, 29085],
                [689, 15923],
                [6658, 15923],
                [8422, 26300],
                [35757, 33466],
                [23602, 29085],
                [26657, 15923],
                [23602, 26300],
                [12462, 26676],
                [23602, 39225],
                [35757, 39225],
                [23602, 27054],
                [6658, 26676],
                [35757, 26676],
                [6658, 26300],
                [26657, 33466],
                [23602, 33466],
                [35757, 26300],
                [12462, 33466],
                [23602, 15923],
                [35757, 29085],
                [35757, 15923],
                [8422, 33466],
                [26657, 26676],
                [8422, 15923],
                [26657, 39225],
                [689, 26300],
                [26657, 27054],
                [8422, 26676],
                [26657, 26300],
                [689, 27054],
                [12462, 29085],
                [6658, 33466],
            ]
        )
        == 663264
    )
