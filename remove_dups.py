def removeDuplicates(s: str, k: int) -> str:
	current = s
	prev = None
	while True:
		if current == prev:
			break
		stage = [c for c in current]
		char = None
		count = 0
		first = 0
		for i in range(len(stage)):
			if stage[i] == char:
				count += 1
			else:
				first = i
				char = stage[i]
				count = 1
			if count == k:
				stage[first:i+1] = ["" for _ in range(i+1-first)]
				char = None
				count = 0
				first = None
		prev = current
		current = "".join(stage)
	return current

if __name__ == '__main__':
	assert removeDuplicates("abcd", 2) == "abcd"
	assert removeDuplicates("d", 2) == "d"
	assert removeDuplicates("deeedbbcccbdaa", 3) == 'aa'
	assert removeDuplicates("pbbcggttciiippooaais", 2) == "ps"
	print(removeDuplicates("ssssseeeeeeddddddddddeeeee", 2))

	# assert removeDuplicates("ssssseeeeeeddddddddddeeeee", 2) == "sd"

