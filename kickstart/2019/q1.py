from heapq import heappop, heappush

def compute_hindex(citations):
	q = []
	hindices = []
	hi = 0
	for cit in citations:
		while q and q[0] <= hi:
			heappop(q)
		if cit > hi:
			heappush(q, cit)
		if len(q) > hi:
			hi += 1
		hindices.append(hi)
	return hindices

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		n_papers = int(input())
		citations = list(map(int, input().split()))
		ans = compute_hindex(citations)
		ans = " ".join(map(str, ans))
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()