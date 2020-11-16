from random import randint, random

def merge(a, b):
    i, j = 0, 0
    m, n = len(a), len(b)
    merged = []
    while i < m and j < n:
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    if i < m:
        merged.extend(a[i:])

    if j < n:
        merged.extend(b[j:])

    return merged

def mergesort(arr):
	n = len(arr)
	jump = 1

	split_arrs = [[arr[i]] for i in range(n)]
	while jump < n:
		for i in range(0, n - jump, 2 * jump):
			split_arrs[i] = merge(split_arrs[i], split_arrs[i+jump])
		jump *= 2
	return split_arrs[0] if arr else arr

def test_1():
	a = [4,6,73,2,1,6]
	assert mergesort(a) == sorted(a)

def test_2():
	a = []
	assert mergesort(a) == []

def test_3():
	a = [randint(0, 1000) + random() for j in range(999)]
	sorted_a = mergesort(a)
	assert sorted_a == sorted(a)

def main():
	test_1()
	test_2()
	test_3()

if __name__ == '__main__':
	main()