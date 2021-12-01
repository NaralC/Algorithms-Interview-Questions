class Solution:
    def isValid(self, s: str) -> bool:
        #Time: O(n)
        #Space: O(n)
        stack = []
        counterparts = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            #O(1) lookup time since there are only 3 parentheses
            if char in counterparts.values():
                stack.append(char)
            else:
                if stack == []: #In case the input is ")"
                    return False
                operand1 = stack.pop()
                operand2 = counterparts[char]
                
                if operand1 != operand2: return False
                
        return True if stack == [] else False #In case the input is "("