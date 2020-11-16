def balancedString(s: str) -> int:
        if is_balanced(s):
            return 0
        ans = len(s)
        cc = get_counts(s)
        equal = len(s) // 4
        changes = [[(equal - c), let] for let, c in cc.items()]
        maxsub, letter = max(changes)
        to_meld = []
        for let, c in cc.items():
        	if c - equal > 0:
        		indices = indices_of(let, s)
        		to_meld.append(consecutive(indices, c-equal))

        return min(ans, meld(to_meld))

# def meld(loi):
# 	mindist = 10**6
# 	merged = []
# 	for i in range:
# 		for pair in indices:
# 			if not merged:
# 				merged.append(pair)
# 			else:

# 	return mindist

def get_counts(s):
    d = {l:0 for l in ('QWER')}
    for ch in s:
        d[ch] += 1
    return d

def indices_of(let, s):
	out = []
	for i, ch in enumerate(s):
		if ch == let:
			out.append(i)
	return out

def consecutive(indices, n):
	idx = []
	m = len(indices)
	for i in range(m - n + 1):
		idx.append(indices[i+n-1] - indices[i])
	return idx

def shortest_consecutive(indices, n):
	dist = indices[-1]
	m = len(indices)
	for i in range(m - n + 1):
		dist = min(dist, indices[i+n-1] - indices[i] + 1)
	return dist


def is_balanced(s):
    d = {l:0 for l in ('QWER')}
    for ch in s:
        d[ch] += 1
    count = d['Q']
    return all(count == val for val in d.values())
        

if __name__ == '__main__':
	assert balancedString('QWER') == 0
	assert balancedString('QQWE') == 1
	assert balancedString('QQQW') == 2
	assert balancedString('QQQQ') == 3
	assert balancedString('QWERQQQRQWERQWER') == 2
	assert balancedString('QWERQWERQWERQQQQ') == 3
	assert balancedString('QWERQWWRQWERQWER') == 1
	assert balancedString('QWQWQWQW') == 4
	assert balancedString('WQWRQQQW') == 3
	assert balancedString("WWEQERQWQWWRWWERQWEQ") == 4




