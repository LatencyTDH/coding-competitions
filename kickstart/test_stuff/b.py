import collections

def get_stable_ordering(matrix, rows, cols):
	adj = compute_graph(matrix, rows, cols)
	visited = set()
	active = set()
	topological_sort = []
	has_cycle = False

	def dfs(start):
		nonlocal has_cycle
		if has_cycle:
			return
		if start in active:
			has_cycle = True
			return
		if start in visited:
			return

		active.add(start)
		for neigh in adj[start]:
			dfs(neigh)
		visited.add(start)
		active.remove(start)
		topological_sort.append(start)

	for start_letter in adj:
		if start_letter not in visited:
			dfs(start_letter)

	if has_cycle:
		return -1
	else:
		return "".join(reversed(topological_sort))


def compute_graph(matrix, rows, cols):
	graph = collections.defaultdict(set)
	for i in range(rows):
		for j in range(cols):
			letter = matrix[i][j]
			if i + 1 < rows:
				neigh = matrix[i+1][j]
				if neigh != letter:
					graph[neigh].add(letter)
			graph[letter]
	return graph


def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		rows, cols = map(int, input().split())
		matrix = [[] for _ in range(rows)]
		for i in range(rows):
			matrix[i].extend([ch for ch in input()])
		ans = get_stable_ordering(matrix, rows, cols)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()
	