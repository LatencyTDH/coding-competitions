import collections
import copy

DIRS = ((0, 1), (1, 0), (-1, 0), (0, -1))

def solve(grid):
	num_islands = get_number_islands(grid)
	if num_islands != 1:
		return 0
	elif is_single_island_removal_sufficient(grid):
		return 1
	else:
		return 2

def is_single_island_removal_sufficient(grid):
	graph = compute_graph(grid)
	return bool(get_articulation_points(graph))

def get_articulation_points(graph):
	articulation_points = []
	times = {}
	low = {}
	visited = set()
	timer = 0
	def dfs(vertex, parent):
		nonlocal timer
		visited.add(vertex)
		times[vertex] = low[vertex] = timer
		timer += 1
		children = 0
		for to in graph[vertex]:
			if to == parent:
				continue
			if to in visited:
				low[vertex] = min(low[vertex], times[to])
			else:
				dfs(to, vertex)
				low[vertex] = min(low[vertex], low[to])
				if low[to] >= times[vertex] and parent != None:
					articulation_points.append(vertex)
				children += 1
		if parent is None and children > 1:
			articulation_points.append(vertex)

	for vertex in graph:
		prev_size = len(visited)
		if vertex not in visited:
			dfs(vertex, None)
			if len(visited) - prev_size == 1:
				articulation_points.append(vertex)
	return articulation_points


def get_number_islands(grid):
	m = len(grid)
	n = len(grid[0])
	visited = set()
	islands = 0

	def dfs(pos):
		visited.add(pos)
		i, j = pos
		for dr, dc in DIRS:
			new_pos = (i + dr, j + dc)
			if (0 <= i + dr < m and 0 <= j + dc < n and 
				grid[i+dr][j+dc] == 1 and new_pos not in visited):
				dfs(new_pos)

	for i in range(m):
		for j in range(n):
			if (i, j) not in visited and grid[i][j] == 1:
				dfs((i, j))
				islands += 1
	return islands


def compute_graph(grid):
	m = len(grid)
	n = len(grid[0])
	graph = collections.defaultdict(set)
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				graph[(i, j)]
				for dr, dc in DIRS:
					if (0 <= i + dr < m and 0 <= j + dc < n and 
						grid[i+dr][j+dc] == 1):
						graph[(i, j)].add((i + dr, j + dc))
	return graph
	
if __name__ == '__main__':
	grid = [[1,1,0,1,1],
			[1,1,1,1,1],
			[1,1,0,1,1],
			[1,1,0,1,1]]
	assert solve(grid) == 1

	grid = [[1,1,0,1,1],
			[1,1,1,1,1],
			[1,1,0,1,1],
			[1,1,1,1,1]]
	assert solve(grid) == 2

	grid = [[1,0,1,0]]
	assert solve(grid) == 0

	grid = [[1,1]]
	assert solve(grid) == 2

	grid = [[1,1,1]]
	assert solve(grid) == 1

	grid = [[1, 0]]
	assert solve(grid) == 1

	grid = [[1]]
	assert solve(grid) == 1

	grid = [[0,1,1,0],
			[0,1,1,0],
			[0,0,0,0]]
	assert solve(grid) == 2

	grid = [[0,1,0,1,1],
			[1,1,1,1,1],
			[1,1,1,1,1],
			[1,1,1,1,0]]
	assert solve(grid) == 1
