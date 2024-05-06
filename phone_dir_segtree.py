import math
import unittest


class PhoneDirectory:
    _UNFOUND = (True, math.inf)

    def __init__(self, max_numbers: int):
        self.segtree = [False] * int(math.ceil(4 * max_numbers))
        self.size = max_numbers

    def _query(
        self,
        tree_index: int,
        node_left_range: int,
        node_right_range: int,
        lo: int,
        hi: int,
    ) -> int:
        if hi < node_left_range or lo > node_right_range or self.segtree[tree_index]:
            return self._UNFOUND

        if node_left_range == node_right_range:
            return (self.segtree[tree_index], node_left_range)

        mid = (node_left_range + node_right_range) // 2
        left = self._query(tree_index * 2, node_left_range, mid, lo, hi)
        left_all_occupied = left[0]
        if not left_all_occupied:
            return left
        else:
            right = self._query(tree_index * 2 + 1, mid + 1, node_right_range, lo, hi)
            return right


    def _update(self, tree_index, node_left_range, node_right_range, pos, val):
        if node_left_range == node_right_range:
            self.segtree[tree_index] = val
            return

        mid = (node_left_range + node_right_range) // 2
        if pos <= mid:
            self._update(tree_index * 2, node_left_range, mid, pos, val)
        else:
            self._update(tree_index * 2 + 1, mid + 1, node_right_range, pos, val)

        self.segtree[tree_index] = (
            self.segtree[tree_index * 2] & self.segtree[tree_index * 2 + 1]
        )

    def get(self) -> int:
        node_start = query_start = 0
        node_end = query_end = self.size - 1

        occupied, phone = self._query(1, node_start, node_end, query_start, query_end)
        if not occupied:
            self._update(1, node_start, node_end, phone, True)
            return phone

        return -1

    def check(self, number: int) -> bool:
        occupied, _ = self._query(1, 0, self.size - 1, number, number)
        return not occupied

    def release(self, number: int) -> None:
        self._update(1, 0, self.size - 1, number, False)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
class PhoneDirectoryTests(unittest.TestCase):
    def test_get_and_release(self):
        test_sizes = [0, -1, 2, 5, 37, 1000]
        for size in test_sizes:
            self._run_standard_get_and_release_simulation(size)

    def _run_standard_get_and_release_simulation(self, size: int):
        pd = PhoneDirectory(size)
        for i in range(size):
            pd.get()

        for i in range(size):
            # phone number i should be in use
            self.assertFalse(
                pd.check(i), f"Phone number {i} should not be available to use."
            )
            pd.release(i)

        for i in range(size):
            pd.get()

        self.assertEqual(
            -1,
            pd.get(),
            "Should not be able to get another phone num because all are allocated",
        )


if __name__ == "__main__":
    unittest.main()
