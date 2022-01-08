class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return shorter(s)
        
def shorter(s):
    #Time: O(n)
    #Space: O(1)
    
    s = s.strip() #Remove leading and trailing spaces
    s = s.split(' ') #Convert words separated by ' ' into a single list
    
    return len(s[-1]) #Get len() of the last word
        
def naive(s):
    #Time: O(n)
    #Space: O(1)

    count = 0
    ptr = len(s) - 1

    #Move ptr to the last word, avoiding spaces
    while s[ptr].isspace():
        ptr -= 1

    #Move ptr until the word ends
    while ptr > -1 and s[ptr].isalpha():
        count += 1
        ptr -= 1

    return count