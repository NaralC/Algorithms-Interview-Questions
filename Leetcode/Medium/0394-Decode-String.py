class Solution:
    def decodeString(self, s: str) -> str:
        #Time: O(n)
        #Space: O(n)
        stack = []
        
        for char in s:
            if char == ']': #Only with ']', do we start decoding strings
                encodedString, multiplier = '', ''
                
                #Inserting in them front of another maintains the original order
                while len(stack) and stack[-1].isalpha():
                    encodedString = stack.pop() + encodedString
                stack.pop() #Dispose of '['
                
                #Get the multiplier
                while len(stack) and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                
                stack.append(encodedString * int(multiplier))
            else:
                stack.append(char)
                
        return ''.join(stack)