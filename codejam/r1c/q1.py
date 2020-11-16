directions = {
	'N': (0, 1),
	'S': (0, -1),
	'E': (1, 0),
	'W': (-1, 0)
}

def manhattan(pos):
	return abs(pos[0]) + abs(pos[1])

def solve(start, move_vec):
	pos = start
	for turn, move in enumerate(move_vec, 1):
		dx, dy = directions[move]
		pos[0] += dx
		pos[1] += dy
		if manhattan(pos) <= turn:
			return turn
			
	return 'IMPOSSIBLE'

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		x, y, moves = input().split()
		ans = solve([int(x), int(y)], moves)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()