def solve(arr, k, n):
	count = 0
	end = n
	i = 0
	while i < end:
		num = arr[i]
		if num == k:
			expected = k
			while i < end and arr[i] == expected and expected > 0:
				if expected == 1:
					count += 1
				i += 1
				expected -= 1
		else:
			i += 1
	
	return count

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		n, k = map(int, input().split())
		arr = list(map(int, input().split()))
		ans = solve(arr, k, n)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()