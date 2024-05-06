import collections

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def increment(num):
            index = num + 1
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        def query(num):
            index = num + 1
            total = 0
            while index >= 1:
                total += tree[index]
                index &= index - 1
            return total

        offset = min(nums)
        tree = [0] * max(10, int(1.000185 * abs(max(nums) + abs(offset))))
        count_smaller_results = collections.deque()
        for num in reversed(nums):
            total = query(num - offset)
            increment(num - offset + 1)
            count_smaller_results.appendleft(total)
        return count_smaller_results
