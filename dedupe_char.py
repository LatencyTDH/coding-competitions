def dedupe(s, target='*'):
	prev = None
	output = []
	for ch in s:
		if ch != target or prev != target:
			output.append(ch)
		prev = ch
	return "".join(output)

if __name__ == '__main__':
	assert dedupe('jasdklfjas**jaklsdf*******') == 'jasdklfjas*jaklsdf*'
	assert dedupe('**') == '*'
	assert dedupe('') == ''
	assert dedupe('*') == '*'
	assert dedupe('a*b*c*d*e*') == 'a*b*c*d*e*'
	assert dedupe('a*b**c***d****e******') == 'a*b*c*d*e*'
