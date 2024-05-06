def min_snow_machines(machines: list[int, int], n: int) -> int:
    intervals = []
    for loc, cover in machines:
        intervals.append([max(0, loc - cover), min(n, loc + cover)])

    intervals.sort()
    i = current_end = farthest_end = num_machines = 0

    while current_end < n:
        while i < len(intervals) and intervals[i][0] <= current_end:
            farthest_end = max(farthest_end, intervals[i][1])
            i += 1

        if current_end == farthest_end:
            return -1
        
        num_machines += 1
        current_end = farthest_end
        
    return num_machines

def main():
    n = 10
    machines = []
    assert min_snow_machines(machines, n) == -1

    n = 2
    machines = [(0, 1), (1, 1), (2, 1)]
    assert min_snow_machines(machines, n) == 1

    n = 3
    machines = [(0, 2)]
    assert min_snow_machines(machines, n) == -1

    n = 3
    machines = [(2, 1)]
    assert min_snow_machines(machines, n) == -1

    n = 5
    machines = [(0, 2), (1, 1), (3, 1), (4, 1)]
    assert min_snow_machines(machines, n) == 3

    n = 5
    machines = [(0, 1), (1, 1), (2, 1), (3, 5), (4, 1), (5, 1)]
    assert min_snow_machines(machines, n) == 1

    n = 5
    machines = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
    assert min_snow_machines(machines, n) == 3

    n = 9
    machines = [(0, 1), (1, 1), (1, 2), (2, 2), (2, 1), (4, 2), (3, 1), (4, 1), (5,2), (6, 1), (7, 1), (8, 1)]
    assert min_snow_machines(machines, n) == 3

if __name__ == "__main__":
    main()