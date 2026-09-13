class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                number = int(token)

                stack.append(number)
                
            # not a number so we try doing arithm operation 
            except:
                # gaurenteed to have two numbers
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "+":
                    stack.append(num2 + num1)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "*":
                    stack.append(num2 * num1)
                elif token == "/":
                    stack.append(int(num2 / num1))


        return stack[-1]
            