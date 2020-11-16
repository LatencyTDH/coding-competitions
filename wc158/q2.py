def queensAttacktheKing(queens, king):
	out = []
	queenset = set(tuple(q) for q in queens)
	king = tuple(king)
	for q in queens:
		if is_attacking_king(tuple(q), king, queenset):
			out.append(q)
	print(out)
	return out

def is_attacking_king(queen, king, queens):
	dirs = ((1,0), (-1, 0), (1,1), (-1, -1), (0, 1), (0, -1), (-1, 1), (1, -1))
	for dv in dirs:
		r, c = queen
		dr, dc = dv
		while 0 <= r + dr < 8 and 0 <= c+dc < 8 and (r+dr, c+dc) not in queens:
			r += dr
			c += dc
			if (r, c) == king:
				return True
	return False



if __name__ == '__main__':
	queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
	king = [0,0]
	out1 = queensAttacktheKing(queens, king)
	assert sorted(out1) == sorted([[0,1],[1,0],[3,3]])

	queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
	king = [3,3]
	out2 = queensAttacktheKing(queens, king)
	assert sorted(out2) == sorted([[2,2],[3,4],[4,4]])

	queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
	king = [3,4]
	out3 = queensAttacktheKing(queens, king)
	assert sorted(out3) == sorted([[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]])