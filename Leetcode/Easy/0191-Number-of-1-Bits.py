class Solution:
    def hammingWeight(self, n: int) -> int:
        #Time: O(1) since all inputs are of length 32
        #Space: O(1)
        
        #str() turns bits into a base-10 number, so it doesn't work
        output = 0
        
        while n > 0:
            output += (n % 2) #Check if the input ends with a 0 or 1
            n = n >> 1 #Shift over to the right, on top of the last bit
        
        return output