class Solution:
    def search(self, queue):
        num = 0
        sumS = 0
        prev = 0
        prevOp = '+'
        while (queue):
            c = queue.popleft()
            if (c >= '0' and c <= '9'):
                num = num * 10 + int(c)
            elif (c == '('):
                num = self.search(queue)
            else:
                if prevOp == '+':
                    sumS += prev
                    prev = num
                elif prevOp == '-':
                    sumS += prev
                    prev = -num
                elif prevOp == '*':
                    prev *= num
                elif prevOp == '/':
                    prev = int(prev / num)

                if c == ')': 
                    break

                num = 0
                prevOp = c
        return sumS + prev
    
    def calculate(self, s: str) -> int:
	    queue = collections.deque()
	    for c in s:
	        if c != " ":
	    	    queue.append(c)
	    queue.append(" ")
	    result = self.search(queue)
	    return result
        