class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notation = ['-', '+', '*', '/']
        stack = []
        for char in tokens:
            if char not in notation:
                stack.append(int(char))
            else:
                if char == '+':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1+n2)
                elif char == '-':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2-n1)
                elif char == '*':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1*n2)
                else:
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2/n1))
        return stack[0]