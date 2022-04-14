class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Time: O(n^2)
        #Space: O(1)
        
        longest = ''
        
        for idx in range(len(s)):
            #Odd cases like 'aba' (both ptrs start on the same middle)
            odd = getPalindrome(idx, idx, s)
            
            #Even cases like 'abba' (one ptr starts on the middle, while the other starts to its right)
            even = getPalindrome(idx, idx + 1, s)
            
            #Update our variable with the longer palindrome
            longest = max(longest, even, odd, key = lambda x: len(x))
                
        return longest
    
def getPalindrome(left, right, s):
    #Time: O(n)
    #Space: O(1)
    
    while left > -1 and right < len(s):
        if s[left] != s[right]:
            break
            
        left -= 1
        right += 1
        
    #'abc' -> 'b' due to how string slicing and indices work in Python
    return s[left + 1 : right]