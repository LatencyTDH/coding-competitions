from collections import deque
from typing import Tuple

DIRS = {(1, 0): 'E', (-1, 0): 'W', (0, 1): 'N', (0, -1): 'S'}

def compute_optimal_path(target: Tuple[int, int]) -> str:
	start_pos = (0, 0)
	target_r, target_c = target
	if not (sum(target) & 1):
		return None

	start = (0, '', start_pos)
	frontier = deque([start])
	visited = set()
	active_set = set([start_pos])
	max_sum = abs(target_r) + abs(target_c)

	while frontier:
		node = frontier.popleft()
		i_move, path, pos = node
		r, c = pos
		
		visited.add(pos)
		active_set.remove(pos)

		if pos == target:
			return path
		elif abs(r) + abs(c) > max_sum:
			continue

		for dr, dc in DIRS:
			new_r, new_c = r + (2 ** i_move) * dr, c + (2 ** i_move) * dc
			new_pos = (new_r, new_c)
			if new_pos not in visited and new_pos not in active_set:
				frontier.append((i_move + 1, path + DIRS[(dr, dc)], new_pos))
				active_set.add(new_pos)

def get_absolute_binary(num):
	return str(bin(abs(num)))[2:]

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		row, col = map(int, input().split())
		ans = compute_optimal_path((row, col))
		if ans is None:
			ans = 'IMPOSSIBLE'
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()