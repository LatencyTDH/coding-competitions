from math import inf, log2

# class SegmentTree(object):
#   def __init__(self, nums=[], func=min, target_range=(-inf, inf)):
#       self.nums = nums
#       self.tree = [inf] * (3*len(nums))
#       self.func = func
#       self.matched_sets = set([])
#       self.target_range = target_range
#       self.build_tree(self.nums, self.tree, 0, len(nums) - 1, 0)

#   def build_tree(self, nums, tree, l, r, pos):
#       print("Tree:",tree, f"\nl: {l}, r: {r}, pos: {pos}\n")
#       if (l == r):
#           tree[pos] = nums[l]
#           if self.does_match(pos):
#               self.matched_sets.add((l,r))
#           return
#       mid = (l + r) // 2
#       self.build_tree(nums, tree, l, mid, 2*pos+1)
#       self.build_tree(nums, tree, mid + 1, r, 2*pos+2)
#       tree[pos] = self.func(tree[2*pos+1], tree[2*pos+2])
#       if self.does_match(pos):
#           self.matched_sets.add((l,r))
    
#   def total_matches(self):
#       return len(self.matched_sets)
    
#   def does_match(self, pos):
#       return self.target_range[0] <= self.tree[pos] <= self.target_range[1]

def match_criterion_gen(lower, upper):
    return lambda num: lower <= num <= upper

class FenwickTree(object):
    def is_match(num, lower, upper):
        return lower <= num <= upper
    
    def __init__(self, arr=[], func):
        self.n = len(arr) + 1
        self.tree = [0] * (self.n + 1)
        self.construct(arr)
        self.matches = set([])
        self.func = func

    def construct(self, arr):
        cus = [0] * self.n
        for i, num in enumerate(arr):
            if self.func(num):
                self.matches.add((i, i))
            i += 1
            left = i & (i - 1)
            cus[i] += num + cus[i-1]
            self.tree[i] = cus[i] - cus[left]
            if self.func(cus[i]):
                self.matches.add((0, i - 1))
            if self.func(self.tree[i]):
                self.matches.add((left - 1, i - 1))

    def sum(self, index):
        index += 1
        tot = 0
        while index > 0:
            tot += self.tree[index]
            index &= (index - 1)
        return tot

    def sum_range(self, l, r):
        return self.sum(r) - self.sum(l - 1)

    def update(self, index, val):
        index += 1
        while index < self.n:
            self.tree[index] += val
            index += (index & -index)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        ft = FenwickTree(nums, func=lambda num: lower <= num <= upper)
        print(ft.matches)
        return len(ft.matches)
        
    
if __name__ == "__main__":
    s = Solution()
    crs = s.countRangeSum
    assert crs([-2,5,-1], -2, 2) == 3
    assert crs([0], 1, 3) == 0
    assert crs([0, 0], 1, 3) == 0
    assert crs([0], -1, 0) == 1
    assert crs([0], -1, 1) == 1
    assert crs([0, 1, 2], 3, 3) == 2
    assert crs([2,1,0], 0, 3) == 6
    assert crs([2,1,0], -3, -2) == 0    
    assert crs([2147483647,-2147483648,-1,0], -1, 0) == 4
    assert crs([-3,1,2,-2,2,-1], -3, -1) == 7
    assert crs([0,0,-3,2,-2,-2], -3, 1) == 16
    assert crs([0,-1,1,2,-3,-3], -3, 1) == 13
    assert crs([1,1,0,-2], -3, 1) == 8
    assert crs([-2,0,-2,-3,2,2,1,-3,4], 4, 11) == 5
    assert crs([1,4,-2,3,-4,3,0,-4,4], 3, 6) == 16
    assert crs([5,-23,-5,-1,-21,13,15,7,18,4,7,26,29,-7,-28,11,-20,-29,19,22,15,25,
                17,-13,11,-15,19,-8,3,12,-1,2,-1,-21,-10,-7,14,-12,-14,-8,
                -1,-30,19,-27,16,2,-15,23,6,14,23,2,-4,4,-9,-8,10,20,-29,29], -19, 10) == 362