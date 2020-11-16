def solve(houses, budget):
	num_purchases = 0
	houses.sort()
	for price in houses:
		if budget >= price:
			budget -= price
			num_purchases += 1
	return num_purchases

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		total_houses, budget = map(int, input().split())
		houses = list(map(int, input().split(' ')))
		ans = solve(houses, budget)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()
