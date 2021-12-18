class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return memoize(nums)
    
def bruteforce(nums):
    #Time: O(n^2)
    #Space: O(1) excluding the output
    output = []
    
    for idx in range(len(nums)):
        newNums = nums[:idx] + nums[idx + 1:]
        curProd = 1
        
        for num in newNums:
            curProd *= num
        
        output.append(curProd)
    
    return output
        
def memoize(nums):
    #Time: O(n)
    #Space: O(n) excluding the output
    output = [1] * len(nums)
    leftProds = [1] * len(nums)
    rightProds = [1] * len(nums)

    curProd = 1
    for idx in range(len(nums)):
        curProd *= nums[idx]
        leftProds[idx] = curProd

    curProd = 1
    for idx in reversed(range(len(nums))):
        curProd *= nums[idx]
        rightProds[idx] = curProd

    for idx in range(len(output)):
        left = leftProds[idx - 1] if idx > 0 else 1
        right = rightProds[idx + 1] if idx < len(nums) - 1 else 1

        output[idx] = left * right

    return output