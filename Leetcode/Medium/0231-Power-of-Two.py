class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return lookForRemainder(n)

def bitOperation(n):
    #Time: O(?)
    #Space: O(?)
    
    if n < 1:
        return False
    
    #A power of two must have only a single 1 in their binary form (since 1 -> 2 -> 4 -> 8 -> ...)
    #So when we & (AND for bitwise operations) with itself minus one, the result always must be 0
    #Example: n = 8
    #n         = 0 1 0 0 0
    #n - 1     = 0 0 1 1 1
    #n & (n-1) = 0 0 0 0 0
    
    return n & (n-1) == 0
    
def lookForRemainder(n):
    #Time: O(log n)
    #Space: O(1)
    
    if n < 1:
        return False
    
    while n % 2 == 0:
        n //= 2
    
    #Since power of two's go like this: 1 -> 2 -> 4 -> 8 -> ...
    #A power of two will always exit the loop and end up as 1
    #While numbers like 6 and 14 will exit the loop as 3
    return n == 1
    
def forLoop(n): 
    #Time: O(log n)
    #Space: O(1)
    
    for exponent in range(32):
        if n == pow(2, exponent):
            return True

    return False
        