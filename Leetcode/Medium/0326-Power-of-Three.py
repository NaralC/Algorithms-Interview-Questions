class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return lookForRemainder(n)

def lookForRemainder(n):
    #Time: O(log3 n)
    #Space: O(1)
    
    if n < 1:
        return False
    
    while n % 3 == 0:
        n //= 3
        
    #Since power of 3's go like 1 -> 3 -> 9 -> 27 -> ...
    #When n exits the loop, if it's a power of 3, it must be 1
    return n == 1
    
def forLoop(n):
    #Time: (log3 n)
    #Space: O(1)
    
    for exponent in range(32):
        if n == pow(3, exponent):
            return True

    return False