from tree_serializer import serialize, deserialize
from tree_node import TreeNode
from typing import List
from math import log2
from pprint import pprint

def euler_tour(root: TreeNode) -> List[int]:
	rmq = []
	def _tour(node):
		rmq.append(node.val)
		for neigh in (node.left, node.right):
			if neigh:
				_tour(neigh)
				rmq.append(node.val)

	_tour(root)
	return rmq

def annotate_backpointers(root):
	parents = {}

	def _annotate(root):
		for neigh in (root.left, root.right):
			if neigh not in parents and neigh:
				parents[neigh] = root
				_annotate(neigh)

	_annotate(root)
	return parents

def path_to_root(node, backpointers):
	path = [node]
	while node in backpointers:
		node = backpointers[node]
		path.append(node)
	return path

def build_rmq(tour):
	n = len(tour)
	max_k = int(log2(n))
	sparse = [[None] * (max_k + 1) for _ in range(n)]

	for i in range(n):
		sparse[i][0] = tour[i]

	for k in range(1, max_k + 1):
		for i in range(n):
			end = i + (2 ** k) - 1
			if end < n:
				shift_index = end - (2 ** (k - 1)) + 1
				sparse[i][k] = min(sparse[i][k - 1], sparse[shift_index][k - 1])
	
	return sparse

def query(rmq, i, j):
	length = j - i + 1
	kpow = int(log2(length))
	shift_index = j - (2 ** kpow) + 1

	return min(rmq[i][kpow], rmq[shift_index][kpow])

def bad_query(rmq, i, j):
	return min(rmq[i:j + 1])

if __name__ == '__main__':
	num_nodes = 7
	# tree_rep_str = str(list(range(1, num_nodes + 1)))
	tree_rep_str = "[1,2,3,4,5,6,null,null,null,7]"

	original = deserialize(tree_rep_str)
	tour = euler_tour(original)
	print(tour)
	rmq = build_rmq(tour)
	pprint(rmq)
	parents = annotate_backpointers(original)
	print("Parents:", {r.val: p.val for r, p in parents.items()})
	path_ex = path_to_root(original, parents)
	print([node.val for node in path_ex])

	locations = {node_id: pos for pos, node_id in enumerate(tour)}
	print(locations)
	
	for i in range(1, num_nodes + 1):
		for j in range(1, num_nodes + 1):
			if i != j:
				left = locations[i]
				right = locations[j]
				if right < left:
					left, right = right, left
				lca_id = query(rmq, left, right)
				assert bad_query(tour, left, right) == lca_id
				print(i, j, "->", lca_id)
