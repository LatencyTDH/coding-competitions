def solve(matrix):
	trace = 0
	dup_rows = 0
	dup_cols = 0
	n = len(matrix)
	rows = [set() for _ in range(n)]
	cols = [set() for _ in range(n)]

	for i in range(n):
		for j in range(n):
			if i == j:
				trace += matrix[i][j]
			val = matrix[i][j]
			rows[i].add(val)
			cols[j].add(val)

	for index in range(n):
		if len(rows[index]) != n:
			dup_rows += 1
		if len(cols[index]) != n:
			dup_cols += 1

	return (trace, dup_rows, dup_cols)

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		n = int(input())
		matrix = [[] for _ in range(n)]
		for i in range(n):
			matrix[i] = list(map(int, input().split()))
		ans = solve(matrix)
		print("Case #{}: {} {} {}".format(case, *ans))

if __name__ == '__main__':
	main()