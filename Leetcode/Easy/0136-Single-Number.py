class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return bitManipulation(nums)
    
def bitManipulation(nums):
    #Time: O(n)
    #Space: O(1)
    
    output = 0
    for num in nums:
        #XOR Operator
        #1 if the operands are the same
        #2 if the operands are the different
        output ^= num
        
    return output
    
        
def hashTable(nums):
    #Time: O(n)
    #Space: O(n)
    
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    for key, val in frequency.items():
        if val == 1:
            return key