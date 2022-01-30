class Solution:
    def isUgly(self, n: int) -> bool:
        #Time: O(log2n) Since 2^32 can be divided by 2 log2n times?
        #Space: O(1)
        
        #Only positive numbers can be ugly, as stated by the problem
        if n < 1: return False
        
        while n > 1:
            #While the number is divisible by 2, 3, 5 -> it's still an ugly number
            if n % 5 == 0:
                n = n // 5
            
            elif n % 3 == 0:
                n = n // 3
            
            elif n % 2 == 0:
                n = n // 2
            
            #If not divisible by any of the three number, the number's not ugly
            else:
                return False
        
        return True