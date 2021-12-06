class Solution:
    def romanToInt(self, s: str) -> int:
        #Time: O(n)
        #Space: O(1) since there are 7 Roman symbols
        romanToInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        output = 0
        
        #Not looping til the end since we're checking for next element
        for idx in range(len(s) - 1):
            currentChar = romanToInt[s[idx]]
            nextChar = romanToInt[s[idx + 1]]
            
            if currentChar < nextChar:
                output -= currentChar
            else:
                output += currentChar
            
        #Add up the last element (since inputs are guaranteed valid)   
        return output + romanToInt[s[-1]]