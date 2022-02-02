class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        for idx in range(1, len(nums)):
            previous = nums[idx - 1]
            current = nums[idx]
            
            #Run the same check on versions without the previous or current element
            if previous >= current:
                noLeft = helper(nums[:idx - 1] + nums[idx:])
                noRight = helper(nums[:idx] + nums[idx + 1:])
                
                return noLeft or noRight
            
        return True
                
def helper(nums):

    for idx in range(1, len(nums)):
        previous = nums[idx - 1]
        current = nums[idx]
        
        if previous >= current:
            return False
        
    return True