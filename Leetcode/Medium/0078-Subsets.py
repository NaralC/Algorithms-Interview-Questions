class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Time: O(2^n * n) #Complexity of subsets of n size, while we (*n) since we're looping through again and again
        #Space: O(2^n * n)
        
        output = [[]]
        
        #Add new numbers on top of each snapshot
        for newNum in nums:
            #Loop through an automatically created snapshot of output
            for idx in range(len(output)):
                newSubset = output[idx] + [newNum]
                output.append(newSubset)
                
        return output