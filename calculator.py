class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        nums = []
        operators = []
        index = 0
        while index < n:
            tok = s[index]
            if tok in {'(', '+'}:
                operators.append(tok)
            elif tok == '-':
                operators.append('+')
                operators.append(tok)
            elif tok.isdigit():
                number = int(tok)
                while index + 1 < n and s[index+1].isdigit():
                    index += 1
                    number = number * 10 + int(s[index])
                nums.append(number)
                handle_top_negation(nums, operators)
            elif tok == ')':
                while operators and nums:
                    op = operators.pop()
                    if op == '(':
                        handle_top_negation(nums, operators)
                        break
                    if op == '+':
                        handle_addition(nums)
                    elif op == '-':
                        nums.append(-nums.pop())
            index += 1
        
        while operators and nums:
            op = operators.pop()
            if op == '+':
                handle_addition(nums)
            elif op == '-':
                nums.append(-nums.pop())
        return nums.pop()

def handle_addition(nums):
    nums.append(nums.pop() + nums.pop())

def handle_top_negation(nums, operators):
    if operators and operators[-1] == '-':
        nums.append(-nums.pop())
        operators.pop()

# if __name__ == '__main__':
#     s = Solution()
#     calc = s.calculate
#     assert calc("2-4-(8+2-6+(8+4-(1)+8-10))") == -15
#     assert calc("1-(5-6)") == 2
#     assert calc("1-2-3") == -4
#     assert calc("(1+(4+5+2)-3)+(6+8)") == 23
#     assert calc(" 2-1 + 2 ") == 3
#     assert calc("120 + 10") == 130
        