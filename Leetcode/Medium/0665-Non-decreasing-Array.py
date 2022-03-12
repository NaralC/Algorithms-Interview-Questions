class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        for idx in range(len(nums) - 1):
            left, right = nums[idx], nums[idx + 1]
            
            if left > right:
                noLeft = helper(nums[:idx] + nums[idx + 1:])
                noRight = helper(nums[:idx + 1] + nums[idx + 2:])
                
                return noLeft or noRight
        
        return True
    
def helper(arr):
    
    for idx in range(len(arr) - 1):
        left, right = arr[idx], arr[idx + 1]

        if left > right:
            return False
        
    return True