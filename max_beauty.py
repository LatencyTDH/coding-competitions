def max_beauty2(n, stacks, plates_per_stack, num_required):
	dp = [[0] * (n * plates_per_stack + 1) for _ in range(n + 1)]

	for stack in range(n):
		dp[stack + 1] = dp[stack][:]
		beauty_sum = 0
		for plate in range(plates_per_stack):
			beauty_sum += stacks[stack][plate]
			for req in range(num_required - plate):
				dp[stack + 1][plate + req + 1] = (
					max(dp[stack][req] + beauty_sum, dp[stack + 1][plate + req + 1])
				)

	return dp[n][num_required]

def max_beauty(n, stacks, plates_per_stack, num_required):
	dp = [0] * (n * plates_per_stack + 1)

	for stack in range(n):
		new_dp = dp[:]
		beauty_sum = 0
		
		for plate in range(plates_per_stack):
			beauty_sum += stacks[stack][plate]
			
			for req in range(num_required - plate):
				new_dp[plate + req + 1] = max(dp[req] + beauty_sum, new_dp[plate + req + 1])

		dp = new_dp

	return dp[num_required]

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		N, K, P = map(int, input().split())
		plates = []
		for _ in range(N):
			plates.append(list(map(int, input().split())))
		ans = max_beauty(N, plates, K, P)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()