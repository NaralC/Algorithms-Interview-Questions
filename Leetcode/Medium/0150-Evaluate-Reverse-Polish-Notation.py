class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time: O(n)
        # Space: O(n)
        stack = []

        def calculate(sign, n2, n1):
            if sign == '+': return n1 + n2
            elif sign == '-': return n1 - n2
            elif sign == '*': return n1 * n2
            elif sign == '/': return int(n1 / n2)

        for char in tokens:
            # If a math sign: pop the top 2 number and calculate
            if char in ['+', '-', '*', '/']:
                result = calculate(char, stack.pop(), stack.pop())
                stack.append(result)

            # If number: add to stack
            else:
                stack.append(int(char))

        return stack[0]
        
