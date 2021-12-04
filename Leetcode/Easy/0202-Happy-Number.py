class Solution:
    def isHappy(self, n: int) -> bool:
        return twoPointers(n)

def twoPointers(number):
    #Time: O(n)
    #Space: O(1)
    slow = number
    fast = squaredDigitsSummed(number)

    while True:
        if slow == 1 or fast == 1: return True
        elif slow == fast: return False
        
        slow = squaredDigitsSummed(slow)
        fast = squaredDigitsSummed((squaredDigitsSummed(fast)))
        
def hashSet(number):
    #Time: O(n)
    #Space: O(n)
    seen = set() #For detecting duplicates

    while True:
        if number in seen:
            return False
        else:
            seen.add(number)
            number = squaredDigitsSummed(number)
            if number == 1: return True

def squaredDigitsSummed(number):
    output = 0

    for char in str(number):
        output += int(char) ** 2
    
    return output