def solve(s):
	stack = []
	output = []
	total_open = 0

	for ch in s:
		if stack and ch == stack[-1]:
			stack.append(ch)
		elif stack and ch != stack[-1]:
			diff = int(stack[-1]) - int(ch)
			while stack:
				output.append(stack.pop())
			if diff > 0:
				for i in range(diff):
					output.append(')')
				total_open -= diff
			else:
				for i in range(abs(diff)):
					output.append('(')
				total_open += -diff
			stack.append(ch)
		else:
			stack.append(ch)
			for i in range(int(ch)):
				output.append('(')
			total_open += int(ch)

	while stack:
		output.append(stack.pop())

	while total_open:
		output.append(')')
		total_open -= 1

	return "".join(output)

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		ans = solve(input())
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()