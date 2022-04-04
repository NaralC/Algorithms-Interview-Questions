class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        
        open_close = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        
        for char in s:
            # Append normally if it's an opening
            if char in open_close.keys():
                stack.append(char)
            
            # If it's a closing, check if it can make a good pair
            else:
                # Handle cases like ')'
                if not len(stack):
                    return False
                
                # ')' should match the element on top of the stack
                operand1 = char
                operand2 = open_close[stack.pop()]
                
                if operand1 != operand2:
                    return False
                
        # Valid parentheses should not have anything left in the stack
        return not len(stack)