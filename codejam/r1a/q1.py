import re
def smallest_match(no_star, with_star):
	regex = re.compile(with_star.replace('*', '[A-Z]*'))
	print(no_star, with_star)
	if regex.match(no_star) is None:
		return None
	else:
		return no_star

def intersection(s, t):
	m = len(s)
	n = len(t)
	if m < n:
		return intersection(t, s)
	sidx = s.rfind('*')
	tidx = t.rfind('*')

	if sidx == -1 and tidx == -1:
		return None if s != t else s
	elif sidx == -1:
		return smallest_match(s, t)
	elif tidx == -1:
		return smallest_match(t, s)
	
	s_suff_idx = sidx + 1 if sidx != -1 else m
	t_suff_idx = tidx + 1 if tidx != -1 else n
	i = j = 0
	intersect = []
	s_is_prefix = t_is_prefix = True

	while i < m and j < n:
		while (s_is_prefix and t_is_prefix
				and (i < m or j < n)
				and (i < s_suff_idx and j < t_suff_idx)):
			if s[i] == '*':
				s_is_prefix = False
			if t[j] == '*':
				t_is_prefix = False

			if s_is_prefix and t_is_prefix:
				if s[i] != t[j]:
					return None
				else:
					intersect.append(s[i])
				i += 1
				j += 1
			elif s_is_prefix:
				intersect.append(s[i])
				i += 1
			elif t_is_prefix:
				intersect.append(t[j])
				j += 1
			else:
				intersect.append('*')
				i += 1
				j += 1

		while i < s_suff_idx and i < m:
			intersect.append(s[i])
			i += 1
		while j < t_suff_idx and j < n:
			intersect.append(t[j])
			j += 1

		if i < m and j < n:
			if s.endswith(t[j:]):
				intersect.extend(s[i:])
				return "".join(intersect)
			elif t.endswith(s[i:]):
				intersect.extend(t[j:])
				return "".join(intersect)
			else:
				return None
	while i < m:
		intersect.append(s[i])
		i += 1

	while j < n:
		intersect.append(t[j])
		j += 1
	return "".join(intersect)	


def solve(num_rules, rules):
	ix_rule = rules[0]
	for i in range(1, num_rules):
		ix_rule = intersection(ix_rule, rules[i])
		# print(ix_rule)
		if ix_rule is None:
			return "*"

	return min_answer(ix_rule)

def min_answer(rule):
	output = []
	for ch in rule:
		if ch != '*':
			output.append(ch)
	sol = "".join(output)
	return sol if sol else '*'

def main():
	tcs = int(input())
	for case in range(1, tcs + 1):
		num_rules = int(input())
		rules = []
		for i in range(num_rules):
			rules.append(input())

		ans = solve(num_rules, rules)
		print("Case #{}: {}".format(case, ans))

if __name__ == '__main__':
	main()