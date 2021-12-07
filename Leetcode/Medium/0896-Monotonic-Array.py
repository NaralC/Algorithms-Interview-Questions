class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        isNotIncreasing = True
        isNotDecreasing = True
        
        for idx in range(1, len(nums)):
            previous =  nums[idx - 1]
            current = nums[idx]
            
            if previous > current:
                isNotDecreasing = False
            if previous < current:
                isNotIncreasing = False
            
        return isNotIncreasing or isNotDecreasing
            