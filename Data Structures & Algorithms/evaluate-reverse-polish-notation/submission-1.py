class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                float(t)
                stack.append(int(t))
            except:
                if t == '+':
                    second = stack.pop()
                    first = stack.pop()
                    ans = first + second
                    stack.append(ans)
                elif t == '-': #order matters
                    second = stack.pop()
                    first = stack.pop()
                    ans = first - second
                    stack.append(ans)
                elif t == '*':
                    second = stack.pop()
                    first = stack.pop()
                    ans = first * second
                    stack.append(ans)
                elif t == '/': #order matters
                    second = stack.pop()
                    first = stack.pop()
                    ans = int(first / second) #truncate toward 0
                    stack.append(ans)
        return stack.pop()

