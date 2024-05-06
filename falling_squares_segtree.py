class SegTreeNode:
    def __init__(self, start, end):
        self._left = self._right = None
        self.range_left = start
        self.range_right = end
        self.val = 0
        self.add = 0

    @property
    def range_mid(self):
        return (self.range_left + self.range_right) // 2

    @property
    def left(self):
        self._left = self._left or SegTreeNode(self.range_left, self.range_mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or SegTreeNode(self.range_mid + 1, self.range_right)
        return self._right


class SegTree:
    def __init__(self):
        self.root = SegTreeNode(0, 1e9)

    def update(self, left: int, right: int, height: int) -> None:
        self._update(self.root, left, right, height)

    def _update(self, node: SegTreeNode, start: int, end: int, height: int) -> None:
        if start > end:
            return
        if start <= node.range_left and node.range_right <= end:
            node.add = height
            node.val = height
            return

        self.pushdown(node)
        if start <= node.range_mid:
            self._update(node.left, start, end, height)
        if end > node.range_mid:
            self._update(node.right, start, end, height)

        node.val = max(node.left.val, node.right.val)

    def _query(self, node: SegTreeNode, left: int, right: int) -> int:
        if right < node.range_left or left > node.range_right:
            return 0
        if left <= node.range_left and node.range_right <= right:
            return node.val

        self.pushdown(node)
        return max(
            self._query(node.left, left, right), self._query(node.right, left, right)
        )

    def query(self, left: int, right: int) -> int:
        return self._query(self.root, left, right)

    def pushdown(self, node):
        # Propagates updates to children nodes and creates them if they don't exist
        if node.add:
            node.left.val = node.add
            node.right.val = node.add
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0


class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        tree = SegTree()
        tallest_stacks = []
        tallest = 0

        for pos, height in positions:
            start, end = pos, pos + height - 1
            max_height_in_range = tree.query(start, end)
            tree.update(start, end, max_height_in_range + height)
            tallest = max(tallest, tree.root.val)
            tallest_stacks.append(tallest)

        return tallest_stacks
