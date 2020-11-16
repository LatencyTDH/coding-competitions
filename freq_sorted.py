def freq(arr, target):
	left = bisect_left(arr, target)
	right = bisect_right(arr, target)
	if (left >= right or arr[left] != target):
		return 0
	return right - left

def bisect_left(arr, target):
	lo, hi = 0, len(arr)
	while lo < hi:
		mid = (lo + hi) // 2
		if arr[mid] < target:
			lo = mid + 1
		else:
			hi = mid
	return lo

def bisect_right(arr, target):
	lo, hi = 0, len(arr)
	while lo < hi:
		mid = (lo + hi) // 2
		if arr[mid] > target:
			hi = mid
		else:
			lo = mid + 1
	return lo

if __name__ == '__main__':
	a = [1,1,2,3,4,4,4,5,6,10]
	assert freq(a, 0) == 0
	assert freq(a, 1) == 2
	assert freq(a, 4) == 3
	assert freq(a, 8) == 0
	assert freq(a, 9) == 0
	assert freq(a, 10) == 1
	assert freq(a, 3) == 1
	assert freq(a, 5) == 1
	assert freq(a, 6) == 1
	assert freq(a, 7) == 0
	assert freq(a, 2.5) == 0
	assert freq(a, 128583592) == 0

	b = [3]
	assert freq(b, 3) == 1
	assert freq(b, 1) == 0
	assert freq(b, 4) == 0

	c = [3,3,3]
	assert freq(c, 3) == 3
	assert freq(c, 11) == 0
	assert freq(c, 2.5) == 0