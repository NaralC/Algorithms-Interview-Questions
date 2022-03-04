class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        #Mark down what happens at each idx
        inc = [0] * length
        dec = [0] * length
        
        for start, end, add in updates:
            inc[start] += add #Add this up before assigning to output
            dec[end] += add #Cancel out with this before moving on to the next idx
        
        #Update the output arrray according to our prefix sum
        output = [None for _ in range(length)]
        prefixSum = 0
        
        for idx in range(length):
            prefixSum += inc[idx]
            output[idx] = prefixSum
            prefixSum -= dec[idx]
            
        return output