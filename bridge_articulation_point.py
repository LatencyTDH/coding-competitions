def get_bridges(graph):
	bridges = []
	times = {}
	low = {}
	visited = set()
	timer = 0
	def dfs(vertex, parent):
		nonlocal timer
		visited.add(vertex)
		times[vertex] = low[vertex] = timer
		timer += 1
		for to in graph[vertex]:
			if to == parent:
				continue
			if to in visited:
				low[vertex] = min(low[vertex], times[to])
			else:
				dfs(to, vertex)
				low[vertex] = min(low[vertex], low[to])
				if low[to] > times[vertex]:
					bridges.append((vertex, to))


	for vertex in graph:
		if vertex not in visited:
			dfs(vertex, None)
	return bridges

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
		if vertex not in visited:
			dfs(vertex, None)
	return articulation_points