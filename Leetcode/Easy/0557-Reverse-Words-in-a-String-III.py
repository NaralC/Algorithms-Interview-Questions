class Solution:
    def reverseWords(self, s: str) -> str:
        #Time: O(n * m) where m = avg word length in s
        #Space: O(1)
        
        left, right = 0, 0
        s = list(s)
        
        while left < len(s) and right < len(s):
            #Move right until it runs into a space
            if not s[right].isspace():
                right += 1
                
            #Reverse s[left:right+1]
            #Move up both right and left
            elif s[right].isspace():
                reverse(left, right - 1, s)
                right = right + 1
                left = right
            
        #Take care of the last word: reverse s[left:right]
        reverse(left, right - 1, s)
        
        return ''.join(s)
    
def reverse(left, right, s):
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1