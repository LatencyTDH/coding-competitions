from typing import List

class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        visited = {}

        def is_bipartite_graph(node, color):
            visited[node] = color
            for neigh in graph[node]:
                if neigh in visited:
                    if visited[neigh] == visited[node]:
                        return False
                else:
                    if not is_bipartite_graph(neigh, color ^ 1):
                        return False

            return True

        for vertex in range(len(graph)):
            if vertex not in visited:
                if not is_bipartite_graph(vertex, 0):
                    return False

        return True
