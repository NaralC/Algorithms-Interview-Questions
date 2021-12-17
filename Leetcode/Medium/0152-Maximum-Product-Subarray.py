class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return minAndMax(nums)
    
def minAndMax(nums):
    #Time: O(n)
    #Space: O(1)
    output = nums[0]
    curMin, curMax = 1, 1
    
    for num in nums:
        candidates = [num, num  * curMin, num * curMax]
        
        curMin = min(candidates)
        curMax = max(candidates)
        output = max(output, curMax)
    
    return output
        
def twoPointers(nums):
    #Time: O(n)
    #Space: O(1)
    
    #For keeping track of the max product and the first iteration where output = max(None, leftProduct, rightProduct)
    output = nums[0]
    leftProduct, rightProduct = 1, 1

    for idx in range(len(nums)):
        #Reset either products to 1 if their last encounter is 0
        if leftProduct == 0: leftProduct = 1
        if rightProduct == 0: rightProduct = 1

        #Create a new subarray product on every iteration
        leftProduct *= nums[idx]
        rightProduct *= nums[len(nums) - 1 - idx]

        output = max(output, leftProduct, rightProduct)

    return output