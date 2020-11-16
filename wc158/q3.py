def dieSimulator(n, rollMax):
	SIDES = 6
	STATES = SIDES * max(rollMax)
	MOD = (10 ** 9) + 7
	dp = [0] * STATES
	for i in range(SIDES):
		dp[i] = 1

	for i in range(n-1):
		new_dp = [0] * STATES
		for state in range(STATES):
			if dp[state] == 0:
				continue
			roll_i = state // SIDES
			side = state % SIDES
			for die in range(6):
				new_rolls = roll_i + 1 if side == die else 0
				if new_rolls + 1 <= rollMax[die]:
					new_dp[new_rolls * SIDES + die] += dp[state]
		print(new_dp)
		dp = [count % MOD for count in new_dp]
	return sum(dp) % MOD

if __name__ == '__main__':
	# assert dieSimulator(2, [1,1,2,2,2,3]) == 34
	# assert dieSimulator(2, [1,1,1,1,1,1]) == 30
	# assert dieSimulator(3, [1,1,1,2,2,3]) == 181
	print(dieSimulator(15, [3,2,3,4,4,1]))

	# print(dieSimulator(5000, [13,12,11,10,9,8]))

