class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element not in ['+', '-', '*', '/']:
                stack.append(element)
            elif element == "+":
                nb1 = int(stack.pop())
                nb2 = int(stack.pop())
                stack.append(nb2 + nb1)
            elif element == "-":
                nb1 = int(stack.pop())
                nb2 = int(stack.pop())
                stack.append(nb2 - nb1)
            elif element == "*":
                nb1 = int(stack.pop())
                nb2 = int(stack.pop())
                stack.append(nb2 * nb1)
            elif element == "/":
                nb1 = int(stack.pop())
                nb2 = int(stack.pop())
                stack.append(int(nb2 / nb1))
        return stack[0]


        