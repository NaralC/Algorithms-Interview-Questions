class Solution:
    def longestPalindrome(self, s: str) -> int:
        #Time: O(n)
        #Space: O(n)
        
        #Get the frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1  
        
        #Start the counting process
        count = 0
        oddFound = False
        
        for val in freq.values():
            #Chars with even frequency can easily be paired together into a palindrome
            if val % 2 == 0:
                count += val
                
            #Chars with odd frequency are forced to leave one element behind to form a palindrome
            else:
                count += val - 1
                oddFound = True
        
        #If we've run into a char with odd frequency before, the middle of the palindrome can be filled with an extra
        return count + 1 if oddFound else count