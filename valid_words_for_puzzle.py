from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        c = defaultdict(int)
        for word in words:
            c[onehot(word)] += 1
        out = []
        for p in puzzles:
            mask = onehot(p)
            count = 0
            for submask in construct(mask, onehot(p[0])):
                count += c[submask] if submask in c else 0
            out.append(count)
        return out

def onehot(s):
    bitint = 0
    first = ord('a')
    for ch in s:
        bitint |= 1 << (ord(ch) - first)
    return bitint

def construct(orig, fixch):
    submask = orig
    submasks = [orig]
    while submask > 0:
        submask = (submask - 1) & orig
        if fixch & submask:
            submasks.append(submask)
    return submasks
