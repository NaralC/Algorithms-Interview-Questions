class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                #Run a palindrome check on:
                #Input string without the element left is pointing at
                noLeft = isPalindrome(left + 1, right, s)
                
                #Input string without the element right is pointing at
                noRight = isPalindrome(left, right - 1, s)
                
                #The two cases above has covered scanning the entire string
                #And we only have one quota of deleting an element, so no need to check any further
                return noLeft or noRight
            
            left += 1
            right -= 1
            
        return True
    
def isPalindrome(left, right, s):
    #Time: O(n)
    #Space: O(1)
    
    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    
    return True