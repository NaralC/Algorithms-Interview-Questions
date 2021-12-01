class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return modulo(n)
        
def iteration(n):
    #Time: O(log(3)n)
    #Space: O(1)
    for exponent in range(n):
        candidate = pow(3, exponent)

        if candidate > n:
            return False
        elif candidate == n:
            return True
        
def modulo(n):
    while n > 1:
    #n must be made up solely of 3's to be divisible by three
        if n % 3 != 0: 
            return False
        n = n // 3 #Example: 45 would fail here since 3 * 3 * 5; 3 cannot divide 5
    return n == 1 

def numberLimitation(n):
    #Time: O(1)
    #Space: O(1)
    #Cut to the chase if we already know the upper bound of 3^x
    # return n > 0 and pow(3, 19) % n == 0
    
    #Time: O(log(3)n)
    #Space: O(1)
    maxNumber = pow(2, 31) - 1  #As mentioned in the prompt
    maxExponent = 0
    candidateNumber = 1
    
    while candidateNumber <= maxNumber:
        maxExponent += 1
        candidateNumber = pow(3, maxExponent)
    
    return n > 0 and pow(3, maxExponent) % n == 0
