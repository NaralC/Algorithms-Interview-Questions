class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #Time: O(n)
        #Space: O(n)
        #Using an array of size 26 to track and turn chars into a string doesn't work since the output has to be a subsequence of s
        #In terms of lexicography and greediness, keep smaller chars at the front while making sure every char has a place in the final output
        
        lastIdx = {char : idx for idx, char in enumerate(s)} #Prevent appending the last one any a char's kind
        seen = set() #Prevent duplicates in the stack
        stack = [] #Monotonic - small chars at the bottom
        
        for idx, char in enumerate(s):
            if char in seen:
                continue
            
            while len(stack) and char < stack[-1] and idx < lastIdx[stack[-1]]:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)