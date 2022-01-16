class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Time: O(n)
        #Space: O(n)

        onlyUpperChars = [char.lower() for char in s if char.isalnum()]
        
        left, right = 0, len(onlyUpperChars) - 1
        
        while left < right:
            if onlyUpperChars[left] != onlyUpperChars[right]:
                return False
            
            left += 1
            right -= 1
        
        return True