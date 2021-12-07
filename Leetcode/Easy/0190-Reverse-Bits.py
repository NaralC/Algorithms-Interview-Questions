class Solution:
    def reverseBits(self, n: int) -> int:
        #Time: O(1) since all inputs are of length 32
        #Space: O(1)
        output = 0
        
        for idx in range(32):
            currentBit = (n >> idx) & 1
            output = output | (currentBit << (31 - idx))
        
        return output