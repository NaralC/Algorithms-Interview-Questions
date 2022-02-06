class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #Time: O(s + t)
        #Space: O(s + t)
        
        stack_s, stack_t = [], []
        
        for char in s:
            if char == '#':
                if len(stack_s): stack_s.pop() #Prevent empty stack exception
                continue
            
            stack_s.append(char)
            
        for char in t:
            if char == '#':
                if len(stack_t): stack_t.pop() #Prevent empty stack exception
                continue
            
            stack_t.append(char)
            
        return stack_s == stack_t