class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        n = len(nums)
        trips = []
        skip = {}
        i = 0
        while i < n:
            elem = nums[i]
            end = bisect_right(nums[i:], elem)
            skip[elem] = (i, i + end)
            i += end
        
        i = 0
        while i < n-2:
            if i > 0 and nums[i-1] == nums[i]: 
                i = skip[nums[i]][1]
            j, k = i + 1, n - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                
                if tot == 0:
                    trips.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j = skip[nums[j]][1]
                    while k > j and nums[k] == nums[k+1]:
                        k = skip[nums[k]][0] - 1
                elif tot < 0: 
                    j += 1
                else:
                    k -= 1
            i += 1
                
        return trips