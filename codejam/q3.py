def solve(intervals):
	starts = sorted([(intv[0], job_id) for job_id, intv in enumerate(intervals)])
	ends = sorted([(intv[1], job_id) for job_id, intv in enumerate(intervals)])

	left = right = 0
	n = len(intervals)
	parents_needed = 0
	freed = ['C', 'J']
	in_progress = []
	assignment_map = {}

	while left < n and right < n:
		end_time, e_job_id = ends[right]
		start_time, s_job_id = starts[left]
		if end_time <= start_time:
			parents_needed -= 1
			finished_p = assignment_map[e_job_id]
			in_progress.remove(finished_p)
			freed.append(finished_p)
			right += 1
		else:
			parents_needed += 1
			if parents_needed > 2:
				return "IMPOSSIBLE"
			parent = freed.pop(0)
			assignment_map[s_job_id] = parent
			in_progress.append(parent)
			left += 1

	output = []

	for job_id in range(n):
		output.append(assignment_map[job_id])

	return "".join(output)


def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		num_tasks = int(input())
		tasks = []
		for i in range(num_tasks):
			tasks.append(list(map(int, input().split())))
		ans = solve(tasks)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()