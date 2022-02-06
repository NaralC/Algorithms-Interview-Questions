class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        increase = True
        decrease = True
        
        for idx in range(1, len(nums)):
            current = nums[idx]
            previous = nums[idx - 1]
            
            if previous > current:
                increase = False
            elif previous < current:
                decrease = False
                
        return increase or decrease