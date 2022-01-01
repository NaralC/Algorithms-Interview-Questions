class Solution:
    def calculate(self, s: str) -> int:
        #Time: O(n)
        #Space: O(n)
        s.replace(' ', '')
        stack, val, sign = [], 0, '+'
        
        for idx, char in enumerate(s):
            if char.isdigit():
                val = (val * 10) + int(char)
            
            if char in '+-*/' or idx == len(s) - 1:
                if sign == '+':
                    stack.append(val)
                elif sign == '-':
                    stack.append(-val)
                elif sign == '*':
                    stack[-1] *= val
                elif sign == '/':
                    stack[-1] = int(stack[-1] / val)
                
                val, sign = 0, char
                
        return sum(stack)