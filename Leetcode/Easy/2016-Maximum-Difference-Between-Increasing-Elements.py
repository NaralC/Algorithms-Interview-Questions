class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        #Same idea as 'Best Time to Buy and Sell Stock'
        
        output = 0
        found = False
        left, right = 0, 1
        
        while right < len(nums):
            if nums[left] >= nums[right]:
                left = right
                right += 1
            
            else:
                found = True
                output = max(output, nums[right] - nums[left])
                right += 1
        
        return output if found else -1