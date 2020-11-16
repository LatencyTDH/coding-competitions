def trim(s):
	i = 0
	j = len(s) - 1
	while i < j and s[i] == ' ':
		i += 1
	while i < j and s[j] == ' ':
		j -= 1
	if i > j or (i == j and s[i] == ' '):
		return ''
	else:
		return s[i:j+1]

if __name__ == '__main__':
	assert trim('  ') == ''
	assert trim('    sean') == 'sean'
	assert trim('      sean  ') == 'sean'
	assert trim('sean  dai') == 'sean  dai'
	assert trim('wins a lot     ') == 'wins a lot'
	assert trim('aa') == 'aa'
	assert trim('s') == 's'
	assert trim(' d ') == 'd'
	assert trim('') == ''
	assert trim('He is the master of the universe. ') == 'He is the master of the universe.'
	assert trim(' ') == ''
	