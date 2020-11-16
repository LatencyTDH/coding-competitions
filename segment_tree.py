from math import inf

class SegmentTree(object):
	def __init__(self, nums=[], func=min, target_range=(-inf, inf)):
		self.nums = nums
		self.tree = [inf] * (3*len(nums))
		self.func = func
		self.matched_sets = set([])
		self.target_range = target_range
		self.build_tree(self.nums, self.tree, 0, len(nums) - 1, 0)
		self.tree = list(filter(lambda x: x != inf, self.tree))

	def build_tree(self, nums, tree, l, r, pos):
		print("Tree:",tree, f"\nl: {l}, r: {r}, pos: {pos}\n")
		if (l == r):
			tree[pos] = nums[l]
			if self.does_match(pos):
				self.matched_sets.add((l,r))
			return
		mid = (l + r) // 2
		self.build_tree(nums, tree, l, mid, 2*pos+1)
		self.build_tree(nums, tree, mid + 1, r, 2*pos+2)
		tree[pos] = self.func(tree[2*pos+1], tree[2*pos+2])
		if self.does_match(pos):
			self.matched_sets.add((l,r))

	def does_match(self, pos):
		return self.target_range[0] <= self.tree[pos] <= self.target_range[1]

	def total_matches(self):
		return len(self.matched_sets)

if __name__ == '__main__':
	sm = lambda x, y: x+y
	# st = SegmentTree([-2,5,-1], func=sm, target_range=(-2,2))
	# st = SegmentTree([0,1,2], func=sm, target_range=(3,3))
	st = SegmentTree([-1,2,4,0,1], func=sm, target_range=(5,6))


	# st = SegmentTree(range(129))
	print(st.tree)
	print(st.matched_sets)
	# print(sum(1 for num in st.tree if num != inf))