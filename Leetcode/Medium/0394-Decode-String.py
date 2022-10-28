class Solution:
    def decodeString(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        
        stack = []
        
        for char in s:
            # Start decoding
            if char == ']':
                multiplier, word = '', ''
                
                # Retrieve alphabets
                while len(stack) and stack[-1].isalpha():
                    word = stack.pop() + word
                
                stack.pop() # Skip '['
                
                # Retrieve multiplier
                while len(stack) and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                    
                stack.append(int(multiplier) * word)
                
            else:
                stack.append(char)
        
        return ''.join(stack)
    