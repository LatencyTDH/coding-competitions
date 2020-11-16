from math import inf

def is_balanced(expression, replacement):
	total_repl = 0
	cnt = 0
	for ch in expression:
		if ch == '<':
			cnt += 1
		elif ch == '>':
			if not cnt:
				total_repl += 1
			else:
				cnt -= 1

	if cnt > 0:
		total_repl += inf

	return total_repl <= replacement

def balancedOrNot(expressions, maxReplacements):
	output_booleans = []
	for expr, repl in zip(expressions, maxReplacements):
		output_booleans.append(int(is_balanced(expr, repl)))
	return output_booleans

if __name__ == '__main__':
	assert balancedOrNot(expressions = ["<<<>>>", "<>"] , maxReplacements=[2,2]) ==  [1,1]
	assert balancedOrNot(expressions = ["<>", "<>><"] , maxReplacements=[2,2]) == [1, 0]
	assert balancedOrNot(expressions = ["<>", "<<><>>"], maxReplacements=[0,0]) == [1,1]
	assert balancedOrNot(expressions = ["<>>>", "<>>>>"], maxReplacements=[2,2]) == [1, 0]
	assert balancedOrNot(expressions = ["<<<>", "<<><><"] , maxReplacements=[2,2]) == [0,0]
	assert balancedOrNot(expressions = ["<<><>>", "<><>"] , maxReplacements=[2,2]) ==  [1,1]
	assert balancedOrNot(expressions = ["<<><>><", "><><><"] , maxReplacements=[2,2]) ==  [0,0]
	assert balancedOrNot(expressions = ["<<><>>>>>>"] , maxReplacements=[4]) ==  [1]
	assert balancedOrNot(expressions = [">><<", ">>", "><><"] , maxReplacements=[0, 0, 0]) ==  [0, 0, 0]

"""
Consider a string, expression consisting of the characters < and > only. We consider the string to be balanced if each < always appears before (i.e., to the left of) a corresponding > character (they do not need to be adjacent). Moreover, each < and > act as a unique pair of symbols and neither symbol can be considered as part of any other pair of symbols. For example, the strings <<>>, <>, and <><> are all balanced, but the strings >>, <<>, and ><>< are unbalanced.
To balance a string, we can replace only > character with <> at most maxReplacement times. Given an expression and the value of maxReplacement, can you turn an unbalanced string into a balanced one?
Complete the balancedOrNot function in the editor below. It has the following parameters:
An array of n strings, expressions, denoting the list of expressions to check.
An array of n integers, maxReplacements, where maxReplacementsi denotes the maximum number of replacements allowed when attempting to balance expressionsi.
The function must return an array of integers where each index i (0 ≤ i < n) contains a 1 if expressionsi is balanced or a 0 if it is not.
Input Format
A set of internal unit tests will be on the code with input in the following format.
The first line contains an integer, n, denoting the size of expressions.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing expressionsi.
The next line contains an integer, m, denoting the size of maxReplacements.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing maxReplacementsi.
Constraints
1 ≤ n ≤ 10^2
1 ≤ length of expressionsi ≤ 10^5
0 ≤ maxReplacementsi ≤ 10^5
Output Format
The function must return an array of integers where each index i (0 ≤ i < n) contains a 1 if expressionsi is balanced or a 0 if it is not.
Observations
"""