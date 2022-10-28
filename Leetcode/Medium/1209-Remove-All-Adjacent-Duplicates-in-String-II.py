class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        
        stack = [] # [char, count]
        
        for char in s:
            if len(stack) and char == stack[-1][0]:
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack.append([char, 1])
                
        return ''.join([char * count for char, count in stack])
        