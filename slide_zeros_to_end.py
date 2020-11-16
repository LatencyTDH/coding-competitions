def slide_zeros_to_end(nums):
	i = 0
	j = len(nums) - 1

	while i < j:
		while j > i and nums[j] == 0:
			j -= 1
		while i < j and nums[i] != 0:
			i += 1

		if i < j:
			nums[i], nums[j] = nums[j], nums[i]

total_swaps = 0
def moveZeroes(nums):
	global total_swaps
	i = 0
	j = 1
	n = len(nums)

	while i < j and j < n:
		while i < j and nums[i] != 0:
			i += 1
		while j < n and nums[j] == 0:
			j += 1

		if i < j < n:
			total_swaps += 1
			nums[i], nums[j] = nums[j], nums[i]
		elif i == j:
			j += 1


def test_it(arr):
	print("Testing")
	print(arr)
	moveZeroes(arr)
	print(arr)

	saw_zero = False
	for num in arr:
		if saw_zero and num != 0:
			assert False

		if num == 0:
			saw_zero = True


if __name__ == '__main__':
	test_it([1,0,0,2,5,0])
	test_it([0,1,0,3,12])
	test_it([2,1,0,1,0,0,-1, -1, 0,0])
	test_it([2,1,0,1,0,0,-1, -1, 0,0])
	test_it([1,2,3,4])
	test_it([1,2,0,3,4])
	test_it([0,0,0,0,0,0])
	test_it([0,0,0,0,0,0,0,1,2,30,0,4,0,54,6,7,8,0,0,0,0])
	test_it([])
	test_it([1])
	test_it([0])
	print(total_swaps)

