class SegmentTree(object):
    def __init__(self, nums: List[int]):
        self.n = len(nums) + 1
        self.tree = [0] * self.n
        self.construct(nums)
    
    def construct(self, nums):
        cus = [0] * self.n
        for i, num in enumerate(nums, 1):
            left = i & (i - 1)
            cus[i] += cus[i-1] + num
            self.tree[i] = cus[i] - cus[left]
    
    def sum(self, index):
        index += 1
        tot = 0
        while index > 0:
            tot += self.tree[index]
            index &= (index - 1)
        return tot
    
    def update(self, i: int, val: int) -> None:
        diff = val - self.sumRange(i, i)
        i += 1
        while i < self.n:
            self.tree[i] += diff
            i += (i & -i)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum(j) - self.sum(i - 1)