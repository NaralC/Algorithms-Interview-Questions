class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        #Early termination if the input is negative or ends with a zero
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        original, backwards = x, 0
        while x > 0:
            backwards *= 10
            backwards += x % 10
            x = x // 10
            
        return original == backwards