class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set({'+','-','*','/'})
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if s == '+':
                    stack.append(num1 + num2)
                elif s == '-':
                    stack.append(num2 - num1)
                elif s == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num2 / num1))
        return stack[0]
 