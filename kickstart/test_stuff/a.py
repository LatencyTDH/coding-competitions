def solve(arr):
    if len(arr) <= 2:
        return len(arr)
    
    prev_diff = None
    length = 1
    maxlen = 1
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == prev_diff:
            length += 1
        else:
            length = 1
            prev_diff = arr[i] - arr[i-1]
        maxlen = max(maxlen, length)

    return maxlen + 1

if __name__ == "__main__":
    cases = int(input())
    for case in range(cases):
        input()
        ans = solve(list(map(int, input().split())))
        print("Case #{}: {}".format(case + 1, ans))
