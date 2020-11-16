def balancedStringSplit(s: str) -> int:
	num_splits = 0
	n = len(s)
	r = 0
	l = 0
	for j in range(n):
		if s[j] == 'R':
			r += 1
		else:
			l += 1
		if r - l == 0:
			num_splits += 1
			r = 0
			l = 0

	return num_splits



if __name__ == '__main__':
	assert balancedStringSplit("RLRRLLRLRL") == 4
	assert balancedStringSplit("RLLLLRRRLR") == 3
	assert balancedStringSplit("LLLLRRRR") == 1
	assert balancedStringSplit("LR") == 1
	assert balancedStringSplit("RRLRRLRLLLRL") == 2
	assert balancedStringSplit("RRRLLRRRLRLLLRRLRLLLLRRL") == 3

