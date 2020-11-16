def findTargetSumWays(nums, S: int) -> int:
    max_possible = sum(nums)
    n = len(nums)
    if abs(S) > max_possible or (max_possible + S) % 2 == 1:
        return 0

    cache = [[None] * (2 * max_possible + 1) for _ in range(n)]
    
    def calc(nums, i, cumulative, S, cache):
        if i == len(nums):
            return cumulative == S
        
        adj_cumulative = cumulative + max_possible
        if cache[i][adj_cumulative] is not None:
            return cache[i][adj_cumulative]
        
        plus = calc(nums, i + 1, cumulative + nums[i], S, cache)
        minus = calc(nums, i + 1, cumulative - nums[i], S, cache)
        cache[i][adj_cumulative] = plus + minus
        return cache[i][adj_cumulative]

    return calc(nums, 0, 0, S, cache)


if __name__ == '__main__':
    print(findTargetSumWays([1,2,3], 4))