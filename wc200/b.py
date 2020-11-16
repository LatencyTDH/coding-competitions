def solve(nums):
    left = 0
    right = 0
    n = len(nums)
    prod = 1
    best = 0
    while right < n:
        if nums[right] != 0:
            prod *= signum(nums[right])
            right += 1
            if prod > 0:
                best = max(best, right - left)
        else:
            if prod < 0:
                left = adjust_left(left, right, nums)
            best = max(best, right - left)
            prod = 1
            right += 1
            left = right
        
    
    if prod < 0:
        left = adjust_left(left, right, nums)
    best = max(best, right - left)
    return best

def adjust_left(left, right, nums):
    while left < right and nums[left] > 0:
        left += 1
    return min(left + 1, right)

def signum(num):
    if num == 0:
        return 0
    return 1 if num > 0 else -1
    
if __name__ == '__main__':
    assert solve([1,-2,-3,4]) == 4
    assert solve([0,1,-2,-3,-4]) == 3
    assert solve([-1,-2,-3,0,1]) == 2
    assert solve([1]) == 1
    assert solve([0]) == 0
    assert solve([-1]) == 0
    assert solve([-1, 0]) == 0
    assert solve([-1, 2]) == 1
    assert solve([1,2,3,5,-6,4,0,10]) == 4
    assert solve([-1,2,3,5,7,8,9,-10]) == 8

