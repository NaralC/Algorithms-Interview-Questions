class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return lookForRemainder(n)

def lookForRemainder(n):
    #Time: O(log4 n)
    #Space: O(1)
    
    if n < 1:
        return False
    
    while n % 4 == 0:
        n //= 4
    
    #Because power of 4's goes like this: 1 -> 4 -> 16 -> 64 -> ...
    #If n is really a power of 4, after going through divisions by 4, it must exit the loop as 1
    return n == 1
        
def forLoop(n):
    #Time: (log4 n)
    #Space: O(1)
    
    for exponent in range(32):
        if n == pow(4, exponent):
            return True

    return False