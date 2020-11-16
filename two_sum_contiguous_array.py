class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        p1, p2 = 0, 1
        n = len(nums)
        total = nums[p1] if p1 < n else 0
        
        while p1 < n and p2 < n:
            print(p1, p2, total)
            if total + nums[p2] == k:
                return True
            elif total + nums[p2] < k:
                total += nums[p2]
                p2 += 1
            else:
                total -= nums[p1]
                p1 += 1
            
            if p1 == p2:
                p2 += 1
                total = nums[p1]
                
        return False

if __name__ == "__main__":
    s = Solution().checkSubarraySum
    assert s([23, 2, 6, 4, 7], 42)
    assert s([23,2,4,6,7], 6)
    assert not s([], 1)
    assert not s([2], 1)
    assert not s([1, 2], 1)    