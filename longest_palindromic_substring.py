class Solution:
    def longestPalindrome(self, s: str) -> str:
        padded = pad(s)
        n = len(padded)
        center, right = 0, 0
        radii = [0] * n
        max_radii, center_i = 0, 0
        
        for i in range(1, n - 1):
            i_mirror = 2 * center - i
            radii[i] = min(right - i, radii[i_mirror]) if right > i else 0
            while (padded[i + radii[i] + 1] == padded[i - radii[i] - 1]):
                radii[i] += 1
            
            if radii[i] + i > right:
                center = i
                right = radii[i] + i
            
            if radii[i] > max_radii:
                max_radii = radii[i]
                center_i = i
        
        start = (center_i - max_radii) // 2
        return s[start:start + max_radii]

def pad(s):
    if not s:
        return '^$'
    return "^#{0}#$".format('#'.join(s))
    
        