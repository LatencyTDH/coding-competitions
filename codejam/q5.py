def solve(N, target_trace):
	if N * N < target_trace:
		return None
	
	solution = [[-1] * N for _ in range(N)]
	empty_parts = [(i, j) for i in range(N) for j in range(N)]
	rows, cols = initialize_rows_cols(N)

	def _solve(solution, trace):
		if not empty_parts:
			return trace == target_trace
		else:
			r, c = empty_parts.pop()

		for num in (rows[r] & cols[c]):
			to_include_in_trace = 0 if r != c else num
			if trace + to_include_in_trace <= target_trace:
				rows[r].remove(num)
				cols[c].remove(num)
				solution[r][c] = num
				if _solve(solution, trace + to_include_in_trace):
					return True
				rows[r].add(num)
				cols[c].add(num)
				solution[r][c] = -1
		
		empty_parts.append((r, c))
		return False

	is_possible = _solve(solution, 0)
	if not is_possible:
		return None
	return solution


def initialize_rows_cols(N):
	rows = [set(range(1, N + 1)) for _ in range(N)]
	cols = [set(range(1, N + 1)) for _ in range(N)]
	return rows, cols

def find_empty(solution):
	n = len(solution)
	for i in range(n):
		for j in range(n):
			if solution[i][j] == -1:
				return (i, j)

def matrix_to_str(matrix):
	s = ""
	for row in matrix:
		s += " ".join(map(str, row)) + '\n'
	return s

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		n, trace = map(int, input().split())
		ans = solve(n, trace)
		if ans is None:
			print("Case #{}: {}".format(case, "IMPOSSIBLE"))
		else:
			print("Case #{}: POSSIBLE\n{}".format(case, matrix_to_str(ans)))

if __name__ == '__main__':
	main()