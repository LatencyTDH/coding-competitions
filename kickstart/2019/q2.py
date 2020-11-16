from heapq import heappush, heappop
from math import log2, inf
DIRS = ((1, 1), (-1, -1), (-1, 1), (1, -1))

def solve(grid, n):
	q = [(0, grid)]
	visited = set()
	best_flips = inf
	if grid == 0:
		return 0

	while q:
		n_flips, cur = heappop(q)
		if cur in visited:
			continue
		if cur == 0:
			return min(n_flips, best_flips)
		visited.add(cur)
		for neigh_grid in neighbors(cur, n):
			if neigh_grid not in visited:
				heappush(q, (n_flips + 1, neigh_grid))

	return best_flips

def neighbors(grid, n):
	tcur = grid
	to_explore = []
	while tcur:
		one = tcur & (-tcur)
		index = int(log2(one))
		to_explore.append(index)
		tcur -= one
		
	for index in to_explore:
		for dv in DIRS:
			bitindex = index
			posr, posc = get_corner(bit_index_to_rc(bitindex, n), dv, n)
			cand = grid
			dr, dc = dv
			incr_by = -dr * n - dc
			while 0 <= posr < n and 0 <= posc < n:
				cand ^= (1 << bitindex)
				if posr + dr >= n or posr + dr < 0 or posc + dc >= n or posc + dc < 0:
					break
				bitindex += incr_by
				posr, posc = bit_index_to_rc(bitindex, n)
			# 	print(posr, posc)
			# print(cand)
			# print("Starting at {}: Moving in dir {}".format(str(bit_index_to_rc(index, n)), dv)),
			# visualize_graph(cand, n)
			# print()
			yield cand

def get_corner(pos, dir, n):
	posr, posc = pos
	if posr == 0 or posr == n-1 or posc == 0 or posc == n-1:
		return pos

	dr, dc = -1*dir[0], -1*dir[1]
	while 0 <= posr < n and 0 <= posc < n:
		posr += dr
		posc += dc
	return posr, posc


# def visualize_graph(grid, n):
# 	ss = format(grid, f'0{n*n}b')
# 	for i in range(len(ss) // n):
# 		print(ss[i*n:(i+1)*n])

def bit_index_to_rc(index, n):
	x = (n*n - 1) - index
	return x // n, x % n

def main():
	tcs = int(input())
	for case in range(tcs):
		n_lines = int(input())
		num = (1 << (n_lines*n_lines)) - 1
		for i in range(n_lines):
			for j, ch in enumerate(input()):
				if ch == '#':
					num ^= (1 << ((n_lines-i)*n_lines - j - 1))
		ans = solve(num, n_lines)
		print("Case #{}: {}".format(case + 1, ans))

if __name__ == '__main__':
	main()