class Solution:
    def addDigits(self, num: int) -> int:
        #Time: O(?)
        #Space: (1)
        
        while num < 10:
            num = nextNumber(num)
        
        return num
        
def nextNumber(n):
    output = 0
    
    while n > 0:
        output += n % 10
        n = n // 10
    
    return output