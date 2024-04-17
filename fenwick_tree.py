class FenwickTree(object):
	def __init__(self, arr=[]):
		self.n = len(arr) + 1
		self.tree = [0]
		self.tree.extend(arr)
		self.construct(arr)

	def construct(self, arr):
		# cus = [0] * self.n
		# for i, num in enumerate(arr, 1):
		# 	left = i & (i - 1)
		# 	cus[i] += num + cus[i-1]
		# 	self.tree[i] = cus[i] - cus[left]
		for i in range(1, len(self.tree)):
			right = i + (i & (-i))

			if right < self.n:
				self.tree[right] += self.tree[i]

		"""Less efficient way O(nlgn) way of constructing the tree:
			for i in range(len(arr)):
				self.update(i, arr[i])
		"""

	def sum(self, index):
		index += 1
		tot = 0
		while index > 0:
			tot += self.tree[index]
			index &= (index - 1)
		return tot

	def sum_range(self, l, r):
		return self.sum(r) - self.sum(l - 1)

	def add(self, index, val):
		index += 1
		while index < self.n:
			self.tree[index] += val
			index += (index & -index)

if __name__ == '__main__':
	arr = [1,2,6,-1,3,1] # [1, 3, 9, 8, 11, 12]
						 # [0, 1, 2, 3,  4,  5]
						 # [1, 2, 6, -1, 3,  1]
	n = len(arr)
	ft = FenwickTree(arr)
	assert ft.sum_range(3, 4) == 2
	assert ft.sum_range(1, 3) == 7
	assert ft.sum_range(1, 1) == 2
	assert ft.sum_range(3, 5) == 3 
	assert ft.sum_range(1, 5) == 11
	for i in range(n):
		print(f"Cumulative sum from start to index {i} is {ft.sum(i)}")
