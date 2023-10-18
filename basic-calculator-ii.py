class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        if s == '0':
            return 0
        num, op, stack = 0, '+', []
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ' ) or i == n-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-1*num)
                elif op == '*':
                    x = stack.pop()
                    stack.append(x*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                op = ch
                num = 0
        res = sum(stack)
        return res