from typing import List

class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     nhash = hash(needle)
    #     m = len(needle)
    #     n = len(haystack)
    #     if m > n:
    #         return -1
    #     for i in range(n - m + 1):
    #         window = hash(haystack[i:i+m])
    #         if window == nhash and haystack[i:i+m] == needle:
    #             return i
    #     return -1
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        if not m:
            return 0
        lps = lps_precompute(needle)
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
            if j == m:
                return i - j
        return -1

def lps_precompute(needle):
    curlen = 0
    i = 1
    m = len(needle)
    lps = [0] * m
    while i < m:
        if needle[curlen] == needle[i]:
            curlen += 1
            lps[i] = curlen
            i += 1
        elif curlen > 0:
            curlen = lps[curlen - 1]
        else:
            i += 1
    return lps

def compute_lps(needle: str) -> List[int]:
    needle_size = len(needle)
    sizes = [0] * needle_size
    prefix_end = 0
    
    for ptr in range(1, needle_size):
        while prefix_end > 0 and needle[ptr] != needle[prefix_end]:
            prefix_end = sizes[prefix_end - 1]
        if needle[ptr] == needle[prefix_end]:
            prefix_end += 1
        sizes[ptr] = prefix_end
        
    return sizes

if __name__ == '__main__':
    arr = lps_precompute('ababb') # [0, 0, 0, 0, 1, 2]
    print(arr)
