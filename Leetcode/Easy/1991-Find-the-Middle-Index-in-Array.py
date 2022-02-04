class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        fromLeft, fromRight = 0, sum(nums)
        
        for idx in range(len(nums)):
            if fromLeft == fromRight - nums[idx]:
                return idx
            
            fromLeft += nums[idx]
            fromRight -= nums[idx]
             
        return -1   