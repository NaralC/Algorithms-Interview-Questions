class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return unicode(num1, num2)
        
def unicode(num1, num2):
    #Time: O(max(num1, num2))
    #Space: O(max(num1, num2))
    
    num1, num2 = list(num1), list(num2)
    carry, output = 0, ''

    while len(num1) or len(num2) or carry:
        #Example: ord('1') - ord('0') = 1
        #Example2: ord('7') - ord('0') = 7
        #Basically difference in Unicode representation
        
        if len(num1):
            carry += ord(num1.pop()) - ord('0') 
        if len(num2):
            carry += ord(num2.pop()) - ord('0')

        output = str(carry % 10) + output
        carry //= 10

    return output
        
def dictionary(num1, num2):
    #Time: O(max(num1, num2))
    #Space: O(max(num1, num2))
    
    strToInt = {str(x) : x for x in range(10)}

    num1, num2 = list(num1), list(num2)
    carry, output = 0, ''

    while len(num1) or len(num2) or carry:
        #Turn strings into numbers with a dictionary
        if len(num1):
            carry += strToInt[num1.pop()]
        if len(num2):
            carry += strToInt[num2.pop()]

        output = str(carry % 10) + output
        carry //= 10

    return output
