
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
            
        lo, hi = 0, m
        med1, med2 = easy_median(nums1), easy_median(nums2)
        if med1 == med2:
            return med1
        
        while lo <= hi:
            split1 = (lo + hi) // 2
            split2 = ((m + n + 1) // 2) - split1
            
            l1_max = nums1[split1-1] if split1 > 0 else -inf
            r1_min = nums1[split1] if split1 < m else inf
            
            l2_max = nums2[split2-1] if split2 > 0 else -inf
            r2_min = nums2[split2] if split2 < n else inf
            
            if l1_max <= r2_min and l2_max <= r1_min:
                if (m + n) % 2 == 1:
                    return max(l1_max, l2_max)
                else:
                    return (min(r1_min, r2_min) + max(l1_max, l2_max)) / 2
            elif l1_max > r2_min:
                hi = split1 - 1
            else:
                lo = split1 + 1
                
def easy_median(a):
    if not a:
        return None
    mid = len(a) // 2
    return (a[mid] + a[~mid]) / 2.0