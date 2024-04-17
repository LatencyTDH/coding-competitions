import math
import random

random.seed(42)


class SkiplistNode:
    def __init__(self, val: int, nxt):
        self.val = val
        self.next = nxt
        self.prev = None
        self.down = None
        self.up = None

    def __repr__(self):
        return f"Val: {self.val}, Prev: {self.prev.val}, Next: {self.next.val}"


class Skiplist:
    def __init__(self):
        self.max_levels = 1
        self.dummy = SkiplistNode(-math.inf, None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.layer1_dummy = self.dummy

    def search(self, target: int) -> bool:
        ret = self._search(target)
        return ret.val == target

    def _search(self, target: int) -> SkiplistNode:
        head = dummy = self.dummy
        while True:
            while target >= head.next.val and head.next != dummy:
                head = head.next
            if not head.down:
                return head
            head = head.down
            dummy = dummy.down

    def _create_new_level(self):
        dummy = self.dummy
        new_dummy = SkiplistNode(-math.inf, None)
        new_dummy.next, new_dummy.prev = new_dummy, new_dummy
        new_dummy.down, dummy.up = dummy, new_dummy
        self.dummy = new_dummy

    def _insert_after(self, node, new_node):
        new_node.prev, new_node.next = node, node.next
        new_node.next.prev, new_node.prev.next = new_node, new_node

    def add(self, num: int) -> None:
        curr = self._search(num)
        cur_level = 1
        new_node = SkiplistNode(num, None)
        self._insert_after(curr, new_node)
        dummy = self.layer1_dummy

        while random.random() < 0.5:
            if cur_level >= self.max_levels:
                self.max_levels += 1
                self._create_new_level()

            while curr.up is None and curr != dummy:
                curr = curr.prev
            curr = curr.up
            dummy = dummy.up

            nxt_lvl_node = SkiplistNode(new_node.val, None)
            self._insert_after(curr, nxt_lvl_node)
            nxt_lvl_node.down = new_node
            new_node.up = nxt_lvl_node

            new_node = nxt_lvl_node
            cur_level += 1

    def erase(self, num: int) -> bool:
        curr = self._search(num)
        if curr.val == num:
            while curr:
                curr.prev.next, curr.next.prev = curr.next, curr.prev
                curr = curr.up
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
