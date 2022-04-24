class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        stack = []
        math = {'+' : lambda a, b: a + b, 
                '-' : lambda a, b: a - b, 
                '*' : lambda a, b: a * b, 
                '/' : lambda a, b: int(a / b)}
        
        # Perform a math operation on the top 2 numbers of the stack when needed
        for char in tokens:
            if char in math:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                operation = math[char]
                stack.append(operation(operand1, operand2))
                
            else:
                stack.append(int(char))
                
        return stack[-1]