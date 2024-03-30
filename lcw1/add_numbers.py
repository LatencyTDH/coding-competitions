from typing import *


class Solution:
    def _not_it(self):
        return None

    def set_mismatch(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor_result = 0
        for i in range(1, n + 1):
            xor_result ^= nums[i - 1] ^ i
        rightmost_set_bit = xor_result & (-xor_result)
        group1, group2 = 0, 0

        for num in nums:
            if num & rightmost_set_bit:
                group1 ^= num
            else:
                group2 ^= num

        for i in range(1, n + 1):
            if i & rightmost_set_bit:
                group1 ^= i
            else:
                group2 ^= i

        for num in nums:
            if num == group1:
                return [group1, group2]
            elif num == group2:
                return [group2, group1]


tests = [
    (
        ([1, 1],),  # input tuple
        [1, 2],  # output
    ),
    (
        ([2, 2],),  # input tuple
        [2, 1],  # output
    ),
]
