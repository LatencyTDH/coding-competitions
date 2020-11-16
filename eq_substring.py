"""
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0."""
def equalSubstring(s: str, t: str, maxCost: int) -> int:
	i = 0
    m = len(s)
    best_len = 0
    currcost = 0
    for j, ch in enumerate(s):
        cost = abs(ord(s[j]) - ord(t[j]))
        if cost + currcost <= maxCost:
            currcost += cost
        elif i == j:
            currcost = 0
            i += 1
        else:
            while cost + currcost > maxCost and i < j:
                currcost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            currcost += cost
        best_len = max(j - i + 1, best_len)
    return best_len

if __name__ == '__main__':
	assert equalSubstring("iktqzyazth", "havakbjzzc", 78) == 8
	assert equalSubstring("abcd", "bcdf", 3) == 3
	assert equalSubstring("abcd", "cdef", 3) == 1
	assert equalSubstring("abcd", "acde", 0) == 1
	assert equalSubstring("asdf", "qwer", 0) == 0
	assert equalSubstring("ujteygggjwxnfl", "nstsenrzttikoy", 43) == 5
	assert equalSubstring("anryddgaqpjdw", "zjhotgdlmadcf", 5) == 1 
	assert equalSubstring("krrgw","zjxss",19) == 2
