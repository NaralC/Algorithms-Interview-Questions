class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        # where n = len(s)
        
        stack = [] # [count, char]
        
        for char in s:
            if len(stack) and stack[-1][1] == char:
                stack[-1][0] += 1
                
                if stack[-1][0] >= k:
                    stack[-1][0] %= k
                    
                    if not stack[-1][0]:
                        stack.pop()
            
            else:
                stack.append([1, char])
                
        
        return ''.join([char * count for count, char in stack])
                