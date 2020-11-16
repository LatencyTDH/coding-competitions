class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        def visit(res, cur, num, i, val, multed):
            if i == N:
                if val == target:
                    res += cur,
                return
            for j in range(i, N):
                if num[i] == '0' and j > i:
                    return
                digits = num[i:j+1]
                x = int(digits)
                if not cur:
                    visit(res, digits, num, j+1, x, x)
                else:
                    visit(res, cur+'+'+digits, num, j+1, val+x, x)
                    visit(res, cur+'-'+digits, num, j+1, val-x, -x)
                    visit(res, cur+'*'+digits, num, j+1, (val-multed)+multed*x, multed*x)
        res = []
        visit(res, "", num, 0, 0, 0)
        return res