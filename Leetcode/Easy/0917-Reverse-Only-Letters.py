class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        #Time: O(n)
        #Space: O(1)
        
        s = list(s)
        
        left, right = 0, len(s) - 1
        while left < right:
            #Swap when both ptrs are on English letters
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            #Move left until it's on an English letter
            if not s[left].isalpha():
                left += 1
            
            #Move right until it's on an English letter
            if not s[right].isalpha():
                right -= 1
        
        return ''.join(s)