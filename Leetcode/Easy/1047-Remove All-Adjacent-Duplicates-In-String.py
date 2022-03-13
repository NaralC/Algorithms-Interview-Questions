class Solution:
    def removeDuplicates(self, s: str) -> str:
        #Time: O(n)
        #Space: O(n)
        
        stack = []
        
        for char in s:
            if len(stack) and stack[-1] == char:
                stack.pop()
                continue
            
            stack.append(char)
            
        return ''.join(stack)