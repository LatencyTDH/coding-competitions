ndef solve(*args):
	pass

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		ans = solve()
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()