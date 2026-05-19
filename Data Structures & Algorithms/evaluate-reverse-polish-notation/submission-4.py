class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []# [5]
        for token in tokens:
            if token in "+-*/":
                b = int(stack.pop()) #4
                a = int(stack.pop()) #9
                if token == "+":
                    stack.append(a + b)
                if token == "-":
                    stack.append(a - b)
                if token == "*":
                    stack.append(a * b)
                if token == "/":
                    stack.append(a / b)
            else:
                stack.append(token)
        return int(stack.pop())