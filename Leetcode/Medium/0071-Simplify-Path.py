class Solution:
    def simplifyPath(self, path: str) -> str:
        #Time: O(n)
        #Space: O(n)
        
        stack = [] #Only contains alphabets
        
        for char in path.split('/'):
            #Remove a parent directory
            if char == '..':
                if len(stack): stack.pop()
            
            #Only append actual directory names
            elif len(char) and char != '.':
                stack.append(char)
        
        return '/' + '/'.join(stack)